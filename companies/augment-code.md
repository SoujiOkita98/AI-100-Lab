---
company_name: Augment Code
legal_name: Augment Computing, Inc.
founded: 2022
headquarters: Palo Alto, CA
sector: AI-Powered Developer Tools
sub_sector: AI Coding Assistants / Agentic Development
website: https://www.augmentcode.com
status: Private (Series B)
valuation: ~$977M (post-money, April 2024)
total_funding: $252M
employee_count: ~156-188 (estimates vary, 2025-2026)
key_investors:
- Index Ventures
- Sutter Hill Ventures
- Lightspeed Venture Partners
- Innovation Endeavors
- Meritech Capital
- Evolution Equity Partners
notable_backers:
- Eric Schmidt (former Google CEO)
last_updated: 2026-03-20
confidence: high
funding_rounds:
- stage: Series A
  date: 2024-01
  amount_m: 25
  lead_investors:
  - Sutter Hill Ventures
  source: https://www.crunchbase.com/funding_round/augment-68db-series-a--b24cdbce
- stage: Series B
  date: 2024-04
  amount_m: 227
  valuation_m: 977
  lead_investors:
  - Sutter Hill Ventures
  source: https://www.augmentcode.com/blog/augment-inc-raises-227-million
one_liner: Augment Code is an enterprise-focused AI coding assistant company that emerged from stealth in April 2024 with
  $252M in total funding and a near-unicorn valuation
website_verified: true
twitter: '@augmentcode'
---

# Augment Code

## Overview

Augment Code is an enterprise-focused AI coding assistant company that emerged from stealth in April 2024 with $252M in total funding and a near-unicorn valuation. The company's core thesis is that existing AI coding tools fail at scale -- they work well on small projects but break down on the large, complex, multi-repository codebases that characterize real enterprise software. Augment's proprietary **Context Engine** is the technical answer to this problem, capable of indexing and semantically understanding 400,000+ files across entire codebases, far beyond the context window limitations of competitors.

## Founders and Leadership

### Guy Gur-Ari -- Co-Founder & CTO

