---
company_name: Greptile
legal_name: Greptile Inc.
founded: 2023
headquarters: San Francisco, CA
sector: AI-Powered Developer Tools
sub_sector: AI Code Review / Code Validation
website: https://www.greptile.com
status: Private (Series A)
valuation: ~$180M (post-money, September 2025)
total_funding: ~$29M
employee_count: ~10-15 (estimated, 2025)
key_investors:
- Benchmark Capital
- Initialized Capital
- Y Combinator
notable_backers:
- Cory Levy
founders:
- name: Daksh Gupta
  role: CEO
  background: Georgia Tech; distributed systems engineering leader
  origin: Indian
- name: Soohoon Choi
  role: Co-Founder
  background: Georgia Tech; co-founded Greptile in 2023
  origin: Korean
- name: Vaishant Kameswaran
  role: Co-Founder
  background: Georgia Tech; co-founded Greptile in 2023
  origin: Indian
last_updated: 2026-03-20
confidence: high
one_liner: Greptile is an AI-powered code review and code validation platform that indexes entire codebases to perform deep,
  context-aware code review
website_verified: true
crunchbase: https://www.crunchbase.com/organization/greptile
crunchbase_verified: true
total_raised_m: 29
funding_rounds:
- stage: Seed
  date: '2024'
  amount_m: 4
  lead_investors:
  - Initialized Capital
  source: https://www.crunchbase.com/organization/greptile
- stage: Series A
  date: 2025-09
  amount_m: 25
  lead_investors:
  - Benchmark Capital
  source: https://www.crunchbase.com/organization/greptile
linkedin: https://www.linkedin.com/company/greptile/
---

# Greptile

## Overview

Greptile is an AI-powered code review and code validation platform that indexes entire codebases to perform deep, context-aware code review. Unlike diff-only review tools, Greptile traces dependencies across files, checks git history, and follows leads across repositories -- mimicking how a senior engineer would review complex changes. The company has reviewed over 500 million lines of code per month for teams at companies including Stripe, Amazon, Brex, and Substack.

## Founders

| Name | Role | Background |
|---|---|---|
| **Daksh Gupta** | CEO & Co-Founder | Georgia Tech graduate (2023). Founded Greptile shortly after graduation. Went through Y Combinator Winter 2024 batch. |
| **Soohoon Choi** | Co-Founder | Georgia Tech graduate. |
| **Vaishant Kameswaran** | Co-Founder | Georgia Tech graduate. |

## Funding History

| Round | Date | Amount | Valuation | Lead Investor(s) |
|-------|------|--------|-----------|-------------------|
| Seed | ~2024 | $4M | Undisclosed | Initialized Capital |
| Series A | Sep 2025 | $25M | ~$180M | Benchmark Capital |
| **Total** | | **~$29M** | | |

The Series A was led by Benchmark partner Eric Vishria. Y Combinator and angel investor Cory Levy also participated.

## Product and Technology

### Full Codebase Indexing

Greptile indexes the entire codebase to build a semantic understanding of architecture, patterns, and dependencies. This enables it to catch issues that diff-only tools miss: cross-file dependency breaks, architectural drift, and convention violations.

### Multi-Hop Investigation

Starting with v3, Greptile performs multi-hop investigation when reviewing pull requests -- tracing dependencies, checking git history, and following leads across files, much like an experienced engineer would when reviewing complex changes.

### Greptile Agent v4 (March 2026)

The latest version features improved bug detection and a significantly lower false positive rate, addressing a key pain point in automated code review.

### Key Metrics

- Reviews 500M+ lines of code per month
- Used by 250+ companies including Stripe, Amazon, Brex, Substack, and Bilt
- Claims: merge 4x faster, catch 3x more bugs

## Business Model

- SaaS platform integrated with GitHub and other code hosting platforms
- Paid plans for teams and enterprises
- Positioned as a code validation layer for both human-written and AI-generated code

## What Makes Greptile Interesting

1. **Benchmark-led Series A at 23 years old.** Daksh Gupta founded Greptile fresh out of college and landed a Benchmark-led Series A at a $180M valuation within two years. Benchmark's involvement (Eric Vishria, who also backed GitHub) is a strong signal.

2. **Full codebase indexing is the right approach for code review.** Most AI code review tools only look at the diff. Greptile's full codebase understanding allows it to catch architectural issues, dependency breaks, and convention violations that diff-only tools are structurally blind to.

3. **Quality gate for the AI-generated code era.** As AI coding assistants produce more code, the need for an independent validation layer becomes critical. Greptile is well-positioned alongside CodeRabbit in this growing market.

4. **Impressive customer roster for an early-stage startup.** Stripe, Amazon, Brex, and Substack represent validation from sophisticated engineering organizations.

5. **Lean team with high output.** With an estimated 10-15 employees processing 500M+ lines of code per month, the team is remarkably capital-efficient.

## Competitive Landscape

- **CodeRabbit** -- direct competitor, also AI code review, raised $60M Series B at $550M valuation
- **Graphite** -- acquired by Cursor (Anysphere) in December 2025
- **Qodo** -- AI code quality and testing
- **Traditional tools** -- SonarQube, Codacy, legacy static analysis

## Key Uncertainties

- Revenue figures are not publicly disclosed
- Whether the lean team can scale to meet enterprise demand
- How defensible the product is against GitHub building native AI review capabilities
- Competition with well-funded CodeRabbit in the same category

## Sources

- [TechCrunch: Benchmark backs AI-code review startup Greptile](https://techcrunch.com/2025/07/18/benchmark-in-talks-to-lead-series-a-for-greptile-valuing-ai-code-reviewer-at-180m-sources-say/)
- [SiliconANGLE: Greptile bags $25M in funding](https://siliconangle.com/2025/09/23/greptile-bags-25m-funding-take-coderabbit-graphite-ai-code-validation/)
- [Greptile: State of AI Coding 2025](https://www.greptile.com/state-of-ai-coding-2025)
- [TechFundingNews: AI startup Greptile eyes $180M valuation](https://techfundingnews.com/ai-startup-greptile-eyes-180m-valuation-to-disrupt-future-of-ai-code-review/)
