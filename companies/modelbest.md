---
name: ModelBest
legal_name: ModelBest Inc. (面壁智能)
website: https://modelbest.cn
sector: On-Device AI / Small Language Models
founded: 2022
headquarters: Haidian District, Beijing, China
founders:
- name: Li Dahai (李大海)
  role: Co-founder & CEO
  nationality: Chinese (mainland)
  education:
  - Tsinghua University (affiliated)
  notable: Led the company's commercial strategy and partnerships with automotive/device OEMs
  origin: Chinese
- name: Liu Zhiyuan (刘知远)
  role: Co-founder & Chief Scientist
  nationality: Chinese (mainland)
  education:
  - Tsinghua University, tenured Associate Professor, Department of Computer Science
  notable: One of China's most prominent NLP researchers. Led the OpenBMB (Open Lab for Big Model Base) open-source initiative
    at Tsinghua. The academic backbone behind the CPM (Chinese Pre-trained Models) series that predates the ChatGPT era.
  origin: Chinese
team_size_estimate: ~100-200 (estimate)
stage: Series B+ (multiple rounds totaling hundreds of millions of RMB)
total_funding: Hundreds of millions of RMB across 3+ rounds (~$50-100M estimated)
estimated_valuation: Not publicly disclosed; likely $300-500M range given investor caliber
estimated_arr_2026: Not disclosed
tags:
- on-device-ai
- small-language-models
- edge-ai
- open-source-models
- tsinghua-spinout
- chinese-founders
- automotive-ai
last_updated: 2026-03-20
one_liner: 'ModelBest is a Tsinghua University spinout that has carved out a distinctive niche in China''s AI landscape: building
  high-performance small language models optimized for on-device deployment'
website_verified: true
crunchbase: https://www.crunchbase.com/organization/modelbest
crunchbase_verified: true
linkedin: https://www.linkedin.com/company/modelbest
funding_rounds:
  - stage: "Angel"
    date: "2023-04"
    lead_investors: ["Undisclosed"]
    source: "https://www.crunchbase.com/organization/modelbest"
  - stage: "Seed"
    date: "2024-04"
    lead_investors: ["Primavera Capital"]
    source: "https://www.crunchbase.com/organization/modelbest"
data_notes: "Funding data not fully disclosed. Raised hundreds of millions of RMB across multiple rounds (~$50-100M estimated). Exact amounts not publicly confirmed."
---

# ModelBest (面壁智能)

## Overview

ModelBest is a Tsinghua University spinout that has carved out a distinctive niche in China's AI landscape: building high-performance small language models optimized for on-device deployment. While most of China's AI Tigers compete on the scale of their foundation models, ModelBest has leaned into efficiency, developing the MiniCPM series -- compact models that run on smartphones, PCs, automotive systems, smart home devices, and robots.

The company emerged from the OpenBMB (Open Lab for Big Model Base) initiative at Tsinghua, which developed the CPM (Chinese Pre-trained Models) series starting in 2020 -- one of the earliest Chinese large language model efforts, predating the ChatGPT era. ModelBest commercializes this research with a focus on edge AI deployment at scale.

## Founders and Team Background

### Li Dahai (CEO)

- **Origin:** Mainland China
- **Role:** Leads business strategy and commercialization. Responsible for building partnerships with major device and automotive OEMs.
- **Profile:** The commercial counterpart to Liu Zhiyuan's academic leadership.

### Liu Zhiyuan (Chief Scientist)

- **Origin:** Mainland China
- **Education:** Tsinghua University, where he holds a tenured associate professor position in the Department of Computer Science and Technology.
- **Research:** One of China's leading NLP researchers. Founded and leads OpenBMB, the open-source community behind the CPM model series. His lab's work on Chinese pre-trained models dates back to 2020, making it one of the earliest Chinese LLM efforts.
- **Profile:** Represents the deep Tsinghua-to-startup pipeline that has produced multiple Chinese AI companies (Zhipu AI, Moonshot AI, etc.). Unlike those companies which target large-scale models, Liu's focus on efficient, deployable models reflects a distinct technical philosophy.

