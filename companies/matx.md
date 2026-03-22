---
company: MatX
legal_name: MatX Inc.
founded: '2022'
headquarters: San Francisco Bay Area, California, USA
sector: AI Hardware / Semiconductors (LLM Training)
stage: Growth (Series B)
latest_valuation: Undisclosed (~$2-3B estimated based on round size)
total_funding: ~$600 million
employees: ~50 (estimate; small team)
website: https://matx.com
last_updated: 2026-03-20
one_liner: MatX is designing a custom AI chip -- the MatX One -- built from the ground up specifically for training large
  language models
website_verified: true
---

# MatX

## Overview

MatX is designing a custom AI chip -- the MatX One -- built from the ground up specifically for training large language models. Unlike most AI chip startups that target inference (running trained models), MatX is taking on Nvidia's most profitable and strategically important market: the training of frontier LLMs. The company claims its chip will be 10x better at LLM training than Nvidia's GPUs.

MatX was founded by two former Google engineers who were central to the design of Google's TPU (Tensor Processing Unit) -- one led the hardware design, the other led the software. Their core insight: existing chips (including TPUs and GPUs) are general-purpose designs adapted for LLMs, but a chip designed exclusively for the specific computational patterns of transformer training can be dramatically more efficient.

## Founders and Team

| Name | Role | Background |
|---|---|---|
| **Reiner Pope** | Co-Founder & CEO | Former Google engineer who led AI software development for Google's TPUs. As Efficiency Lead for Google PaLM, designed and implemented the world's fastest LLM inference software. Helped conceive Google's TPU v5e and optimize it for LLMs. Left Google in 2022 to start MatX. |
| **Mike Gunter** | Co-Founder & CTO | Former lead hardware designer for Google's TPU. Designed the physical chip architecture that Pope's software ran on. Deep expertise in ASIC design for AI workloads. |

The Pope-Gunter partnership mirrors the Groq founding story (Jonathan Ross also came from Google's TPU team), but with a critical difference: MatX is targeting training, not inference. The two founders represent a rare combination -- the software architect and the hardware architect of the same chip program, now collaborating on a clean-sheet design.

## Funding History

| Round | Date | Amount | Lead Investor(s) | Notes |
|---|---|---|---|---|
| Series A | ~2024 | ~$100M | Spark Capital | First major round; company emerged from stealth |
| Series B | Feb 2026 | $500M | Jane Street, Situational Awareness (Leopold Aschenbrenner) | Largest AI chip round of early 2026. Other backers: Marvell Technology, NFDG, Spark Capital, Patrick and John Collison (Stripe co-founders) |

**Total raised:** ~$600 million.

**Notable investors:**
- **Jane Street** -- The quantitative trading firm, which has become an increasingly active tech investor
- **Situational Awareness** -- Investment fund run by Leopold Aschenbrenner, former OpenAI researcher and author of the influential "Situational Awareness" essay on AI scaling trajectories
- **Marvell Technology** -- Strategic semiconductor investor ($10B+ revenue company)
- **Patrick and John Collison** -- Stripe co-founders; prolific angel investors in frontier technology
- **Spark Capital** -- Series A lead; early believer

## Technology: MatX One

The MatX One chip is based on a **splittable systolic array** architecture -- a design that breaks the processing elements into smaller, reconfigurable systolic arrays to optimize efficiency across different phases of LLM training (forward pass, backward pass, optimizer steps).

Key specifications and goals:
- **10x better** at LLM training than Nvidia GPUs (company claim)
- **Fabrication:** TSMC (process node undisclosed; likely 4nm or 3nm)
- **Target ship date:** 2027
- **Focus:** Transformer model training exclusively

**Status (March 2026):** Pre-silicon. The chip has not taped out, and no third-party benchmarks or customer deployments exist. The 2027 ship date means MatX is at least 12-18 months from production.

## Business Model

MatX plans to sell training systems to hyperscalers, AI labs, and large enterprises that are spending billions on LLM training compute. The addressable market is the ~$100B+ annual spend on AI training infrastructure, currently dominated almost entirely by Nvidia.

## What Makes MatX Interesting

1. **The TPU lineage is the strongest possible pedigree for this bet.** Pope and Gunter did not just use TPUs -- they designed them. Google's TPU is the only non-Nvidia chip that has successfully trained frontier LLMs at scale (PaLM, Gemini). If anyone outside Nvidia knows how to build a chip that can train massive models, it is this team.

2. **Training is the harder, higher-value market.** Most AI chip startups target inference because it is technically more tractable. MatX is going after training, where the stakes are higher (individual clusters cost hundreds of millions), the technical bar is steeper (reliability, interconnect, scaling), and the customer concentration is more favorable (a few massive buyers rather than thousands of small ones).

3. **Leopold Aschenbrenner's involvement is a signal.** Aschenbrenner's "Situational Awareness" thesis argues that AI capabilities will continue scaling rapidly, requiring ever more training compute. His fund co-leading the round means MatX's bet is directly aligned with the "scaling maximalist" worldview that drives much of frontier AI investment.

4. **Jane Street as lead investor is unusual.** Quantitative trading firms rarely lead AI hardware rounds. Jane Street's involvement may reflect both a financial bet and a potential customer relationship (trading firms are among the most compute-intensive enterprises).

5. **The Stripe founders' investment pattern.** The Collisons have a track record of investing in infrastructure companies that become industry standards. Their participation in MatX echoes their early bets on companies like Anthropic.

## Key Risks

- **Pre-silicon, 2027 ship date.** MatX is at least 18 months from shipping. In the AI chip market, a lot changes in 18 months. Nvidia's Blackwell and Rubin architectures will be fully deployed by then.
- **Training market has extreme switching costs.** Hyperscalers have invested billions in Nvidia GPU clusters and CUDA software stacks. Convincing them to adopt a new, unproven training chip requires not just better hardware but a complete software ecosystem.
- **No disclosed customers or partnerships.** As of March 2026, no hyperscaler or AI lab has publicly committed to MatX.
- **Capital intensity.** Building a training-class chip at TSMC requires enormous upfront investment. $600M is significant but may not be enough if tapeout iterations are needed.
- **Google's TPU is the direct competitor from the founders' own alma mater.** Google continues to invest heavily in TPU development (TPU v5, Trillium). MatX must demonstrate why an independent chip can beat the system its founders helped create.

## Comparable Companies

- Google TPU (internal; the founders' prior work)
- Nvidia (dominant training GPU)
- Cerebras (wafer-scale; training + inference)
- Etched (transformer ASIC; inference-focused counterpart)

---

*Profile compiled 2026-03-20. Sources: [TechCrunch](https://techcrunch.com/2026/02/24/nvidia-challenger-ai-chip-startup-matx-raised-500m/), [DCD](https://www.datacenterdynamics.com/en/news/ai-chip-startup-matx-raises-500m-for-development-of-llm-training-chip/), [Bloomberg](https://www.bloomberg.com/news/articles/2026-02-24/ai-chip-startup-matx-raises-500-million-to-compete-with-nvidia), [Outset Capital](https://www.outsetcapital.com/post/investing-in-matx-the-future-compute-platform-for-agi).*
