"""Tests for DataForSEO client response parsing."""

import sys
from pathlib import Path

sys.path.insert(
    0, str(Path(__file__).parent.parent / "scripts")
)

from lib.dataforseo import DataForSEOClient


def test_extract_serp_empty():
    client = DataForSEOClient("test", "test")
    result = client._extract_serp({"tasks": []})
    assert result["organic"] == []
    assert result["paa"] == []
    assert result["featured_snippet"] is None


def test_extract_serp_with_organic():
    raw = {
        "tasks": [{
            "result": [{
                "se_results_count": 1000000,
                "items": [
                    {
                        "type": "organic",
                        "rank_absolute": 1,
                        "url": "https://example.com/page",
                        "domain": "example.com",
                        "title": "Test Page",
                        "description": "A test description",
                    },
                    {
                        "type": "organic",
                        "rank_absolute": 2,
                        "url": "https://other.com/page",
                        "domain": "other.com",
                        "title": "Other Page",
                        "description": "Another description",
                    },
                    {
                        "type": "people_also_ask",
                        "items": [
                            {"title": "What is a test?"},
                            {"title": "How do tests work?"},
                        ],
                    },
                ]
            }]
        }]
    }

    client = DataForSEOClient("test", "test")
    result = client._extract_serp(raw)

    assert len(result["organic"]) == 2
    assert result["organic"][0]["position"] == 1
    assert result["organic"][0]["url"] == "https://example.com/page"
    assert result["organic"][1]["title"] == "Other Page"

    assert len(result["paa"]) == 2
    assert result["paa"][0] == "What is a test?"

    assert result["total_results"] == 1000000


def test_extract_keywords_empty():
    client = DataForSEOClient("test", "test")
    result = client._extract_keywords({"tasks": []})
    assert result == []


def test_extract_keywords_with_data():
    raw = {
        "tasks": [{
            "result": [{
                "items": [
                    {
                        "keyword_data": {
                            "keyword": "test keyword one",
                            "keyword_info": {
                                "search_volume": 5000,
                                "cpc": 1.50,
                                "competition": 0.7,
                            },
                            "keyword_properties": {
                                "keyword_difficulty": 42,
                            },
                        }
                    },
                    {
                        "keyword_data": {
                            "keyword": "test keyword two",
                            "keyword_info": {
                                "search_volume": 8000,
                                "cpc": 2.10,
                                "competition": 0.85,
                            },
                            "keyword_properties": {
                                "keyword_difficulty": 55,
                            },
                        }
                    },
                ]
            }]
        }]
    }

    client = DataForSEOClient("test", "test")
    result = client._extract_keywords(raw)

    # Should be sorted by volume descending
    assert len(result) == 2
    assert result[0]["keyword"] == "test keyword two"
    assert result[0]["volume"] == 8000
    assert result[1]["keyword"] == "test keyword one"
    assert result[1]["volume"] == 5000
    assert result[1]["difficulty"] == 42


def test_extract_headings():
    """Headings come from main_topic[] + secondary_topic[] objects with
    h_title (text) and level (int). DataForSEO does NOT return flat
    h1/h2/h3 arrays. Regression test for empty-headings bug."""
    page_content = {
        "main_topic": [
            {"h_title": "Main Section", "level": 2, "primary_content": []},
            {"h_title": "Subsection A", "level": 3, "primary_content": []},
            {"h_title": "Page Title", "level": 1, "primary_content": []},
        ],
        "secondary_topic": [
            {"h_title": "Sidebar Heading", "level": 2},
            {"h_title": "", "level": 2},  # should be skipped
            {"h_title": "No Level Default", "level": None},  # default to H2
        ],
    }
    headings = DataForSEOClient._extract_headings(page_content)
    assert "H1: Page Title" in headings
    assert "H2: Main Section" in headings
    assert "H3: Subsection A" in headings
    assert "H2: Sidebar Heading" in headings
    assert "H2: No Level Default" in headings
    # Empty h_title is skipped
    assert len(headings) == 5


