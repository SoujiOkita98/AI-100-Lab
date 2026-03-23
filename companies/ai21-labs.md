---
name: AI21 Labs
slug: ai21-labs
founded: '2017'
headquarters: Tel Aviv, Israel
us_operations: New York, NY
website: https://www.ai21.com
sector: Enterprise AI / Foundation Models
stage: Late Stage (Series C closed; Series D status disputed)
latest_valuation: $1.4B (Series C, August 2023)
total_funding_confirmed: ~$336M (through Series C)
employee_count: ~230 (as of early 2026)
status: Independent (potential Nvidia acquisition under discussion as of late 2025)
founders:
- name: Yoav Shoham
  role: Co-Founder, Co-CEO
  background: Professor Emeritus of Computer Science, Stanford University; former Google Principal Scientist; PhD CS Yale
  origin: Israeli
- name: Ori Goshen
  role: Co-Founder, Co-CEO
  background: Serial entrepreneur (Fring, Crowdx); IDF Unit 8200 veteran; 15+ years technology leadership
  origin: Israeli
- name: Amnon Shashua
  role: Co-Founder
  background: CS Professor, Hebrew University of Jerusalem; Co-founder of Mobileye (Intel acquisition, $15.3B), OrCam, OneZero;
    160+ papers, 94+ patents
  origin: Israeli
key_products:
- Jamba (hybrid SSM-Transformer foundation models)
- Maestro (enterprise AI planning & orchestration platform)
- Wordtune (consumer writing assistant — discontinued April 2025)
key_investors:
- Walden Catalyst
- Pitango
- Google
- Nvidia
- Intel Capital
- Samsung Next
- Comcast Ventures
- SCB10X
- b2venture
- Ahren
tags:
- foundation-models
- enterprise-ai
- israeli-ai
- hybrid-architecture
- SSM-transformer
- RAG
- agentic-ai
last_updated: 2026-03-20
confidence: medium-high
one_liner: AI21 Labs is an Israeli AI company founded in November 2017 that develops proprietary large language models and
  enterprise AI systems
website_verified: true
linkedin: https://www.linkedin.com/company/ai21
crunchbase: https://www.crunchbase.com/organization/ai21-labs
crunchbase_verified: true
total_raised_m: 336
funding_rounds:
  - stage: "Seed"
    date: "2019"
    amount_m: 9.5
    lead_investors: ["Undisclosed"]
    source: "https://www.crunchbase.com/organization/ai21"
  - stage: "Series A"
    date: "2020-07"
    amount_m: 34
    lead_investors: ["Pitango"]
    source: "https://www.crunchbase.com/organization/ai21"
  - stage: "Series B"
    date: "2021-07"
    amount_m: 64
    lead_investors: ["Ahren"]
    source: "https://www.crunchbase.com/organization/ai21"
  - stage: "Series C"
    date: "2023-08"
    amount_m: 208
    lead_investors: ["Walden Catalyst", "Pitango"]
    source: "https://www.ai21.com/blog/ai21-completes-208-million-oversubscribed-series-c-round/"
---

# AI21 Labs

## Overview

AI21 Labs is an Israeli AI company founded in November 2017 that develops proprietary large language models and enterprise AI systems. The company is notable for pioneering the hybrid Mamba (Structured State Space Model) and Transformer architecture at production scale, and for being founded by an unusually credentialed trio: a Stanford professor, a Hebrew University professor / Mobileye founder, and a Unit 8200 veteran turned serial entrepreneur.

As of early 2026, the company is at a strategic inflection point: it has pivoted fully to enterprise, shut down its consumer product (Wordtune), and faces reports of a potential $2-3B acquisition by Nvidia -- which the company has publicly denied.

## Founders and Leadership

### Yoav Shoham (Co-Founder, Co-CEO)

Professor Emeritus of Computer Science at Stanford University. PhD from Yale in computer science. Shoham's academic work spans AI, game theory, and multi-agent systems. He served as Google's Principal Scientist and has a track record of founding and exiting AI companies: TradingDynamics (acquired by Ariba), Timeful (acquired by Google), and Katango (acquired by Google). His Stanford pedigree and deep academic-to-industry bridge make him a credible figure in enterprise AI. Shoham brings the research gravitas and Silicon Valley network.

### Ori Goshen (Co-Founder, Co-CEO)

A serial entrepreneur with over 15 years in technology leadership. Goshen started programming at age four, ran a web development business at 16, and served in the IDF's elite Unit 8200 intelligence unit. He previously founded and sold Fring (a VoIP and messaging app) and Crowdx (a telco analytics firm). Goshen is the operational and product leader of the pair, handling the commercial and go-to-market dimensions.

### Amnon Shashua (Co-Founder)

