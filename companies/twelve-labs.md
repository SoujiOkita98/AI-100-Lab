---
company: Twelve Labs
legal_name: Twelve Labs, Inc.
website: https://www.twelvelabs.io
domain: twelvelabs.io
sector: Multimodal AI / Video Understanding
founded: 2021
headquarters: San Francisco, CA (660 4th Street)
headcount_estimate: ~73 (as of 2025-2026)
total_funding: ~$107M across 5 rounds
latest_valuation: ~$300M (Series B, mid-2024; unconfirmed for later rounds)
status: Private, growth-stage
tags:
- multimodal-ai
- video-understanding
- foundation-models
- API-platform
- computer-vision
- NLP
last_updated: 2026-03-20
confidence: medium-high
one_liner: Twelve Labs builds foundation models purpose-built for video understanding
founders:
- name: Jae Lee
  role: Co-Founder & CEO
  background: Born in Seoul; studied CS at UC Berkeley; founded Twelve Labs in 2021 during military service at Korean Cyber
    Command
  origin: Korean
- name: Aiden Lee
  role: Co-Founder
  background: Recruited by Jae Lee; met at Korean Cyber Command
  origin: Korean
- name: SJ Kim
  role: Co-Founder
  background: One of five co-founders recruited from Jae Lee's network
  origin: Korean
- name: Dave Chung
  role: Co-Founder
  background: One of five co-founders recruited from Jae Lee's network
  origin: Korean
- name: Soyoung Lee
  role: Co-Founder
  background: One of five co-founders recruited from Jae Lee's network
  origin: Korean
data_notes: Some sources report Series A and B as a single $103M round. SK Telecom invested $3M in Oct 2025.
crunchbase: https://www.crunchbase.com/organization/twelve-labs
crunchbase_verified: true
total_raised_m: 107
funding_rounds:
- stage: Seed
  date: '2022'
  amount_m: 12
  lead_investors:
  - Index Ventures
  - Radical Ventures
  source: https://www.crunchbase.com/organization/twelve-labs
- stage: Series A
  date: 2024-06
  amount_m: 50
  lead_investors:
  - NEA
  - NVIDIA NVentures
  source: https://www.crunchbase.com/organization/twelve-labs
- stage: Series B
  date: 2024-07
  amount_m: 42
  lead_investors:
  - NEA
  - NVIDIA
  source: https://www.crunchbase.com/organization/twelve-labs
linkedin: https://www.linkedin.com/company/twelve-labs/
name: Twelve Labs
---

# Twelve Labs

Twelve Labs builds foundation models purpose-built for video understanding. Unlike general-purpose multimodal LLMs that bolt video onto text capabilities, Twelve Labs trains natively multimodal models that jointly process visual frames, audio, speech, and on-screen text to understand video the way humans do. The company sells access via API and, more recently, through cloud marketplaces like Amazon Bedrock.

## Founders & Team

All five co-founders are of **Korean origin** and met while serving in or around the **Korean Cyber Command** (South Korean military). This shared background is a distinctive founding story in Silicon Valley AI.

| Name | Role | Background |
|------|------|------------|
| **Jae Lee** | CEO & Co-Founder | Born in Seoul; studied CS at UC Berkeley; served as lead data scientist at the South Korean Ministry of National Defense (Korean Cyber Command); prior software engineering stints at Amazon and Samsung; named a WEF Technology Pioneer |
| **Aiden Lee** | CTO & Co-Founder | Technical lead; details on prior roles not publicly documented in detail |
| **Soyoung Lee** | Co-Founder, Head of Business Development | Leads go-to-market and partnerships |
| **Dave Chung** | Co-Founder | Also founded at least one other company (details unclear) |
| **SJ Kim** | Co-Founder | Role details limited in public sources |

Jae Lee has described the founding story as starting the company in 2021 with "four of his best friends" he met during military service. The team's deep familiarity with video surveillance and intelligence analysis in the military context appears to have informed the company's focus on rich, multimodal video comprehension.

> **Note on uncertainty:** Detailed professional backgrounds for Aiden Lee, Dave Chung, SJ Kim, and Soyoung Lee are not well-documented in public sources. The above reflects what is available as of March 2026.

## Funding History

