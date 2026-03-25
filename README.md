# SEO-AGI

### One command. Competitive data in. Ranking pages out.

Most SEO tools tell you what's wrong with your site. This one writes the pages.

`/seoagi "airport parking JFK"` pulls the current SERP, analyzes what's ranking, finds the gaps in their content, and writes you a complete page -- with the heading structure, depth, FAQ section, and schema markup that actually competes. Not thin content. Not keyword-stuffed filler. Pages backed by live data from the tools the pros use.

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
  12. Validates against 28-point quality checklist
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

**The 28-point quality checklist every page runs through:**
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

Pages scoring below 22/28 get flagged with specific items to fix. The scorecard is printed at the end of every output so you see exactly what passed.

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
claude install-skill gbessoni/seo-agi
```

**OpenClaw:**
```bash
git clone https://github.com/gbessoni/seo-agi.git ~/.claude/skills/seo-agi
```

**Codex:**
```bash
git clone https://github.com/gbessoni/seo-agi.git ~/.codex/skills/seo-agi
```

**Manual (any platform):**
```bash
git clone https://github.com/gbessoni/seo-agi.git ~/.claude/skills/seo-agi
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

seo-agi is that pattern, automated. The 20 years of pattern recognition compressed into a SKILL.md file, backed by live data APIs, running inside a super agent that can decompose and parallelize the work.

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
