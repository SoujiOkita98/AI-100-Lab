---
company: Fireworks AI
legal_name: Fireworks AI, Inc.
founded: 2022
headquarters: Redwood City, CA
sector: AI Infrastructure
subsector: Generative AI Inference & Model Deployment
website: https://fireworks.ai
total_funding: ~$331M
latest_valuation: $4B (Oct 2025, Series C)
estimated_annual_revenue: ~$130M ARR (May 2025 est., per Sacra)
employee_count_approx: ~166 (Jan 2026)
status: Private
tags:
- AI inference
- compound AI
- open-source models
- PyTorch
- LLM serving
- fine-tuning
- enterprise AI
- model deployment
last_updated: 2026-03-20
funding_rounds:
- stage: Series A
  date: 2024-03
  amount_m: 25
  lead_investors:
  - Benchmark
  source: https://www.thesaasnews.com/news/fireworks-ai-secures-25-million-in-series-a
- stage: Series B
  date: 2024-07
  amount_m: 52
  valuation_m: 552
  lead_investors:
  - Sequoia Capital
  source: https://fireworks.ai/blog/fireworks-ai-series-b-compound-ai
- stage: Series C
  date: 2025-10
  amount_m: 250
  valuation_m: 4000
  lead_investors:
  - Lightspeed Venture Partners
  - Index Ventures
  source: https://fireworks.ai/blog/series-c
one_liner: Fireworks AI is a high-performance AI inference platform founded by the team that built and maintained PyTorch
  at Meta
website_verified: true
twitter: '@FireworksAI_HQ'
linkedin: https://www.linkedin.com/company/fireworks-ai
crunchbase: https://www.crunchbase.com/organization/fireworks-ai
crunchbase_verified: true
founders:
- name: Lin Qiao
  role: CEO
  background: PhD CS, UC Santa Barbara. Former Head of PyTorch at Meta.
  origin: Chinese-American
- name: Benny Chen
  role: Co-founder
  background: Former Meta Ads Infrastructure Lead.
  origin: Chinese-American
- name: Dmytro Dzhulgakov
  role: Co-founder
  background: PyTorch core maintainer at Meta.
  origin: Ukrainian
name: Fireworks AI
linkedin_verified: true
---

# Fireworks AI

## Overview

Fireworks AI is a high-performance AI inference platform founded by the team that built and maintained PyTorch at Meta. The company's core thesis is that inference -- not training -- is the bottleneck for enterprise AI adoption, and that a purpose-built serving stack can deliver dramatically better speed, cost, and flexibility than generic cloud infrastructure. As of 2025, Fireworks processes over 10 trillion tokens per day for more than 10,000 customers. In March 2026, it launched on Microsoft Foundry in public preview, integrating its inference engine directly into the Azure enterprise stack.

## Founders & Leadership

Fireworks AI was co-founded in 2022 by seven former Meta and Google engineers, nearly all drawn from the PyTorch ecosystem. The founding team is notably international, with roots in China, Ukraine, and the United States.

