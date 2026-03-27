---
name: MiniMax (MiniMax Group Inc.)
ticker: 'SEHK: 100'
founded: '2021'
headquarters: Shanghai, China
founders:
- name: Yan Junjie (闫俊杰)
  role: CEO & Chairman
  background: Former VP & Deputy Head of Research at SenseTime; PhD from Chinese Academy of Sciences; postdoc at Tsinghua
    University
  origin: Chinese
- name: Zhou Yucong
  role: Executive Director, Visual Model Research & Engineering Lead
  background: Former SenseTime (2018-2019); former Huawei (2019-2022), focused on algorithms
  origin: Chinese
- name: Yang Bin
  role: Co-founder (listed as former co-founder in some sources)
  background: Veteran of China's AI scene
  origin: Chinese
- name: Yun Yeyi
  role: COO
  background: Former SenseTime employee
  origin: Chinese
sector: Artificial Intelligence — Foundation Models, Generative AI (Video, Text, Speech)
status: Public (Hong Kong IPO, January 9, 2026)
ipo_raised: ~$619M USD
market_cap_at_debut: ~$13.7B USD (after 109% first-day surge)
last_updated: 2026-03-20
one_liner: MiniMax is one of China's "Six AI Tigers" — the cohort of leading Chinese AI startups that emerged in the post-ChatGPT
  era (alongside Zhipu AI, Moonshot AI / Kimi, Baichuan, 01.AI, and StepFun)
website: https://www.minimax.io
website_verified: true
crunchbase: https://www.crunchbase.com/organization/minimax
crunchbase_verified: true
linkedin: https://www.linkedin.com/company/minimax-ai
total_raised_m: 1291
linkedin_verified: true
funding_rounds:
- stage: Angel
  date: 2021-12
  amount_m: 31
  lead_investors:
  - Hillhouse Capital
  other_investors:
  - miHoYo
  - Yunqi Capital
  - IDG Capital
  source: https://www.techflowpost.com/en-US/article/29875
- stage: Pre-A
  date: 2022-05
  amount_m: 50
  lead_investors:
  - Mingshi Capital
  source: https://www.techflowpost.com/en-US/article/29875
- stage: Series A
  date: 2023-06
  amount_m: 260
  lead_investors:
  - Tencent
  other_investors:
  - Xiaomi
  - Xiaohongshu
  - Shunwei Capital
  source: https://www.crunchbase.com/funding_round/minimax-a48a-series-a--0b8070b9
- stage: Series A+
  date: 2023-06
  amount_m: 50
  lead_investors:
  - HongShan (Sequoia China)
  source: https://www.techflowpost.com/en-US/article/29875
- stage: Series B
  date: 2024-03
  amount_m: 600
  lead_investors:
  - Alibaba Group
  other_investors:
  - HongShan Capital
  - Matrix Partners China
  - China Life
  source: https://siliconangle.com/2024/03/05/report-chinese-ai-startup-minimax-raises-600m-2-5b-valuation-led-alibaba/
- stage: Series B Extension
  date: 2025-07
  amount_m: 300
  lead_investors:
  - Shanghai STVC Group
  other_investors:
  - China Life
  source: https://hrone.com/blog/chinas-minimax-secures-300m-funding-valued-at-4b-tech-in-asia/
  notes: MiniMax IPO'd on HKEX Jan 9, 2026 raising $619M additional.
confidence: medium
---

# MiniMax

## Overview

MiniMax is one of China's "Six AI Tigers" — the cohort of leading Chinese AI startups that emerged in the post-ChatGPT era (alongside Zhipu AI, Moonshot AI / Kimi, Baichuan, 01.AI, and StepFun). Founded in December 2021 — notably *before* ChatGPT's public release — MiniMax has built a full-stack generative AI platform spanning large language models, video generation, and speech synthesis. The company listed on the Hong Kong Stock Exchange on January 9, 2026, in what became the largest IPO among AI foundation model companies globally at the time.

NVIDIA CEO Jensen Huang has publicly praised MiniMax as a "world-class" AI company.

## Founders & Team

### Yan Junjie (CEO, age ~36 as of 2026)

Yan Junjie is the driving force behind MiniMax. His trajectory is remarkable:

- Grew up in a county town in Henan province
- Undergraduate degree in Mathematics from Southeast University
- PhD from the Institute of Automation, Chinese Academy of Sciences
- Postdoctoral research at Tsinghua University
- Interned at Baidu in 2014
- Joined SenseTime and rose from intern to Vice President over roughly seven years, serving as Deputy Head of Research and CTO of the Smart City business unit
- Left SenseTime in late 2021 — just before its IPO — to found MiniMax, believing that "building general-purpose AI for the public was important"
- Became a billionaire at age 36 following the IPO

### Co-founders

- **Zhou Yucong** (age ~32): Executive Director and visual model research lead. Worked at SenseTime (2018-2019) and Huawei (2019-2022) on algorithm development before joining MiniMax.
- **Yang Bin**: Co-founder with deep AI industry experience. (Note: some later sources list him as a "former co-founder" — his current role is uncertain.)
- **Yun Yeyi**: COO, also formerly of SenseTime.

