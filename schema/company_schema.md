# Company File Schema — Canonical Reference

Every company file in `companies/` is a markdown file with YAML frontmatter and a markdown body.

## YAML Frontmatter Fields

### Required fields (every company must have these)

| Field | Type | Description |
|-------|------|-------------|
| `name` | string | Company display name |
| `founded` | integer | Year founded (e.g. 2023) |
| `headquarters` | string | "City, State/Country" format |
| `website` | string | Full URL with https:// |
| `sector` | list of strings | Multi-tag taxonomy |
| `one_liner` | string | One sentence, <200 chars |
| `status` | string | "active", "acquired", or "public" |

### Funding fields

| Field | Type | Unit | Description |
|-------|------|------|-------------|
| `total_raised_m` | number | Millions USD | Total equity raised |
| `latest_valuation_m` | number | Millions USD | Most recent valuation |

### Founder fields

```yaml
founders:
  - name: "First Last"        # REQUIRED: string
    role: "CEO"                # REQUIRED: string
    background: "Brief bio"    # OPTIONAL: string (education, prior companies)
    origin: "American"         # OPTIONAL: string (nationality/ethnicity)
```

**DO NOT USE:** `education`, `nationality`, `ethnicity`, `prior_experience`, `notable`, `age_approx`, `source` as founder sub-fields. Put education and experience into `background`. Put nationality/ethnicity into `origin`.

### Funding round fields

```yaml
funding_rounds:
  - stage: "Series A"          # REQUIRED: string (Seed, Series A/B/C, etc.)
    date: "2025-06"            # REQUIRED: string (YYYY-MM or YYYY)
    amount_m: 50               # number, in MILLIONS USD
    valuation_m: 200           # number, in MILLIONS USD
    lead_investors: ["Name"]   # list of strings
    other_investors: ["Name"]  # list of strings
    source: "https://..."      # URL to source article
    notes: "..."               # optional string
```

**DO NOT USE:**
- `amount_usd` — use `amount_m` (in millions)
- `valuation_usd` — use `valuation_m` (in millions)
- `amount` — use `amount_m`
- `valuation` — use `valuation_m`
- `round` — use `stage`
- `lead_investor` — use `lead_investors` (plural, list)
- `amount_eur` — convert to USD millions and use `amount_m`

### Optional metadata fields

| Field | Type | Description |
|-------|------|-------------|
| `linkedin` | string | LinkedIn company page URL |
| `linkedin_verified` | boolean | HTTP-verified |
| `twitter` | string | Twitter/X URL |
| `crunchbase` | string | Crunchbase URL |
| `employees` | string or integer | Headcount |
| `revenue_signals` | string | Public revenue info |
| `confidence` | string | "low", "medium", or "high" |
| `last_updated` | string | YYYY-MM-DD format |
| `data_notes` | string | Notes about data quality/gaps |

### Fields that should NOT exist at company level

These are non-standard and should be removed or renamed:
- `company`, `company_name` → use `name`
- `hq`, `location`, `hq_city`, `hq_country` → use `headquarters`
- `total_funding_usd`, `total_funding`, `total_raised` → use `total_raised_m`
- `latest_valuation`, `valuation` → use `latest_valuation_m`
- `stage` (at company level) → remove (stage belongs in rounds)
- `slug`, `domain`, `legal_name` → remove (slug is the filename)
- `tags` → use `sector`

## Markdown Body

After the `---` closing the frontmatter, the body contains narrative research in standard markdown. No required structure, but typically includes `# Company Name` heading and `## Overview` section.
