---
company: Tavus
website: https://www.tavus.io
founded: 2021
headquarters: San Francisco, CA
other_offices:
  - London
  - Munich
founders:
  - name: Hassaan Raza
    role: Co-Founder & CEO
  - name: Quinn Favret
    role: Co-Founder & COO
employees: ~40
sector: AI Video / Human Computing
tags:
  - generative-ai
  - digital-avatars
  - conversational-ai
  - developer-platform
  - real-time-video
yc_batch: S21
total_funding: $64.2M
latest_round: Series B
latest_round_date: 2025-11-12
latest_round_amount: $40M
valuation: undisclosed
status: Private
last_updated: 2026-03-20
---

# Tavus

## One-Liner

AI research lab building "human computing" -- real-time, emotionally intelligent AI humans that see, hear, speak, and react in face-to-face video interactions, delivered as a developer platform.

## Overview

Tavus began as a personalized video generation tool (record one video, generate thousands of AI-tailored variants) and has evolved into a full-stack "human computing" platform. The company now builds proprietary models that power lifelike AI avatars capable of real-time, face-to-face conversations with sub-one-second latency. Their positioning is developer-first: white-labeled APIs and SDKs that let product teams embed AI humans into applications across sales, recruiting, education, healthcare, and customer service.

Over 100,000 developers and enterprises reportedly use Tavus today.

## Founders & Team

### Hassaan Raza -- Co-Founder & CEO

- **Education:** B.S. Computer Science, University of Texas at Austin (2015--2019).
- **Career before Tavus:** Software engineer at Hewlett Packard Enterprise and MD Anderson Cancer Center; roles at vAuto/Cox Automotive and JPMorgan Chase (2016--2017); engineering program manager / software engineer at Apple working on macOS security (2018); technical program manager at Google with ML-related responsibilities (2019--2021). In parallel, he led product development at the product studio Simublade (AI/ML focus) and co-founded Accantus, a SaaS/IoT startup applying telemetry to musculoskeletal treatment outcomes.
- Raza has stated he worked in ML areas including avatars, 3D reconstruction, and lip sync for five to six years before founding Tavus.