The SenseTime connection is a defining feature of MiniMax's DNA. Multiple founders and early employees came from SenseTime's research apparatus, bringing deep expertise in computer vision, deep learning, and distributed computing.

## Funding History

| Round | Date | Amount | Valuation | Lead / Key Investors |
|-------|------|--------|-----------|---------------------|
| Angel | 2021 | Undisclosed | — | Yunqi Partners |
| Seed | July 2022 | Undisclosed | — | Gaorong Capital, IDG Capital, miHoYo, Mingshi Investment |
| Series A | June 2023 | ~$250M | — | Tencent, HongShan Capital (fka Sequoia China) |
| Series B | March 2024 | ~$600M | $2.5B | Alibaba Group, Hillhouse Investment |
| Series B Extension | July 2025 | ~$300M | ~$4B | Shanghai STVC Group (state-owned capital) |
| **IPO (HKEX)** | **Jan 9, 2026** | **$619M** | **~$6.5B at offer; ~$13.7B after first-day trading** | Public market |

**Total pre-IPO funding**: ~$1.15B USD
**Key investors**: miHoYo (gaming company behind *Genshin Impact*), Alibaba, Tencent, Hillhouse Investment, HongShan Capital, IDG Capital, Yunqi Capital, Gaorong Capital, Shanghai STVC Group

The miHoYo backing is notable — it is a strategic investor, and the gaming company's involvement likely reflects both the AI-entertainment synergy and miHoYo founder Cai Haoyu's personal interest in AGI.

## Products & Technology

### Foundation Models

- **MiniMax-M2 / M2.7**: Text/code LLM built on a Mixture-of-Experts (MoE) architecture with 230B total parameters and ~10B active parameters per inference. Positioned as a cost-efficient coding and agent model (marketed at ~8% the price of Claude Sonnet with 2x speed). M2.7 is the latest iteration focusing on model self-improvement.
- **Hailuo Video Models (Video-01, Hailuo 02, Hailuo 2.3)**: AI video generation models. Hailuo 2.3 is the flagship, delivering near-photorealistic video with complex character body movements, cinematic camera work, and support for anime/illustration styles. Hailuo 2.3-fast is a speed-optimized variant.
- **MiniMax Speech-02 / Speech-2.8**: AI speech generation models.
- **Media Agent**: An evolution of the Hailuo Video Agent — a multi-modal creation tool that automatically selects the right model for a given input, enabling "one-click video generation."

### Consumer Products

- **Hailuo AI**: The main consumer-facing product for AI video generation, available globally.
- **Talkie**: An AI companion/character chat app for overseas markets. Ranked among the most-downloaded free entertainment apps in the U.S. (per WSJ, July 2024), with ~11M monthly active users at that time. Features AI-simulated conversations with virtual characters. Strong user stickiness and willingness to pay.
- **MiniMax Agent**: AI assistant product.
- **MiniMax Audio**: Audio generation product.

### Enterprise Platform

- Open platform for enterprise clients and developers
- ~214,000 enterprise clients and developers as of end of 2025
- ~236 million total users across all products as of end of 2025

## Business Model & Financials

MiniMax operates a **consumer-first** business model, which distinguishes it from many Chinese AI peers that lean heavily on enterprise/B2B revenue. The majority of commercial revenue comes from consumer products, particularly Talkie (subscriptions and advertising).

### Revenue (Full Year 2025)

- **Revenue**: $79.0M USD (+158.9% YoY, up from $30.5M in 2024)
- **International revenue**: ~73% of total (the overseas/consumer tilt is distinctive)
- **Gross profit**: $20.1M (+437.2% YoY)
- **Gross margin**: 25.4% (up 13.2 percentage points YoY)
- **Adjusted net loss**: $250.9M (roughly flat vs. $244.2M in 2024)
- **Reported net loss**: $1.87B (inflated by $1.59B in fair-value losses on financial liabilities — a non-cash, non-operational item common in pre-IPO structures)

The company is still deeply unprofitable on an absolute basis, which is typical for foundation model companies at this stage.

## What Makes MiniMax Interesting

1. **Pre-ChatGPT conviction**: Founded in December 2021, before ChatGPT launched. Yan Junjie left a VP role at SenseTime on the eve of its IPO because he believed in general-purpose AI — a high-conviction bet that paid off.

2. **Consumer-first in a B2B-heavy market**: Most Chinese AI Tigers lean toward enterprise sales. MiniMax built Talkie into a top-ranked U.S. entertainment app and derives 73% of revenue from international markets. This is rare for a Chinese AI company.

3. **Full multimodal stack**: Unlike competitors that specialize in one modality, MiniMax has competitive offerings across text (M2), video (Hailuo), and speech (Speech-02), plus an agent framework that ties them together.

4. **Hailuo video quality**: The Hailuo video models are widely regarded as among the best globally for AI video generation, competing with Runway, Pika, and Sora. The Hailuo 2.3 model's realism in character movement and cinematic quality has drawn significant attention.

