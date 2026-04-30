#!/usr/bin/env python3
"""
tributary_gen.py -- Generate Tier 1/Tier 2 companion content briefs
for the Tributary Trust Protocol (see SKILL.md, Section 11A).

This script does NOT write final tributary content. It:
  1. Reads the money page (markdown file or URL)
  2. Extracts its 500-token chunks, key entities, target keyword, and
     verification tags
  3. Derives one companion brief per Tier 1 asset, mapped to the chunk
     each tributary covers in greater depth
  4. Writes structured drafts to ~/Documents/SEO-AGI/tributaries/<slug>/
     plus a manifest.json mapping each draft to its host platform

The agent then refines each draft into platform-native voice and applies
all SKILL.md quality gates (Reddit Test, Information Gain, {{VERIFY}}
resolution, Section 9 banned patterns) before publishing.

Usage:
  python3 tributary_gen.py "<keyword>" --money-page=<path-or-url> [--tiers=1]
  python3 tributary_gen.py "airport parking JFK" --money-page=~/Documents/SEO-AGI/pages/jfk.md
  python3 tributary_gen.py "best crm 2026" --money-page=https://example.com/best-crm
"""

import argparse
import json
import re
import sys
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

OUTPUT_ROOT = Path.home() / "Documents" / "SEO-AGI" / "tributaries"

TIER_1_ASSETS = [
    {
        "host": "google_sites",
        "label": "Google Sites",
        "voice": "encyclopedic, structured, neutral; uses headings, embedded maps where geo-relevant, simple tables",
        "derives_from": "geographic/local detail OR pricing comparison table",
        "min_words": 600,
        "anchor_text_pattern": "entity-rich descriptive (e.g., 'JFK long-term parking rates')",
    },
    {
        "host": "medium",
        "label": "Medium",
        "voice": "essay/narrative, first-person observation, expanded operational detail, photos if available",
        "derives_from": "Original Research / Data Experiment block",
        "min_words": 1000,
        "anchor_text_pattern": "in-line natural mentions plus one bottom-of-article reference",
    },
    {
        "host": "subreddit",
        "label": "Custom Subreddit (you moderate)",
        "voice": "community thread, Q&A reframed, mod-pinned canonical answer",
        "derives_from": "FAQ / PAA section",
        "min_words": 400,
        "anchor_text_pattern": "single contextual link in mod-pinned comment",
    },
    {
        "host": "google_sheets",
        "label": "Google Sheets (published to web)",
        "voice": "tabular, methodology notes in cell comments, formula transparency",
        "derives_from": "pricing comparison table OR break-even math",
        "min_words": 200,
        "anchor_text_pattern": "header cell linking back to money page methodology section",
    },
    {
        "host": "linkedin",
        "label": "LinkedIn Article",
        "voice": "industry-framed, methodology deep-dive, peer commentary invitation",
        "derives_from": "Original Research block OR Information Gain insight",
        "min_words": 800,
        "anchor_text_pattern": "in-line entity mention plus 'further reading' reference",
    },
]

TIER_2_ASSETS = [
    {
        "host": "youtube_description",
        "label": "YouTube video description + transcript",
        "voice": "spoken-style transcript, timestamped sections",
        "derives_from": "any 500-token chunk with visual potential",
        "min_words": 300,
        "anchor_text_pattern": "first-line link in description",
    },
    {
        "host": "github_readme",
        "label": "GitHub repository README",
        "voice": "technical, code-friendly, citation-heavy",
        "derives_from": "data/methodology if vertical is technical",
        "min_words": 500,
        "anchor_text_pattern": "Resources section link",
    },
    {
        "host": "substack",
        "label": "Substack newsletter post",
        "voice": "newsletter conversational, weekly framing",
        "derives_from": "any chunk reframed as 'this week's analysis'",
        "min_words": 600,
        "anchor_text_pattern": "in-line plus footer 'further reading'",
    },
]


def slugify(text: str) -> str:
    s = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
    return s[:60] or "untitled"


