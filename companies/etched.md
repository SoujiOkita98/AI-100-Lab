---
company: Etched
legal_name: Etched Inc.
founded: 2022
headquarters: Cupertino, California, USA
sector: AI Hardware / Semiconductors (Inference ASICs)
stage: Growth (Series B)
latest_valuation: $5 billion (Series B, January 2026)
total_funding: ~$625 million
employees: ~50-100 (estimate)
website: https://etched.com
last_updated: 2026-03-20
one_liner: Etched is building Sohu, the first ASIC (application-specific integrated circuit) purpose-built exclusively for
  transformer model inference
website_verified: true
---

# Etched

## Overview

Etched is building Sohu, the first ASIC (application-specific integrated circuit) purpose-built exclusively for transformer model inference. Rather than designing a general-purpose AI accelerator that can handle many architectures, Etched has made the radical bet that transformers will remain the dominant AI architecture for the foreseeable future -- and that hard-wiring transformer-specific operations directly into silicon can deliver an order-of-magnitude improvement in inference speed and energy efficiency over Nvidia GPUs. Sohu is fabricated on TSMC's 4nm process with HBM (High Bandwidth Memory).

The company claims an 8-chip Sohu server can generate over 500,000 tokens per second on Llama-70B, compared to roughly 23,000 tokens/second from an equivalent 8xH100 Nvidia configuration -- a ~20x improvement.

## Founders and Team

Etched was founded by three Harvard dropouts in 2022, making it one of the youngest and most audacious entrants in the AI chip race.

| Name | Role | Background |
|---|---|---|
| **Gavin Uberti** | Co-Founder & CEO | Was completing concurrent Master's and Bachelor's degrees in CS and Math at Harvard when he dropped out. Previously developed the ARM Cortex-M backend for Apache TVM (open-source deep learning compiler). Software engineer at OctoML. Has guest lectured at Columbia and spoken at multiple AI conferences. |
| **Chris Zhu** | Co-Founder & CTO | Degrees in Mathematics and Computer Science from Harvard. Previously a math and HPC researcher at Harvard and a software engineering intern at AWS. |
| **Robert Wachen** | Co-Founder | Harvard dropout. Limited additional public background. |

The company started as a dorm room project in early 2023. Uberti and Zhu closed a $5.36M seed round led by Primary Venture Partners in March 2023, dropped out, and relocated to the Bay Area.

## Funding History

| Round | Date | Amount | Valuation | Lead Investor(s) | Notes |
|---|---|---|---|---|---|
| Seed | Mar 2023 | $5.36M | ~$30M (est.) | Primary Venture Partners | Dorm-room stage; founded months earlier |
| Series A | Jun 2024 | $120M | ~$750M-$1.5B | Peter Thiel, Primary VC | Investors include GitHub CEO Thomas Dohmke. Funds earmarked for TSMC fabrication |
| Series B | Jan 2026 | $500M | $5B | Stripes | Total raised approaches ~$625M |

**Notable investors:** Peter Thiel, Stripes, Primary Venture Partners, GitHub CEO Thomas Dohmke, Rambus (technology partnership).

## Technology: The Sohu Chip

Sohu hard-wires the matrix multiplication patterns specific to transformer inference directly into the silicon, eliminating the overhead of general-purpose programmability. Key design choices:

- **TSMC 4nm process** with High Bandwidth Memory (HBM)
- **Transformer-only:** Cannot run CNNs, RNNs, or other non-transformer architectures. This is the core tradeoff -- extreme specialization for extreme performance.
- **Claimed performance:** 500,000+ tokens/sec on Llama-70B (8-chip server) vs. 23,000 tokens/sec on 8xH100
- **Power efficiency:** Significantly lower energy per token than GPU-based alternatives

**Shipping status (as of March 2026):** Key details including tapeout status, production timelines, sampling dates, customer deployments, and third-party benchmarks remain undisclosed. No independent verification of performance claims has been published.

## Business Model

Etched plans to sell Sohu-based inference servers to hyperscalers, cloud providers, and enterprises running transformer-based AI applications. The company is positioning for a world where inference (running trained models) becomes a far larger compute market than training.

## What Makes Etched Interesting

1. **The most extreme architectural bet in AI chips.** Every other AI chip startup hedges by supporting multiple model architectures. Etched is betting the company that transformers are "the last architecture" -- and that this conviction justifies burning general-purpose flexibility for 10-20x performance gains. If transformers remain dominant for the next decade, this is brilliant. If a post-transformer architecture emerges, the chip is a paperweight.

2. **Harvard dropouts vs. the semiconductor establishment.** The founding team has no prior chip design experience at major semiconductor companies. They are compiler and software people who decided to build an ASIC. This is either a feature (fresh thinking, no legacy assumptions) or a massive red flag (chip design is notoriously unforgiving). The $625M in funding suggests investors see it as the former.

3. **$5B valuation before shipping a single chip.** Etched has achieved a valuation comparable to companies with production silicon and real customers (d-Matrix at $2B, Positron at $1B). The market is pricing in the performance claims at face value. Third-party benchmarks will be the moment of truth.

4. **Leopold Aschenbrenner connection.** The Series B was co-led by Situational Awareness, the investment fund formed by former OpenAI researcher Leopold Aschenbrenner, whose influential essay on AI scaling made him a prominent voice in the "scaling maximalist" camp. His involvement signals a bet on massive inference demand.

5. **Speed of fundraising.** Going from dorm room to $5B valuation in under three years, without shipping product, is extraordinary even by AI boom standards.

## Key Risks

- **No shipped product or third-party benchmarks.** All performance claims are internal. The chip industry is littered with startups whose benchmarks did not survive contact with production workloads.
- **Architecture concentration risk.** If attention-based transformers are superseded (e.g., by state-space models like Mamba, or hybrid architectures), Sohu's value proposition collapses.
- **Execution risk.** First-time chip designers building a complex ASIC at TSMC 4nm. Tapeout and yield issues can be extremely expensive and time-consuming.
- **No disclosed customers.** As of March 2026, no customer deployments or partnerships have been announced.

## Comparable Companies

- Groq (acquired by Nvidia; inference-specific LPU)
- Cerebras (wafer-scale engine; training + inference)
- Positron AI (inference-focused; FPGA-based first generation)
- MatX (transformer-focused; training-oriented)

---

*Profile compiled 2026-03-20. Sources: [TechCrunch](https://techcrunch.com/2024/06/25/etched-is-building-an-ai-chip-that-only-runs-transformer-models/), [DCD](https://www.datacenterdynamics.com/en/news/etchedai-raises-500m-for-a-5bn-valuation-report/), [Wikipedia](https://en.wikipedia.org/wiki/Etched_(company)), [Rambus Blog](https://www.rambus.com/blogs/from-dorm-room-beginnings-to-a-pioneer-in-the-ai-chip-revolution-how-etched-is-collaborating-with-rambus-to-achieve-their-vision/), [CNBC](https://www.cnbc.com/2024/06/25/etched-raises-120-million-to-build-chip-to-take-on-nvidia-in-ai.html).*
