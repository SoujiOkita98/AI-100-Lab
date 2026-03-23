# AI-100-Lab

**A research-grade database of 600+ AI and robotics startups worldwide — funding rounds, founder profiles, investor networks, and origin analysis.**

Built with research-grade rigor: every claim is sourced, uncertainty is marked explicitly, and quality takes precedence over completeness.

---

## At a Glance

| Metric | Count |
|--------|------:|
| Companies | 615 |
| Funding rounds | 1,259 |
| Founders tracked | 1,314 |
| 2025 seed rounds | 180+ |
| 2026 seed rounds | 30+ |
| Countries covered | 20+ |

## Data Quality

| Field | Coverage | Notes |
|-------|:--------:|-------|
| Company name | 100% | |
| Founded year | 100% | |
| Sector/category | 98% | Multi-tag taxonomy |
| Website URL | 96% | Verified via HTTP request |
| HQ location | 95% | City + country |
| One-liner description | 97% | Auto-extracted from narrative body where available |
| Total funding raised | 94% | In millions USD, normalized across currencies |
| Round amount | 97% | Per-round detail for 1,045 rounds |
| Lead investors | 92% | Per-round |
| Founder profiles | 93% | Name, role, background, origin |
| Source URL | 73% | Traceable to original reporting |
| Founder background | 66% | Education, prior companies, notable experience |
| LinkedIn | 44% | Company page URLs |
| Latest valuation | 32% | Sparse for seed/early stage (market reality) |
| Revenue signals | 8% | Only where publicly disclosed |

---

## Repository Structure

```
AI-100-Lab/
  companies/           # 615 markdown files — one per company
  exports/             # Clean CSV + JSON exports (rebuilt on demand)
    companies_clean.csv
    rounds_clean.csv
    founders_clean.csv
    companies_clean.json
  schema/              # Schema definitions, sector taxonomy, field glossary
  scripts/             # Data pipeline scripts (parsers, scrapers, exporters)
  logos/               # Company logos (where collected)
  data/                # Raw data files
```

## Company File Format

Each company is a single markdown file with **YAML frontmatter** (structured data) and a **markdown body** (narrative research). Example:

```yaml
---
name: "Anthropic"
founded: 2021
headquarters: "San Francisco, CA"
website: "https://www.anthropic.com"
sector: ["AI safety", "foundation models", "enterprise AI"]
one_liner: "AI safety company building Claude, the leading enterprise LLM."
status: active

total_raised_m: 67300
latest_valuation_m: 380000

founders:
  - name: "Dario Amodei"
    role: "CEO"
    background: "PhD biophysics Princeton. VP Research at OpenAI."
    origin: "Italian-American"
  - name: "Daniela Amodei"
    role: "President"
    background: "BA English Literature UC Santa Cruz. VP Safety at OpenAI."
    origin: "Italian-American"

funding_rounds:
  - stage: "Series A"
    date: "2021-05"
    amount_m: 124
    valuation_m: 550
    lead_investors: ["Jaan Tallinn", "Dustin Moskovitz"]
    source: "https://..."

team_china_profile: "No known Chinese-origin founders."
revenue_signals: "$19B annualized revenue as of March 2026."
confidence: high
last_updated: 2026-03-20
---

# Anthropic

## Overview
Anthropic is an AI safety company and one of the three leading frontier model labs...
```

---

## Taxonomy & Tags

### Sector Categories

Companies are tagged with one or more sectors from this taxonomy:

