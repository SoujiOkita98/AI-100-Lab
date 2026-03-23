---
company_name: Brightwave
legal_name: Brightwave, Inc.
website: https://www.brightwave.io
one_liner: AI-powered investment research platform that synthesizes thousands of pages of financial documents into actionable
  insights for investment professionals
sector: AI for Finance / Investment Research
founded: 2023
headquarters: Boulder, CO
founders:
- name: Mike Conover
  role: Co-Founder & CEO
  origin: American
- name: Brandon Kotara
  role: Co-Founder & CTO
  origin: American
latest_valuation: Undisclosed
total_funding_raised: $21M
arr_estimate: Undisclosed (reported 4x revenue growth in four months post-seed; no public ARR figure)
employee_count_estimate: ~22 (as of Jan 2026, per Tracxn)
status: Private
last_updated: 2026-03-20
website_verified: true
linkedin: https://www.linkedin.com/company/brightwave-io
crunchbase: https://www.crunchbase.com/organization/brightwave
crunchbase_verified: true
total_raised_m: 21
funding_rounds:
- stage: Seed
  date: 2024-06
  amount_m: 6
  lead_investors:
  - Decibel Partners
  source: https://www.businesswire.com/news/home/20240611417446/en/
- stage: Series A
  date: 2024-10
  amount_m: 15
  lead_investors:
  - Decibel Partners
  source: https://www.businesswire.com/news/home/20241029778071/en/
name: Brightwave
linkedin_verified: true
---

# Brightwave -- Company Profile

## Overview

Brightwave is an AI-powered investment research platform that uses autonomous agents to synthesize insights across thousands of pages of financial documents -- SEC filings, earnings calls, sell-side research, web content, and proprietary knowledge bases -- into actionable intelligence. The company positions itself as an "IDE for information," enabling investment professionals to run fleets of research agents from a single control plane. Founded in 2023 in Boulder, Colorado, Brightwave has raised $21M and serves a growing base of institutional asset managers, hedge funds, private credit investors, and wealth management firms.

## Founders & Key People

### Mike Conover -- Co-Founder & CEO

- **Education:** PhD in complexity science from Indiana University, focused on understanding large-scale patterns in human society.
- **Prior career (20+ years in AI/ML):**
  - Engineering lead for LinkedIn homepage news relevance; his team used 500 million job transitions to forecast market movements.
  - Co-founded SkipFlag (NLP startup), which was acquired by Workday.
  - Director of Financials Machine Learning at Workday.
  - Established Databricks' language model engineering practice; created Dolly, one of the first open-source LLMs exhibiting ChatGPT-like behavior (trained for ~$30).
- **Role at Brightwave:** CEO, overall strategy, product vision, and fundraising.

