---
name: FlexAI
legal_name: FlexAI SAS
website: https://www.flex.ai
founded: 2023
headquarters: Paris, France
other_offices:
- San Francisco, CA, USA
- Bangalore, India
sector: AI Infrastructure / GPU Cloud Compute
stage: Seed
total_funding_usd: ~30,500,000
employee_count_approx: 45
founders:
- name: Brijesh Tripathi
  role: Co-founder & CEO
  origin: Indian
- name: Dali Kilani
  role: Co-founder & CTO
  origin: Tunisian-French
last_updated: 2026-03-20
confidence: high
website_verified: true
---

# FlexAI

## One-Liner

FlexAI is building a hardware-agnostic AI compute platform that abstracts away GPU vendor lock-in, letting developers run training, fine-tuning, and inference workloads across NVIDIA, AMD, Intel, and Tenstorrent chips without code changes.

## Founding Story

Brijesh Tripathi and Dali Kilani met over cappuccinos in Paris and bonded over frustrations with the AI compute landscape -- the supply bottleneck, the global skills shortage, and the painful complexity of deploying models across heterogeneous hardware. They founded FlexAI in 2023 and operated in stealth until April 2024.

## Founders & Key People

### Brijesh Tripathi -- Co-founder & CEO

Tripathi is a veteran chip and systems architect with deep experience across the major semiconductor and tech giants:

- **NVIDIA** -- Senior design engineer (early career)
- **Apple** -- Senior engineering roles
- **Tesla** -- Senior engineering, reporting directly to Elon Musk
- **Zoox** -- Engineering leadership
- **Intel** -- General Manager & Chief Architect for AI and Supercompute Platforms; previously VP & CTO of the Client Computing Group

His career arc -- from silicon design at NVIDIA to leading Intel's AI platform strategy -- gives him an unusually complete view of the full compute stack.

### Dali Kilani -- Co-founder & CTO

Kilani's background spans both infrastructure and product engineering:

- **NVIDIA** -- Technical roles
- **Zynga** -- Engineering
- **Boston Consulting Group** -- Consulting
- **Lifen** (French healthtech startup) -- CTO, building digital infrastructure for healthcare

Kilani brings the software and platform-building lens that complements Tripathi's hardware expertise.

### Broader Team

FlexAI reports team members across 25+ countries with alumni from Google, Microsoft, Amazon, and leading startups. The company currently has approximately 45 employees and is actively hiring across all three offices.

## Funding

| Round | Date | Amount | Lead Investors | Notable Participants |
|-------|------|--------|----------------|---------------------|
| Seed | April 2024 | ~$30M (EUR 28.5M) | Alpha Intelligence Capital (AIC), Elaia Partners, Heartcore Capital | Bpifrance, Frst Capital, Motier Ventures, Partech, Karim Beguir (InstaDeep CEO) |

**Total raised:** ~$30.5M across one disclosed round.

**Note:** As of March 2026, no Series A has been publicly announced. Given the company's traction (50,000+ GPUs deployed, multiple strategic partnerships), a follow-on round may have occurred or be in progress, but this is unconfirmed.

## Business Model

FlexAI operates a **Workload-as-a-Service (WaaS)** model:

1. **Aggregator of demand** -- FlexAI rents GPU capacity from cloud providers and data center partners (including NeoCloud providers like Sesterce), then allocates resources to customers based on workload requirements.
2. **Hardware abstraction** -- The platform automatically maps workloads to the most cost-effective hardware (NVIDIA CUDA, AMD ROCm, Intel Gaudi, Tenstorrent Wormhole) without requiring code changes from the developer.
3. **Pricing advantage** -- By leveraging strong relationships with chipmakers (Intel, AMD, Tenstorrent) and achieving 90%+ GPU utilization through multi-tenancy and intelligent packing, FlexAI claims 67% average cost savings versus direct cloud GPU rental.
4. **Revenue model** -- Customers pay per workload rather than reserving GPUs by the hour. FlexAI captures the spread between its bulk procurement costs and customer pricing.

### Product Offerings

- **Two-click training deployment** -- Simplified cluster provisioning for model training
- **Serverless inference** -- Auto-scaling with architecture recommendations
- **Fine-tuning workflows** -- Managed fine-tuning across hardware backends
- **FlexAI Startup Program** -- Dedicated program for early-stage AI companies

## Strategic Partnerships

- **Tenstorrent** (June 2025) -- Integrated Tenstorrent's Wormhole accelerators into FlexAI's WaaS platform, with plans to open-source key software integrations. This is significant because it adds a credible non-NVIDIA option to the platform.
- **Sesterce** (2025) -- Sovereign AI compute solution with GPU infrastructure hosted entirely in France (H100/H200 clusters). Full GDPR, NIS2, and CNIL compliance. This positions FlexAI as a viable option for European enterprises and government-adjacent AI projects with data residency requirements.