| Round | Date | Amount | Lead Investors | Notable Participants |
|-------|------|--------|----------------|---------------------|
| Seed | ~2022 | ~$12M | Index Ventures, Radical Ventures | WndrCo, Korea Investment Partners |
| Strategic | ~2023 | Undisclosed | NVIDIA NVentures | -- |
| Series A | June 2024 | $50M | NEA, NVIDIA NVentures (co-led) | Index Ventures, Radical Ventures, WndrCo, Korea Investment Partners |
| Series B | ~July 2024 | ~$103M | NEA, NVIDIA (reported) | -- |
| Corporate Minority | Oct 2025 | $3M | SK Telecom (reported) | -- |
| Additional round | Dec 2024 | $30M | -- | Described by Twelve Labs as validating "video understanding technology to the AI ecosystem" |

**Total raised:** ~$107M+ (per Tracxn/Crunchbase aggregations; some rounds may overlap or reflect tranches of the same round -- exact breakdown has minor discrepancies across sources).

**Key investors:** NEA, NVIDIA NVentures, Index Ventures, Radical Ventures, WndrCo, Korea Investment Partners, SK Telecom.

> **Note on uncertainty:** The Series B is reported as both $100M and $103M across sources. The $30M December 2024 round may be a tranche or extension of the Series B rather than a standalone round. Tracxn lists 5 rounds totaling $107M, which suggests some overlap.

## Core Technology & Products

Twelve Labs develops **video-native foundation models**, not wrappers around text LLMs:

- **Marengo** -- An encoder/embedding model that processes video natively across visual, audio, and text modalities. Generates multimodal vector embeddings for semantic search, anomaly detection, and recommendation. As of March 2026, upgrading to **Marengo 3.0** with automatic reindexing for existing customers.
- **Pegasus** -- A video-language generation model for video-to-text tasks: summarization, chapter generation, question answering, structured data extraction from video. State-of-the-art on video understanding benchmarks.
- **Jockey** -- An agentic video intelligence system built on top of Marengo and Pegasus, adding an orchestration layer for more complex reasoning over video.

**Platform capabilities:**
- Semantic video search (natural language queries to find exact moments)
- Video-to-text generation (summaries, chapters, custom reports)
- Multimodal embeddings (for search, recommendations, clustering)
- Fine-tuning for domain-specific video analysis
- REST API with JSON responses; also available on **Amazon Bedrock** and **AWS Marketplace**

## Business Model

- **API-as-a-service** with pay-as-you-go pricing (tiered: free tier for experimentation, usage-based for production)
- **Cloud marketplace distribution** via Amazon Bedrock (launched 2025-2026), expanding reach to AWS enterprise customers
- **Enterprise contracts** -- multiyear deals with large organizations (e.g., Oracle for model training infrastructure)
- **Partnership/integration revenue** -- integrations with media asset management platforms (Mimir, Iconik, Adobe)

## Customers & Use Cases

**Named customers/partners:**
- **Washington Post** -- media/journalism video archive search
- **MLSE** (Maple Leaf Sports & Entertainment) -- sports video analysis
- **Oracle** -- multiyear infrastructure contract for model training on OCI
- **Adobe, Mimir, Iconik** -- media asset management integrations
- **Backblaze** -- storage + video understanding integration

**Key verticals:**
- Media & entertainment (archive search, content production, highlight reels)
- Advertising & marketing (video content analysis at scale)
- Security & public safety (surveillance video understanding)
- Sports analytics
- Manufacturing (visual inspection)
- Government

## What Makes Twelve Labs Interesting

1. **Video-native foundation models.** Most competitors (including Google Gemini, OpenAI) treat video as a secondary modality bolted onto text models. Twelve Labs builds models that are architecturally designed for video from the ground up, jointly processing visual, audio, and textual streams within video. This yields stronger temporal reasoning and cross-modal understanding.

2. **Founding story and team cohesion.** Five Korean co-founders who met during military service and share deep trust built a company in one of AI's most competitive domains. The military intelligence background (analyzing surveillance video) is directly relevant to the product.

3. **NVIDIA as both investor and partner.** Having NVentures co-lead the Series A signals strategic alignment. NVIDIA's infrastructure (GPUs, CUDA) is essential for video model training, and the investment likely comes with meaningful technical and go-to-market support.