### Lin Qiao -- CEO & Co-Founder
- Born and educated in China. Graduated from **Fudan University** (Shanghai) with BS and MS in Computer Science before earning a **Ph.D. in Computer Science from UC Santa Barbara**.
- 24+ years of industry experience: began at IBM Research, then served as engineering lead at LinkedIn, and ultimately became **Head of PyTorch at Meta**, overseeing deployment across Meta's data centers, mobile devices, and AR/VR hardware.
- Recognized by 36Kr as one of China's most notable female founders in tech.
- Sources: [36Kr profile](https://eu.36kr.com/en/p/3407737936137857), [Sequoia podcast](https://sequoiacap.com/podcast/training-data-lin-qiao/), [The AI Conference](https://aiconference.com/speakers/lin-qiao/)

### Dmytro Dzhulgakov -- CTO & Co-Founder
- Originally from **Kharkiv, Ukraine**. Graduated from Kharkiv Polytechnic Institute.
- Joined Facebook in 2011; became a **PyTorch core maintainer** at Meta, working closely with Lin Qiao.
- Sources: [LinkedIn](https://www.linkedin.com/in/dzhulgakov/), [Scroll Media](https://scroll.media/en/2025/05/19/fireworks-ai-soars-from-552m-to-4b-valuation-two-ukrainians-among-founders/)

### Dmytro Ivchenko -- Co-Founder
- Originally from **Kyiv, Ukraine**. Graduated from Kyiv Polytechnic Institute.
- Worked at LinkedIn and then Meta, where he led **PyTorch for ranking**.
- Sources: [dev.ua](https://dev.ua/en/news/american-startup-fireworks-ai-co-founded-by-two-ukrainians-raises-4-billion-in-investment)

### Other Co-Founders
- **Benny Chen** -- Previously Meta ads infrastructure lead.
- **Chenyu Zhao** -- Previously Google Vertex AI lead.
- **James Reed** -- Previously PyTorch compiler at Meta.
- **Pawel Garbacki** -- Previously Meta Newsfeed core ML lead.
- Source: [Fireworks Team page](https://fireworks.ai/team)

## Funding History

| Round | Date | Amount | Valuation | Lead Investors | Notable Participants |
|-------|------|--------|-----------|---------------|---------------------|
| Series A | Mar 2024 | $25M | Undisclosed | Benchmark (Eric Vishria) | Sequoia Capital, Databricks Ventures, Frank Slootman (ex-Snowflake CEO), Alexandr Wang (Scale AI CEO) |
| Series B | Jul 2024 | $52M | ~$552M | Sequoia Capital | Nvidia, AMD, MongoDB, Benchmark, Databricks Ventures, Sheryl Sandberg, Howie Liu (Airtable CEO) |
| Series C | Oct 2025 | $254M ($230M primary + $24M secondary) | $4B | Lightspeed Venture Partners, Index Ventures, Evantic | Sequoia Capital, Nvidia, AMD, Databricks |

**Total raised:** ~$331M

Note: No public seed round has been disclosed. The company operated for roughly two years before announcing its Series A, suggesting either bootstrapped early operations or undisclosed angel/pre-seed funding.

Sources: [BusinessWire Series C](https://www.businesswire.com/news/home/20251028604819/en/Fireworks-AI-Raises-$250M-Series-C-to-Lead-the-AI-Inference-Market), [SiliconANGLE Series B](https://siliconangle.com/2024/07/11/fireworks-ai-raises-52m-led-sequoia-522m-valuation/), [Finsmes Series A](https://www.finsmes.com/2024/03/fireworks-ai-raises-25m-in-series-a-funding.html), [Fireworks blog](https://fireworks.ai/blog/series-c)

## Business Model

Fireworks operates a **usage-based B2B infrastructure platform**. Revenue scales with customer token consumption rather than per-seat licensing:

- **Serverless inference** -- Pay-per-token pricing for API calls to open-source and proprietary models.
- **Dedicated/reserved deployments** -- GPU-hour billing for customers needing guaranteed capacity.
- **Fine-tuning services** -- Per-task charges for LoRA and reinforcement learning-based model customization.
- **Provisioned throughput units (PTUs)** -- Available through the Microsoft Foundry integration for steady-state workloads.

Sacra estimated ~$130M ARR as of May 2025, representing roughly 20x growth from ~$6.5M ARR in May 2024. This growth trajectory (if accurate) is exceptional even by AI infrastructure standards.

Sources: [Sacra](https://sacra.com/c/fireworks-ai/), [Lightspeed investment memo](https://lsvp.com/stories/our-investment-in-fireworks-ai-the-inference-platform-aiming-to-power-every-genai-application/)

## Key Products & Technology

- **FireAttention V2** -- Custom CUDA kernel-based serving stack claiming 12x faster inference for long-context prompts (RAG, multi-turn, multimodal).
- **FireFunction V2** -- Function-calling model benchmarked on par with GPT-4o at 2.5x speed and ~10% of cost (per company claims).
- **Compound AI orchestration** -- Agent orchestration combining multiple models, retrievers, and external APIs in a single pipeline.
- **Ultra-fast LoRA fine-tuning** -- Dataset-to-query in minutes, not hours.
- **Model lifecycle management** -- Deploy, version, A/B test, and rollback models.
- **Global Virtual Cloud** -- Spans 8 cloud providers and 18 regions for data sovereignty and latency optimization.
- **Eval Protocol** (launched 2025) -- Structured model evaluation framework paired with application-tailored reinforcement learning tuning.

Sources: [eesel.ai overview](https://www.eesel.ai/blog/fireworks-ai), [Fireworks Series B blog](https://fireworks.ai/blog/fireworks-ai-series-b-compound-ai)

## Customers

Notable enterprise customers (as of late 2025):
- **Samsung**
- **Uber**
- **DoorDash**
- **Notion**
- **Shopify**
- **Upwork**

The company reports 10,000+ customers total and 99.99% API uptime.

Sources: [BusinessWire](https://www.businesswire.com/news/home/20251028604819/en/Fireworks-AI-Raises-$250M-Series-C-to-Lead-the-AI-Inference-Market)

## Strategic Partnerships

- **Microsoft Foundry** (Mar 2026) -- Multi-year partnership; Fireworks inference engine available natively on Azure with models including DeepSeek V3.2, Kimi K2.5, and MiniMax M2.5.
- **Nvidia** and **AMD** -- Both are investors and hardware partners.
- **Databricks** -- Investor; complementary positioning (Databricks for data/training, Fireworks for inference).

Sources: [Azure Blog](https://azure.microsoft.com/en-us/blog/introducing-fireworks-ai-on-microsoft-foundry-bringing-high-performance-low-latency-open-model-inference-to-azure/), [Fireworks blog](https://fireworks.ai/blog/fireworks-on-microsoft-foundry)

## Competitive Landscape

Direct competitors in the AI inference infrastructure space:
- **Together AI** -- Similar open-model inference platform; higher reported ARR (~$300M est.) but similar valuation tier.
- **Groq** -- Custom LPU hardware for inference; different approach (custom silicon vs. GPU optimization).
- **Modal** -- Developer-focused serverless GPU platform.
- **Baseten** -- Model serving infrastructure.
- **Anyscale / vLLM ecosystem** -- Open-source inference serving.
- **Hyperscaler native offerings** -- AWS Bedrock, Azure AI, Google Vertex AI.

Fireworks differentiates primarily through its custom CUDA kernel stack (FireAttention), compound AI orchestration, and the depth of its PyTorch-native engineering team.

## What Makes Fireworks AI Interesting

1. **Founding team pedigree is unusually deep.** Seven co-founders who collectively built and maintained PyTorch -- the dominant deep learning framework -- at Meta. This is not "ex-FAANG" branding; this team literally wrote the infrastructure that most AI companies depend on.

2. **Immigrant founder story.** The leadership reflects the international talent pipeline that drives Silicon Valley AI: a Chinese-born CEO from Fudan University, two Ukrainian co-founders from Kharkiv and Kyiv, and additional founders from Google and Meta's global engineering orgs. The company is a case study in how deep technical talent from global universities (Fudan, Kharkiv Polytechnic, Kyiv Polytechnic, UCSB) converges in the Bay Area startup ecosystem.

3. **Inference-as-the-bottleneck thesis.** While most AI funding has chased training (frontier model labs, GPU clouds), Fireworks bet early that inference cost and latency would be the binding constraint for enterprise adoption. The 20x ARR growth suggests this thesis is playing out.

4. **Compound AI vision.** Fireworks is positioning not just as a fast inference endpoint but as orchestration infrastructure for multi-model, multi-tool AI systems -- the "compound AI" paradigm championed by Berkeley and Databricks researchers. This is a bet on the architecture of future AI applications.

5. **Strategic investor constellation.** Having Nvidia, AMD, Sequoia, Lightspeed, Index, and Databricks as investors creates a web of distribution and integration partnerships that is difficult for competitors to replicate.

6. **Microsoft Foundry integration (2026).** Being embedded natively in Azure positions Fireworks to capture enterprise workloads that require cloud governance and compliance -- a channel that pure-play API startups typically struggle to access.

## Uncertainties & Open Questions

- The ~$130M ARR figure comes from Sacra's estimate, not company disclosure. Actual revenue could differ.
- No seed/pre-seed round has been publicly disclosed, leaving a gap in early funding history.
- Employee count sources vary (120-166 range); the company may be lean relative to its valuation.
- Long-term defensibility against hyperscaler inference optimization (e.g., AWS Inferentia, Google TPU inference) is unproven.
- The 10 trillion tokens/day figure (from Oct 2025 press release) has not been independently verified.

## Sources

- [Fireworks AI Series C announcement (BusinessWire)](https://www.businesswire.com/news/home/20251028604819/en/Fireworks-AI-Raises-$250M-Series-C-to-Lead-the-AI-Inference-Market)
- [Fireworks AI Series C blog](https://fireworks.ai/blog/series-c)
- [SiliconANGLE -- Series B](https://siliconangle.com/2024/07/11/fireworks-ai-raises-52m-led-sequoia-522m-valuation/)
- [Finsmes -- Series A](https://www.finsmes.com/2024/03/fireworks-ai-raises-25m-in-series-a-funding.html)
- [Sacra -- Revenue & Valuation](https://sacra.com/c/fireworks-ai/)
- [Lightspeed investment memo](https://lsvp.com/stories/our-investment-in-fireworks-ai-the-inference-platform-aiming-to-power-every-genai-application/)
- [Index Ventures -- Inference is the New Runtime](https://www.indexventures.com/perspectives/inference-is-the-new-runtime-our-investment-in-fireworks/)
- [Sequoia -- Training Data podcast with Lin Qiao](https://sequoiacap.com/podcast/training-data-lin-qiao/)
- [36Kr -- Lin Qiao / Fudan profile](https://eu.36kr.com/en/p/3407737936137857)
- [Scroll Media -- Ukrainian co-founders](https://scroll.media/en/2025/05/19/fireworks-ai-soars-from-552m-to-4b-valuation-two-ukrainians-among-founders/)
- [dev.ua -- Ukrainian co-founders](https://dev.ua/en/news/american-startup-fireworks-ai-co-founded-by-two-ukrainians-raises-4-billion-in-investment)
- [Azure Blog -- Microsoft Foundry partnership](https://azure.microsoft.com/en-us/blog/introducing-fireworks-ai-on-microsoft-foundry-bringing-high-performance-low-latency-open-model-inference-to-azure/)
- [Fireworks Team page](https://fireworks.ai/team)
- [eesel.ai -- Fireworks AI overview](https://www.eesel.ai/blog/fireworks-ai)
- [SiliconANGLE -- Series C](https://siliconangle.com/2025/10/28/fireworks-ai-gets-250m-funding-help-enterprises-ai-inference-workloads/)
