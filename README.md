# seobuild-onpage v1.6.0

### One command. Competitive data in. Ranking pages out.

```
claude install-skill gbessoni/seobuild-onpage
```

Most SEO tools tell you what's wrong with your site. This one writes the pages.

`/seoagi "airport parking JFK"` pulls the current SERP, analyzes what's ranking, finds the gaps in their content, and writes you a complete page -- with the heading structure, depth, FAQ section, and schema markup that actually competes. Not thin content. Not keyword-stuffed filler. Pages backed by live data from the tools the pros use.

**New in v1.6.0 -- ICP-Driven Content + Local Trust Signals:**
- **Ideal Customer Persona (ICP) Integration** -- page briefs now require a defined ICP with demographics, psychographics, and specific pain points. Content maps to who it's actually for, not a generic audience.
- **Deep Entity History & Identity Tags** -- founding dates, generational ownership, and identity attributes (women-owned, veteran-owned, family-owned) are now explicit entity signals. Maps directly to GBP tags and conversational AI filtering.
- **The Self-Placement Rule** -- ranking the client #1 in a listicle is now an approved tactic, provided the entry is strictly objective with a defined use-case and honest tradeoffs.
- **Keyword Cannibalization Governance** -- strict rule against creating pages that compete with existing URLs for the same intent. Sales-focused duplicates of informational pages get tagged with `noindex` recommendation.
- **41-point quality checklist** adding ICP alignment, entity history, and cannibalization checks.

**New in v1.5.0 -- Forensic SEO + Structural Signals:**
- **Semantic HTML Containers** -- generated HTML now uses `<article>`, `<section>`, `<aside>`, `<main>` instead of generic `<div>`. Google's crawler uses these elements to identify the Main Content zone for passage extraction and AI retrieval.
- **Proof-Term Proximity** -- supporting evidence (numbers, entity names, operational details) must live in the same 500-token chunk as the H2 it supports. BERT evaluates within the passage window, not page-wide. Orphaned proof terms don't help.
- **QDD Vulnerability Check** -- UGC (Instagram, Pinterest, Reddit) ranking for a commercial keyword is a structural gap, not a signal to avoid. Flag as HIGH_CONFIDENCE_TAKEOVER.
- **Site Over Page Rule** -- generalist competitors ranking with one page are vulnerable to specialist site architecture. Niche Site Pivot trigger fires when 2/3 top results are generalist pages.
- **Query Fan-Out (QFO) Facet Coverage** -- each 500-token chunk now targets a specific AI sub-query. 40% of future traffic arrives via AI fan-out from a single user prompt.
- **Forensic EMQ Check** -- EMQ in H1 is conditionally required when 2/3 top competitors use it. Competitive context overrides the default entity-based heading rule.
- **Orcas One CVR Modeling** -- keywords now ranked by estimated conversion value, not raw volume. Position 1 at 4.5% CVR vs position 7 at 2%.
- **41-point quality checklist** with QDD, Site vs. Page, EMQ ratio, and QFO facet checks.

**New in v1.4.0 -- March 2026 Update Protocols:**
- **NavBoost Geographic Click Relevance** -- pages now reranked by geographic click patterns. Local pages require neighborhood-level specificity, not just city names. Observed across SEO X community testing.
- **Click Satisfaction as Primary Signal** -- Google watches if users are satisfied after clicking. Content must deliver value in the first 3 chunks or rankings drop regardless of quality. Confirmed via practitioner NavBoost analysis.
- **AI Overview Link Optimization** -- earning a link inside AI Overviews drives 70-80% CTR. Pages structured for snippet extraction with clean tables and FAQ markup.
- **AI Overview Theft Defense** -- rising impressions + falling clicks = your content cited without credit. Interactive elements (calculators, widgets) defend against extraction.
- **QDD (Query Deserves Diversity)** -- Google pulls diverse results into overviews. Information Gain Test now critical for QDD survival.
- **FHASS Replaces YMYL** -- Financial, Health, And Safety, and Security. Expanded scrutiny for risk-adjacent content. Discussed in Google Cloud documentation updates.
- **Banned 2026 Content Patterns** -- generic AI FAQs, 300-word thin pages, blog rolls outside topical circle all confirmed penalized.
- **34-point quality checklist** with geographic specificity, click satisfaction, FHASS compliance, and minimum 1,500-word depth checks.