5. **Jensen Huang endorsement**: Being publicly called "world-class" by the NVIDIA CEO is meaningful signal in the AI industry.

6. **Blockbuster IPO**: 109% first-day pop, 1,830x retail oversubscription, and subsequent ~5x appreciation from IPO price. The market is pricing in significant growth expectations.

7. **SenseTime talent pipeline**: The founding team's deep roots in SenseTime's research infrastructure gave MiniMax a strong technical foundation, particularly in computer vision (which feeds into the video generation capability).

8. **Strategic investor base**: miHoYo, Alibaba, Tencent, and state-owned Shanghai capital — covering gaming, cloud infrastructure, distribution, and government alignment.

## Risks & Open Questions

- Still deeply unprofitable; path to profitability unclear given the capital intensity of foundation model development
- Heavy reliance on Talkie for consumer revenue — concentration risk
- U.S.-China geopolitical tensions could affect the overseas consumer business (73% of revenue)
- Compute access constraints under U.S. chip export controls
- Intense competition from both Chinese peers (Zhipu, Kimi, etc.) and global players (OpenAI, Google, etc.)
- Stock has appreciated ~5x from IPO — pricing is aggressive relative to current revenue

## Sources

- [Caproasia — MiniMax Plans Hong Kong IPO](https://www.caproasia.com/2025/12/23/china-ai-startup-minimax-plans-hong-kong-ipo-in-2026-q1-to-raise-700-million-at-4-billion-valuation-founded-in-2022-by-yan-junjie-yang-bin-zhou-yucong-investors-include-mihoyo-alibaba-tencent/)
- [TechNode — MiniMax Jumps on Hong Kong Debut](https://technode.com/2026/01/09/mihoyo-backed-ai-firm-minimax-jumps-on-hong-kong-debut-market-value-tops-11-5-billion/)
- [CNBC — MiniMax Doubles in Hong Kong Debut](https://www.cnbc.com/2026/01/09/minimax-hong-kong-ipo-ai-tigers-zhipu.html)
- [SCMP — MiniMax Shines on IPO Debut](https://www.scmp.com/business/banking-finance/article/3339251/chinese-ai-start-minimax-shines-hong-kong-ipo-debut)
- [SCMP — MiniMax 'World-Class' AI Startup Applies for HK IPO](https://www.scmp.com/business/banking-finance/article/3318485/minimax-world-class-ai-start-lauded-jensen-huang-applies-hong-kong-ipo)
- [VnExpress — Yan Junjie Becomes Billionaire at 36](https://e.vnexpress.net/news/business/billionaires/yan-junjie-founder-of-chinese-ai-firm-minimax-becomes-billionaire-at-36-5005067.html)
- [PANews — MiniMax: A Young Man from Henan](https://www.panewslab.com/en/articles/019d0038-e2d3-714a-a59f-417a9db968d4)
- [Wikipedia — Yan Junjie](https://en.wikipedia.org/wiki/Yan_Junjie)
- [Wikipedia — MiniMax Group](https://en.wikipedia.org/wiki/MiniMax_(company))
- [36Kr — Unicorns Emerge from SenseTime Ecosystem](https://eu.36kr.com/en/p/3609258452141057)
- [KrASIA — SenseTime Alumni Emerge as New Draw for Investors](https://kr-asia.com/after-dji-sensetime-alumni-emerge-as-a-new-draw-for-investors)
- [Asia Tech Lens — Meet MiniMax](https://www.asiatechlens.com/p/meet-minimax-the-chinese-tech-company)
- [Quartz — Meet the Six Tigers](https://qz.com/china-six-tigers-ai-startup-zhipu-moonshot-minimax-01ai-1851768509)
- [Yicai Global — MiniMax Revenue More Than Doubles](https://www.yicaiglobal.com/news/minimax-surges-despite-chinese-ai-startups-annual-loss-swelling-as-revenue-soars)
- [MiniMax Official — Full Year 2025 Financial Results](https://www.minimax.io/news/minimax-global-announces-full-year-2025-financial-results)
- [MiniMax Official — Hailuo 2.3 Announcement](https://www.minimax.io/news/minimax-hailuo-23)
- [MiniMax Official — M2 Model](https://www.minimax.io/news/minimax-m2)
- [SiliconANGLE — MiniMax Raises $619M in Hong Kong IPO](https://siliconangle.com/2026/01/08/minimax-raises-619m-hong-kong-ipo-investor-appetite-generative-ai-remains-strong/)
- [Bloomberg — MiniMax Shares Double in Hong Kong Debut](https://www.bloomberg.com/news/articles/2026-01-08/ai-firm-minimax-set-for-hong-kong-debut-after-619-million-ipo)
- [Founded.com — MiniMax $618M IPO Creates China's Latest AI Billionaire](https://www.founded.com/minimaxs-618m-ipo-creates-chinas-latest-ai-billionaire/)
- [US News — China's MiniMax Reports Strong Revenue Growth](https://money.usnews.com/investing/news/articles/2026-03-02/chinas-minimax-reports-strong-revenue-growth-charts-broader-ai-ambitions)
