---
founded: June
headquarters: San Francisco, CA
sector: AI Infrastructure / Cloud
subsector: Open-Source AI Inference, Training & Fine-Tuning
website: https://www.together.ai
estimated_annual_revenue: ~$300M ARR (Sep 2025 est.)
employee_count_approx: ~200 (est. late 2025)
status: Private
last_updated: 2026-03-20
funding_rounds:
- stage: Seed
  date: 2023-05
  amount_m: 20.0
  lead_investors:
  - Lux Capital
  source: https://www.together.ai/blog/series-a
- stage: Series A
  date: 2023-11
  amount_m: 102.5
  lead_investors:
  - Kleiner Perkins
  - NVIDIA
  source: https://techcrunch.com/2023/11/29/together-lands-102-5m-investment-to-grow-its-cloud-for-training-generative-ai/
- stage: Series A Extension
  date: 2024-03
  amount_m: 106.0
  valuation_m: 1250.0
  lead_investors:
  - Salesforce Ventures
  source: https://news.crunchbase.com/cloud/together-ai-valuation-jump-general-catalyst-nvda/
- stage: Series B
  date: 2025-02
  amount_m: 305.0
  valuation_m: 3300.0
  lead_investors:
  - General Catalyst
  - Prosperity7 Ventures
  source: https://www.together.ai/blog/together-ai-announcing-305m-series-b
founders:
- name: Vipul Ved Prakash
  role: Co-Founder & CEO
  background: Serial entrepreneur; created Vipul's Razor (anti-spam); co-founded Cloudmark and Topsy Labs (acquired by Apple
    ~$200M). Former Director of Engineering at Apple
  origin: Indian-American
- name: Ce Zhang
  role: Co-Founder & CTO
  background: Associate Professor of Computer Science at ETH Zurich (on leave); expert in decentralized/distributed training
    and data-centric ML Ops
  origin: Chinese
one_liner: Together AI is an AI-native cloud platform that provides infrastructure for running, training, and fine-tuning
  open-source AI models
website_verified: true
linkedin: https://www.linkedin.com/company/togethercomputer
twitter: '@togethercompute'
crunchbase: https://www.crunchbase.com/organization/together-ai
crunchbase_verified: true
name: Together AI
linkedin_verified: true
total_raised_m: 534.0
latest_valuation_m: 3300.0
confidence: high
---

# Together AI

## Overview

Together AI is an AI-native cloud platform that provides infrastructure for running, training, and fine-tuning open-source AI models. The company positions itself as the leading alternative to closed-model providers (OpenAI, Anthropic) by offering a full-stack cloud optimized for open-source models. Its core thesis: enterprises and developers increasingly want control over their AI stack, and open-source models are closing the quality gap with proprietary ones.

## Founders & Leadership

Together AI was co-founded by five individuals with deep roots in AI research and entrepreneurship, primarily connected through Stanford University.

