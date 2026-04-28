# Changelog

All notable changes to seo-agi are documented here.

## [1.6.0] - 2026-04-15

### Added
- **Ideal Customer Persona (ICP)**: Page brief template now requires a defined ICP with demographics, psychographics, and specific pain points. Content maps to the actual reader, not a generic audience.
- **Deep Entity History & Identity Tags**: Founding dates, generational ownership, and identity attributes (women-owned, veteran-owned) are now explicit entity signals in Section 4 SEAT Signals.
- **The Self-Placement Rule**: Listicle guidance now explicitly allows ranking the client #1, provided the entry is objective with a specific use-case and honest tradeoffs.
- **Keyword Cannibalization Governance**: Section 9 "Never Do" list now prohibits creating pages that compete with existing URLs for the same intent. Sales-focused duplicates get tagged with `noindex` recommendation.

### Changed
- Quality checklist expanded from 38 to 41 items (ICP alignment, entity history, cannibalization)
- Minimum passing score raised to 33/41
- Both brief templates (Page Brief Template + Execution Protocol) updated with ICP field

## [1.3.0] - 2026-03-25

### Added
- **AI Summary Nugget**: Mandatory 200-character fact-dense block at top of every page, designed for LLM scrapers (Perplexity, Gemini, ChatGPT) to cite as a consensus source
- **Original Research Block**: Every page must include a data experiment or first-hand observation section to satisfy Google's Experience (E-E-A-T) signal
- **Map Traffic Shifting**: Local SEO instruction to link from high-traffic informational pages to map embeds, shifting user interaction signals toward local intent
- **Spam Resilience Logic**: Quality checklist now prioritizes technical relevance density over "human tone" -- factually perfect content is not downgraded for sounding clinical
- **Recursive Fact-Checking**: New execution step validates every claim against 2+ high-ranking sources for Entity Consensus before delivery

### Changed
- Quality checklist expanded from 24 to 28 items
- Minimum passing score raised to 22/28
- Execution protocol now has 11 steps (was 10)

## [1.2.0] - 2026-03-25

### Added
- Anti-spam ranking signals: single H1 rule, no EMQ in meta descriptions, no keyword-stuffed alt text, no duplicate content, internal linking requirements
- EMQ allowed in title and URL, banned in H2/H3/H4 subheadings
- Interactive elements section (cost calculators, widgets) to defend against AI Overview traffic loss
- Broken backlink monitoring guidance
- "Boat anchor" page culling (410 status for unindexable cruft)

### Changed
- Quality checklist expanded from 20 to 24 items (added H1, meta desc, heading, alt text checks)

## [1.1.0] - 2026-03-24

### Added
- Hard rule: "beefy" banned from all output (framework is seo-agi)
- Mandatory printed scorecard at end of every page output (no exceptions)
- FAQ/PAA section required (3+ questions, FAQPage schema)
- JSON-LD schema block required per page type
- Hub/spoke internal links required in every output
- RAG Targeting section (write for AI retrieval, not keyword volume)
- Topical Circle Audit (stay inside core service topic, noindex strays)
- Off-Page Sequencing (establish external brand footprint before on-page)
- Reddit Subdomain Indexing (subdomains over standard posts for AI retrieval)
- Ask Maps / Conversational GBP Optimization

### Changed
- Quality checklist expanded from base to 20 items
- Scorecard enforcement language strengthened ("INCOMPLETE without this table")

## [1.0.0] - 2026-03-23

### Added
- Initial release: GEO framework skill for Claude Code, OpenClaw, and Codex
- 500-token chunk architecture for Google AI retrieval
- SEAT signals (Semantic + E-E-A-T + Entity/Knowledge Graph)
- Google AI Search 7 ranking signals (Gecko, Jetstream, BM25, PCTR, Freshness, Boost/Bury)
- Reddit Test, Prove-It Details, Not For You, Information Gain quality gates
- Verification tagging system (VERIFY, RESEARCH NEEDED, SOURCE NEEDED)
- DataForSEO integration with graceful no-creds fallback
- MCP tool integration (Ahrefs, SEMRush)
- Google Search Console pull scripts
- Skill root discovery loop (works across Claude Code, OpenClaw, Codex, Gemini)
- Reference files: page templates, schema patterns, quality checklist
- Mock mode for testing without API keys