A professor of computer science at the Hebrew University of Jerusalem and one of Israel's most prominent technologists. Shashua co-founded Mobileye, which went public in 2014 in the largest-ever Israeli IPO on a US exchange and was acquired by Intel in 2017 for $15.3 billion. He also founded OrCam (assistive AI for the visually impaired) and OneZero (a digital bank). With 160+ publications and 94+ patents, Shashua brings deep technical credibility and significant personal capital. He participated in AI21's Series C as an investor as well.

**Team composition note:** The ~230-person team is reported to be heavily skewed toward PhDs and researchers with advanced degrees in machine learning -- a key factor in the Nvidia acquisition interest.

## Funding History

| Round | Date | Amount | Valuation | Lead / Notable Investors |
|-------|------|--------|-----------|--------------------------|
| Seed | Jan 2019 | $9.5M | Undisclosed | Undisclosed |
| Series A | Nov 2021 | ~$25M | Undisclosed | Pitango First; Walden Catalyst ($20M) |
| Series B | Jul 2022 | Undisclosed | Undisclosed | Ahren and others |
| Series C | Aug 2023 | $155M (extended to $208M by Nov 2023) | $1.4B | Walden Catalyst, Pitango, Google, Nvidia, SCB10X, Samsung Next, Intel Capital |
| Series D (reported) | May 2025 | $300M (reported) | ~$1.4B | Google, Nvidia (reported) |

**Total confirmed funding:** ~$336M through the completed Series C extension.

**Critical caveat on Series D:** Multiple sources (notably Calcalist/Ctech) report that the $300M Series D round announced in May 2025 was **never formally closed**. The round was reportedly never reflected in the company's capital structure. If accurate, total funding stands at ~$336M, not $636M. This is a significant discrepancy that surfaces in various databases. Treat the $636M total-funding figure with skepticism.

## Technology and Products

### Jamba: Hybrid SSM-Transformer Models

AI21's flagship technical contribution is the **Jamba architecture** -- the first production-grade hybrid model combining Mamba (a Structured State Space Model) with Transformer attention layers. Key characteristics:

- **Architecture:** Interleaves Mamba SSM layers with Transformer attention layers and Mixture-of-Experts (MoE) components. The largest model (Jamba 1.5 Large) has 398B total parameters with 94B active.
- **Context window:** 256K tokens natively, with claimed ability to handle up to 1M tokens in certain configurations.
- **Efficiency:** Up to 2.5x faster inference on long contexts compared to similarly sized pure-Transformer models. Linear-time scaling on sequence length (vs. quadratic for standard attention).
- **Open weights:** Jamba 1.5 Mini and Large released with open weights on Hugging Face under permissive licensing.
- **Jamba 1.6:** Released March 2025 for private enterprise deployment, with claimed benchmark leadership among open models.
- **Jamba Reasoning 3B:** A compact, open-source reasoning model with 2-5x efficiency gains over competitors.

The hybrid architecture thesis is that SSMs handle long-range dependencies and sequential processing efficiently, while Transformer attention layers handle precise recall and complex reasoning. This is a genuine architectural innovation, not merely a training or scaling contribution.

### Maestro: Enterprise AI Orchestration

Launched March 2025, Maestro is AI21's enterprise platform product:

- **Structured RAG (S-RAG):** Combines structured and embedding-based retrieval, claiming up to 60% accuracy improvement with near-perfect recall.
- **Agentic orchestration:** Plans and coordinates multi-step workflows using LLMs, reasoning models, and other tools.
- **Accuracy claims:** Up to 50% improvement in output quality over standalone model calls.
- **Target verticals:** Finance, pharma, legal, manufacturing, technology.
- **Deployment:** Available via SaaS, VPC, and on-premises; integrations with AWS, Google Cloud, Azure, and Nvidia NIM.

### Wordtune (Discontinued)

Wordtune was AI21's consumer-facing AI writing assistant, launched as one of the company's earliest products. In April 2025, development was halted as the company pivoted fully to enterprise. This is a telling strategic decision: consumer AI writing became a commodity market dominated by ChatGPT, Grammarly, and others, while enterprise accuracy-focused AI offered higher margins and defensibility.

## Business Model

AI21 operates a **B2B enterprise model** selling:

1. **API access** to Jamba models (usage-based pricing)
2. **Maestro platform** licenses for enterprise AI orchestration
3. **Private deployment** of models for security-sensitive customers

Revenue was reportedly ~$50-58M in 2024, roughly flat from 2023. For a company with $336M+ in funding, this revenue trajectory raises questions about growth velocity and capital efficiency. The enterprise pivot with Maestro is designed to address this.

**Available through:** Amazon Bedrock, Google Cloud Vertex AI, Azure, Nvidia NIM, and direct API.

## What Makes AI21 Labs Interesting

1. **Architectural originality.** AI21 is one of very few companies that has shipped a genuinely novel model architecture (hybrid SSM-Transformer) at production scale, rather than simply scaling up the standard Transformer recipe. This is a meaningful research contribution.

