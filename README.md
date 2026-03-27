# AI-100-Lab

**A research-grade database of 1,007 AI and robotics startups worldwide — funding rounds, founder profiles, investor networks, and origin analysis.**

Built with research-grade rigor: every claim is sourced, uncertainty is marked explicitly, and quality takes precedence over completeness.

---

## At a Glance

| Metric | Count |
|--------|------:|
| Companies | 1,007 |
| Funding rounds | 2,043 |
| Founders tracked | 2,202 |
| Countries covered | 30+ |

## Data Quality

| Field | Coverage | Notes |
|-------|:--------:|-------|
| Company name | 100% | |
| Founded year | 91% | |
| Website URL | 100% | Verified via HTTP request |
| HQ location | 100% | City + country |
| One-liner description | 100% | |
| Sector/category | 100% | Multi-tag taxonomy |
| Total funding raised | 99% | In millions USD, normalized across currencies |
| Founder names | 100% | 2,202 founders with verified names |
| Founder background | ~80% | Education, prior companies, notable experience |
| Round amount | ~88% | Per-round detail for 2,043 rounds |
| Lead investors | ~94% | Per-round |
| Source URL | ~79% | Traceable to original reporting |
| Latest valuation | 22% | Most startups don't disclose (market reality) |
| Revenue signals | 6% | Only where publicly disclosed |

### Honest Caveats

- **Founder "background" is ~80%, not 100%.** All 1,007 companies have founder names and roles, but some have name+role only — no education or work history.
- **Valuation data is growing.** 226 companies now have a recorded valuation (22%), up from ~4%. Seed and early-stage companies rarely disclose.
- **Funding totals may undercount earlier rounds.** A random validation of 20 companies found only 8-9 had fully correct totals. We back-filled missing rounds but gaps likely remain.
- **Coverage is biased toward English-language media.** China (65), Japan (3), India (8) are still underrepresented relative to their AI ecosystems.

---

## Repository Structure

```
AI-100-Lab/
  companies/           # 1,026 markdown files — one per company (THE source of truth)
  exports/             # Generated outputs (rebuilt by CI on every push)
    companies.csv
    founders.csv
    rounds.csv
    companies.json     # Nested format — company + founders + rounds
    ai100lab.db        # SQLite database for querying
  schema/              # Schema definitions and sector taxonomy
    database-schema.json
    sectors.yaml
    company-template.md
  scripts/             # Active pipeline scripts
    rebuild_exports.py
    create_company.py
    validate_schema.py
    generate_dashboard.py
    verify_urls.py
  docs/                # GitHub Pages dashboard
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

confidence: high
last_updated: 2026-03-20
---

# Anthropic

## Overview
Anthropic is an AI safety company and one of the three leading frontier model labs...
```

---

## Geographic Coverage

| Region | Companies |
|--------|----------:|
| California, US | 529 |
| New York, US | 87 |
| Other US | 87 |
| China / Hong Kong | 65 |
| United Kingdom | 57 |
| Israel | 43 |
| Germany | 22 |
| France | 20 |
| Canada | 13 |
| India | 8 |
| South Korea | 6 |
| Japan | 3 |
| Other (30+ countries) | 67 |

## Top Founder Origins

| Origin | Founders |
|--------|--------:|
| American | 503 |
| Chinese | 166 |
| Indian | 152 |
| Israeli | 142 |
| Chinese-American | 126 |
| Indian-American | 113 |
| German | 63 |
| French | 60 |
| British | 54 |
| Canadian | 25 |
| Korean | 19 |
| Iranian-American | 17 |
| Dutch | 17 |
| Swedish | 14 |

---

## Methodology

### Data Collection Sources

This database was built through systematic multi-source research, not a single data provider:

