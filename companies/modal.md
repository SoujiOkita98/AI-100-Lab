---
company: Modal (Modal Labs, Inc.)
sector: AI Infrastructure / Cloud Computing
stage: Growth (Series B closed; Series C reportedly in talks)
founded: 2021
headquarters: New York, NY
website: https://modal.com
founders:
- name: Erik Bernhardsson
  role: CEO
  background: 'Ex-Spotify (~employee #30), built music recommendations (Discover Weekly, Related Artists, Radio); created
    open-source tools Luigi and Annoy; M.Sc. Physics, KTH Stockholm; ran tech team at Better.com (1 to ~300 engineers)'
  origin: Swedish
- name: Akshat Bubna
  role: CTO
  background: Early employee at Scale AI; MIT B.S. Math & CS (2014-2017); IOI Gold Medalist 2014 (first Indian student to
    achieve this); competitive crossword solver
  origin: Indian-American
employees: ~118 (as of Feb 2026)
total_funding: ~$111M (through Series B)
latest_valuation: $1.1B (Series B, Sep 2025); in talks for ~$2.5B (Series C, Feb 2026)
key_investors:
- Lux Capital (led Series B)
- Redpoint Ventures (led Series A)
- Amplify Partners (led Seed)
- Definition Capital
- General Catalyst (reportedly leading Series C talks)
competitors:
- Baseten
- Replicate
- RunPod
- Fal
- AWS SageMaker / GCP Vertex AI (hyperscaler alternatives)
last_updated: 2026-03-20
confidence: high on funding/founders; moderate on revenue/valuation talks
funding_rounds:
- stage: Seed
  date: '2022'
  amount_m: 7
  lead_investors:
  - Amplify Partners
  source: https://modal.com/blog/general-availability-and-series-a-press-release
- stage: Series A
  date: 2023-10
  amount_m: 16
  lead_investors:
  - Redpoint Ventures
  source: https://techcrunch.com/2023/10/10/modal-labs-lands-16m/
- stage: Series B
  date: 2025-07
  amount_m: 87
  valuation_m: 1100
  lead_investors:
  - Lux Capital
  source: https://modal.com/blog/announcing-our-series-b
one_liner: Modal is a serverless compute platform purpose-built for AI and ML workloads
website_verified: true
linkedin: https://www.linkedin.com/company/modal-labs
crunchbase: https://www.crunchbase.com/organization/modal
crunchbase_verified: true
twitter: '@modal_labs'
---

# Modal — Serverless Cloud for AI/ML

## Overview

Modal is a serverless compute platform purpose-built for AI and ML workloads. Developers write plain Python, decorate functions with Modal's SDK, and run them in the cloud with automatic containerization, GPU attachment, and autoscaling — no Dockerfiles, Kubernetes, or infrastructure management required. The platform supports the full ML lifecycle: training, fine-tuning, batch processing, and inference.

## Founding Story

Erik Bernhardsson started Modal in early 2021 after spending nearly a decade frustrated by the gap between writing ML code and deploying it at scale. At Spotify (where he was roughly the 30th employee), he built the first generation of recommendation systems and created widely-used open-source tools — **Luigi** (workflow orchestration, 17k+ GitHub stars) and **Annoy** (approximate nearest neighbor search). After leading engineering at Better.com from 2015-2021, he set out to build infrastructure that would let any developer run compute-heavy Python in the cloud as easily as running it locally.

Akshat Bubna joined as CTO and co-founder in August 2021. Bubna was an early engineer at Scale AI, where he built core engineering and operations systems. A competitive programmer (IOI Gold 2014, the first Indian student to win gold), he brought deep systems engineering expertise from MIT and Scale AI.

The two recruited a small initial team of ~4, drawing from backgrounds at companies including Cockroach Labs, LinkedIn, Asana, Uber, Spotify, Canva, and Zendesk.

## Funding History

| Round | Date | Amount | Lead | Valuation | Notes |
|-------|------|--------|------|-----------|-------|
| Seed | Jan 2022 | $7M | Amplify Partners | Undisclosed | — |
| Series A | Oct 2023 | $16M | Redpoint Ventures | Undisclosed | Amplify, Lux Capital, Definition Capital participated |
| Series B | Sep 2025 | $87M | Lux Capital | $1.1B (post-money) | Achieved unicorn status; total raised: ~$111M |
| Series C (reported) | Feb 2026 | TBD | General Catalyst (reportedly) | ~$2.5B (target) | Early-stage talks; not confirmed. CEO Erik Bernhardsson characterized VC meetings as "general conversations" |

