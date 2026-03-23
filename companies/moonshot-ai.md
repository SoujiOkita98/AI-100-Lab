---
name: "Moonshot AI"
founded: 2023
headquarters: "Beijing, China"
website: "https://www.moonshot.cn"
sector: ["foundation models", "long-context AI", "consumer AI"]
one_liner: "Beijing-based AI lab behind the Kimi chatbot, pioneering long-context LLMs in China."
status: active
total_raised_m: 3000
latest_valuation_m: 18000
founders:
  - name: "Yang Zhilin"
    role: "CEO"
    background: "BS CS Tsinghua, PhD CS Carnegie Mellon. Co-first author of Transformer-XL and XLNet. Research at Google Brain and Meta AI."
    origin: "Chinese"
  - name: "Zhou Xinyu"
    role: "Co-founder"
    background: "Tsinghua University. Former engineering at Hulu, Tencent, and Megvii."
    origin: "Chinese"
  - name: "Wu Yuxin"
    role: "Co-founder"
    background: "BS CS Tsinghua, MS CMU. Former Google Brain and Facebook AI Research."
    origin: "Chinese"
funding_rounds:
  - stage: "Seed"
    date: "2023-06"
    amount_m: 25
    lead_investors: ["HongShan (Sequoia China)", "ZhenFund"]
  - stage: "Series A"
    date: "2023-12"
    amount_m: 200
    lead_investors: ["HongShan", "ZhenFund"]
  - stage: "Series B"
    date: "2024-02"
    amount_m: 1000
    valuation_m: 2500
    lead_investors: ["Alibaba", "HongShan"]
  - stage: "Follow-on"
    date: "2024-08"
    amount_m: 300
    valuation_m: 3300
    lead_investors: ["Tencent", "Gaorong Capital"]
  - stage: "Series C"
    date: "2025-12"
    amount_m: 500
    valuation_m: 4300
    lead_investors: ["IDG Capital", "Alibaba", "Tencent"]
  - stage: "Series D"
    date: "2026-02"
    amount_m: 700
    valuation_m: 10000
    lead_investors: ["Alibaba", "Tencent"]
confidence: medium
last_updated: 2026-03-23
---

# Moonshot AI — Company Profile

## Overview

Moonshot AI (月之暗面, literally "Dark Side of the Moon") is a Beijing-based artificial intelligence company best known for its Kimi chatbot and large language model family. Founded in March 2023, the company has become China's fastest-ever decacorn, reaching a $10B+ valuation within roughly two years of founding. The company name is a nod to Pink Floyd's *The Dark Side of the Moon* — it launched on the album's 50th anniversary.

Moonshot AI pioneered long-context processing in the Chinese AI landscape. Its first Kimi release (October 2023) could handle 128K tokens — or approximately 200,000 Chinese characters — losslessly in a single conversation, a first-of-its-kind capability at the time.

## Founders & Leadership

### Yang Zhilin (杨植麟) — CEO & Co-Founder