| Source | Method | What It Captures |
|--------|--------|-----------------|
| **VC Portfolio Pages** | Browser automation scraping a16z, Index, Khosla, Greylock, General Catalyst, Accel, Felicis, Bessemer, NEA, Thrive, Coatue, Tiger Global | Portfolio companies, including stealth investments |
| **startups.gallery** | Sitemap cross-referencing (1,254 companies compared against our DB) | 86 AI companies we were missing, systematic gap-fill |
| **Y Combinator Directory** | Batch-by-batch sweep: W22, S22, W23, S23, W24, S24, W25, S25 | 43 early-stage AI companies |
| **TechCrunch Roundup Articles** | Definitive "$100M+ AI startups" lists cross-referenced | Authoritative coverage of major rounds |
| **Crunchbase News** | Free articles and weekly roundups | Funding announcements, valuations |
| **SEC EDGAR Form D Filings** | Public fundraising filings via FormDs.com | Under-the-radar companies with zero press |
| **Regional Tech Press** | Sifted (EU), TechNode (China), KrASIA (Asia), YourStory (India), Calcalist (Israel) | International companies missed by US outlets |
| **Weekly Funding Aggregators** | PYMNTS, SiliconANGLE, VentureBeat, HackerNoon, Crescendo.ai | Smaller deals ($3–20M) not covered individually |
| **Company Websites & Press Releases** | Direct verification | Product info, team bios |
| **Random Validation** | 20-company random audit against Crunchbase/press | Found 8-9/20 correct; drove back-fill of 121 missing rounds |

### Data Quality Principles

1. **Quality over completeness** — An empty field is better than a fabricated one
2. **Every claim is sourced** — Funding amounts link to original reporting where possible
3. **Uncertainty is explicit** — `confidence: low/medium/high` per company; unconfirmed rounds marked
4. **Schema is a guide, not a cage** — Capture what's interesting, skip what's not findable
5. **Name-based origin inference** — Founder ethnicity inferred from names + backgrounds + public info; marked as inference not confirmed fact

### Known Limitations

- **Valuation data is sparse** — Only 22% of companies have a recorded valuation
- **Revenue data is rare** — Only 6% have revenue signals (private company reality)
- **Coverage is biased toward English-language media** — Chinese, Japanese, Korean companies are underrepresented
- **Paywalled databases not used** — No Crunchbase Pro or PitchBook access; SEC EDGAR partially compensates
- **Founder backgrounds are incomplete** — ~80% have full profiles; ~20% have name+role only
- **Funding totals may undercount** — Systematic undercounting of earlier rounds (pre-seed/seed) is a known issue

---

## Exports

Clean, analysis-ready exports are in `exports/`:

| File | Rows | Description |
|------|-----:|-------------|
| `companies.csv` | 1,026 | One row per company — all normalized fields |
| `rounds.csv` | 2,096 | One row per funding round — stage, date, amount, valuation, investors |
| `founders.csv` | 2,249 | One row per founder — name, role, background, origin |
| `companies.json` | 1,026 | Nested format — company + founders + rounds combined |
| `ai100lab.db` | — | SQLite database for direct querying |

### CSV Field Reference

**companies.csv:**
`slug, name, status, founded_year, hq, website, sector, one_liner, total_raised_m, latest_valuation_m, employees, revenue_signals, business_model, key_customers, confidence, last_updated`

**rounds.csv:**
`company_slug, stage, date, amount_m, valuation_m, lead_investors, other_investors, source, notes`

**founders.csv:**
`company_slug, name, role, background, origin, prior`

---

## Scripts

| Script | Purpose |
|--------|---------|
| `scripts/rebuild_exports.py` | **THE canonical pipeline** — parse all markdown files, regenerate CSV/JSON/SQLite exports |
| `scripts/create_company.py` | Create new company markdown files from JSON input |
| `scripts/validate_schema.py` | Schema validation — reports deviations from canonical schema (read-only) |
| `scripts/generate_dashboard.py` | Generate the GitHub Pages dashboard from live data |
| `scripts/verify_urls.py` | URL verification — checks website and LinkedIn URLs via HTTP |

---

## How to Use

**Rebuild exports after editing company files:**
```bash
python3 scripts/rebuild_exports.py
```

**Add new companies from JSON:**
```bash
python3 scripts/create_company.py new_companies.json
```

---

## Example Queries

With the CSV exports, you can answer questions like:

- **Rank all 2025 AI seed rounds by amount raised** → Filter `rounds.csv` for `stage=Seed` and `date LIKE '2025%'`, sort by `amount_m`
- **Which VCs lead the most AI rounds?** → Parse `lead_investors` column in `rounds.csv`
- **Founder origin breakdown by sector** → Join `founders.csv` with `companies.csv` on `company_slug`
- **Chinese-founded AI startups and their total funding** → Filter founders by `origin LIKE '%Chinese%'`
- **Fastest-growing startups by valuation trajectory** → Track `valuation_m` across rounds per company
- **YC batch comparison** → Filter by YC batch tag in company profiles

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