## What Makes FlexAI Interesting

1. **Hardware-agnostic bet at the right time.** As AI chip competition intensifies (AMD, Intel, Tenstorrent, custom silicon from hyperscalers), the value of a true abstraction layer increases. FlexAI is betting that NVIDIA's dominance will erode and that customers will want optionality -- a thesis that gets stronger every quarter.

2. **Founder-market fit is unusually strong.** Having a CEO who was Chief Architect for AI at Intel and a design engineer at NVIDIA, paired with a CTO who has built production infrastructure at scale, means this team understands both the hardware and software sides of the problem at a level few competitors can match.

3. **European strategic positioning.** Headquartered in Paris with sovereign compute partnerships, FlexAI is well-positioned to capture European AI sovereignty demand -- a growing policy priority with real budget behind it (e.g., Bpifrance as an investor). This is a differentiated go-to-market that US-based competitors largely ignore.

4. **Capital efficiency.** Deploying 50,000+ GPUs and signing major partnerships on ~$30M in seed funding suggests either strong revenue traction or creative partnership structures (or both). For context, many GPU cloud competitors have raised 10x more capital.

5. **Multi-chip future is the right long-term thesis.** The Tenstorrent partnership signals FlexAI is serious about non-NVIDIA hardware. If open-source chip architectures gain traction (RISC-V via Tenstorrent, for example), FlexAI could be the platform that makes them commercially accessible.

## Key Metrics (as reported by FlexAI)

- 50,000+ GPUs deployed
- 67% average cost savings (vs. direct cloud)
- 90%+ GPU utilization
- Supports NVIDIA, AMD, Intel Gaudi, and Tenstorrent hardware

## Risks & Open Questions

- **No disclosed Series A** as of March 2026, nearly two years post-seed. This could mean the company is profitable/self-sustaining, or it could indicate fundraising challenges. [Uncertain]
- **Aggregator model margins** -- Renting GPUs and reselling compute is margin-sensitive. If hyperscalers or chip vendors go direct, FlexAI's pricing advantage could compress.
- **NVIDIA moat** -- CUDA's ecosystem lock-in remains formidable. If most customers stay on NVIDIA regardless, the hardware-agnostic value proposition weakens.
- **Competition** -- CoreWeave, Lambda, Together AI, RunPod, and others are well-funded in the GPU cloud space, though most are NVIDIA-only.

## Competitors

- CoreWeave (NVIDIA-focused GPU cloud)
- Lambda (GPU cloud for AI)
- Together AI (inference and training platform)
- RunPod (GPU cloud)
- Crusoe Energy (green GPU cloud)
- Hyperscalers (AWS, GCP, Azure) with their own AI compute offerings

## Sources

- [TechCrunch: French startup FlexAI exits stealth with $30M](https://techcrunch.com/2024/04/23/french-startup-flexai-exits-stealth-with-30m-to-ease-access-to-ai-compute/)
- [GlobeNewsWire: FlexAI Launches with $30M in Seed Funding](https://www.globenewswire.com/news-release/2024/04/24/2868408/0/en/FlexAI-Launches-with-30-Million-in-Seed-Funding-to-Deliver-Universal-AI-Compute.html)
- [Silicon Canals: FlexAI founded by ex-Apple, Intel, NVIDIA, Tesla veterans](https://siliconcanals.com/flexai-launches-with-28-5m/)
- [The Next Platform: Startup FlexAI Wants To Make AI Compute Accessible to All](https://www.nextplatform.com/2024/10/15/startup-flexai-wants-to-make-ai-compute-accessible-to-all/)
- [FlexAI and Tenstorrent Partner to Democratize AI Infrastructure](https://www.pr.com/press-release/940583)
- [Sesterce and FlexAI Join Forces for Sovereign AI Computing](https://www.pr.com/press-release/940590)
- [FlexAI Official Website](https://www.flex.ai/)
- [FlexAI Blog: Breaking Vendor Lock-In for AI Startups](https://www.flex.ai/blog/flexai-expands-platform-breaking-vendor-lock-in-for-ai-startups)
- [French Tech Journal: FlexAI Pioneering Universal AI Compute Infrastructure](https://www.frenchtechjournal.com/flexai-pioneering-universal-infrastructure-ai-compute/)
- [The SaaS News: FlexAI Secures $30M in Seed Round](https://www.thesaasnews.com/news/flexai-secures-30-million-in-seed-round)