2. **Founder caliber.** The combination of a Stanford CS professor (Shoham), a Hebrew University professor who built a $15B company (Shashua), and a Unit 8200 veteran with multiple exits (Goshen) is an unusually strong founding team -- spanning academia, deep tech, and operational execution across both Israel and the US.

3. **Israeli AI ecosystem leadership.** AI21 is one of Israel's most prominent AI startups and a magnet for the country's deep pool of ML talent (military intelligence units, top universities). The ~230-person team with high PhD concentration represents rare human capital.

4. **Enterprise accuracy positioning.** Rather than competing on general-purpose chatbot capabilities, AI21 has carved a niche around reliability, traceability, and accuracy for enterprise workflows -- a positioning that could prove durable as AI moves from experimentation to mission-critical deployment.

5. **Strategic uncertainty creates optionality.** The Nvidia acquisition rumors ($2-3B), the disputed Series D, and the consumer-to-enterprise pivot all create an interesting strategic situation. If Nvidia acquires AI21, it validates the talent-as-asset thesis for Israeli AI companies. If AI21 remains independent, it must demonstrate that Maestro and Jamba can generate enterprise revenue at scale.

## Key Risks and Open Questions

- **Revenue growth stagnation.** ~$50-58M in revenue with minimal growth from 2023 to 2024 is a concern for a company that has raised $300M+. The enterprise pivot needs to show results.
- **Series D uncertainty.** Whether the $300M round actually closed is material. If it did not, the company may face funding pressure.
- **Acquisition overhang.** Nvidia acquisition reports (denied by Shashua) create uncertainty for customers, employees, and partners.
- **Competitive pressure on hybrid architectures.** Nvidia (Nemotron-H), IBM (Bamba), and Mistral (Codestral Mamba) are all exploring hybrid SSM-Transformer models, eroding AI21's first-mover advantage.
- **Scale disadvantage.** With ~230 employees and ~$50M revenue, AI21 is significantly smaller than peers like Anthropic, OpenAI, and Mistral.

## Sources

- [AI21 Labs Official Site](https://www.ai21.com)
- [AI21 Labs Wikipedia](https://en.wikipedia.org/wiki/AI21_Labs)
- [Contrary Research: AI21 Labs Business Breakdown](https://research.contrary.com/company/ai21-labs)
- [AI21 Series C Announcement](https://www.ai21.com/blog/ai21-completes-208-million-oversubscribed-series-c-round/)
- [Calcalist: AI21 never closed its reported $300M round](https://www.calcalistech.com/ctechnews/article/rjswz37eze)
- [Calcalist: AI21 Labs raising $300M Series D](https://www.calcalistech.com/ctechnews/article/hkuxkg6gle)
- [SiliconAngle: AI21 Labs raises $300M from Google and Nvidia](https://siliconangle.com/2025/05/11/ai21-labs-raises-300m-google-nvidia-expand-enterprise-ai-offerings/)
- [Calcalist: Nvidia in advanced talks to acquire AI21](https://www.calcalistech.com/ctechnews/article/rkbh00xnzl)
- [Times of Israel: Nvidia in talks to buy AI21 for up to $3B](https://www.timesofisrael.com/report-nvidia-in-advanced-talks-to-buy-israels-ai21-labs-for-up-to-3-billion/)
- [Globes: AI21 Labs denies Nvidia acquisition talks](https://en.globes.co.il/en/article-ai21-labs-denies-nvidia-acquisition-talks-1001531815)
- [TechCrunch: AI21 Labs lands $155M at $1.4B valuation](https://techcrunch.com/2023/08/30/generative-ai-startup-ai21-labs-lands-155m-at-a-1-4b-valuation/)
- [Pitango: Ori Goshen Founder Story](https://www.pitango.com/resources/founder-story-ori-goshen-ai21/)
- [Walden Catalyst: Founder Spotlight Ori Goshen](https://waldencatalyst.com/blog/founder-spotlight-ori-goshen-using-artificial-intelligence-to-reimagine-how)
- [SiliconAngle: AI21 debuts Maestro](https://siliconangle.com/2025/03/10/ai21-debuts-maestro-ai-planning-orchestration-system/)
- [AI21 Maestro Official Page](https://www.ai21.com/maestro/)
- [AI21 Jamba Architecture Blog](https://www.ai21.com/blog/announcing-jamba/)
- [AI21 Jamba 1.5 Announcement](https://www.ai21.com/blog/announcing-jamba-model-family/)
- [Yahoo Finance: Nvidia and Google Back AI21 Labs in $300M Series D](https://finance.yahoo.com/news/nvidia-google-back-ai21-labs-140222256.html)
- [GetLatka: AI21 Labs Revenue Data](https://getlatka.com/companies/ai21.com)
- [SkyWork: AI21 Labs Deep Dive](https://skywork.ai/skypage/en/AI21-Labs-Deep-Dive:-Jamba,-Maestro,-and-the-Future-of-Enterprise-AI/1976107792340807680)