Sources: [Silicon Flatirons bio](https://siliconflatirons.org/people/mike-conover/), [Latent Space podcast](https://www.latent.space/p/brightwave), [Cerebral Valley profile](https://cerebralvalley.ai/blog/brightwave-your-autonomous-investment-research-system-UyEIRBb6pFgqvNDhxewLO)

### Brandon Kotara -- Co-Founder & CTO

- **Education:** The University of Texas at Austin.
- **Prior career:**
  - Technical lead overseeing AI systems for Workday's human capital management suite; filed his first deep learning patent in 2018.
  - CTO of LedgerX, a federally-regulated derivatives exchange and clearinghouse; led the company through its sale to FTX (2021) and subsequent sale to MIAX (2023). Built multi-region, active-active cloud architecture with single-digit microsecond matching engine performance.
- **Role at Brightwave:** CTO, leads engineering and infrastructure.

Sources: [Crunchbase](https://www.crunchbase.com/person/brandon-kotara), [LinkedIn](https://www.linkedin.com/in/brandon-kotara-49242a60/)

### Origin Story

Conover and Kotara both worked at Workday (Conover via the SkipFlag acquisition, Kotara on HCM AI systems), giving them a shared background in enterprise AI. Conover's subsequent experience building Dolly at Databricks gave him deep insight into the power of LLMs, and his long career in finance-adjacent ML (LinkedIn labor market signals, Workday financials) pointed him toward investment research as a high-value, underserved domain. The pair founded Brightwave in 2023 and operated in stealth before publicly launching with their seed round in June 2024.

## Funding History

| Round    | Date           | Amount | Lead Investor     | Notable Co-Investors                                                                 |
|----------|----------------|--------|-------------------|--------------------------------------------------------------------------------------|
| Seed     | June 2024      | $6M    | Decibel Partners  | Point72 Ventures, Moonfire Ventures; angels from OpenAI, Databricks, Uber, LinkedIn  |
| Series A | October 2024   | $15M   | Decibel Partners  | OMERS Ventures                                                                       |
| **Total**|                | **$21M** |                 |                                                                                      |

The seed round was oversubscribed. Between the seed announcement and the Series A close (roughly four months), Brightwave reported 4x revenue growth. No post-money valuation has been publicly disclosed for either round.

Sources: [BusinessWire -- Seed](https://www.businesswire.com/news/home/20240611417446/en/Brightwave-Secures-$6-Million-Seed-Round-to-Launch-AI-Powered-Financial-Research-Assistant), [BusinessWire -- Series A](https://www.businesswire.com/news/home/20241029778071/en/Brightwave-Secures-15M-Series-A-to-Scale-AI-Powered-Financial-Research-Platform), [TechCrunch](https://techcrunch.com/2024/10/29/brightwaves-ai-agent-helps-asset-managers-find-signal-and-its-fundraising-fast/)

## Product & Technology

### Core Platform

Brightwave's platform ingests and reasons over large corpora of financial documents. It synthesizes insights from SEC filings, earnings transcripts, sell-side research, web sources, and users' proprietary data rooms. Key capabilities:

- **Research Agents (launched Aug 2025):** Autonomous, long-running background agents that spawn sub-agents for search, reasoning, planning, presentation, and fact-checking. After completing a task, outputs are submitted to an LLM judge to verify whether the research fulfills the original request. Users can run fleets of agents from a unified control plane.
- **Report Builder & Blueprints:** Configurable templates for producing shareable analytical reports from diverse deal-room materials, financial models, and proprietary notes.
- **Private Market Diligence Platform:** Purpose-built for private market investors to accelerate deal analysis across data rooms.
- **Sandbox Agents & Agent-to-Agent Orchestration (March 2026):** Multi-agent coordination for complex research workflows.
- **Excel Agents (Feb 2026):** Agents that work directly with spreadsheet data.
- **Microsoft Office Agents & JSON/XML Support (March 2026):** Enterprise integration features.

### Technical Approach

Brightwave is building a purpose-built AI system for finance rather than a thin wrapper around foundation models. The platform uses multi-agent orchestration, retrieval-augmented generation over financial documents, and a knowledge graph that the company is expanding through strategic data partnerships. The system is designed to surface fact patterns across thousands of pages of primary sources.

Sources: [BusinessWire -- Research Agents](https://www.businesswire.com/news/home/20250812210320/en/Brightwave-Launches-Research-Agents-The-First-Analyst-Grade-AI-Chat-That-Builds-Thinks-and-Works-in-Every-Dataroom), [SiliconANGLE](https://siliconangle.com/2025/08/12/brightwaves-new-platform-orchestrates-autonomous-agents-create-extensive-research-reports-topic/), [Brightwave blog](https://www.brightwave.io/blog/introducing-research-agents)

## Business Model

Brightwave operates as an enterprise SaaS platform targeting financial services. Key characteristics:

- **Go-to-market:** Offers a free trial for new users (no enterprise contract required), with conversion to paid enterprise plans. This is a relatively unusual bottom-up motion for institutional finance software.
- **Target customers:** Institutional asset managers, hedge funds (long-short, crossover), private credit investors, private equity firms, boutique consultancies, wealth management firms, and pension funds.
- **Pricing:** Not publicly disclosed. Likely seat-based or usage-based enterprise pricing given the institutional customer base. [Uncertain -- no public pricing page found.]
- **Revenue trajectory:** 4x revenue growth reported between June and October 2024. Specific ARR figures not disclosed.

## Customers & Traction

- While operating in stealth (pre-June 2024), Brightwave signed customers managing over **$120 billion in combined AUM**, ranging from owner-operated RIAs to $20B crossover hedge funds.
- Client testimonials reference portfolio managers at $4B hedge funds, managing directors at $1B+ private credit funds, and managing partners at top-50 AUM pension funds.
- Use cases include: rapidly understanding new sectors, deep equity research, private market opportunity discovery and diligence, investment thesis development, and wealth management client preparation.

Sources: [Decibel Partners](https://www.decibel.vc/articles/brightwave-an-ai-investment-research-assistant-for-everyone), [Brightwave blog -- seed announcement](https://www.brightwave.io/blog/ai-financial-research-brightwave-6-million)

## Competitive Landscape

Brightwave competes in the AI-for-finance research space alongside:

- **Hebbia** -- AI-powered document analysis for finance and legal (raised $130M Series B in 2024).
- **AlphaSense** -- Market intelligence and search platform (more established, $4B+ valuation).
- **Alphanome.AI, BridgeWise, Daloopa** -- Various AI tools for financial data extraction and analysis.
- **Bloomberg Terminal AI features** -- Incumbents adding AI capabilities.

Brightwave differentiates through its multi-agent architecture (agents that spawn sub-agents for complex research), its focus on autonomous long-running research tasks rather than simple chat/search, and its private-market diligence capabilities.

## What Makes Brightwave Interesting

1. **Founder-market fit is exceptional.** Conover has 20+ years in AI/ML spanning LinkedIn (labor market signals), Workday (financial ML), and Databricks (LLMs). He built Dolly, one of the seminal open-source LLMs. Kotara brings exchange-grade infrastructure experience from LedgerX. Together they combine deep AI expertise with real finance-domain knowledge.

2. **Agentic architecture ahead of the curve.** Brightwave's multi-agent orchestration -- where agents spawn sub-agents for search, reasoning, fact-checking, and an LLM judge evaluates output quality -- is more architecturally ambitious than most competitors, who tend to offer RAG-based chat over documents.

3. **Strong early traction signals.** $120B+ in customer AUM during stealth, 4x revenue growth in four months, and oversubscribed funding rounds suggest genuine product-market fit in a notoriously demanding customer segment.

4. **Finance is an ideal AI wedge.** Investment research is high-value, document-heavy, time-sensitive, and tolerates premium pricing -- ideal conditions for AI automation. The willingness of institutional investors to pay for edge creates a large TAM.

5. **Capital-efficient growth.** $21M total raised with a ~22-person team serving institutional clients suggests disciplined capital deployment. The team is small relative to the customer base they serve, which speaks to the leverage of their agent-based approach.

6. **Rapid product velocity (2026).** The cadence of feature releases in early 2026 (Excel Agents, Sandbox Agents, Agent-to-Agent Orchestration, Microsoft Office Agents) suggests the team is shipping aggressively to widen their platform moat.

## Key Risks & Open Questions

- **Valuation unknown.** No post-money valuation has been disclosed, making it hard to assess whether the company is priced for its traction.
- **Revenue scale unclear.** Without public ARR figures, the absolute size of the business is uncertain despite strong growth rates.
- **Competitive pressure from Hebbia** and other well-funded AI-for-finance startups, plus incumbents like Bloomberg adding AI features.
- **Dependency on foundation model providers.** Unclear to what extent Brightwave builds proprietary models vs. orchestrating third-party LLMs. [Uncertain.]
- **Small team (22 employees).** Could limit ability to serve enterprise customers at scale, though this may be a deliberate choice given the agent-based architecture.

## Sources

- [Brightwave website](https://www.brightwave.io/)
- [Brightwave About page](https://www.brightwave.io/about)
- [BusinessWire -- $6M Seed Round (June 2024)](https://www.businesswire.com/news/home/20240611417446/en/Brightwave-Secures-$6-Million-Seed-Round-to-Launch-AI-Powered-Financial-Research-Assistant)
- [BusinessWire -- $15M Series A (Oct 2024)](https://www.businesswire.com/news/home/20241029778071/en/Brightwave-Secures-15M-Series-A-to-Scale-AI-Powered-Financial-Research-Platform)
- [BusinessWire -- Research Agents Launch (Aug 2025)](https://www.businesswire.com/news/home/20250812210320/en/Brightwave-Launches-Research-Agents-The-First-Analyst-Grade-AI-Chat-That-Builds-Thinks-and-Works-in-Every-Dataroom)
- [TechCrunch -- Series A coverage](https://techcrunch.com/2024/10/29/brightwaves-ai-agent-helps-asset-managers-find-signal-and-its-fundraising-fast/)
- [Decibel Partners -- investment thesis](https://www.decibel.vc/articles/brightwave-an-ai-investment-research-assistant-for-everyone)
- [SiliconANGLE -- Research Agents](https://siliconangle.com/2025/08/12/brightwaves-new-platform-orchestrates-autonomous-agents-create-extensive-research-reports-topic/)
- [Latent Space podcast -- Mike Conover](https://www.latent.space/p/brightwave)
- [Cerebral Valley profile](https://cerebralvalley.ai/blog/brightwave-your-autonomous-investment-research-system-UyEIRBb6pFgqvNDhxewLO)
- [Silicon Flatirons -- Mike Conover bio](https://siliconflatirons.org/people/mike-conover/)
- [Tracxn -- Brightwave 2026 profile](https://tracxn.com/d/companies/brightwave/__0-YFrk782HiMd6vgSpQxlcrXZNqxBFEAqiQbHqD6F3E)
- [Litquidity -- deep dive](https://litquidity.co/when-ai-meets-wall-street-a-deep-dive-on-brightwave/)
