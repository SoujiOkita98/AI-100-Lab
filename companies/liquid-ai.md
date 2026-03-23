---
name: Liquid AI
legal_name: Liquid AI Inc.
founded: 2023
headquarters: Cambridge, Massachusetts, USA
origin: MIT CSAIL spinout
sector: Artificial Intelligence / Foundation Models
subsector: Alternative AI Architectures (non-transformer)
stage: Series A
total_funding: $297M (approx.)
latest_valuation: $2B-$2.35B (Dec 2024)
unicorn_status: true
unicorn_year: 2024
employee_count_approx: ~88 (2025 est.)
revenue_approx: $13.2M (Nov 2025, per Getlatka — treat with caution)
status: Active, private
website: https://www.liquid.ai
last_updated: '2026-03-20'
confidence: high on funding/founders; moderate on revenue/headcount (third-party estimates)
funding_rounds:
- stage: Seed
  date: 2023-12
  amount_m: 37.5
  valuation_m: 303
  lead_investors:
  - OSS Capital
  - PagsGroup
  - Samsung Next
  source: https://siliconangle.com/2023/12/06/liquid-ai-raises-37-6m/
- stage: Series A
  date: 2024-12
  amount_m: 250
  valuation_m: 2300
  lead_investors:
  - AMD Ventures
  source: https://www.liquid.ai/blog/we-raised-250m
one_liner: Liquid AI is an MIT CSAIL spinout building foundation models based on **liquid neural networks** — an alternative
  architecture to the transformer models that underpin most modern AI systems
website_verified: true
linkedin: https://www.linkedin.com/company/liquid-ai-inc
crunchbase: https://www.crunchbase.com/organization/liquid-ai
crunchbase_verified: true
---

# Liquid AI

## Overview

Liquid AI is an MIT CSAIL spinout building foundation models based on **liquid neural networks** — an alternative architecture to the transformer models that underpin most modern AI systems. The company's core thesis is that biologically-inspired, dynamically-adaptive neural networks can deliver competitive performance at dramatically smaller model sizes and lower compute requirements, making them ideal for edge deployment, on-device inference, and latency-sensitive enterprise workloads.

The company emerged from stealth in December 2023 and reached unicorn status within a year.

## Founders and Leadership

All four co-founders come from MIT's Computer Science and Artificial Intelligence Laboratory (CSAIL):

| Name | Role | Background |
|------|------|------------|
| **Ramin Hasani** | Co-Founder & CEO | Postdoctoral Associate at MIT CSAIL under Daniela Rus. Research focus on modeling intelligence and sequential decision-making. PhD background in machine learning. Led the foundational research on liquid time-constant networks. |
| **Daniela Rus** | Co-Founder | Director of MIT CSAIL — one of the most prominent academic CS labs in the world. A leading robotics and AI researcher. Her involvement lends significant academic credibility. |
| **Mathias Lechner** | Co-Founder & CTO | PhD (2022) from the Institute of Science and Technology Austria (ISTA), supervised by Tom Henzinger. BS/MS in Computer Science from TU Wien. Research affiliate at MIT CSAIL. Co-inventor of liquid neural networks. |
| **Alexander Amini** | Co-Founder & CSO | BS, MS, and PhD from MIT in Computer Science. Creator and lead lecturer of MIT's "Introduction to Deep Learning" course (6.S191), which has amassed over 10 million views. Research deployed in autonomous vehicles and medical drug discovery. |

This founding team is unusually strong: a sitting CSAIL director, the inventor-CEO, and two deep technical co-founders with complementary strengths in theory (Lechner) and applications (Amini).

## Technology: Liquid Neural Networks

The core innovation draws inspiration from the nervous system of *C. elegans*, a roundworm with only 302 neurons that nonetheless exhibits complex behaviors. Key properties:

- **Dynamic parameters**: Unlike traditional neural networks with fixed weights after training, liquid neural networks use parameters that adjust continuously based on input data at inference time.
- **Compact models**: Liquid foundation models (LFMs) achieve competitive quality at much smaller parameter counts, enabling on-device deployment.
- **Efficiency**: Up to ~2x prefill and decode speedups vs. similarly-sized transformer baselines on CPUs, per Liquid AI's benchmarks.
- **Hardware flexibility**: Models run on CPUs, GPUs, and NPUs without architecture changes.