### Vipul Ved Prakash -- CEO & Co-Founder
- Serial entrepreneur and former Apple executive.
- Created Vipul's Razor (anti-spam system); co-founded Cloudmark and Topsy Labs.
- Topsy was acquired by Apple (~$200M, 2013); Prakash served as Director of Engineering at Apple post-acquisition.
- Brings operator/business-building experience to complement the research co-founders.
- Source: [Contrary Research](https://research.contrary.com/company/together-ai), [Clay](https://www.clay.com/dossier/together-ai-ceo)

### Ce Zhang -- Co-Founder & CTO
- Associate Professor of Computer Science at ETH Zurich (on leave).
- Expert in decentralized/distributed training and data-centric ML Ops.
- Research focus on making ML systems more efficient and accessible.
- Source: [Salesforce Ventures](https://salesforceventures.com/perspectives/welcome-together-ai/)

### Chris Re -- Co-Founder
- Professor of Computer Science at Stanford University.
- Co-director of the Stanford Center for Research on Foundation Models (CRFM).
- Also co-founded SambaNova Systems (another AI chip/infrastructure company).
- Known for research on data-centric AI and novel model architectures.
- Source: [Emergence Capital](https://www.emcap.com/thoughts/building-the-future-of-ai-together)

### Percy Liang -- Co-Founder
- Associate Professor of Computer Science at Stanford University.
- Co-director of Stanford CRFM alongside Chris Re.
- Leading researcher in foundation model evaluation and benchmarking (HELM benchmark).
- Source: [Contrary Research](https://research.contrary.com/company/together-ai)

### Tri Dao -- Co-Founder & Chief Scientist
- PhD from Stanford (advised by Chris Re and Stefano Ermon).
- Creator of **FlashAttention** and **FlashAttention-2**, which became standard infrastructure for efficient transformer training worldwide.
- Now also Assistant Professor at Princeton University.
- FlashAttention alone would make Tri Dao one of the most impactful AI researchers of the 2020s; his presence at Together AI is a significant talent moat.
- Source: [Together AI Blog](https://www.together.ai/blog/tri-dao-flash-attention), [AI2050](https://ai2050.schmidtsciences.org/fellow/tri-dao/)

## Funding History

| Round | Date | Amount | Valuation | Lead Investor(s) | Key Co-Investors | Source |
|-------|------|--------|-----------|-------------------|-------------------|--------|
| Seed | May 2023 | $20M | Undisclosed | Lux Capital | SV Angel, First Round Capital, Long Journey Ventures, Robot Ventures, Definition Capital, Susa Ventures, Cadenza Ventures, SCB 10X; angels incl. Scott Banister (PayPal co-founder) | [TechCrunch](https://techcrunch.com/2023/05/15/together-raises-20m-to-build-open-source-generative-ai-models/) |
| Series A | Nov 29, 2023 | $102.5M | ~$650M (est.) | Kleiner Perkins | NVIDIA, NEA, Emergence Capital, Prosperity7, Greycroft, 137 Ventures, Lux Capital, Definition Capital, Long Journey Ventures, SCB10x, SV Angel | [Together AI Blog](https://www.together.ai/blog/series-a) |
| Series A-1 (Extension) | Mar 13, 2024 | $106M | $1.25B | Salesforce Ventures | Coatue Management, Lux Capital, Emergence Capital | [Yahoo Finance](https://finance.yahoo.com/news/together-ai-valued-1-25-160246183.html) |
| Series B | Feb 20, 2025 | $305M | $3.3B | General Catalyst, Prosperity7 (co-lead) | Salesforce Ventures, DAMAC Capital, NVIDIA, Kleiner Perkins, March Capital, Emergence Capital, Lux Capital, SE Ventures, Greycroft, Coatue, Definition, Cadenza Ventures, Long Journey Ventures, Brave Capital, SK Telecom, Scott Banister, John Chambers | [Together AI Blog](https://www.together.ai/blog/together-ai-announcing-305m-series-b) |

**Total raised: ~$534M across 4 rounds.**

*Note: The Series A valuation of ~$650M is an estimate based on the reported doubling to $1.25B at the A-1 round. Exact Series A valuation was not publicly disclosed.*

## Business Model

Together AI generates revenue through two primary lines:

1. **Serverless Inference API (est. 30-40% of revenue):** Pay-per-token pricing for running open-source models (Llama, Mixtral, etc.) via Together's API endpoints. Attractive to startups and developers with variable workloads. No infrastructure management or long-term commitments required.

2. **Dedicated GPU Clusters (est. 60-70% of revenue):** Longer-term rentals of GPU capacity for training, fine-tuning, and high-volume inference. Enterprise customers commit to larger contracts. Includes access to NVIDIA H100 and Blackwell GPUs.

3. **Platform Services:** Fine-tuning workflows, custom model training, and model optimization tooling layered on top of the compute.

Revenue trajectory:
- 2024 full-year revenue: ~$130M
- Sep 2025 annualized revenue: ~$300M (per [Sacra](https://sacra.com/c/together-ai/) estimates)
- 10x YoY growth in annual contract revenue (ACR) reported at AI Native Conf, March 2026
- 27 customer deals exceeding $1M; one deal exceeding $1B (likely a hyperscaler or large enterprise commitment)

Source: [Sacra](https://sacra.com/c/together-ai/), [PR Newswire](https://www.prnewswire.com/news-releases/together-ai-announces-business-and-product-milestones-at-first-ai-native-conference-302705505.html)

## Customers & Ecosystem

- **Named customers:** Cursor (AI code editor), Decagon (AI customer support), Cartesia (AI model company).
- **Scale:** Thousands of enterprise customers, 1M+ developers on the platform.
- **Use cases:** Production inference for AI-native applications, pre-training custom models, fine-tuning open-source models on proprietary data.
- Together AI operates its own data centers in **Maryland** (live Jul 2025), **Memphis**, and **Sweden** (live Sep 2025), supplemented by capacity from CoreWeave, Lambda Labs, and academic institutions.

Source: [PR Newswire](https://www.prnewswire.com/news-releases/together-ai-announces-business-and-product-milestones-at-first-ai-native-conference-302705505.html)

## What Makes Together AI Interesting

### 1. Founder-Research Moat
The founding team represents a unique concentration of top-tier AI research talent. Three Stanford professors (Re, Liang, Dao) plus an ETH Zurich professor (Zhang), combined with a proven operator-CEO (Prakash). Tri Dao's FlashAttention is arguably the single most impactful systems optimization in modern deep learning -- and Together AI gets first access to his research pipeline.

### 2. Open-Source Bet Is Paying Off
Together AI wagered early that open-source models would become competitive with proprietary ones. That thesis has been validated by Meta's Llama family, Mistral, DeepSeek, and others. As open-source models improve, demand for infrastructure to run them grows -- and Together AI is the dedicated platform.

### 3. Research-to-Product Pipeline
The company doesn't just host models; it produces foundational research:
- **FlashAttention / FlashAttention-2:** Now industry-standard for efficient attention computation.
- **RedPajama:** One of the first large-scale open-source training dataset efforts.
- **Inference optimizations:** Speculative decoding, near-lossless quantization, and custom draft models that deliver up to 2x faster inference than competitors on key benchmarks.

### 4. Rapid Revenue Growth
Growing from ~$130M to ~$300M ARR in under a year, with a $1B+ single customer deal, suggests strong product-market fit. The 10x YoY ACR growth reported in March 2026 is exceptional.

### 5. Vertical Integration
Moving from pure API/cloud to owning data centers (Maryland, Memphis, Sweden) gives Together AI more control over margins, latency, and capacity -- critical as GPU supply remains constrained.

## Competitive Landscape

| Competitor | Differentiation |
|------------|----------------|
| Fireworks AI | Direct competitor; also fast GPU-based inference for open-source models |
| Groq, Cerebras, SambaNova | Custom silicon; faster on raw speed but less model flexibility |
| Replicate, Modal, Baseten | Developer-friendly inference platforms; less research depth |
| DeepInfra | Price-competitive open-source inference |
| Major clouds (AWS, GCP, Azure) | Broader ecosystem but less optimized for open-source AI workloads |

Together AI's edge vs. pure inference competitors is the research bench (FlashAttention, training expertise) and vs. hyperscalers is specialization and speed.

## Key Risks

- **Margin pressure:** Inference is becoming commoditized; price competition from Groq, DeepInfra, and hyperscalers could compress margins.
- **GPU dependency:** Heavy reliance on NVIDIA hardware; supply constraints or pricing shifts could impact operations.
- **Concentration risk:** A $1B+ single customer deal is impressive but creates dependency. If that customer churns, it would be material.
- **Open-source model quality plateau:** If open-source models stop closing the gap with proprietary ones, the core thesis weakens.

## Sources

- [Together AI Official Blog - Series B](https://www.together.ai/blog/together-ai-announcing-305m-series-b)
- [Together AI Official Blog - Series A](https://www.together.ai/blog/series-a)
- [Together AI Official Blog - Seed Funding](https://www.together.ai/blog/seed-funding)
- [Together AI - AI Native Conf Milestones (Mar 2026)](https://www.prnewswire.com/news-releases/together-ai-announces-business-and-product-milestones-at-first-ai-native-conference-302705505.html)
- [Sacra - Together AI Revenue & Valuation](https://sacra.com/c/together-ai/)
- [TechCrunch - Seed Round](https://techcrunch.com/2023/05/15/together-raises-20m-to-build-open-source-generative-ai-models/)
- [Yahoo Finance - $1.25B Valuation](https://finance.yahoo.com/news/together-ai-valued-1-25-160246183.html)
- [Contrary Research - Business Breakdown](https://research.contrary.com/company/together-ai)
- [Crunchbase - Together AI](https://www.crunchbase.com/organization/together-1a7e)
- [Emergence Capital](https://www.emcap.com/thoughts/building-the-future-of-ai-together)
- [Salesforce Ventures](https://salesforceventures.com/perspectives/welcome-together-ai/)
- [Together AI Blog - Tri Dao & FlashAttention](https://www.together.ai/blog/tri-dao-flash-attention)