4. **Vertical focus in a horizontal market.** While frontier labs build general-purpose multimodal models, Twelve Labs bets that video understanding is hard enough and valuable enough to sustain a specialized company. The bet is that purpose-built video models will outperform general models on enterprise video workloads -- a plausible thesis given the unique challenges of temporal reasoning, long-context video, and multimodal alignment.

5. **Agentic evolution.** The Jockey system signals a move from "model API" to "video intelligence agent" -- a higher-value, stickier product. Agentic video workflows (automated content moderation, real-time sports analysis, security monitoring) are a natural extension.

6. **Cloud marketplace distribution (Amazon Bedrock).** Availability on Bedrock dramatically lowers friction for enterprise adoption and positions Twelve Labs models alongside Anthropic, Meta, and other foundation model providers.

## Risks & Open Questions

- **Competition from frontier labs.** Google Gemini, OpenAI, and Anthropic are all investing in multimodal video. If general-purpose models become "good enough" at video, the specialized model advantage erodes.
- **Burn rate vs. revenue.** $107M+ raised with ~73 employees suggests significant compute spend on training. Revenue trajectory is unclear from public sources.
- **Valuation trajectory.** The $300M Series B valuation (if accurate) is modest by 2024-2025 AI standards, but defensibility depends on enterprise lock-in and model quality moats.
- **Founder concentration.** Five co-founders is unusually many; long-term alignment and role clarity will matter.

## Sources

- [Twelve Labs Official Website](https://www.twelvelabs.io/)
- [Twelve Labs About Page](https://www.twelvelabs.io/about-us)
- [Series A Announcement - Twelve Labs Blog](https://www.twelvelabs.io/blog/series-a-announcement)
- [$30M Funding Announcement - Twelve Labs Blog](https://www.twelvelabs.io/blog/twelve-labs-secures-30-million-in-funding-validating-the-importance-of-twelve-labs-video-understanding-technology-to-the-ai-ecosystem)
- [TechCrunch - Twelve Labs Building AI for Video (Dec 2024)](https://techcrunch.com/2024/12/12/twelve-labs-is-building-ai-that-can-analyze-and-search-through-videos/)
- [TechCrunch - Twelve Labs Deep Video Understanding (Oct 2023)](https://techcrunch.com/2023/10/24/twelve-labs-is-building-models-that-can-understand-videos-at-a-deep-level/)
- [NEA Investment Blog Post](https://www.nea.com/blog/twelve-labs-multimodal-ai-investment)
- [PRWeb - Series A Announcement](https://www.prweb.com/releases/twelve-labs-earns-50-million-series-a-co-led-by-nea-and-nvidias-nventures-to-build-the-future-of-multimodal-ai-302163279.html)
- [SalesTools - Series B $103M Report](https://salestools.io/en/report/twelve-labs-raises-103m-series-b)
- [Tracxn - Twelve Labs Profile](https://tracxn.com/d/companies/twelvelabs/__eZXrk6YPamabNtuA7HzJhUEnE2Tu0OTrBAOris8TVJs)
- [Crunchbase - Twelve Labs](https://www.crunchbase.com/organization/twelve-labs-62b5)
- [Jae Lee - World Economic Forum Profile](https://www.weforum.org/people/jae-lee/)
- [AWS - TwelveLabs on Amazon Bedrock](https://aws.amazon.com/bedrock/twelvelabs/)
- [Twelve Labs Models Overview](https://www.twelvelabs.io/product/models-overview)
- [Starter Story - How 3 Founders Built Video AI](https://www.starterstory.com/twelve-labs-breakdown)
- [Cedra - Twelve Labs Video AI (Feb 2026)](https://www.cedra.ai/2026/02/24/can-twelve-labs-video-ai-revolution-avoid-bias-while-transforming-industries/)
- [Twelve Labs - Video Intelligence Going Agentic (Blog)](https://www.twelvelabs.io/blog/video-intelligence-is-going-agentic)
- [KED Global - NVIDIA Co-leads Series A](https://www.kedglobal.com/artificial-intelligence/newsView/ked202406050019)
- [Databricks Blog - Mastering Multimodal AI with Twelve Labs](https://www.databricks.com/blog/mastering-multimodal-ai-twelve-labs)
- [Oracle Customer Story - Twelve Labs](https://www.oracle.com/customers/twelvelabs/)