**Sources:**
- [Modal Series B announcement](https://modal.com/blog/announcing-our-series-b)
- [TechCrunch: Series C talks at $2.5B](https://techcrunch.com/2026/02/11/ai-inference-startup-modal-labs-in-talks-to-raise-at-2-5b-valuation-sources-say/)
- [TechCrunch: Series A ($16M)](https://techcrunch.com/2023/10/10/modal-labs-lands-16m-to-abstract-away-big-data-workload-infrastructure/)
- [SiliconANGLE: Series B ($80M+)](https://siliconangle.com/2025/09/29/modal-labs-raises-80m-simplify-cloud-ai-infrastructure-programmable-building-blocks/)

## Revenue

Modal's annualized revenue run rate (ARR) is approximately **$50M** as of early 2026, per TechCrunch reporting on the Series C talks. Exact revenue figures are not publicly disclosed. This implies significant growth given the company reached unicorn status only five months prior.

## Business Model

- **Usage-based pricing**: Per-second billing for CPU, GPU, and memory. No upfront commitments.
- **Tiered plans**: Free tier (limited credits) through enterprise contracts.
- **No infrastructure lock-in**: Pure Python SDK means workloads are relatively portable.
- Modal handles container orchestration, GPU scheduling, storage, and networking transparently. Customers pay only for compute time actually consumed.

## Technical Differentiation

What makes Modal technically distinctive:

1. **Sub-second cold starts**: A custom Rust-based container runtime, image builder, and distributed file system enable startup times far below typical cloud containers. This is critical for bursty inference workloads.
2. **Pure Python interface**: No YAML, no Dockerfiles, no REST API boilerplate. A `@app.function(gpu="A100")` decorator is enough to ship code to a GPU in the cloud.
3. **Serverless GPUs**: Auto-scaling from zero to thousands of GPUs, with per-second billing. The platform handles scheduling across GPU types (T4, A10G, A100, H100).
4. **Full lifecycle support**: Unlike inference-only platforms (Baseten, Replicate), Modal supports training, fine-tuning, batch jobs, web endpoints, and cron jobs in a unified environment.

## Customers

Modal powers infrastructure for **10,000+ teams** (as of mid-2025). Notable customers and use cases include:

- **Ramp** — Financial operations / ML pipelines
- **Substack** — Migrated nearly all ML training and deployment from AWS SageMaker to Modal (2024)
- Use cases span biotech, generative AI media, fintech, and developer tools

Over 100 enterprise customers were reported as of April 2024.

## Competitive Landscape

| Competitor | Positioning | Modal's Edge |
|-----------|-------------|--------------|
| **Baseten** | Serverless inference via Truss framework | Modal is more general-purpose (not inference-only); Python-native vs. YAML config |
| **Replicate** | Model marketplace + serverless inference | Modal targets builders, not consumers of pre-trained models |
| **RunPod** | Flexible GPU rental (serverless + persistent) | Modal offers tighter DX and true serverless abstraction |
| **Fal** | Media generation model endpoints | Modal is workload-agnostic, not media-focused |
| **AWS/GCP/Azure** | Full cloud platforms | Modal is dramatically simpler for AI workloads; avoids cloud complexity |

## What Makes Modal Interesting (Investment Thesis)

1. **Developer experience as moat**: Modal has built genuine developer love — rare in infrastructure. The Python-native SDK eliminates entire categories of DevOps work, creating strong bottom-up adoption.

2. **Riding the inference wave**: As AI models proliferate, inference compute demand is exploding. Modal's serverless GPU model is well-positioned for the shift from training-dominated to inference-dominated spend.

3. **Efficient capital use**: Reaching $1.1B valuation and ~$50M ARR on only $111M raised is capital-efficient relative to GPU-heavy competitors like CoreWeave or Lambda Labs that require massive capex.

4. **Platform breadth**: Supporting training, fine-tuning, batch, and inference in one platform creates switching costs and expands addressable market beyond inference-only startups.

5. **Founder-market fit**: Erik Bernhardsson built production ML systems at Spotify scale and understands the pain of ML infrastructure firsthand. Akshat Bubna brings Scale AI's operational rigor and deep systems engineering.

6. **Valuation trajectory**: 2.3x valuation jump in ~5 months ($1.1B to $2.5B target) signals strong demand signal, though this remains unconfirmed.

## Risks and Open Questions

- **GPU supply dependence**: Modal does not own GPUs — it relies on upstream cloud providers (including Oracle Cloud Infrastructure, per a TechCrunch/Oracle partnership feature). Margin pressure from GPU costs is a concern.
- **Hyperscaler competition**: AWS, GCP, and Azure could replicate the developer experience layer. Serverless GPU offerings from major clouds are improving.
- **Revenue durability**: Usage-based models can be volatile. Customer concentration data is not publicly available.
- **Series C terms unconfirmed**: The $2.5B valuation and General Catalyst lead are based on TechCrunch reporting of early discussions (Feb 2026). Terms may change.

## Key Sources

- [Modal official website](https://modal.com/)
- [Modal Series B blog post](https://modal.com/blog/announcing-our-series-b)
- [TechCrunch: $2.5B valuation talks (Feb 2026)](https://techcrunch.com/2026/02/11/ai-inference-startup-modal-labs-in-talks-to-raise-at-2-5b-valuation-sources-say/)
- [TechCrunch: Series A (Oct 2023)](https://techcrunch.com/2023/10/10/modal-labs-lands-16m-to-abstract-away-big-data-workload-infrastructure/)
- [Contrary Research: Modal Business Breakdown](https://research.contrary.com/company/modal)
- [Amplify Partners: Modal investment memo](https://www.amplifypartners.com/blog-posts/modal)
- [Erik Bernhardsson personal site](https://erikbern.com/about.html)
- [Orb interview with Erik Bernhardsson](https://www.withorb.com/blog/in-conversation-with-erik-bernhardsson-ceo-and-founder-of-modal)
- [Software Engineering Daily: Modal and Scaling AI Inference](https://softwareengineeringdaily.com/2025/07/31/modal-and-scaling-ai-inference-with-erik-bernhardsson/)
- [SiliconANGLE: Series B coverage](https://siliconangle.com/2025/09/29/modal-labs-raises-80m-simplify-cloud-ai-infrastructure-programmable-building-blocks/)
- [BeBeez: Unicorn valuation](https://bebeez.eu/2025/09/30/swedish-modal-raises-87m-series-b-hits-unicorn-valuation-with-ai-native-cloud-platform/)
