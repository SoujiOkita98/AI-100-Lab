# AI-100-Lab

Top 100 AI and robotics startups operating in the US — research database.

## Structure

```
AI-100-Lab/
  companies/         # One markdown per company (narrative + YAML frontmatter)
  schema/            # Schema definition, sector taxonomy, field glossary
  scripts/           # Any helper scripts (CSV generation, validation)
  exports/           # Generated outputs (master CSV, filtered views)
```

## How it works
- Claude gathers data per company into `companies/`
- Each file has YAML frontmatter (structured) + markdown body (narrative)
- Master CSV in `exports/` is regenerated from company files on demand
- Schema definitions in `schema/` keep things consistent

## Scope
- AI and robotics startups operating in the US
- Includes: foundation models, infra, dev tools, agents, applied AI, robotics, autonomous systems, and anything at the intersection
- Tracks funding history, team backgrounds, founder origin profiles
- Qualitative analysis alongside hard numbers
