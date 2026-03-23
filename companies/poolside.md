---
company: Poolside
legal_name: Poolside AI
domain: AI Code Generation / AI Software Engineering
founded: 2023
headquarters: Paris, France (legal HQ in US; ~80% of team in Europe)
website: https://poolside.ai
founders:
- name: Jason Warner
  role: CEO
  background: Former CTO of GitHub (incubated Copilot); previously VP Engineering at Heroku; ex-Canonical; Managing Director
    at Redpoint Ventures (2021-2023)
  origin: American
- name: Eiso Kant
  role: CTO
  background: Founded source{d} (first AI-on-code company); co-founded Athenian (engineering analytics); serial developer-tools
    entrepreneur
  origin: Estonian-Dutch
funding_total_estimated: $1.6B+
latest_valuation: $12B (Oct 2025)
key_investors:
- Bain Capital Ventures (led Series B)
- Nvidia (up to $1B investment, Oct 2025)
- Felicis Ventures
- Redpoint Ventures
- DST Global
- eBay Ventures
- Xavier Niel
- Citi Ventures
- StepStone Group
- SentinelOne S Ventures
- Air Street Capital
employee_count_approx: 162-256 (2025 estimates vary by source)
status: Private, Pre-IPO
last_updated: 2026-03-20
confidence: high on funding figures; moderate on revenue projections and employee count
one_liner: Poolside is building purpose-built foundation models for software engineering
website_verified: true
crunchbase: https://www.crunchbase.com/organization/poolside
crunchbase_verified: true
linkedin: https://www.linkedin.com/company/poolsideai
total_raised_m: 626.0
name: Poolside
---

# Poolside

## Company Overview

Poolside is building purpose-built foundation models for software engineering. Unlike general-purpose LLM providers that treat code as one capability among many, Poolside trains domain-specific models from scratch, optimized exclusively for code generation, completion, refactoring, testing, and documentation. The company deploys its models inside enterprise customer environments, keeping proprietary code off third-party servers.

Founded in early 2023 by Jason Warner and Eiso Kant, Poolside has rapidly become one of the most heavily funded AI startups in the world, with a $12 billion valuation as of late 2025.

## Founding Story

Jason Warner and Eiso Kant first met in 2017 when Warner, then CTO of GitHub, attempted to acquire Kant's company source{d} to serve as the AI engine at the core of GitHub. The acquisition fell through, but the two became friends and spent the next six years discussing how to build an AI-native approach to software development. In early 2023, they left their respective positions (Warner from Redpoint Ventures, Kant from his entrepreneurial ventures) to co-found Poolside.

Their complementary backgrounds are notable: Warner brings deep platform-level experience from scaling GitHub and Heroku, plus first-hand knowledge of what made Copilot successful (and its limitations). Kant brings years of research into applying machine learning to source code from his work at source{d} and Athenian.