| Category | Examples | Count |
|----------|---------|------:|
| **Foundation Models** | OpenAI, Anthropic, Mistral, DeepSeek, xAI | 30+ |
| **AI Infrastructure / Cloud** | Baseten, Together AI, Lambda, CoreWeave, Nscale | 25+ |
| **AI Chips / Semiconductors** | Etched, Cerebras, d-Matrix, Groq, Celestial AI | 25+ |
| **AI-Powered Developer Tools** | Cursor/Anysphere, Augment Code, Windsurf, Cognition AI | 20+ |
| **AI Agents / Automation** | Sierra, /dev/agents, LangChain, Braintrust, CrewAI | 20+ |
| **AI Healthcare / Biotech** | Hippocratic AI, Abridge, OpenEvidence, Rad AI | 25+ |
| **AI Cybersecurity** | 7AI, Sola Security, Cylake, Tenzai, Oasis Security | 15+ |
| **Humanoid Robotics** | Figure AI, 1X Technologies, Apptronik, AgiBot, Unitree | 15+ |
| **AI Drug Discovery** | Xaira, Chai Discovery, Insilico Medicine, XtalPi | 12+ |
| **AI Voice / Audio** | ElevenLabs, Deepgram, Gradium, Wispr AI | 10+ |
| **AI Video / Media** | Runway, Pika, Luma AI, Synthesia, Fal, Higgsfield | 10+ |
| **AI Legal** | Harvey AI, Luminance, Paxton, Eudia, Spellbook | 8+ |
| **AI Finance / Fintech** | Kalshi, Samaya AI, Basis, Numeric | 8+ |
| **AI Defense / GovTech** | Anduril, Shield AI, Overland AI, NODA AI, Pryzm | 10+ |
| **AI for Science** | Periodic Labs, CuspAI, Lila Sciences, WindBorne | 8+ |
| **AI EdTech** | MagicSchool AI, Brisk Teaching, Oboe | 5+ |
| **AI Gaming** | General Intuition, Sett, Studio Atelico, Iconic | 5+ |
| **AI Climate / Energy** | Emerald AI, OCELL, Tibo Energy | 5+ |

### Founder Origin Tags

Founder ethnicity/national origin is tracked where publicly known or inferable from names and backgrounds. Top categories:

| Origin | Founders |
|--------|--------:|
| American | 178 |
| Indian-American | 42 |
| Israeli | 41 |
| Chinese-American | 35 |
| Chinese | 26 |
| German | 22 |
| Indian | 21 |
| French | 19 |
| British | 18 |
| Dutch | 11 |
| Canadian | 8 |
| Swedish | 7 |

### Geographic Coverage

| Region | Companies |
|--------|----------:|
| California, US | 192 |
| New York, US | 28 |
| Other US | 17 |
| China | 31 |
| United Kingdom | 27 |
| Israel | 15 |
| France | 10 |
| Germany | 6 |
| Canada | 6 |
| South Korea | 3 |
| Australia | 3 |
| India | 2 |
| Other (20+ countries) | 52 |

---

## Methodology

### Data Collection Sources

This database was built through systematic multi-source research, not a single data provider:

| Source | Method | What It Captures |
|--------|--------|-----------------|
| **VC Portfolio Pages** | Browser automation (browser-use CLI) scraping a16z, Index Ventures, Khosla Ventures, Greylock, General Catalyst, Accel, Felicis, Bessemer, NEA, Thrive, Coatue, Tiger Global | Portfolio companies, including stealth investments |
| **TechCrunch Roundup Articles** | Definitive "$100M+ AI startups" lists cross-referenced | Authoritative coverage of major rounds |
| **Crunchbase News** | Free articles and weekly roundups | Funding announcements, valuations |
| **StartupHub.ai** | Structured funding round data | 2025 AI funding deals |
| **startups.gallery** | Curated early-stage AI list | VC-vetted seed-stage companies |
| **Y Combinator Directory** | W24, S24, W25, S25 batch scraping | Early-stage AI companies |
| **SEC EDGAR Form D Filings** | Public fundraising filings via FormDs.com | Under-the-radar companies with zero press |
| **Regional Tech Press** | Sifted (EU), TechNode (China), KrASIA (Asia), YourStory (India), etc. | International companies missed by US outlets |
| **Weekly Funding Aggregators** | PYMNTS, SiliconANGLE, VentureBeat, HackerNoon, Crescendo.ai | Smaller deals ($3–20M) not covered individually |
| **Company Websites & Press Releases** | Direct verification | Product info, team bios, logos |
| **Web Search** | Google for specific companies, sectors, and geographies | Gap-filling and verification |

### Data Quality Principles

