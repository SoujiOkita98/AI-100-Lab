---
company_name: Semgrep
legal_name: Semgrep, Inc. (formerly Return to Corporation / r2c)
founded: 2017
headquarters: San Francisco, CA
sector: AI-Powered Developer Tools
sub_sector: AI Code Security / Static Analysis
website: https://semgrep.dev
status: Private (Series D)
valuation: ~$500M-$1B (estimated, February 2025; undisclosed)
total_funding: ~$204M
employee_count: ~210-250 (estimates vary, 2025-2026)
key_investors:
- Menlo Ventures
- Sequoia Capital
- Lightspeed Venture Partners
- Redpoint Ventures
- Felicis Ventures
- Harpoon Ventures
notable_backers: []
last_updated: 2026-03-20
confidence: high
funding_rounds:
- stage: Series A
  date: 2020-10
  amount_m: 13
  lead_investors:
  - Redpoint Ventures
  - Sequoia Capital
  source: https://semgrep.dev/blog/2020/introducing-semgrep-and-r2c/
- stage: Series B
  date: 2021-07
  amount_m: 27
  lead_investors:
  - Felicis Ventures
  source: https://techcrunch.com/2021/07/07/r2c-raises-27m/
- stage: Series C
  date: 2023-04
  amount_m: 53
  lead_investors:
  - Lightspeed Venture Partners
  source: https://www.prnewswire.com/news-releases/semgrep-announces-53m-in-series-c/
- stage: Series D
  date: 2025-02
  amount_m: 100
  lead_investors:
  - Menlo Ventures
  source: https://news.crunchbase.com/cybersecurity/application-startup-semgrep-fundraise-menlo/
one_liner: Semgrep (formerly r2c / Return to Corporation) is an AI-powered code security platform that combines deterministic
  static analysis with large language models to find vulnerabilities in code
website_verified: true
crunchbase: https://www.crunchbase.com/organization/semgrep
crunchbase_verified: true
founders:
- name: Isaac Evans
  role: CEO & Co-Founder
  background: MIT alumnus. Led development of the open-source Semgrep tool.
  origin: American
- name: Drew Dennison
  role: CTO & Co-Founder
  background: MIT alumnus. Technical lead for the Semgrep engine and platform.
  origin: American
- name: Luke O'Malley
  role: CPO & Co-Founder
  background: MIT alumnus. Leads product strategy and design.
  origin: American
linkedin: https://www.linkedin.com/company/semgrep/
name: Semgrep
---

# Semgrep

## Overview

Semgrep (formerly r2c / Return to Corporation) is an AI-powered code security platform that combines deterministic static analysis with large language models to find vulnerabilities in code. The company's core insight is that neither traditional rule-based scanning nor pure LLM-based analysis is sufficient alone -- combining both yields higher true positive rates with lower false positive rates. Semgrep's platform scans code in the editor, at commit time, and in CI pipelines, serving customers including Snowflake, Lyft, Spotify, Figma, Plaid, and Intuit.

## Founders

| Name | Role | Background |
|---|---|---|
| **Isaac Evans** | CEO & Co-Founder | MIT background. Led the development of the open-source Semgrep tool. |
| **Drew Dennison** | CTO & Co-Founder | Technical lead for the Semgrep engine and platform. |
| **Luke O'Malley** | CPO & Co-Founder | Leads product strategy and design. |

The company originated from the open-source Semgrep static analysis tool, which gained wide adoption in the security community before the commercial platform was built on top of it.

## Funding History

| Round | Date | Amount | Valuation | Lead Investor(s) |
|-------|------|--------|-----------|-------------------|
| Series A | ~2020 | ~$13M | Undisclosed | Redpoint Ventures |
| Series B | ~2021 | $38M | Undisclosed | Felicis Ventures |
| Series C | Apr 2023 | $53M | $395M | Lightspeed Venture Partners |
| Series D | Feb 2025 | $100M | Undisclosed (~$500M-$1B est.) | Menlo Ventures |
| **Total** | | **~$204M** | | |

## Revenue and Growth