- **Born:** 1992, China
- **Education:** B.S. in Computer Science, Tsinghua University (2015); Ph.D. in Computer Science, Carnegie Mellon University (2019, completed in 4 years vs. the typical 6)
- **PhD Advisors:** Ruslan Salakhutdinov (Apple's former Director of AI Research) and William W. Cohen (Google DeepMind principal scientist)
- **Industry experience:** Research stints at Google Brain and Meta AI (FAIR)
- **Key publications:** Co-first author of **Transformer-XL** and primary author of **XLNet** — both landmark papers in the evolution of transformer architectures. Published 20+ influential AI papers, with co-authors including Turing Award winners Yoshua Bengio and Yann LeCun.
- **Recognition:** Named to MIT Technology Review's *Innovators Under 35*

Yang is widely regarded as one of the strongest technical founders in the Chinese AI ecosystem. His academic work on extending transformer context windows directly informed Moonshot's long-context differentiation strategy.

### Zhou Xinyu — Co-Founder

- **Education:** Tsinghua University (classmate of Yang Zhilin)
- **Prior roles:** Engineering positions at Hulu, Tencent, and Megvii (Face++)
- **Focus area:** Systems engineering, model deployment, and inference optimization — particularly deploying deep neural networks on resource-constrained hardware
- **Role at Moonshot:** Leads production engineering, ensuring models scale from research to deployment

### Wu Yuxin — Co-Founder

- **Education:** B.S. in Computer Science, Tsinghua University (2015); M.S. in Computer Vision, Carnegie Mellon University
- **Prior roles:** Extended research stints at Google Brain (foundation model research) and Facebook AI Research (FAIR) with contributions to computer vision and AI infrastructure
- **Role at Moonshot:** Focuses on model architecture and AI infrastructure

All three co-founders were classmates at Tsinghua University and reportedly bandmates in a group called "Splay." The founding team combines deep research credentials (Yang, Wu) with production engineering expertise (Zhou).

## Funding History

| Round | Date | Amount | Valuation | Lead Investors |
|-------|------|--------|-----------|----------------|
| Seed | June 2023 | ~$25M (estimated) | ~$300M | HongShan (fka Sequoia China), ZhenFund |
| Series A | Late 2023 | ~$200M | ~$300M | HongShan, ZhenFund |
| Series B | February 2024 | ~$1B | $2.5B | Alibaba, HongShan, with Meituan and Xiaohongshu |
| Follow-on | August 2024 | ~$300M | $3.3B | Tencent, Gaorong Capital |
| Series C | Dec 2025–Jan 2026 | $500M | $4.3B | IDG Capital, Alibaba, Tencent |
| Series D (est.) | Feb 2026 | $700M+ | $10B | Alibaba, Tencent (increased stakes) |
| Reported new round | Mar 2026 (in progress) | Seeking $1B | ~$18B (target) | TBD |

**Note:** The exact structuring of early rounds (Seed vs. Series A) varies across sources. The $18B valuation round was reported by Bloomberg (March 14, 2026) but had not been officially confirmed as of this writing.

**Key investors across rounds:** Alibaba Group, Tencent, HongShan (Sequoia China), IDG Capital, Gaorong Capital, ZhenFund, Meituan, Xiaohongshu.

## Product & Technology

### Kimi Chatbot (Consumer Product)

- Launched in public beta: November 16, 2023
- Initially differentiated by **128K-token context window** (200K Chinese characters) — the first Chinese LLM to offer this
- March 2024: began testing a **2-million-character context window**
- July 2024: "context caching" entered public beta, reducing costs and latency for long-context use
- Available on web, iOS, Android, and via API

### Model Family Timeline

| Model | Release | Key Specs |
|-------|---------|-----------|
| Moonshot v1 | Oct 2023 | 128K context, Chinese-first LLM |
| Kimi K1.5 | ~2025 | Reasoning-focused model |
| Kimi K2 | July 2025 | 1T-parameter MoE, 32B active params, open-sourced (modified MIT license), 128K context |
| Kimi K2.5 | January 2026 | 1T-parameter MoE, 32B active params, native multimodal (vision + language), 256K context, Agent Swarm support |

### Kimi K2.5 — Current Flagship (as of March 2026)

- **Architecture:** 1 trillion parameter Mixture-of-Experts (MoE) with 32 billion active parameters
- **Training data:** 15 trillion tokens, mixing visual and textual data from the start (native multimodality rather than grafted-on vision)
- **Context window:** 256K tokens
- **Modes:** Instant mode and Thinking (reasoning) mode
- **Agent Swarm:** Coordinates up to 100 specialized AI agents working in parallel, reportedly cutting execution time by 4.5x
- **Benchmark claims:** 50.2% on Humanity's Last Exam at 76% lower cost than Claude Opus 4.5 (*company-reported; independent verification pending*)
- **Quantization:** Native INT4 weight-only quantization (group size 32) optimized for NVIDIA Hopper architecture

### Open Source

Kimi K2 was open-sourced under a modified MIT license and is available on Hugging Face (`moonshotai/Kimi-K2.5`), making it one of the most capable openly available MoE models.

## Business Model

Moonshot AI generates revenue through multiple channels:

1. **Consumer subscription (Kimi chatbot)**
   - Free tier ("Adagio"): unlimited basic conversations
   - Paid tier ("Andante"): ~¥49 CNY/month (China) / ~$19 USD/month (international) with access to advanced features, longer outputs, and priority

2. **API / Developer platform**
   - Token-based pricing, competitive with Western frontier models
   - K2.5 API: ~$0.60/M input tokens, ~$2.50/M output tokens (cache hits: $0.15/M input)
   - Positioned significantly below OpenAI and Anthropic pricing
   - Available through Moonshot's own platform and third-party providers (OpenRouter, Together AI, NVIDIA NIM)

3. **Enterprise and productivity tools**
   - Focus on complex task workflows: in-depth research, presentations, data analysis, website development
   - Agentic capabilities for multi-step tool invocation

### Revenue Trajectory

- In fewer than 20 days after the K2.5 launch (early 2026), Kimi's cumulative revenue **exceeded its entire 2025 annual revenue**
- Since November 2025, overseas API revenue quadrupled
- Monthly growth rates for both overseas and domestic paying users exceeded 170%
- Exact revenue figures have not been publicly disclosed

## What Makes Moonshot AI Interesting

1. **Long-context pioneer:** Moonshot was the first Chinese AI company to ship a 128K-context consumer product, and has consistently pushed context boundaries (now 256K tokens). Yang Zhilin's academic work on Transformer-XL — a foundational paper on extending context in transformers — directly informed this strategy. The company isn't just riding a trend; the founder literally wrote the paper.

2. **Fastest Chinese decacorn:** Reaching $10B+ valuation in ~2 years from founding is unprecedented in China's tech ecosystem. The velocity from $4.3B (December 2025) to a reported $18B (March 2026) — a 4x jump in three months — signals extraordinary market confidence (or froth, depending on perspective).

3. **Explosive revenue inflection:** The claim that 20 days of K2.5 revenue exceeded all of 2025 suggests a genuine product-market fit breakout, not just hype-driven valuation inflation.

4. **Open-source credibility:** Open-sourcing the 1T-parameter K2 model under a permissive license builds developer goodwill and ecosystem lock-in, an unusual move for a Chinese startup of this scale.

5. **Agent Swarm architecture:** The multi-agent orchestration system (up to 100 parallel agents) represents a bet on agentic AI that goes beyond chatbot interactions — aligning with the broader industry shift toward AI agents.

6. **Elite founding team density:** Three Tsinghua classmates, two with CMU graduate degrees, with combined experience across Google Brain, Meta AI, Megvii, and Tencent. Yang's publication record (Transformer-XL, XLNet, collaborations with Bengio and LeCun) is arguably the strongest of any Chinese AI startup founder.

7. **Strategic investor base:** Having both Alibaba and Tencent as investors simultaneously is rare and strategically significant — it provides distribution channels across China's two largest internet ecosystems.

## Risks & Open Questions

- **Burn rate:** Frontier model training and inference at scale is extraordinarily capital-intensive. Whether the recent revenue surge is sustainable or a launch spike remains to be seen.
- **Regulatory environment:** Chinese AI regulation is evolving rapidly; compliance requirements could constrain product development.
- **Valuation sustainability:** The $18B target valuation implies very aggressive growth expectations. The jump from $4.3B to $18B in three months warrants scrutiny.
- **Competition:** Faces intense domestic competition from DeepSeek, Baichuan, Zhipu AI, and incumbents (Baidu's Ernie, Alibaba's Qwen), plus global competition from OpenAI, Anthropic, Google, and Meta.
- **Overseas expansion:** While overseas API revenue is growing rapidly, building a durable international presence from China involves significant geopolitical and infrastructure challenges.

## Sources

- [Moonshot AI — Wikipedia](https://en.wikipedia.org/wiki/Moonshot_AI)
- [Kimi (chatbot) — Wikipedia](https://en.wikipedia.org/wiki/Kimi_(chatbot))
- [Yang Zhilin — Wikipedia](https://en.wikipedia.org/wiki/Yang_Zhilin)
- [Bloomberg: China AI Startup Moonshot Snags Funds at $18 Billion Valuation (March 2026)](https://www.bloomberg.com/news/articles/2026-03-14/china-ai-startup-moonshot-snags-funds-at-18-billion-valuation)
- [PYMNTS: Chinese AI Firm Moonshot Aims for $18 Billion Valuation](https://www.pymnts.com/artificial-intelligence-2/2026/chinese-ai-firm-moonshot-aims-for-18-billion-valuation/)
- [The China Academy: Kimi Becomes China's Fastest Decacorn (Feb 2026)](https://thechinaacademy.org/kimi-moonshot-ai-becomes-chinas-fastest-decacorn-as-20-day-revenue-surpasses-entire-2025-total-china-ai-daily-february-24-2026/)
- [TechCrunch: Moonshot AI Raises $1B (Feb 2024)](https://techcrunch.com/2024/02/21/moonshot-ai-funding-china/)
- [South China Morning Post: Moonshot AI $1B Round Led by Alibaba and HongShan](https://www.scmp.com/tech/big-tech/article/3252574/chinese-start-moonshot-ai-raises-us1-billion-funding-round-led-alibaba-and-vc-hongshan-amid-strong)
- [Caproasia: Moonshot AI Funding Timeline (March 2026)](https://www.caproasia.com/2026/03/15/china-ai-startup-moonshot-ai-to-raise-1-billion-at-18-billion-valuation-raised-500-million-in-series-c-funding-at-4-3-billion-valuation-in-2025-december-founded-in-2023-by-yang-zhilin-investors/)
- [KR-Asia: Moonshot AI Overseas Revenue Surge](https://kr-asia.com/moonshot-ai-sees-overseas-revenue-surge-as-kimi-k2-5-gains-traction-abroad)
- [IndexBox: Moonshot AI Funding at $18B Valuation](https://www.indexbox.io/blog/moonshot-ai-seeks-1b-funding-at-18b-valuation/)
- [Asian Intelligence: Leadership Team of Moonshot AI](https://asianintelligence.ai/reports/leadership-team-of-moonshot-ai)
- [Entrepreneurloop: Moonshot AI Series C Funding](https://entrepreneurloop.com/moonshot-ai-500m-series-c-funding-ai-infrastructure/)
- [Hugging Face: Kimi K2.5 Model Card](https://huggingface.co/moonshotai/Kimi-K2.5)
- [Codecademy: Kimi K2.5 Complete Guide](https://www.codecademy.com/article/kimi-k-2-5-complete-guide-to-moonshots-ai-model)
- [Moonshot AI Official Platform](https://platform.moonshot.ai/)
- [Yang Zhilin — MIT Innovators Under 35](https://www.innovatorsunder35.com/the-list/zhilin-yang/)
