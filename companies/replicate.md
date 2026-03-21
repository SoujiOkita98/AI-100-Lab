---
company: Replicate
website: https://replicate.com
founded: 2019
headquarters: San Francisco, CA
founders:
  - name: Ben Firshman
    role: Co-founder & CEO
    background: "Creator of Docker Compose; former Director of Product Management at Docker; 4x founder"
  - name: Andreas Jansson
    role: Co-founder & CTO
    background: "Former Staff ML Engineer at Spotify (2014-2019); PhD in ML for music"
yc_batch: W20
status: "Acquired by Cloudflare (announced November 17, 2025)"
total_funding: ~$58M
last_valuation: $350M (post-Series B, Dec 2023)
acquisition_price: "$350M-$550M (estimated; terms not officially disclosed)"
employees: ~36 (pre-acquisition)
users: "3.7M+ developers; 30,000+ paying customers (as of late 2023)"
revenue: "$5.3M reported for 2024; 'tens of millions' by late 2025 per YC profile"
sector: AI Infrastructure / MLOps / Developer Tools
tags: [AI, open-source, developer-tools, cloud-API, inference, MLOps]
last_updated: 2026-03-20
---

# Replicate

## One-Liner

Cloud API platform that lets developers run open-source ML models with a single API call, eliminating the need to manage GPUs or infrastructure.

## Company Overview

Replicate built one of the largest catalogs of production-ready open-source AI models (50,000+ models by late 2025), accessible via a simple REST API. The platform handles GPU provisioning, scaling, and containerization so developers can integrate AI capabilities -- image generation, LLMs, video, audio, and more -- without ML engineering expertise. The company's open-source packaging tool, **Cog**, lets model authors containerize their models in a standardized, reproducible way (think "Docker for ML models").

## Founders & Origins

**Ben Firshman** and **Andreas Jansson** first met in London in 2012 while both working at **This Is My Jam**, a small music platform with a four-person team. They stayed in touch over the years.

- **Ben Firshman** went on to found **Orchard** (EC2 for containers) in 2013, which led to the creation of **Fig** -- later renamed **Docker Compose**, now an industry-standard tool for defining multi-container applications. He joined Docker, Inc. in 2014, rising to Director of Product Management overseeing Docker's open-source projects. Earlier in his career he built The Guardian's award-winning iPad app and worked on GOV.UK. He is a 4x founder.

- **Andreas Jansson** holds a PhD in machine learning for music and spent five years as a Staff ML Engineer at Spotify (2014-2019), building internal tools for ML model deployment. His frustration with the difficulty of getting ML models from research into production -- requiring extensive collaboration between researchers and engineers -- was a key motivation for Replicate.

The combination of Ben's deep expertise in developer tooling and containerization with Andreas's firsthand experience of ML deployment pain at scale gave Replicate a distinctive founding DNA.

**Note:** Ben Firshman created Docker Compose, not Docker itself. Some sources loosely describe him as a "Docker founder," but more precisely he founded Orchard (acqui-hired by Docker) and created the Compose tool within Docker.

## Funding History

| Round    | Date       | Amount   | Lead Investor         | Notable Participants                                          |
|----------|------------|----------|-----------------------|---------------------------------------------------------------|
| Seed     | ~2020      | $5.3M    | Undisclosed           | Y Combinator, angel investors (Dylan Field/Figma, Guillermo Rauch/Vercel) |
| Series A | Feb 2023   | $12.5M   | Andreessen Horowitz   | Y Combinator, Sequoia Capital, angel investors                |
| Series B | Dec 2023   | $40M     | Andreessen Horowitz   | NVentures (Nvidia), Sequoia Capital, Y Combinator, Heavybit   |
| **Total**|            | **~$58M**|                       |                                                               |

Post-Series B valuation: **$350M**.

The company was part of **Y Combinator's Winter 2020 batch**.

## Acquisition by Cloudflare

On **November 17, 2025**, Cloudflare announced its agreement to acquire Replicate. The deal was expected to close within approximately two months. Financial terms were not officially disclosed, though industry estimates placed the price between **$350M and $550M** (unconfirmed).

Strategic rationale: Cloudflare aimed to integrate Replicate's 50,000+ model catalog and developer platform into Cloudflare Workers AI, enabling serverless AI inference at global edge scale. Ben Firshman's LinkedIn title updated to Cloudflare post-acquisition.

Replicate stated that existing APIs and models would continue to operate without disruption.

## Business Model

- **Usage-based pricing**: Customers pay per second of compute time on GPUs during active inference. Replicate marks up underlying GPU costs while handling all infrastructure management.
- **Pay-as-you-go tier**: Aimed at individual developers and startups; no upfront commitment.
- **Enterprise contracts**: Annual commitments with volume discounts, dedicated deployments for guaranteed performance and isolation, plus compliance and monitoring features.
- **Free tier / community models**: A large catalog of community-contributed models drives developer adoption and top-of-funnel growth.