The underlying math is based on "liquid time-constant networks," published at AAAI 2021 and subsequent venues.

## Products and Model Releases

| Model | Release | Description |
|-------|---------|-------------|
| **LFM-1 series** | Sep 2024 (approx.) | First public Liquid Foundation Models — 1B, 3B, 40B parameter variants |
| **LFM-7B** | Jan 2025 | 7B parameter model; best-in-class for local deployment and latency-constrained tasks; multilingual |
| **Hyena Edge** | Apr 2025 | Purpose-built for smartphones and edge devices |
| **LFM2 series** | Mid 2025 | 350M, 1.2B, 8B-A1B (mixture-of-experts) variants. 200% faster decode/prefill vs. Qwen3 and Gemma 3 on CPU. Available on Hugging Face. |
| **LFM2.5** | Jan 2026 | Frontier-level reasoning at 1B scale. 239 tok/s decode on AMD CPU, 82 tok/s on mobile NPU. |

Models are available via Hugging Face (open weights for some variants) and through Liquid AI's own API.

## Funding History

| Round | Date | Amount | Lead / Key Investors | Valuation |
|-------|------|--------|----------------------|-----------|
| **Seed** | Dec 2023 | ~$46.6M | OSS Capital, PagsGroup; angels incl. Naval Ravikant. Other participants: Capgemini, Samsung NEXT, Breyer Capital, Safar Partners, ISAI, Bold Capital Partners, Automattic | Undisclosed |
| **Series A** | Dec 2024 | $250M | AMD Ventures (strategic lead); OSS Capital, Duke Capital Partners, PagsGroup | ~$2–2.35B |

**Total raised**: ~$297M across 2 rounds from 22 investors (14 institutional, 8 angel).

*No additional funding rounds have been publicly announced as of March 2026.*

## Business Model

Liquid AI operates a **multi-channel enterprise AI model**:

1. **API access**: Cloud-hosted inference endpoints for Liquid Foundation Models.
2. **Model licensing**: Enterprise licensing for on-premise and edge deployment (e.g., the Shopify deal).
3. **Consulting / co-development**: Strategic engagements with partners like Capgemini to build custom solutions.
4. **Open-weight models on Hugging Face**: Community adoption and ecosystem building (likely a funnel to paid products).

The company has stated it targets **profitability by 2026** through this combination of revenue streams. Revenue reportedly reached $13.2M by November 2025 (source: Getlatka; accuracy uncertain — treat as directional).

## Key Partnerships and Customers

- **AMD**: Strategic investor (led Series A). Joint work on on-device AI; demo of local private meeting summarization on AMD Ryzen hardware (2026).
- **Capgemini**: Seed investor and go-to-market partner. Multi-year collaboration to bring LNN-powered solutions to enterprise clients in manufacturing, healthcare, and finance.
- **Shopify**: Multi-year licensing deal (Nov 2025) to deploy LFMs in commerce workflows. First production deployment: sub-20ms text model for search enhancement.
- **G42** (Abu Dhabi): Partnership (Jun 2025) to deliver private, local AI solutions for enterprises.

## What Makes Liquid AI Interesting

1. **Genuine architectural differentiation**: In a market dominated by transformer variants, Liquid AI is one of very few well-funded startups pursuing a fundamentally different neural network architecture. If liquid neural networks prove broadly competitive, the efficiency gains could be structurally disruptive.

2. **Edge-native thesis**: While most AI labs race to build ever-larger cloud models, Liquid AI's sweet spot is small, fast, on-device models. This positions them for the wave of edge AI in phones, cars, wearables, IoT, and defense — markets where latency, privacy, and bandwidth constraints make cloud inference impractical.

3. **World-class founding team**: Having a sitting MIT CSAIL director (Daniela Rus) as co-founder is rare. The team invented the underlying science and has deep, published expertise.

4. **AMD as strategic lead**: AMD's $250M-led round signals serious hardware-ecosystem alignment. As AMD competes with NVIDIA for AI workloads, supporting an efficient alternative architecture that runs well on AMD silicon is strategically valuable for both parties.

