---
company: Cartesia
legal_name: Cartesia AI, Inc.
website: https://cartesia.ai
founded: 2023
headquarters: San Francisco, CA, USA
sector: AI Infrastructure / Voice AI / Edge AI
tags:
- state-space-models
- voice-AI
- text-to-speech
- edge-AI
- real-time-inference
- SSM
founders:
- Karan Goel (CEO)
- Albert Gu (Chief Scientist)
- Arjun Desai
- Brandon Yang
- Chris Ré (Stanford Professor, co-founder)
headcount: ~91 (as of Feb 2026)
total_funding: ~$91M
latest_round: Series A ($64M, March 2025)
lead_investors:
- Kleiner Perkins
- Index Ventures
status: Private, Series A
last_updated: 2026-03-20
one_liner: Cartesia builds real-time AI models based on State Space Model (SSM) architectures, enabling ultra-low-latency
  voice AI and on-device inference that challenges transformer-based approaches
website_verified: true
linkedin: https://www.linkedin.com/company/cartesia-ai
crunchbase: https://www.crunchbase.com/organization/cartesia
crunchbase_verified: true
---

# Cartesia

## One-Liner

Cartesia builds real-time AI models based on State Space Model (SSM) architectures, enabling ultra-low-latency voice AI and on-device inference that challenges transformer-based approaches.

## Overview

Cartesia is a San Francisco-based AI company founded in 2023 by a team of Stanford AI Lab PhD researchers who invented State Space Models (SSMs) -- a fundamentally different architecture from transformers for sequence modeling. The company has rapidly moved from research to commercial products, shipping Sonic (text-to-speech), Ink (speech-to-text), and Line (voice agent platform), all built on their proprietary SSM-based foundation models.

Their core thesis: SSMs can match or exceed transformer quality while being dramatically more efficient, enabling real-time AI that runs on edge devices without cloud connectivity.

## Founders & Team Origins

Cartesia's founding team is deeply rooted in the Stanford AI Lab (Hazy Research group led by Prof. Chris Re):

- **Karan Goel (CEO):** Stanford PhD. Co-authored the foundational S4 paper on structured state spaces and the SaShiMi paper on audio generation with SSMs. Led the transition from research to company building.
- **Albert Gu (Chief Scientist):** Stanford PhD. Primary architect of the S4 (Structured State Spaces) model and co-creator of Mamba, arguably the most influential SSM architecture. His 2021 paper "Efficiently Modeling Long Sequences with Structured State Spaces" is a landmark work in the field.
- **Chris Re:** Stanford CS Professor, MacArthur Fellow, and co-founder. Leads the Hazy Research group, which has produced foundational work in data-centric AI, weak supervision (Snorkel), and now SSMs. Serial academic entrepreneur.
- **Arjun Desai:** Stanford PhD, contributed to SSM research at the Hazy Research lab.
- **Brandon Yang:** Stanford PhD, contributed to SSM research at the Hazy Research lab.

The broader team includes hires from DoorDash, Salesforce, Meta, Scale AI, Microsoft, Google Brain, Apple, and Zoom.

## Funding History

| Round    | Date         | Amount | Lead Investor(s)  | Notable Participants                                                        |
|----------|--------------|--------|--------------------|-----------------------------------------------------------------------------|
| Seed     | Dec 2024     | $27M   | Index Ventures     | --                                                                          |
| Series A | Mar 2025     | $64M   | Kleiner Perkins    | Index Ventures, Lightspeed, A*, Factory, Greycroft, Dell Technologies Capital, Samsung Ventures |

**Total raised:** ~$91M (some sources report slightly different totals; exact valuation not publicly disclosed).

*Note: One source (Startup Stag) references "$100M" in connection with the Sonic-3 launch, which may conflate cumulative funding with the Series A round. The most consistently reported figures are $27M seed + $64M Series A = $91M total.*

## Products & Technology

### Core Architecture: State Space Models (SSMs)

Cartesia's technical moat is SSMs -- an alternative to transformers that processes sequences with constant memory and linear-time complexity (vs. quadratic for attention). Key advantages:
- **Fixed memory footprint** regardless of sequence length
- **Streaming-native** -- designed for real-time, token-by-token generation
- **Hardware-efficient** -- can run on edge devices (phones, laptops) without cloud

The team's research lineage runs: S4 (2021) -> H3/Hungry Hungry Hippos (2022) -> Mamba (2023) -> Mamba-2 -> Cartesia's commercial models.

### Sonic (Text-to-Speech)

Cartesia's flagship product. The latest version, **Sonic-3**, is their most advanced TTS model:
- **Time-to-first-audio (TTFA):** ~90ms (Sonic Turbo: ~40ms)
- **42 languages** covering ~95% of global population, including 9 Indian languages
- **Emotional expression:** fine-grained control over volume, speed, emotion, laughter, and non-verbal sounds
- **Instant voice cloning** from a 3-second audio clip
- **On-device deployment:** Sonic On-Device runs locally without internet, a differentiator vs. cloud-only competitors
- In blind human testing, 62% of users preferred Sonic-3 over competing solutions

### Ink (Speech-to-Text)

Streaming STT model family. Debut model is **Ink-Whisper**, an optimized variant of OpenAI's Whisper for low-latency conversational transcription. Priced at $0.13/hour -- positioned as the lowest-cost streaming STT available.

### Line (Voice Agent Platform)

Full-stack voice agent development platform combining Sonic + Ink + LLM orchestration:
- Background reasoning capabilities
- System integration hooks
- Real-time streaming architecture
- Phone connectivity at $0.014/minute
- Positioned as developer-first, code-centric alternative to no-code voice agent builders