1. **Quality over completeness** — An empty field is better than a fabricated one
2. **Every claim is sourced** — Funding amounts link to original reporting where possible
3. **Uncertainty is explicit** — `confidence: low/medium/high` per company; unconfirmed rounds marked
4. **Schema is a guide, not a cage** — Capture what's interesting, skip what's not findable
5. **Name-based origin inference** — Founder ethnicity inferred from names + backgrounds + public info; marked as inference not confirmed fact

### Known Limitations

- **Valuation data is sparse for seed/early stage** — most startups don't disclose seed valuations (35% coverage)
- **Revenue data is rare** — only 11% of companies have revenue signals (private company reality)
- **Coverage is biased toward English-language media** — Chinese, Japanese, Korean companies are underrepresented
- **Paywalled databases not used** — No Crunchbase Pro or PitchBook access; SEC EDGAR partially compensates
- **Employee counts are stale** — Only 42% coverage, often from time of last funding announcement

---

## Exports

Clean, analysis-ready exports are in `exports/`:

| File | Rows | Description |
|------|-----:|-------------|
| `companies_clean.csv` | 615 | One row per company — all normalized fields |
| `rounds_clean.csv` | 1,259 | One row per funding round — stage, date, amount, valuation, investors |
| `founders_clean.csv` | 1,314 | One row per founder — name, role, background, origin |
| `companies_clean.json` | 615 | Nested format — company + founders + rounds combined |

### CSV Field Reference

**companies_clean.csv:**
`slug, name, status, founded_year, hq, website, sector, one_liner, total_raised_m, latest_valuation_m, employees, revenue_signals, business_model, key_customers, team_china_profile, confidence, last_updated`

**rounds_clean.csv:**
`company_slug, stage, date, amount_m, valuation_m, lead_investors, other_investors, source, notes`

**founders_clean.csv:**
`company_slug, name, role, background, origin, prior`

---

## Scripts

| Script | Purpose |
|--------|---------|
| `scripts/rebuild_clean_export.py` | Parse all 615 markdown files and regenerate clean CSV/JSON exports |
| `scripts/inject_rounds.py` | Inject funding round data into existing company frontmatter from JSON |
| `scripts/create_company.py` | Create new company markdown files from JSON input |
| `scripts/overnight_pipeline.py` | Systematic VC portfolio scraper using browser-use CLI |
| `scripts/vc_scraper.py` | Generic VC portfolio scraping utilities |

---

## How to Use

**Rebuild exports after editing company files:**
```bash
python3 scripts/rebuild_clean_export.py
```

**Add new companies from JSON:**
```bash
python3 scripts/create_company.py new_companies.json
```

**Inject funding rounds into existing companies:**
```bash
python3 scripts/inject_rounds.py rounds_data.json
```

---

## Example Queries

With the CSV exports, you can answer questions like:

- **Rank all 2025 AI seed rounds by amount raised** → Filter `rounds_clean.csv` for `stage=Seed` and `date LIKE '2025%'`, sort by `amount_m`
- **Which VCs lead the most AI rounds?** → Parse `lead_investors` column in `rounds_clean.csv`
- **Founder origin breakdown by sector** → Join `founders_clean.csv` with `companies_clean.csv` on `company_slug`
- **Chinese-founded AI startups and their total funding** → Filter founders by `origin LIKE '%Chinese%'`
- **Fastest-growing startups by valuation trajectory** → Track `valuation_m` across rounds per company

---

## License

This dataset is released under the **[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)** license. Data is aggregated from public sources — press releases, news articles, SEC filings, and company websites.

**If you use this dataset, please credit the maintainer — it means a lot:**

```
Dataset: AI-100-Lab by Gavin Zhu (@SoujiOkita98)
https://github.com/SoujiOkita98/AI-100-Lab
```

Or tag [@SoujiOkita98](https://github.com/SoujiOkita98) in your work. Thank you!

---

*Built with [Claude Code](https://claude.ai/claude-code) by Anthropic. Maintained by [Gavin Zhu](https://github.com/SoujiOkita98). Last updated: March 2026.*