| Metric | Value | Source |
|--------|-------|--------|
| 2025 Revenue | ~$33.6M | [Latka](https://getlatka.com/companies/semgrep.dev) |

## Product and Technology

### Open-Source Foundation

Semgrep started as an open-source static analysis tool that allows developers to write custom rules for pattern matching in code. The open-source tool has broad adoption and serves as a top-of-funnel for the commercial platform.

### Commercial Platform

The commercial Semgrep platform adds:

1. **Semgrep Code (SAST)**: AI-enhanced static application security testing
2. **Semgrep Supply Chain (SCA)**: Open-source dependency vulnerability scanning with reachability analysis
3. **Semgrep Secrets**: Detection of hardcoded credentials and API keys
4. **Managed Rules**: Curated vulnerability detection rules maintained by the Semgrep security research team

### Semgrep Multimodal (March 2026)

The latest major product launch combines AI reasoning with rule-based analysis, finding up to 8x more true positives while cutting noise by 50% compared to foundation models alone. This represents Semgrep's core technical thesis: deterministic rules provide precision, while AI provides coverage for complex business logic flaws.

### Semgrep Secure 2026

In February 2026, Semgrep announced AI-powered detection built on a foundation of deterministic static analysis, capable of surfacing both traditional OWASP Top 10 vulnerabilities and complex business logic flaws.

## Business Model

- Freemium model: open-source Semgrep CLI is free; commercial platform is paid
- Enterprise SaaS pricing based on number of developers and repositories
- Target customers: security and engineering teams at technology companies
- Notable customers: Snowflake, Lyft, Spotify, Figma, Plaid, Intuit

## What Makes Semgrep Interesting

1. **The "deterministic + AI" hybrid approach is technically sound.** Pure LLM-based security scanning produces too many false positives. Pure rule-based scanning misses complex vulnerabilities. Semgrep's combination of both -- claiming 8x more true positives with 50% less noise -- is a genuinely differentiated approach.

2. **Open-source flywheel creates distribution moat.** The free, open-source Semgrep tool is widely adopted by security engineers. This creates a natural pipeline to the commercial platform, similar to how GitLab and Elastic built their businesses.

3. **Sequoia + Menlo + Lightspeed investor syndicate signals confidence.** Having three top-tier firms backing the company across rounds is a strong signal.

4. **Blue-chip customer base.** Snowflake, Lyft, Spotify, Figma, Plaid, and Intuit represent exactly the type of high-growth, security-conscious engineering organizations that Semgrep targets.

5. **AI-generated code amplifies demand for code security.** As AI coding assistants produce more code faster, the attack surface expands proportionally. Semgrep is positioned to capture this growing demand for automated security scanning.

6. **Revenue is still modest relative to the opportunity.** ~$33.6M in revenue for a well-funded, well-positioned company suggests significant room for growth -- or potential execution challenges.

## Competitive Landscape

- **Snyk** -- larger, broader developer security platform ($343M ARR)
- **SonarSource / SonarQube** -- traditional code quality and security
- **Veracode, Checkmarx** -- legacy SAST vendors
- **GitHub Advanced Security** (Microsoft) -- integrated CodeQL scanning
- **Endor Labs** -- emerging SCA competitor

## Key Uncertainties

- Exact valuation from the Series D round is undisclosed
- Whether the $33.6M revenue figure from Latka is accurate
- Path to profitability is unclear at this scale
- Competition from both legacy AppSec vendors and Snyk

## Sources

- [Crunchbase News: Application Security Startup Semgrep Locks Down $100M Series D](https://news.crunchbase.com/cybersecurity/application-startup-semgrep-fundraise-menlo/)
- [Semgrep: $100M Series D Announcement](https://www.prnewswire.com/news-releases/semgrep-announces-100m-series-d-funding-to-advance-ai-powered-code-security-302367780.html)
- [TechCrunch: Semgrep (formerly r2c) lands $53M](https://techcrunch.com/2023/04/18/semgrep-formerly-r2c-lands-53m-investment-to-grow-code-security-platform/)
- [Contrary Research: Semgrep Business Breakdown](https://research.contrary.com/company/semgrep)
- [Latka: Semgrep Revenue](https://getlatka.com/companies/semgrep.dev)
- [BusinessWire: Semgrep Launches Multimodal](https://www.businesswire.com/news/home/20260319711078/en/Semgrep-Launches-Multimodal-Combining-AI-Reasoning-With-Rule-Based-Analysis-for-Detection-Triage-and-Remediation)