### Rene (Open-Source Language Model)

A 1.3B parameter language model with a hybrid Mamba-2 SSM backbone, open-sourced and tailored for on-device inference. Demonstrates SSM viability for language modeling beyond audio.

### Edge (Open-Source Library)

Software library to optimize SSMs for different hardware configurations, starting with Apple M-series chips. Open-sourced to build ecosystem adoption.

## Business Model

Cartesia operates a **developer platform / API-as-a-service** model:

- **Credit-based pricing:** Monthly credit subscriptions consumed per-character (TTS) or per-second (STT)
- **Tiered plans:** Free tier for experimentation, Scale plan for production workloads
- **Platform revenue:** Line voice agents billed per-minute for calls + LLM usage
- **Enterprise deals:** Fortune 500 customers (specific names not disclosed)
- **On-device licensing:** Sonic On-Device for edge deployment (pricing model unclear)

**Revenue:** One source (GetLatka) reports ~$17M revenue in 2024 with a 49-person team, suggesting strong revenue-per-employee efficiency. *This figure is unverified and should be treated with caution.*

## What Makes Cartesia Interesting

1. **Foundational IP advantage:** The founders literally invented the SSM architectures (S4, Mamba lineage) that underpin their products. This is not a wrapper startup -- they own the science.

2. **Architecture bet against transformers:** Cartesia is one of the highest-profile companies wagering that transformers are not the endgame for all AI workloads. If SSMs prove superior for real-time, streaming, and edge use cases, Cartesia has a multi-year head start.

3. **Edge-native AI:** While most AI companies optimize for cloud GPUs, Cartesia's SSM architecture is inherently suited to edge deployment. Sonic On-Device running locally without internet is a genuine technical achievement that most competitors cannot match.

4. **Full-stack voice platform:** Rather than just selling a model API, Cartesia is building the complete voice AI stack (STT + TTS + agent orchestration + on-device runtime), increasing switching costs and platform lock-in.

5. **Research-to-product velocity:** From foundational papers (2021-2023) to $17M revenue (2024, if accurate) to $91M raised (2025) in roughly 2 years. The Stanford Hazy Research pipeline (previously Snorkel, now Cartesia) continues to produce commercially viable research spinouts.

6. **Latency as competitive moat:** 40-90ms TTFA is meaningfully faster than most competitors and critical for conversational AI applications where latency directly impacts user experience.

## Competitive Landscape

- **ElevenLabs:** Larger, more established voice AI competitor; transformer-based; stronger brand recognition but cloud-only
- **OpenAI (Whisper/TTS):** General-purpose models; Cartesia's Ink-Whisper is explicitly optimized against Whisper for streaming
- **Deepgram:** Enterprise STT/TTS; overlapping market
- **Resemble AI, Respeecher:** Voice cloning specialists
- **Mistral AI:** Competes on efficient model architectures but focused on LLMs, not voice

## Key Risks & Open Questions

- Can SSMs truly rival transformers for general-purpose language modeling at scale, or will they remain best-suited for specific modalities (audio, time-series)?
- Voice AI market is crowding quickly; differentiation on latency alone may erode as competitors optimize
- Revenue figures are unverified; unclear how much is API consumption vs. enterprise contracts
- On-device deployment could cannibalize cloud API revenue
- Valuation not publicly disclosed -- difficult to assess whether funding terms reflect sustainable growth expectations

## Sources

- [Fortune: Cartesia raises $64M Series A (Mar 2025)](https://fortune.com/2025/03/11/exclusive-cartesia-voice-ai-startup-raises-64-million-series-a/)
- [Cartesia Blog: Series A announcement](https://cartesia.ai/blog/series-a)
- [Index Ventures: Investment in Cartesia](https://www.indexventures.com/perspectives/building-the-next-generation-of-real-time-ai-models-our-investment-in-cartesia/)
- [TechCrunch: Cartesia AI efficient enough to run anywhere (Dec 2024)](https://techcrunch.com/2024/12/12/cartesia-claims-its-ai-is-efficient-enough-to-run-pretty-much-anywhere/)
- [Amplify Partners: Interview with Karan Goel](https://www.amplifypartners.com/barrchives/how-cartesia-edges-out-the-big-labs-with-audio-ai-models-with-karan-goel-founder-and-ceo-at-cartesia)
- [Foundation Capital: The promise of State Space Models -- Karan Goel](https://foundationcapital.com/ideas/the-promise-of-state-space-models---karan-goel-(co-founder-ceo-of-cartesia))
- [Cartesia Blog: Introducing Line](https://cartesia.ai/blog/introducing-line-for-voice-agents)
- [Cartesia Blog: Introducing Ink](https://cartesia.ai/blog/introducing-ink-speech-to-text)
- [Cartesia Blog: On-device intelligence](https://cartesia.ai/blog/on-device)
- [Cartesia Pricing Page](https://cartesia.ai/pricing)
- [Dell Technologies Capital: Inside Cartesia's jump to voice AI leadership](https://www.delltechnologiescapital.com/resources/cartesia-voice-ai)
- [The SaaS News: Cartesia raises $64M](https://www.thesaasnews.com/news/cartesia-raises-64-million-in-series-a)
- [ArXiv: S4 paper (Gu, Goel, Re)](https://arxiv.org/abs/2111.00396)
- [Tracxn: Cartesia 2026 profile](https://tracxn.com/d/companies/cartesia/__ViCPaxy5xjTcNRZb2Njd3bZbE5VNNFrxFvBA3r6pavM)
- [GetLatka: Cartesia revenue data](https://getlatka.com/companies/cartesia.ai/competitors)