Sources: [Upstarts Media founder interview](https://www.upstartsmedia.com/p/poolside-ai-founders-interview), [French Tech Journal spotlight](https://www.frenchtechjournal.com/spotlight-interview-poolside-cofounders/), [Redpoint Ventures announcement](https://medium.com/redpoint-ventures/fresh-ink-hello-poolside-384923ff3ad4)

## Funding History

| Round | Date | Amount | Valuation | Lead Investors |
|-------|------|--------|-----------|----------------|
| Seed | May 2023 | $26M | Undisclosed | Felicis, Redpoint Ventures, Xavier Niel |
| Series A | Aug 2023 | ~$100M | ~$526M | Felicis Ventures, Redpoint Ventures |
| Series B | Oct 2024 | $500M | ~$3B | Bain Capital Ventures |
| Nvidia Investment | Oct 2025 | Up to $1B | ~$12B | Nvidia |

**Notable:** The jump from $3B to $12B valuation in roughly one year (Oct 2024 to Oct 2025) represents a 4x increase driven primarily by Nvidia's massive commitment.

Additional Series B participants included Nvidia, eBay Ventures, DST Global, StepStone Group, Citi Ventures, Felicis Ventures, Redpoint Ventures, and SentinelOne's S Ventures.

Sources: [TechCrunch (Series B)](https://techcrunch.com/2024/10/02/ai-coding-startup-poolside-raises-500m-from-ebay-nvidia-and-others/), [TechCrunch (Nvidia $1B)](https://techcrunch.com/2025/10/30/nvidia-is-reportedly-investing-up-to-1-billion-in-poolside/), [Crunchbase](https://news.crunchbase.com/ai/coding-startup-poolside-raises-massive-series-b-bain/), [Sifted (seed/relocation)](https://sifted.eu/articles/poolside-raises-126m-relocated-france-news)

## Technology & Models

Poolside's core technical differentiation is **Reinforcement Learning from Code Execution Feedback (RLCEF)**, a proprietary training methodology. Unlike RLHF (which relies on human preference signals), RLCEF leverages the deterministic nature of code: models generate code, execute it, and receive rewards based on whether the code actually runs correctly. This creates a scalable synthetic-data flywheel that avoids dependence on scarce human-labeled training data.

### Model Lineup

- **Malibu** -- High-capacity model for complex tasks: multi-file code generation, refactoring, test writing, documentation. Designed for agentic workflows.
- **Point** -- Smaller, quantized model optimized for sub-200ms latency code completion in IDEs. Context-aware inline suggestions.

Both models are available on **Amazon Bedrock** and **Amazon EC2** through a strategic partnership with AWS announced in December 2024.

### Four-Layer Architecture

Poolside's product stack consists of four integrated layers (details partially proprietary):
1. Foundation models (Malibu, Point)
2. Fine-tuning infrastructure for customer-specific adaptation
3. Context engine (ingests codebases, documentation, Jira tickets, Slack messages)
4. Developer-facing interfaces (API, IDE assistant)

Sources: [AWS Bedrock listing](https://aws.amazon.com/bedrock/poolside/), [AWS Startups case study](https://aws.amazon.com/startups/learn/hpoolside-pioneers-ai-assisted-software-development-on-awsow-), [Wikipedia](https://en.wikipedia.org/wiki/Poolside_AI)

## Business Model

Poolside operates as a **B2B enterprise software company** targeting organizations with 5,000+ developers.

**Key characteristics:**
- **On-premise / private deployment:** Models are deployed inside the customer's infrastructure. Code never leaves the client environment. This is a major selling point for regulated industries (finance, defense, healthcare).
- **Custom fine-tuning:** Poolside spins up dedicated training environments and fine-tunes models on each client's proprietary codebases, coding patterns, and internal documentation.
- **Forward-deployed engineers:** Revenue includes professional services -- Poolside research engineers work directly with customer teams for integration.
- **Enterprise contracts:** Revenue comes from large multi-year enterprise deals rather than self-serve API pricing.

**Revenue projections** (unverified, sourced from third-party estimates):
- 2025: ~$25M-$50M [*uncertainty: figures vary across sources*]
- 2026: ~$60M (projected)
- 2027: ~$120M (projected)

Sources: [Contrary Research breakdown](https://research.contrary.com/company/poolside), [Sacra](https://sacra.com/c/poolside/), [Citi Ventures](https://www.citi.com/ventures/perspectives/pressrelease/investing-in-poolside.html), [SentinelOne S Ventures](https://www.sentinelone.com/s-ventures/blog/s-ventures-invests-in-poolside-next-generation-ai-for-software-engineering/)

## Infrastructure: Project Horizon

In October 2025, Poolside announced **Project Horizon**, a 2-gigawatt AI campus on 568 acres in West Texas (Longfellow Ranch, Permian Basin). Key details:

- **CoreWeave** is the anchor tenant for Phase 1 (250MW, expandable to 500MW, 15-year lease).
- **40,000+ Nvidia GB300 NVL72 GPUs** coming online starting December 2025 for model training and research.
- Powered by natural gas from the Permian Basin for low-cost, high-density energy.
- Full construction expected Q1 2027.

This is an unusual move for a startup -- vertical integration into infrastructure signals long-term ambitions beyond being an application-layer company.

Sources: [Poolside blog](https://poolside.ai/blog/announcing-project-horizon), [Bloomberg](https://www.bloomberg.com/news/articles/2025-10-15/ai-startup-poolside-teams-with-coreweave-on-massive-data-center), [Data Center Dynamics](https://www.datacenterdynamics.com/en/news/ai-startup-poolside-teams-up-with-coreweave-on-2gw-data-center-in-texas/)

## Team & Organization

- **~80% of team based in Europe**, with monthly gatherings in Paris. The company maintains a US legal headquarters.
- Team is roughly **70% technical** (research scientists, ML engineers, infrastructure engineers).
- Employee count has grown rapidly: ~62 in late 2024 to an estimated 162-256 by 2025 (sources conflict; exact figure uncertain).
- European research talent base may be a strategic advantage for recruiting ML researchers from institutions like INRIA, ENS, Polytechnique, and other French/European AI labs -- competing for talent in a market less saturated than the Bay Area.

Sources: [Sifted](https://sifted.eu/articles/poolside-500m-series-b-news), [GetLatka](https://getlatka.com/companies/poolside-ai), [Bain Capital Ventures](https://baincapitalventures.com/insight/poolside-is-scaling-a-team-to-help-billions-code-and-realize-agi/)

## What Makes Poolside Interesting (Research Assessment)

1. **Domain-specific foundation model thesis.** While most competitors (Cursor, Copilot, Windsurf) build application layers on top of general-purpose LLMs (GPT-4, Claude, etc.), Poolside is training its own models from scratch, specialized for code. This is a high-risk, high-reward bet: if code-specific models significantly outperform general models at software tasks, Poolside owns the full stack. If general models keep improving and the gap narrows, the capital expenditure may not justify the marginal gains.

2. **RLCEF as a data moat.** The ability to generate unlimited synthetic training data by executing code and using pass/fail signals as reward is genuinely differentiated. It sidesteps the data scarcity problem that constrains other model trainers and creates a compounding advantage as models improve.

3. **Enterprise-first, privacy-first positioning.** Deploying inside customer infrastructure is painful and expensive, but it unlocks the Fortune 500 segment that cannot send proprietary code to third-party APIs. This is a defensible wedge.

4. **Founder-market fit.** Warner literally oversaw Copilot's creation at GitHub and understands both its strengths and structural limitations. Kant has been working on ML-for-code since before it was fashionable. The combination is unusually strong.

5. **Nvidia relationship.** A $1B investment from Nvidia is not just capital -- it signals deep hardware-level partnership, early access to next-gen GPU architectures, and potential co-optimization of models for Nvidia silicon.

6. **Infrastructure ambition.** Project Horizon (2GW campus, 40K+ GPUs) is a bet that compute will remain the bottleneck and that owning infrastructure is a long-term advantage. This is more typical of hyperscalers than startups.

## Key Risks & Open Questions

- **Execution risk:** Training frontier models from scratch requires enormous capital and elite talent. The burn rate is likely very high relative to current revenue.
- **Competition:** GitHub Copilot has >50% market share. Cursor and Windsurf are growing fast with lighter-weight approaches. Can Poolside's enterprise-only model capture enough market before competitors move upmarket?
- **Revenue reality:** At ~$25-50M in revenue against a $12B valuation, the company trades at 240-480x revenue -- extreme even by AI startup standards. Revenue growth must be dramatic to justify this.
- **Infrastructure bet:** Project Horizon commits billions in capital over 15 years. If the AI landscape shifts (e.g., inference becomes cheap and commoditized), this could become a liability.

## Competitive Landscape

| Company | Approach | Key Difference vs. Poolside |
|---------|----------|-----------------------------|
| GitHub Copilot | App layer on OpenAI models | Largest installed base; not enterprise-private |
| Cursor (Anysphere) | IDE with multi-model support | Developer-first, not enterprise-deployed |
| Windsurf (ex-Codeium) | IDE + own models | Hybrid approach; less enterprise focus |
| Cognition (Devin) | Autonomous AI engineer agent | Agent-first; different product category |
| Magic AI | Own long-context models for code | Similar thesis but less funded, less enterprise traction |

---

*Profile compiled March 2026. Data sourced from public reporting; revenue figures are third-party estimates and should be treated with caution. Valuation and funding figures are based on confirmed reporting from TechCrunch, Bloomberg, and company announcements.*