def load_money_page(source: str) -> str:
    """Load money page from local path or URL. Returns raw markdown/HTML."""
    src = source.strip()
    if src.startswith(("http://", "https://")):
        req = urllib.request.Request(
            src, headers={"User-Agent": "seobuild-onpage/1.7.0"}
        )
        with urllib.request.urlopen(req, timeout=30) as resp:
            return resp.read().decode("utf-8", errors="ignore")
    path = Path(src).expanduser()
    if not path.exists():
        raise FileNotFoundError(f"Money page not found: {path}")
    return path.read_text(encoding="utf-8")


def extract_chunks(content: str) -> list[dict]:
    """Naive 500-token chunk extraction by H2 boundary.

    A chunk is the H2 heading and the body text that follows up to the
    next H2. Each chunk is a distinct QFO facet candidate per
    SKILL.md Section 3.
    """
    # Strip YAML frontmatter
    if content.startswith("---"):
        end = content.find("\n---", 3)
        if end != -1:
            content = content[end + 4 :]

    chunks = []
    current = {"h2": None, "body": []}
    for line in content.splitlines():
        if line.startswith("## ") and not line.startswith("### "):
            if current["h2"] or current["body"]:
                chunks.append(current)
            current = {"h2": line[3:].strip(), "body": []}
        else:
            current["body"].append(line)
    if current["h2"] or current["body"]:
        chunks.append(current)

    # Filter empty / no-h2 prelude
    return [
        {
            "h2": c["h2"],
            "body": "\n".join(c["body"]).strip(),
            "word_count": len(" ".join(c["body"]).split()),
        }
        for c in chunks
        if c["h2"]
    ]


def extract_entities(content: str) -> list[str]:
    """Best-effort entity extraction. Looks for proper-noun phrases and
    inline RDFa span markers (`<span typeof="...">`). Real entity work
    happens in the agent layer; this is a starting list."""
    entities = set()
    # RDFa spans
    for m in re.finditer(r'<span[^>]*typeof="[^"]+"[^>]*>([^<]+)</span>', content):
        entities.add(m.group(1).strip())
    # Capitalized multi-word phrases (rough heuristic)
    for m in re.finditer(r"\b([A-Z][A-Za-z]+(?:\s+[A-Z][A-Za-z]+){1,4})\b", content):
        if len(m.group(1)) > 4:
            entities.add(m.group(1))
    return sorted(entities)[:30]


def extract_verify_tags(content: str) -> list[str]:
    return re.findall(r"\{\{(?:VERIFY|RESEARCH NEEDED|SOURCE NEEDED)[^}]*\}\}", content)


def derive_brief(asset: dict, keyword: str, chunks: list[dict], entities: list[str], verify_tags: list[str], money_page_ref: str) -> dict:
    """Build a tributary brief for one Tier 1 / Tier 2 asset."""
    # Pick a chunk to derive from. Heuristic: keyword match in h2 / body
    target_chunk = chunks[0] if chunks else {"h2": "(no chunks parsed)", "body": ""}
    for c in chunks:
        if asset["derives_from"].split()[0].lower() in (c["h2"] or "").lower():
            target_chunk = c
            break

    return {
        "host": asset["host"],
        "label": asset["label"],
        "target_keyword": keyword,
        "money_page": money_page_ref,
        "derives_from_chunk": target_chunk["h2"],
        "derives_from_facet": asset["derives_from"],
        "voice_directive": asset["voice"],
        "min_words": asset["min_words"],
        "anchor_text_pattern": asset["anchor_text_pattern"],
        "entities_to_mention": entities[:10],
        "inherited_verify_tags": verify_tags,
        "quality_gates_required": [
            "Reddit Test (host-platform appropriate)",
            "Information Gain Test (1+ fact not in top 10 SERP)",
            "Prove-It Details (2+ hard operational facts)",
            "All {{VERIFY}} / {{SOURCE NEEDED}} resolved before publish",
            "Section 9 banned patterns (no em dashes, no nestled, no generic intros)",
            "Entity Consensus (claims cross-checked against 2+ sources)",
            "Link to money page with descriptive anchor",
            "Cross-link to at least one other tributary in the network",
        ],
        "agent_instructions": (
            f"Refine this brief into a publish-ready {asset['label']} post. "
            f"Voice: {asset['voice']}. Cover the '{target_chunk['h2']}' "
            f"facet in greater depth than the money page does. Reuse the "
            f"entity names and key numbers verbatim for Entity Consensus. "
            f"Resolve every {{VERIFY}} tag with a real source before output."
        ),
    }