5. **Capital efficiency**: Reaching ~$13M revenue with ~88 people and only $297M raised (modest by AI lab standards) suggests a leaner operation than peers like Anthropic, OpenAI, or Mistral.

6. **Biological inspiration with real math**: The C. elegans / liquid time-constant framing is not just marketing — it is backed by peer-reviewed publications (AAAI, NeurIPS) and provable properties around adaptability and robustness.

## Risks and Open Questions

- **Scaling ceiling**: It remains unclear whether liquid neural networks can match transformer-scale performance (100B+ parameters) on the hardest reasoning and generation benchmarks. Most published results are at 1B–8B scale.
- **Competitive moat**: If LNNs prove superior, larger labs (Google, Meta, OpenAI) could adopt or replicate the architecture with far more compute budget.
- **Revenue durability**: The $13.2M revenue figure is from a single third-party source and may not reflect recurring ARR. Enterprise deals like Shopify and G42 are promising but early.
- **Transformer momentum**: The transformer ecosystem (tooling, hardware optimization, community knowledge) has enormous momentum. Switching costs for developers are real.

## Competitors

- **Transformer-based foundation model labs**: Mistral AI, Cohere, AI21 Labs (direct competitors for enterprise LLM deployment)
- **Edge AI / on-device**: Qualcomm AI, MediaTek, Apple MLX ecosystem
- **Alternative architectures**: State-space model companies (e.g., Cartesia AI with Mamba-based models), RWKV community

## Sources

- [Liquid AI official website](https://www.liquid.ai)
- [Liquid AI: $250M Series A announcement](https://www.liquid.ai/blog/we-raised-250m-to-scale-capable-and-efficient-general-purpose-ai)
- [TechCrunch: Liquid AI raises $250M (Dec 2024)](https://techcrunch.com/2024/12/13/liquid-ai-just-raised-250m-to-develop-a-more-efficient-type-of-ai-model/)
- [TechCrunch: Liquid AI MIT spinoff (Dec 2023)](https://techcrunch.com/2023/12/06/liquid-ai-a-new-mit-spinoff-wants-to-build-an-entirely-new-type-of-ai/)
- [Liquid AI LFM2 announcement](https://www.liquid.ai/blog/liquid-foundation-models-v2-our-second-series-of-generative-ai-models)
- [Liquid AI Capgemini collaboration](https://www.liquid.ai/blog/liquid-ai-announces-collaboration-with-capgemini-to-build-next-generation-ai-solutions-for-enterprises)
- [AMD + Liquid AI on-device demo (2026)](https://www.amd.com/en/blogs/2026/liquid-ai-amd-ryzen-on-device-meeting-summaries.html)
- [MIT News: Liquid machine-learning systems (2021)](https://news.mit.edu/2021/machine-learning-adapts-0128)
- [SiliconANGLE: LFM2 raises $250M](https://siliconangle.com/2024/12/13/liquid-ai-raises-250m-led-amd-build-new-type-generative-ai-model/)
- [SiliconANGLE: Small foundation models for on-device (Sep 2025)](https://siliconangle.com/2025/09/25/liquid-ai-debuts-extremely-small-high-performance-foundation-models-device-processing/)
- [AI Business Weekly: $2.35B valuation](https://aibusinessweekly.net/p/liquid-ai-250-million-series-a-foundation-models)
- [TechFundingNews: AMD-led funding](https://techfundingnews.com/liquid-ai-closes-250m-hits-2b-valuation-with-amd-led-funding/)
- [Getlatka: Liquid AI revenue/headcount](https://getlatka.com/companies/liquid.ai)
- [Ramin Hasani profile — Liquid AI](https://www.liquid.ai/team/ramin-hasani)
- [Alexander Amini profile — Liquid AI](https://www.liquid.ai/team/alexander-amini)
- [Mathias Lechner personal page](https://mlech26l.github.io/)
- [Tracxn: Liquid AI company profile](https://tracxn.com/d/companies/liquid-ai/__WcgGMTavFS-PIXLKpe46XDv3j7Q4kwlkc7Hd-zvaYko)
- [Hugging Face: LFM2-1.2B](https://huggingface.co/LiquidAI/LFM2-1.2B)
- [LFM2 Technical Report (arXiv)](https://arxiv.org/pdf/2511.23404)