- **Background**: Senior Staff Research Scientist at Google, where he worked on foundational large language model research.
- **Education**: BSc from Hebrew University of Jerusalem (2007); PhD from Weizmann Institute of Science (2014), originally in theoretical physics before pivoting to machine learning.
- **Research Profile**: Over 20,400 citations on Google Scholar. Contributed to major Google AI projects including **PaLM 2** (Google's state-of-the-art language model) and **BIG-bench** (the 204-task benchmark for evaluating LLM capabilities with 442 co-authors across 132 institutions). Also published influential work on deep learning theory, notably showing that gradient descent converges to a tiny subspace of the Hessian.
- **Significance**: Gur-Ari represents the "deep AI research" half of the founding team. His hands-on experience building and evaluating frontier LLMs at Google gives Augment credibility in training custom models tuned specifically for code understanding.

### Igor Ostrovsky -- Co-Founder & CTO [Note: exact current title uncertain; some sources list both founders as co-founders without distinguishing CEO/CTO roles at founding]

- **Background**: Former Chief Architect at Pure Storage; prior experience as a software engineer at Microsoft. Expertise in distributed systems and high-performance infrastructure.
- **Education**: University of British Columbia.
- **Significance**: Ostrovsky brings the systems engineering discipline needed to build a product that handles massive codebases with millisecond-level responsiveness. His Pure Storage connection also links to Scott Dietzen and the broader Pure Storage alumni network in the company.

### Scott Dietzen -- CEO

- **Background**: Former CEO of Pure Storage, where he scaled the company from zero to $1B+ revenue, grew headcount from 15 to thousands, and led a successful IPO. A four-time entrepreneur.
- **Education**: PhD in Computer Science (emphasis on Machine Learning) from Carnegie Mellon University.
- **Significance**: A seasoned enterprise CEO with a rare combination of deep technical credentials and go-to-market experience. His involvement signals serious enterprise ambitions, not just a developer tool but a platform sale.

### Dion Almaer -- VP of Product

- **Background**: Former Google engineering director (Chrome, Search, Android developer products reaching millions of developers); VP of Developer Experience at Shopify; prior roles at Mozilla, Walmart Labs, and Palm.
- **Significance**: Deep product intuition for developer tools, with experience building products at massive scale.

### Broader Team

The engineering team draws heavily from Google, Meta, NVIDIA, Microsoft, Databricks, Snowflake, VMware, and Pure Storage. This "big tech alumni" density is notable -- the team has direct experience building and operating the types of large-scale systems that Augment's enterprise customers maintain.

## Funding History

| Round | Date | Amount | Valuation | Lead Investors |
|-------|------|--------|-----------|----------------|
| Series A | ~2023 (exact date unclear) | $25M | Undisclosed | Sutter Hill Ventures |
| Series B | April 2024 | $227M | $977M post-money | Index Ventures, Sutter Hill Ventures, Innovation Endeavors, Lightspeed Venture Partners, Meritech Capital |
| **Total** | | **$252M** | | |

Evolution Equity Partners also participated in the Series B round (announced November 2024). Eric Schmidt's involvement (likely via Innovation Endeavors, his venture fund) attracted significant press attention.

## Product and Technology

### Context Engine (Core Differentiator)

The Context Engine is Augment's proprietary system for indexing and understanding entire codebases. Key claims:

- Processes **400,000+ files** through semantic chunking (vs. competitors limited to ~100K-200K token context windows)
- Maintains **millisecond-level sync** with ongoing code changes
- Creates semantic embeddings across multiple repositories, understanding cross-repo dependencies and architectural patterns
- Custom GPU kernels for 3x faster inference (per company claims)
- Achieves **70.6% on SWE-bench** vs. GitHub Copilot's reported 54%

### Product Surface

- **IDE Extensions**: VS Code, JetBrains IDEs
- **CLI Tool**: Command-line interface for agentic workflows
- **Intent**: Purpose-built agentic development environment for enterprise teams, featuring a coordinator/specialist/verifier orchestration model and living specifications
- **MCP Integration**: Launched Model Context Protocol support in February 2026, with one-click integrations for CircleCI, MongoDB, Redis, Sentry, Stripe, and 100+ native tools

### Enterprise Security

- **SOC 2 Type II** attestation
- **ISO/IEC 42001:2023** certification (first AI coding assistant to achieve this)
- Customer-managed encryption keys (CMEK)
- VPC and on-premises deployment options

## Business Model

- **Pricing**: Credit-based model, $20-$200/month per seat depending on usage tier
- **Target Customer**: Enterprise software teams working with large, complex codebases
- **Revenue**: Reported ~$20M ARR as of October 2025 (source: Latka; accuracy uncertain -- treat as approximate)
- **Notable Customers**: Webflow, Kong, Pigment

## What Makes Augment Code Interesting (Research Notes)

1. **The "context at scale" bet is strategically sound.** Most AI coding tools optimize for individual developer productivity on greenfield code. Augment targets the harder, more valuable problem: navigating and modifying large legacy codebases where most enterprise engineering time is actually spent. If their Context Engine works as advertised, the moat is real -- indexing and understanding 100K+ file codebases is a genuinely hard systems problem.

2. **The team composition is unusually strong for this stage.** Having a Google LLM researcher (Gur-Ari, with PaLM 2 credentials) paired with a distributed systems architect (Ostrovsky), led by a CEO who took Pure Storage through IPO (Dietzen), is a rare combination. The team has both the AI research depth to build custom models and the enterprise software experience to sell them.

3. **Near-unicorn valuation before GA.** Raising $227M at $977M before having a generally available product (the Series B closed before the product fully launched) reflects either exceptional investor conviction or frothy market conditions -- possibly both. The ~$20M revenue figure for 2025, if accurate, suggests early enterprise traction but a long way to grow into the valuation.

4. **Enterprise-first in a consumer-first market.** While Cursor captured developer mindshare with a consumer-friendly approach, Augment is explicitly going after enterprise procurement with SOC 2, ISO certifications, on-prem deployment, and CMEK. This is a harder go-to-market but potentially more defensible if they win enterprise accounts.

5. **Custom models vs. API wrappers.** Augment appears to train custom AI models tuned specifically for code, rather than simply wrapping foundation model APIs. This is more capital-intensive but could yield better performance on enterprise-specific coding patterns and reduce hallucinations. [Note: the exact degree of model customization vs. fine-tuning vs. RAG augmentation is not fully disclosed.]

6. **Competition is fierce.** GitHub Copilot has distribution (Microsoft/GitHub ecosystem), Cursor has developer love, and new entrants arrive constantly. Augment's enterprise positioning is differentiated but the market is evolving rapidly.

## Key Uncertainties

- Exact revenue figures are from third-party estimates (Latka) and should be treated with caution
- The degree to which Augment trains its own models vs. fine-tunes existing foundation models is not fully transparent
- Whether the $977M valuation will hold in subsequent rounds is unknown
- Competitive dynamics with GitHub Copilot Enterprise, Cursor Business, and emerging agentic coding tools remain fluid
- Guy Gur-Ari's exact title/role division with Igor Ostrovsky at the company has varied across sources

## Sources

- [Augment Code Official Funding Announcement](https://www.augmentcode.com/blog/augment-inc-raises-227-million)
- [TechCrunch: Eric Schmidt-backed Augment launches out of stealth with $252M](https://techcrunch.com/2024/04/24/eric-schmidt-backed-augment-a-github-copilot-rival-launches-out-of-stealth-with-252m/)
- [SiliconANGLE: Augment raises $227M to rival GitHub's Copilot](https://siliconangle.com/2024/04/24/secretive-ai-coding-assistant-startup-augment-raises-227m-rival-githubs-copilot/)
- [SiliconANGLE: Augment Code makes semantic coding capability available for any AI agent (Feb 2026)](https://siliconangle.com/2026/02/06/augment-code-makes-semantic-coding-capability-available-ai-agent/)
- [Evolution Equity Partners Series B Investment Announcement](https://www.prnewswire.com/news-releases/evolution-equity-partners-invests-in-series-b-round-of-augment-inc-empowering-software-development-teams-with-ai-302295054.html)
- [FinSMES: Augment Raises $227M at $977M Valuation](https://www.finsmes.com/2024/04/augment-raises-227m-in-series-b-funding-at-977m-valuation.html)
- [Data Innovation: 5 Q's Interview with Scott Dietzen](https://datainnovation.org/2025/02/5-qs-interview-with-scott-dietzen-ceo-of-augment/)
- [Dion Almaer: Introducing Augment](https://blog.almaer.com/introducing-augment-a-company-dedicated-to-empowering-developers-with-ai/)
- [Codacy: How Augment Code Solved the Large Codebase Problem](https://blog.codacy.com/ai-giants-how-augment-code-solved-the-large-codebase-problem)
- [Augment Code Context Engine](https://www.augmentcode.com/context-engine)
- [Google Cloud Customer Case Study: Augment](https://cloud.google.com/customers/augment)
- [Guy Gur-Ari -- Google Scholar](https://scholar.google.com/citations?user=mx8P4QUAAAAJ&hl=en)
- [Latka: Augment Code Revenue Estimate](https://getlatka.com/companies/augmentcode.com)
- [Augment Code on Crunchbase](https://www.crunchbase.com/organization/augment-68db)