Revenue was reported at **$5.3M in 2024**. By late 2025, the YC company page described revenue as "tens of millions of dollars," suggesting rapid growth leading into the Cloudflare acquisition.

## Technology

- **Cog** (open-source): A tool for packaging ML models into standard, production-ready Docker containers. Handles CUDA/cuDNN/PyTorch/TensorFlow compatibility automatically. Generates an OpenAPI schema from Python type annotations.
- **Model catalog**: 50,000+ models including popular open-source models (Stable Diffusion variants, LLaMA, Whisper, etc.) as well as proprietary models (OpenAI GPT-5.1, Sora 2, Google Veo 3 were listed by the time of the Cloudflare acquisition).
- **Auto-scaling infrastructure**: Scales GPU resources from zero to match demand, so customers pay only for active inference.

## Customers & Use Cases

- **3.7M+ registered developers** and **30,000+ paying customers** (figures cited in late 2023/2025 sources).
- Many AI startups reportedly built their entire businesses on top of Replicate's inference API.
- Common use cases: image generation, text-to-image, LLM inference, audio transcription, video generation, and custom fine-tuned model deployment.

## What Makes Replicate Interesting

1. **Docker Compose for ML**: The founding insight -- that ML model deployment is a packaging and infrastructure problem analogous to what Docker solved for applications -- proved prescient. Cog became a genuine open-source standard for model containerization.

2. **Developer-first distribution**: By making it trivially easy to run any open-source model with one API call, Replicate captured a massive developer community (3.7M users) that created strong network effects -- model authors publish to Replicate because developers are there, and vice versa.

3. **Open-source ecosystem leverage**: Rather than building proprietary models, Replicate bet on the open-source model ecosystem as its moat. This proved strategically sound as open-source models proliferated (Stable Diffusion, LLaMA, Mistral, etc.).

4. **Founder-market fit**: A Docker Compose creator building "Docker for ML models" alongside a Spotify ML infrastructure veteran is a near-perfect founding team for this problem space.

5. **Successful exit trajectory**: From YC W20 to a $350M+ acquisition by Cloudflare in ~5 years, with only ~$58M raised -- a capital-efficient outcome relative to many AI infrastructure peers.

6. **Strategic acquirer fit**: Cloudflare's global edge network + Replicate's model catalog and developer tooling = a compelling serverless AI inference platform, positioning Cloudflare against AWS, Google Cloud, and Azure in the AI inference market.

## Key Uncertainties

- The exact Cloudflare acquisition price remains officially undisclosed. The $350M-$550M range is based on industry reporting, not confirmed figures.
- Revenue figures: the $5.3M (2024) figure comes from secondary sources (Sacra); the "tens of millions" descriptor from YC's profile is vague.
- Post-acquisition, it is unclear how much of Replicate operates as an independent product vs. being fully absorbed into Cloudflare Workers AI.

## Sources

- [Cloudflare acquisition press release](https://www.cloudflare.com/press/press-releases/2025/cloudflare-to-acquire-replicate-to-build-the-most-seamless-ai-cloud-for-developers/)
- [Replicate blog: Joining Cloudflare](https://replicate.com/blog/replicate-cloudflare)
- [Cloudflare blog: Why Replicate is joining Cloudflare](https://blog.cloudflare.com/why-replicate-joining-cloudflare/)
- [CTOL: Cloudflare acquires Replicate for up to $550M](https://www.ctol.digital/news/cloudflare-acquires-ai-model-platform-replicate-550-million-compete-amazon-google/)
- [Replicate Series B announcement blog](https://replicate.com/blog/series-b)
- [a16z: Investing in Replicate](https://a16z.com/announcement/investing-in-replicate/)
- [Orrick: Replicate raises $40M](https://www.orrick.com/en/News/2023/12/Open-Source-AI-Replicate-Raises-40-Million)
- [TechCrunch: Replicate wants to take the pain out of running ML models](https://techcrunch.com/2023/02/21/replicate-wants-to-take-the-pain-out-of-running-and-hosting-ml-models/)
- [Sequoia: Painting the Town AI (Replicate spotlight)](https://sequoiacap.com/article/replicate-spotlight/)
- [Sequoia: Partnering with Replicate](https://sequoiacap.com/article/partnering-with-replicate-machine-learning-simplified/)
- [Y Combinator: Replicate company page](https://www.ycombinator.com/companies/replicate)
- [Sacra: Replicate funding & analysis](https://sacra.com/c/replicate/)
- [Cog GitHub repository](https://github.com/replicate/cog)
- [SiliconANGLE: Cloudflare acquires Replicate](https://siliconangle.com/2025/11/17/cloudflare-acquires-ai-deployment-startup-replicate/)