def write_drafts(slug: str, briefs: list[dict], keyword: str, money_page_ref: str) -> Path:
    out_dir = OUTPUT_ROOT / slug
    out_dir.mkdir(parents=True, exist_ok=True)

    manifest = {
        "keyword": keyword,
        "money_page": money_page_ref,
        "generated": datetime.now(timezone.utc).isoformat(),
        "tributaries": [],
    }

    for brief in briefs:
        fname = f"{brief['host']}.md"
        path = out_dir / fname
        body = (
            f"# Tributary Brief: {brief['label']}\n\n"
            f"**Target keyword:** {brief['target_keyword']}\n"
            f"**Money page:** {brief['money_page']}\n"
            f"**Derives from chunk:** {brief['derives_from_chunk']}\n"
            f"**Facet:** {brief['derives_from_facet']}\n"
            f"**Min words:** {brief['min_words']}\n\n"
            f"## Voice\n{brief['voice_directive']}\n\n"
            f"## Anchor text pattern\n{brief['anchor_text_pattern']}\n\n"
            f"## Entities to mention (Entity Consensus)\n"
            + "".join(f"- {e}\n" for e in brief["entities_to_mention"])
            + "\n## Inherited {{VERIFY}} tags (must be resolved before publish)\n"
            + ("".join(f"- {t}\n" for t in brief["inherited_verify_tags"]) or "- (none)\n")
            + "\n## Quality gates (all required)\n"
            + "".join(f"- {g}\n" for g in brief["quality_gates_required"])
            + f"\n## Agent instructions\n{brief['agent_instructions']}\n\n"
            "---\n\n## Draft\n\n_Agent fills this section. Apply every "
            "quality gate above. Do not publish until all {{VERIFY}} tags "
            "are resolved._\n"
        )
        path.write_text(body, encoding="utf-8")
        manifest["tributaries"].append(
            {"host": brief["host"], "path": str(path), "min_words": brief["min_words"]}
        )

    (out_dir / "manifest.json").write_text(
        json.dumps(manifest, indent=2), encoding="utf-8"
    )
    return out_dir


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("keyword", help="Target keyword for the money page")
    p.add_argument("--money-page", required=True, help="Path or URL to the money page")
    p.add_argument(
        "--tiers",
        default="1",
        help="Comma-separated tier numbers to generate (1 = Tier 1 only, '1,2' = both). Default: 1",
    )
    p.add_argument("--output-root", default=str(OUTPUT_ROOT), help="Override output dir")
    args = p.parse_args()

    try:
        content = load_money_page(args.money_page)
    except Exception as e:
        print(f"ERROR loading money page: {e}", file=sys.stderr)
        return 1

    chunks = extract_chunks(content)
    entities = extract_entities(content)
    verify_tags = extract_verify_tags(content)

    if not chunks:
        print(
            "WARNING: no H2 chunks parsed from money page. Tributary briefs "
            "will derive from generic facet hints instead of real chunks.",
            file=sys.stderr,
        )

    tier_set = {t.strip() for t in args.tiers.split(",")}
    assets = []
    if "1" in tier_set:
        assets.extend(TIER_1_ASSETS)
    if "2" in tier_set:
        assets.extend(TIER_2_ASSETS)

    briefs = [
        derive_brief(a, args.keyword, chunks, entities, verify_tags, args.money_page)
        for a in assets
    ]

    slug = slugify(args.keyword)
    out_dir = write_drafts(slug, briefs, args.keyword, args.money_page)

    print(f"Generated {len(briefs)} tributary brief(s) for: {args.keyword}")
    print(f"Output: {out_dir}")
    print(f"Manifest: {out_dir / 'manifest.json'}")
    print()
    print("Next: agent refines each draft to platform-native voice, applies")
    print("all quality gates, and resolves {{VERIFY}} tags before publish.")
    print("See SKILL.md Section 11A 'Tributary Trust Protocol' for full rules.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