**New in v1.3.0 -- 2026 SEO Protocols:**
- **AI Summary Nuggets** -- every page opens with a 200-character fact-dense block designed for Perplexity/Gemini/ChatGPT to cite as a consensus source. Position zero for LLM retrieval.
- **Original Research Block** -- mandatory data experiment or first-hand observation section. Google's highest-priority E-E-A-T signal: Experience. Pages without original research cap at 20/28.
- **Map Traffic Shifting** -- internal links from high-traffic informational pages to map embeds, shifting engagement signals toward local intent.
- **Spam Resilience** -- quality scoring now prioritizes technical relevance density over "human tone." Factually perfect content is not downgraded for sounding clinical.
- **Recursive Fact-Checking** -- every claim validated against 2+ high-ranking sources for Entity Consensus before delivery.
- **28-point quality checklist** with mandatory printed scorecard at the end of every output.

**New in v1.2.0 -- Anti-Spam Ranking Signals:**
- Single H1 rule, no exact-match keyword in meta descriptions or subheadings
- No keyword-stuffed alt text, no duplicate content
- Internal linking requirements, broken backlink awareness
- Interactive elements (calculators, widgets) to defend against AI Overview traffic loss

**New in v1.1.0 -- GEO Framework Additions:**
- RAG Targeting: zero-volume long-tail queries that "train" AI to cite your domain
- Topical Circle Audit: stay inside your core service topic or dilute AI authority
- Off-Page Sequencing: establish third-party brand footprint before on-page SEO
- Reddit Subdomain Indexing: seed entity consensus across indexed Reddit layers
- Ask Maps / Conversational GBP Optimization
- FAQ/PAA section and JSON-LD schema now mandatory in every output

**I built this because I got tired of the gap between "SEO audit" and "published page."** I've been doing SEO for 20+ years in ground transportation (1M+ bookings, 2M+ rides across my companies). The workflow was always the same: pull SERP data, analyze competitors, find gaps, write brief, write page, add schema, publish. Over and over. So I turned that entire workflow into a single skill that any AI agent can execute.

The result? I used this to research a competitor's best-performing pages, built equivalent content with `/seoagi`, bought the exact-match domains, and every single page is ranking on page 1. That's not theory. That's the workflow.

---

## What It Actually Does

```
You: /seoagi "best project management tools 2026"

SEO-AGI:
  1.  Pulls SERP top 10 via DataForSEO
  2.  Parses competitor content (word count, headings, topics covered)
  3.  Extracts People Also Ask questions
  4.  Pulls related keywords with search volumes
  5.  Detects search intent (informational vs commercial vs transactional)
  6.  Generates a data-driven content brief
  7.  Writes the complete page (Markdown + YAML frontmatter)
  8.  Adds 200-char AI Summary Nugget for LLM citation
  9.  Adds FAQ section from real PAA data
  10. Generates JSON-LD schema markup + inline RDFa entities
  11. Validates every claim against 2+ sources (Entity Consensus)
  12. Validates against 41-point quality checklist
  13. Prints scorecard so you see exactly what passed
```

For rewrites, point it at any URL. It compares your page against the current top 3 ranking competitors, identifies exactly what you're missing, and rewrites with a change summary explaining every edit.

---

## The SEO Knowledge Inside

This isn't a wrapper around "write me an SEO article." The skill encodes strategies from the best in the game:

**Traditional SEO**
- Intent-first content architecture (match what searchers actually want, not what you think the keyword means)
- Competitive word count targeting (page length based on what's ranking, not arbitrary "write 2000 words")
- Heading hierarchy derived from SERP analysis (not templates, not guesswork)
- People Also Ask coverage as FAQ sections (answer the questions Google already knows people are asking)
- Schema markup patterns by page type (FAQPage, LocalBusiness, HowTo, Product, BreadcrumbList)
- Internal linking suggestions based on actual site data from GSC

**GEO / LLM SEO (Generative Engine Optimization)**
- 200-char AI Summary Nugget at top of every page, designed for Perplexity/Gemini/ChatGPT to cite as a consensus source
- 500-token chunk architecture matching Google AI's retrieval window
- Content structured for AI citation (Perplexity, ChatGPT, Google AI Overviews)
- Entity-rich writing that LLMs can extract and reference
- Depth-over-length philosophy (comprehensive coverage that becomes the authoritative source)
- FAQ patterns that match how AI systems parse and surface answers
- Data-backed claims that AI systems prefer to cite over vague assertions
- RAG targeting: zero-volume long-tail queries that "train" AI to cite your domain
- Off-page sequencing: establish third-party brand footprint before on-page SEO
- Reddit subdomain indexing: seed entity consensus across indexed Reddit layers
- Topical circle enforcement: stay inside your core service topic to avoid diluting AI authority signals
- Recursive fact-checking: every claim validated against 2+ high-ranking sources for Entity Consensus
- Spam resilience: technical relevance density prioritized over "human tone" in quality scoring

**Structural & DOM Signals**
- Semantic HTML containers: `<article>`, `<section>`, `<aside>`, `<main>` in generated HTML for Main Content zone identification
- Proof-term proximity: supporting evidence must live in the same 500-token chunk as its H2 (BERT evaluates within passage window, not page-wide)
- Query Fan-Out facet coverage: each chunk answers a distinct AI sub-query for multiplicative retrieval
- Forensic EMQ check: conditionally require exact-match keyword in H1 based on competitor optimization ratio
- QDD vulnerability detection: UGC in top 10 = HIGH_CONFIDENCE_TAKEOVER opportunity flag
- Site-level entity dominance: niche site architecture beats generalist single-page competitors

**Local / GBP Optimization**
- Ask Maps & conversational GBP optimization (structured data that answers "who has X available?")
- Holiday/exception hours, discrete service items, pre-populated Q&A
- GBP fields treated as AEO markup, not optional admin work
- Map traffic shifting: internal links from high-traffic informational pages to map embeds to boost local engagement signals

**Content Quality Signals (2026 protocols)**
- Mandatory Original Research / Data Experiment block in every page (Google's top E-E-A-T signal: Experience)
- Verification tagging system: every claim tagged with `{{VERIFY}}`, `{{RESEARCH NEEDED}}`, or `{{SOURCE NEEDED}}`
- "Not For You" block: honest section telling readers when this option is a bad fit (trust signal competitors skip)
- Information Gain Test: every page must contain content not found in the top 10 Google results

**The 41-point quality checklist every page runs through (selected highlights):**
- Information gain over top 10 Google results? Check.
- Reddit Test: would a practitioner upvote this? Check.
- Core answer in first 150 words? Check.
- Fast-scan summary within first 200 words? Check.
- 2+ hard operational Prove-It facts? Check.
- Real HTML tables (not bullet lists)? Check.
- Every section doing a unique job (no repetition)? Check.
- All specific numbers tagged with `{{VERIFY}}`? Check.
- All citations specific and traceable? Check.
- "Not For You" block present? Check.
- 500-token chunk architecture? Check.
- No banned phrases or patterns? Check.
- Word count within competitive range? Check.
- JSON-LD schema block matching page type? Check.
- FAQ section with 3+ PAA questions? Check.
- Hub/spoke internal links? Check.
- Title tag <60 chars with target keyword? Check.
- Meta description <155 chars with value prop? Check.
- Content inside site's core topical circle? Check.
- `reddit_test` and `information_gain` in frontmatter? Check.
- Single H1 tag only? Check.
- No exact-match keyword in meta description? Check.
- No keyword stuffing in H2/H3/H4 tags? Check.
- Image alt text descriptive, not keyword-stuffed? Check.
- AI Summary Nugget (200-char) at top of page? Check.
- Original Research / Data Experiment block present? Check.
- Map-to-informational internal link (local pages)? Check.
- Every claim validated against 2+ sources? Check.

- QDD check run -- UGC in top 10 flagged or cleared? Check.
- Site vs. Page audit -- competitor type identified? Check.
- Forensic EMQ ratio checked -- applied correctly? Check.
- Each 500-token chunk targets a distinct QFO facet? Check.
- ICP defined in brief and content tailored to their pain points? Check.
- Deep entity history / identity tags included where applicable? Check.
- No keyword cannibalization with existing site URLs? Check.

Pages scoring below 33/41 get flagged with specific items to fix. The scorecard is printed at the end of every output so you see exactly what passed.

---

## Data Integrations (BYOK)

Bring your own API keys. Use one, use all. The skill adapts:

| Integration | What It Provides | Required? |
|---|---|---|
| **DataForSEO** | Live SERP results, keyword volumes, People Also Ask, competitor content parsing | Yes (core) |
| **Google Search Console** | Your actual query data, CTR, positions, cannibalization detection | Optional |
| **Ahrefs** (via MCP) | Backlink profiles, domain authority, referring domains | Optional |
| **SEMRush** (via MCP) | Traffic estimates, keyword gaps, competitive positioning | Optional |

No keys at all? The skill falls back to web search. You lose precision but the workflow still runs.

---

## Install + Setup

### Step 1: Install the skill

Pick your platform:

**Claude Code (Mac app / CLI):**
1. Download the [latest release zip](https://github.com/gbessoni/seo-agi/archive/refs/heads/main.zip)
2. In Claude Code, go to **Settings > Skills > Upload skill**
3. Drag the `.zip` file into the upload dialog

Or install via CLI:
```bash
claude install-skill gbessoni/seobuild-onpage
```

**OpenClaw:**
```bash
git clone https://github.com/gbessoni/seobuild-onpage.git ~/.claude/skills/seo-agi
```

**Codex:**
```bash
git clone https://github.com/gbessoni/seobuild-onpage.git ~/.codex/skills/seo-agi
```

**Manual (any platform):**
```bash
git clone https://github.com/gbessoni/seobuild-onpage.git ~/.claude/skills/seo-agi
```

### Step 2: Install Python dependency

```bash
pip install requests
```

### Step 3: Configure API keys (optional but recommended)

```bash
mkdir -p ~/.config/seo-agi
cp ~/.claude/skills/seo-agi/.env.example ~/.config/seo-agi/.env
```

Then edit `~/.config/seo-agi/.env` with your keys:

```env
# DataForSEO -- sign up at https://dataforseo.com (~$0.002/query)
DATAFORSEO_LOGIN=your_email@example.com
DATAFORSEO_PASSWORD=your_password

# Google Search Console (optional)
GSC_SERVICE_ACCOUNT_PATH=/path/to/service-account.json
```

**No API keys?** The skill still works. It falls back to Ahrefs/SEMRush MCP tools (if connected) or web search. You lose SERP content parsing but the framework still writes quality pages.

### Step 4: Verify it works

```bash
# Test the research pipeline (uses mock data, no API keys needed)
python3 ~/.claude/skills/seo-agi/scripts/research.py "airport parking JFK" --mock --output=compact
```

You should see SERP results, PAA questions, related keywords, and heading structure data. If you see that, you're good.

### Step 5: Use it

Open Claude Code (or OpenClaw, or Codex) and type:

```
Write an SEO page for "airport parking JFK"
```

The skill auto-triggers on SEO content requests. It will:
1. Run the research script to pull competitive data
2. Show you a content brief and confirm before writing
3. Write the full page following the SEO-AGI framework
4. Validate against the quality checklist
5. Save to `~/Documents/SEO-AGI/pages/`

---

## Verify Your Setup (Troubleshooting)

**Check if the skill is installed:**
```bash
ls ~/.claude/skills/seo-agi/SKILL.md && echo "Installed" || echo "Not found"
```

**Check if API keys are configured:**
```bash
cat ~/.config/seo-agi/.env 2>/dev/null || echo "No .env file -- skill will use fallback mode"
```

**Test with live DataForSEO (if you have keys):**
```bash
python3 ~/.claude/skills/seo-agi/scripts/research.py "best crm software" --output=compact
```

**Run unit tests:**
```bash
cd ~/.claude/skills/seo-agi
python3 tests/test_env.py && python3 tests/test_serp_analyze.py && python3 tests/test_dataforseo.py
```

---

## Use Cases

**Exact-match domain play**: Research competitor's top pages with OpenClaw, generate equivalent content with `/seoagi`, buy the domains, publish. Page 1.

**Location page generation**: `/seoagi "plumber in [city]"` x 50 cities. Each page gets city-specific research, local PAA questions, LocalBusiness schema. Not cookie-cutter templates.

**Content refresh**: Point it at your underperforming URLs. It pulls your actual GSC data, compares against current top 3, and tells you exactly what to add, expand, or restructure. Then does it.

**Competitive intelligence**: `/seoagi research "competitor keyword"` gives you the full landscape without writing anything. Word count ranges, heading structures, topic gaps, related keywords with volumes.

**Brief handoff**: `/seoagi brief "keyword"` generates a structured content brief you can hand to a human writer. Research-backed, not vibes-based.

---

## The Workflow That Got Me Here

I've been running this workflow manually for 20 years across ParkingAccess.com (1M+ bookings) and Shuttlefare.com (2M+ rides). The pattern never changed:

1. Find what's ranking
2. Figure out what they cover that you don't
3. Write something deeper
4. Add the technical SEO (schema, meta, structure)
5. Publish and move on

seobuild-onpage is that pattern, automated. The 20 years of pattern recognition compressed into a SKILL.md file, backed by live data APIs, running inside a super agent that can decompose and parallelize the work.

It's not AI replacing SEO expertise. It's SEO expertise finally having the right delivery mechanism.

---

## Testing

See "Verify Your Setup" above for full test commands. Quick version:

```bash
cd ~/.claude/skills/seo-agi

# Unit tests (no API keys needed)
python3 tests/test_env.py && python3 tests/test_serp_analyze.py && python3 tests/test_dataforseo.py

# Mock mode (full pipeline with fixture data)
python3 scripts/research.py "airport parking JFK" --mock --output=compact

# No-creds mode (returns skeleton for agent to fill via MCP/WebSearch)
python3 scripts/research.py "test keyword" --output=compact
```

---

## Contributing

Open source, MIT license. PRs welcome.

The skill is modular. Want to add a new page template? Edit `references/page-templates.md`. New schema pattern? `references/schema-patterns.md`. Better quality checks? `references/quality-checklist.md`. New data source? Add a client in `scripts/lib/` and wire it into `research.py`.

---

## Credits

Built by [Greg Bessoni](https://github.com/gbessoni) ([@gregbessoni](https://x.com/gregbessoni)).

## License

MIT