def test_extract_headings_empty():
    """Missing or null buckets must not crash."""
    assert DataForSEOClient._extract_headings({}) == []
    assert DataForSEOClient._extract_headings(
        {"main_topic": None, "secondary_topic": None}
    ) == []


def test_count_words_from_markdown():
    """Word count prefers page_as_markdown when available.
    Exact count varies with how aggressively URL fragments survive the
    syntax-strip regex; the contract is 'roughly the body word count',
    not perfect markdown parsing."""
    md = "# Title\n\nThis is a test of the markdown stripper here today."
    count = DataForSEOClient._count_words({}, md)
    assert 10 <= count <= 14, f"expected ~12 words, got {count}"


def test_count_words_fallback_to_topics():
    """When markdown is empty, walk primary_content text."""
    page_content = {
        "main_topic": [
            {
                "primary_content": [
                    {"text": "First sentence has five words."},
                    {"text": "Second has four words."},
                ]
            }
        ],
        "secondary_topic": [
            {"primary_content": [{"text": "Three more words here."}]}
        ],
    }
    # 5 + 4 + 4 = 13 words across all primary_content text fields
    assert DataForSEOClient._count_words(page_content, "") == 13


def test_extract_title_from_markdown():
    md = "# The Real Title\n\n## A Subhead\n\nbody"
    assert DataForSEOClient._extract_title({}, md) == "The Real Title"


def test_extract_title_fallback_to_main_topic():
    page_content = {"main_topic": [{"h_title": "Fallback Title", "level": 2}]}
    assert (
        DataForSEOClient._extract_title(page_content, "") == "Fallback Title"
    )


def test_extract_content_full_response():
    """Integration shape test against a realistic content_parsing/live payload."""
    raw = {
        "tasks": [
            {
                "result": [
                    {
                        "items": [
                            {
                                "type": "page_content",
                                "page_content": {
                                    "header": {
                                        "primary_content": [],
                                        "secondary_content": [],
                                    },
                                    "main_topic": [
                                        {
                                            "h_title": "JFK Parking Guide",
                                            "main_title": "JFK Parking Guide",
                                            "level": 2,
                                            "primary_content": [
                                                {
                                                    "text": "Long term parking at JFK costs about twenty dollars per day."
                                                }
                                            ],
                                        },
                                        {
                                            "h_title": "Best Lots",
                                            "level": 3,
                                            "primary_content": [],
                                        },
                                    ],
                                    "secondary_topic": [
                                        {
                                            "h_title": "FAQ",
                                            "level": 2,
                                            "primary_content": [],
                                        }
                                    ],
                                    "footer": {},
                                },
                                "page_as_markdown": "# JFK Parking Guide\n\n## Rates\n\nLong term parking at JFK costs about twenty dollars per day.",
                            }
                        ]
                    }
                ]
            }
        ]
    }
    client = DataForSEOClient("test", "test")
    out = client._extract_content(raw)
    assert out is not None
    assert out["title"] == "JFK Parking Guide"
    assert out["word_count"] >= 10
    assert "H2: JFK Parking Guide" in out["headings"]
    assert "H3: Best Lots" in out["headings"]
    assert "H2: FAQ" in out["headings"]
    # H2 + H3 counts the analyzer cares about
    h2 = sum(1 for h in out["headings"] if h.startswith("H2:"))
    h3 = sum(1 for h in out["headings"] if h.startswith("H3:"))
    assert h2 == 2
    assert h3 == 1


def test_auth_header():
    client = DataForSEOClient("user@test.com", "mypassword")
    assert client._auth_header.startswith("Basic ")
    assert len(client._auth_header) > 10


if __name__ == "__main__":
    test_extract_serp_empty()
    test_extract_serp_with_organic()
    test_extract_keywords_empty()
    test_extract_keywords_with_data()
    test_extract_headings()
    test_extract_headings_empty()
    test_count_words_from_markdown()
    test_count_words_fallback_to_topics()
    test_extract_title_from_markdown()
    test_extract_title_fallback_to_main_topic()
    test_extract_content_full_response()
    test_auth_header()
    print("All tests passed.")