Sources: [Sacra interview](https://sacra.com/research/hassan-raza-tavus-ai-avatar-developer-platform/), [Sequoia founder page](https://sequoiacap.com/founder/hassaan-raza/), [Leviathan Encyclopedia](https://www.leviathanencyclopedia.com/article/hassaan-raza)

### Quinn Favret -- Co-Founder & COO

- Previously co-founded Chime Menu. Handles operations and go-to-market at Tavus.
- Less publicly profiled than Raza; details on his earlier background are limited.

Sources: [The Org](https://theorg.com/org/tavus/org-chart/quinn-favret), [Crunchbase](https://www.crunchbase.com/person/quinn-favret)

### Research Leadership

The research team includes notable academics from affective computing and computer vision:

- **Dr. Maja Pantic** -- renowned researcher in affective computing and facial analysis (previously at Imperial College London and Meta/Facebook AI Research).
- **Professor Ioannis Patras** -- specialist in rendering and perception (Queen Mary University of London).

The broader research team draws from leading universities and AI labs. The company had approximately 40 employees as of late 2025 and was actively hiring across engineering, product, support, design, and science.

Source: [BusinessWire Series B announcement](https://www.businesswire.com/news/home/20251111507298/en/Tavus-Raises-$40M-to-Build-the-Next-Frontier-of-Intelligence-Human-Computing)

## Funding History

| Round    | Date         | Amount  | Lead Investor          | Notable Participants                                              |
|----------|--------------|---------|------------------------|-------------------------------------------------------------------|
| YC S21   | Summer 2021  | --      | Y Combinator           | --                                                                |
| Seed     | Oct 2023     | $6.1M   | Sequoia Capital        | Y Combinator, others                                             |
| Series A | Mar 2024     | $18M    | Scale Venture Partners | Sequoia Capital, HubSpot Ventures, others                        |
| Series B | Nov 2025     | $40M    | CRV                    | Scale Venture Partners, Sequoia Capital, YC, HubSpot Ventures, Flex Capital |

**Total raised: ~$64.2M across 4 rounds from 19 investors.**

Valuation is not publicly disclosed.

Sources: [TechCrunch Series A](https://techcrunch.com/2024/03/12/generative-ai-video-startup-tavus-raises-18m-to-bring-face-and-voice-cloning-to-any-app/), [BusinessWire Series B](https://www.businesswire.com/news/home/20251111507298/en/Tavus-Raises-$40M-to-Build-the-Next-Frontier-of-Intelligence-Human-Computing), [FinSMEs](https://www.finsmes.com/2025/11/tavus-raises-40m-in-series-b-funding.html)

## Products & Technology

### Proprietary Model Family

Tavus develops its own models rather than wrapping third-party foundation models:

| Model       | Function                                                                 | Status (as of early 2026)       |
|-------------|--------------------------------------------------------------------------|---------------------------------|
| **Phoenix-4** | Real-time human rendering with emotional intelligence; full-duplex (listens and responds simultaneously); generates full head/shoulders including eye blinks; developer-controllable emotional expression. Sub-600ms latency. | Launched Feb 2026               |
| **Raven-1**   | Perception model -- enables the AI human to see and interpret visual context. | GA                              |
| **Sparrow-1** | Multilingual audio model for humanlike conversational timing and floor transfer (when to listen, wait, or speak). | GA (Jan 2026)                   |

Together these form an end-to-end behavioral stack: rendering (Phoenix) + perception (Raven) + conversational timing (Sparrow).

Sources: [Tavus Research page](https://www.tavus.io/research), [Phoenix-4 launch](https://www.businesswire.com/news/home/20260218278213/en/Tavus-Launches-Phoenix-4-the-First-Real-Time-Human-Rendering-Model-with-Emotional-Intelligence), [Sparrow-1 blog](https://www.tavus.io/post/sparrow-1-human-level-conversational-timing-in-real-time-voice)

### Product Surface

1. **Conversational Video Interface (CVI):** Real-time, face-to-face AI human conversations. The AI avatar appears on screen, sees and hears the user via camera/mic, and reacts in real time.
2. **Video Generation (Replicas):** Script-to-video with AI digital twins -- the original personalized-video product. Record once, generate thousands of personalized variants.
3. **PALs:** AI humans with emotional intelligence, agentic capabilities, and true multimodality (text + voice + face-to-face). Launched alongside the Series B.

### Developer Platform

- White-labeled API endpoints, SDKs, and webhooks.
- Configurable: swap in any LLM, RAG pipeline, or TTS provider.
- Features: persona setup with objectives/guardrails, knowledge base (RAG), memories, transcripts, optional recordings, function calling.

## Business Model & Pricing

**Usage-based SaaS with tiered plans:**

| Plan       | Price         | Key Inclusions                                                        |
|------------|---------------|-----------------------------------------------------------------------|
| Starter    | $39/month     | Pay-as-you-go usage, 3 personal replicas, up to 3 concurrent conversations |
| Growth     | $375/month    | Discounted usage rates, 10 replicas, 15 concurrent conversations, recording/transcripts |
| Enterprise | Custom        | Unlimited replicas, volume discounts, premium support, custom SLAs    |

Revenue is driven by a combination of seat count and per-video / per-conversation usage. Enterprise contracts likely represent the bulk of revenue given the resource-intensive nature of real-time video rendering. (*Exact revenue figures are not publicly available.*)

Source: [Tavus Pricing page](https://www.tavus.io/pricing)

## Customers & Use Cases

Tavus claims both Fortune 500 companies and startups as customers. Specific named logos are not prominently disclosed. Verticals include:

- **Sales & Marketing:** Personalized outreach videos at scale; AI sales agents for demos.
- **Recruiting:** AI-powered screening interviews and candidate engagement.
- **Education:** Interactive AI tutors and training content.
- **Healthcare:** Patient engagement and telehealth assistance.
- **Customer Service:** AI humans handling support interactions face-to-face.
- **Financial Services:** Personalized advisory and client communications.

The company holds SOC 2 compliance, automated content moderation, and anti-hallucination quality checks -- positioning for enterprise-grade security requirements.

Source: [Tavus AI info page](https://www.tavus.io/lp/ai-info-page)

## Competitive Landscape

Key competitors include **HeyGen**, **Synthesia**, **D-ID**, **Soul Machines**, and **DeepBrain AI**.

### What differentiates Tavus:

1. **Real-time conversational video (not just pre-rendered clips).** HeyGen and Synthesia focus primarily on programmatic/asynchronous video generation. Tavus and Soul Machines are the main players in real-time interactive AI humans, but Tavus claims lower latency and more developer flexibility.
2. **Developer-first platform.** Tavus is designed as infrastructure for product teams to embed, not a standalone SaaS tool for marketers. HeyGen's API and Synthesia's API are less mature by comparison.
3. **Proprietary, vertically integrated model stack.** Phoenix + Raven + Sparrow give Tavus control over rendering, perception, and conversational timing as a unified system, rather than stitching together third-party components.
4. **Emotional intelligence.** Phoenix-4 (Feb 2026) is positioned as the first real-time model that generates and controls emotional states, active listening behavior, and continuous facial motion as a single system.

Source: [Tavus competitor comparisons](https://www.tavus.io/post/heygen-api), [MarkTechPost Phoenix-4 analysis](https://www.marktechpost.com/2026/02/18/tavus-launches-phoenix-4-a-gaussian-diffusion-model-bringing-real-time-emotional-intelligence-and-sub-600ms-latency-to-generative-video-ai/)

## What Makes Tavus Interesting (Research Notes)

1. **Category creation ambition.** "Human computing" is a deliberate attempt to define a new category beyond "AI avatars" or "video personalization." The thesis is that human-AI interaction should feel as natural as face-to-face conversation -- not chat windows or voice-only assistants.

2. **Research lab identity with a commercial product.** Tavus publishes its own models (Phoenix, Raven, Sparrow) and has recruited serious academics (Maja Pantic is one of the most cited researchers in affective computing). This is unusual for a 40-person startup and signals deep technical ambition.

3. **Investor signal quality.** Sequoia at seed, Scale Venture Partners leading Series A, CRV leading Series B -- a strong, escalating investor trajectory. YC S21 pedigree.

4. **Platform vs. application bet.** By going developer-first / API-first, Tavus is betting on being the infrastructure layer that many applications are built on, rather than competing application-by-application with HeyGen or Synthesia. This is a higher-risk, higher-reward positioning.

5. **Speed of model iteration.** Phoenix-3 (Mar 2025) to Phoenix-4 (Feb 2026) with Raven and Sparrow models shipping in between suggests a rapid research cadence for a company this size.

6. **Founder background.** Hassaan Raza's path through Apple, Google, and ML-focused product work before age 25 is notable. The combination of engineering depth and program management experience at major tech companies is a useful founder archetype for a developer-platform company.

7. **Open question: unit economics.** Real-time video rendering is compute-intensive. Whether Tavus can achieve attractive margins at scale -- especially on the $39/month Starter tier -- is an important question. The Enterprise tier with custom pricing likely subsidizes, but long-term gross margin trajectory is worth watching.

8. **Open question: specific customer traction.** The "100,000+ developers and enterprises" claim lacks named references. It is unclear how much of this is free-tier/trial usage versus paying customers. No public revenue figures exist.

## Key Sources

- [Tavus official site](https://www.tavus.io/)
- [TechCrunch: Series A coverage (Mar 2024)](https://techcrunch.com/2024/03/12/generative-ai-video-startup-tavus-raises-18m-to-bring-face-and-voice-cloning-to-any-app/)
- [BusinessWire: Series B announcement (Nov 2025)](https://www.businesswire.com/news/home/20251111507298/en/Tavus-Raises-$40M-to-Build-the-Next-Frontier-of-Intelligence-Human-Computing)
- [BusinessWire: Phoenix-4 launch (Feb 2026)](https://www.businesswire.com/news/home/20260218278213/en/Tavus-Launches-Phoenix-4-the-First-Real-Time-Human-Rendering-Model-with-Emotional-Intelligence)
- [Sacra: Hassaan Raza interview](https://sacra.com/research/hassan-raza-tavus-ai-avatar-developer-platform/)
- [Sequoia: Hassaan Raza founder profile](https://sequoiacap.com/founder/hassaan-raza/)
- [Y Combinator: Tavus profile](https://www.ycombinator.com/companies/tavus)
- [VentureBeat: Series B coverage](https://venturebeat.com/business/tavus-raises-40m-to-build-the-next-frontier-of-intelligence-human-computing/)
- [MarkTechPost: Phoenix-4 technical analysis](https://www.marktechpost.com/2026/02/18/tavus-launches-phoenix-4-a-gaussian-diffusion-model-bringing-real-time-emotional-intelligence-and-sub-600ms-latency-to-generative-video-ai/)
- [Cerebral Valley: Tavus profile](https://cerebralvalley.ai/blog/tavus-is-revolutionizing-ai-powered-video-2LgxA00cMmdw9YoXpqMMBk)
- [Crunchbase: Tavus](https://www.crunchbase.com/organization/tavus)