Sources:
- [Tsinghua NLP Lab page](https://nlp.csai.tsinghua.edu.cn/~lzy/)
- [Global Times interview with co-founder](https://www.globaltimes.cn/page/202406/1314470.shtml)

## Funding Rounds

| Round | Date | Amount | Lead Investor(s) | Key Co-Investors | Source |
|-------|------|--------|-------------------|-------------------|--------|
| Early rounds | 2022-2023 | Undisclosed | — | Zhihu (Chinese Quora-like platform) | — |
| Round (Huawei-led) | April 2024 | Hundreds of millions of RMB | Huawei Hubble Technology VC | Chunhua Capital, Beijing AI Industry Investment Fund, Zhihu | [Gasgoo](https://autonews.gasgoo.com/articles/icv/modelbest-secures-fresh-funding-to-accelerate-on-device-ai-deployment-70040208) |
| Round (Moutai-led) | May 2025 | Several hundred million RMB | Moutai Fund (co-led) | Hong Tai APlus, Guozhong Capital, SinoKing Capital | [AsianFin](https://www.asianfin.com/articles/126896) |

**Total raised:** Multiple rounds totaling hundreds of millions of RMB (estimated $50-100M+). Exact totals not publicly confirmed.

**Notable investors:** Huawei's venture arm (Hubble Technology) leading a round is strategically significant -- it signals alignment with Huawei's HarmonyOS and on-device AI ecosystem. Moutai (China's premier liquor brand) investing in an AI company reflects the broad Chinese enthusiasm for AI investment.

Sources:
- [Shanghai Metal Market on financing](https://www.metal.com/en/newscontent/103088170)
- [MIT Technology Review on Chinese startups](https://www.technologyreview.com/2025/02/04/1110942/four-chinese-ai-startups-deepseek/)

## Products and Technology

### MiniCPM Series

ModelBest's flagship product line. Key versions:

| Model | Description |
|-------|-------------|
| MiniCPM | Foundational small language model achieving GPT-3.5-comparable performance at a fraction of the size |
| MiniCPM-V | Multimodal variant supporting vision + language on-device |
| MiniCPM 4 / 4.1 | Latest generation, claiming "ultra-efficient LLMs on end devices" with 3x+ generation speedup on reasoning tasks |

**Deployment scale:** Over 10 million cumulative downloads across Hugging Face, Ollama, and ModelScope. Deployed at scale across automobiles, smartphones, PCs, and smart home devices.

**Key partnerships:** Geely, Changan, Volkswagen, Huawei -- major automotive OEMs integrating MiniCPM into vehicle systems.

### Open-Source Strategy

ModelBest maintains a strong open-source presence through the OpenBMB GitHub organization, which includes MiniCPM and related tools. This mirrors the broader Chinese AI open-source trend (DeepSeek, Qwen) but focused specifically on small, deployable models.

Sources:
- [GitHub OpenBMB/MiniCPM](https://github.com/OpenBMB/MiniCPM)
- [MarkTechPost on MiniCPM](https://www.marktechpost.com/2024/04/12/this-ai-paper-from-china-introduces-minicpm-introducing-innovative-small-language-models-through-scalable-training-approaches/)

## Business Model

ModelBest monetizes through:

1. **Enterprise licensing:** Licensing MiniCPM models to device OEMs (automotive, smartphone, PC manufacturers) for on-device deployment
2. **Integration services:** Custom model fine-tuning and deployment for enterprise clients
3. **Open-source + commercial:** Free open-source base models with commercial licensing for enterprise-scale deployment

The automotive AI integration is a particularly promising revenue stream, given the rapid adoption of in-vehicle AI assistants in China.

## What Makes ModelBest Interesting

1. **Contrarian bet on small models.** While the Chinese AI landscape is dominated by "bigger is better" foundation model competition, ModelBest has bet on efficiency and on-device deployment. This is proving prescient as the industry shifts toward edge AI.

2. **Tsinghua academic pedigree with early mover advantage.** The CPM model series predates ChatGPT and most Chinese LLM efforts. Liu Zhiyuan's research lab has been working on Chinese language models since 2020.

3. **Huawei ecosystem alignment.** Huawei Hubble leading a funding round signals deep integration with Huawei's device ecosystem (smartphones, HarmonyOS, automotive). In a market where Huawei is rebuilding its device business post-sanctions, an AI model partner is strategically valuable.

4. **Real-world deployment at scale.** Unlike many Chinese AI startups that compete on benchmarks, ModelBest has concrete deployments across major automotive OEMs -- Geely, Changan, and even Volkswagen. This represents tangible commercial traction.

5. **The Stanford plagiarism incident.** In 2024, a Stanford AI project was found to have plagiarized work from ModelBest's team, inadvertently validating the quality and originality of their research.

## Uncertainties and Caveats

- Exact funding amounts and valuation are not publicly confirmed. Chinese startup funding disclosures often use vague terms like "hundreds of millions of RMB."
- Revenue figures are not disclosed. The commercial viability of on-device AI licensing in China's competitive market is not yet proven at scale.
- Competition from Qualcomm, MediaTek, and other chip makers who bundle their own on-device AI solutions.
- Whether small models remain differentiated as larger models become more efficient (model distillation, quantization) is an open question.
