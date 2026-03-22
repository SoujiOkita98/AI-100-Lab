---
name: Magic
legal_name: Magic AI, Inc.
website: https://magic.dev
founded: 2022
headquarters: San Francisco, CA
founders:
- name: Eric Steinberger
  role: Co-founder & CEO
  background: Born in Vienna, Austria. Obsessed with AI from age 14. Studied Computer Science at University of Cambridge (2018-2020).
    Researcher in Deep Reinforcement Learning at Facebook AI Research (FAIR) from 2019-2022, where he collaborated with Noam
    Brown on poker AI (PokerRL). Founded ClimateScience, a climate education nonprofit. Left Cambridge and FAIR in 2022 to
    start Magic.
  origin: Austrian
- name: Sebastian De Ro
  role: Co-founder & CTO
  background: Holds a Master's degree in Computer Science. Previously at Google Research, specializing in large-scale machine
    learning systems. Co-founded two AI startups in Europe focused on NLP. Expertise in neural architecture design, distributed
    systems, and AI safety.
  origin: German
sector: AI / Developer Tools / Code Generation
stage: Series C
total_funding_usd: ~466M
latest_valuation_usd: ~1.5B (reported target, July 2024; unconfirmed final valuation)
employees: ~97 (as of January 2026)
status: Active, Pre-revenue or very early revenue
last_updated: 2026-03-20
funding_rounds:
- stage: Seed
  date: 2022-03
  amount_m: 5.1
  lead_investors:
  - ROI Ventures
  source: https://www.crunchbase.com/organization/magic-83fe
- stage: Series A
  date: 2023-02
  amount_m: 23
  lead_investors:
  - CapitalG
  source: https://news.crunchbase.com/ai/coding-venture-funding-magic-codeium/
- stage: Series B
  date: 2024-02
  amount_m: 117
  lead_investors:
  - NFDG Ventures
  source: https://news.crunchbase.com/ai/coding-venture-funding-magic-codeium/
- stage: Series C
  date: 2024-08
  amount_m: 320
  lead_investors:
  - Eric Schmidt
  - Sequoia
  source: https://techcrunch.com/2024/08/29/generative-ai-coding-startup-magic-lands-320m-investment-from-eric-schmidt-atlassian-and-others/
one_liner: Magic is building an AI software engineer designed to function as a collaborative "co-worker" rather than a simple
  autocomplete copilot
---

# Magic -- AI Software Engineer with Ultra-Long Context

## Company Overview

Magic is building an AI software engineer designed to function as a collaborative "co-worker" rather than a simple autocomplete copilot. The company's core technical differentiator is its proprietary Long-Term Memory (LTM) architecture, which enables context windows of up to 100 million tokens -- roughly 10 million lines of code or 750 novels. Magic frames its work as a step on the path toward safe AGI.

## Founding Story

Eric Steinberger, born in Vienna, became obsessed with AI at age 14. While still a high school student at HTL Spengergasse (2013-2018), he caught the attention of Noam Brown at Meta's FAIR lab by implementing and improving upon one of Brown's reinforcement learning papers, becoming FAIR's youngest working student. At Cambridge, he continued RL research and created the open-source PokerRL framework for deep reinforcement learning in imperfect-information games.

After Cambridge, Steinberger pivoted to climate work, founding ClimateScience (a nonprofit he grew to over 1,000 volunteers worldwide). In 2022, he concluded that AGI was closer than expected and co-founded Magic with Sebastian De Ro to accelerate the path there through automated software engineering.

De Ro brings complementary engineering depth -- experience at Google Research on large-scale ML systems, two prior AI startup co-founding experiences in Europe, and expertise in distributed systems and neural architecture design. He has overseen the development of Magic's 100M-token context model and its inference platform.

## Funding History

| Round    | Date          | Amount   | Lead / Key Investors                                                        |
|----------|---------------|----------|-----------------------------------------------------------------------------|
| Seed     | 2022          | ~$20K    | Techstars                                                                   |
| Series A | February 2023 | $45M     | CapitalG (Alphabet), Amplify Partners                                       |
| Series B | February 2024 | $117M    | NFDG Ventures (Nat Friedman & Daniel Gross), CapitalG, Elad Gil             |
| Series C | March 2024    | $320M    | Eric Schmidt; with CapitalG, Atlassian, Elad Gil, Jane Street, Nat Friedman & Daniel Gross, Sequoia |

**Total raised:** ~$466M across 4 rounds.

The Series C reportedly valued Magic at approximately $1.5 billion, though the exact post-money valuation has not been officially confirmed by the company.

## Notable Team Hires

- **Ben Chess** -- former lead on OpenAI's supercomputing team, joined Magic to scale infrastructure.
- The team is described as small but composed of former senior professionals from top tech companies and academia. As of January 2026, the company had approximately 97 employees.

## Core Technology: Long-Term Memory (LTM)

Magic's central technical bet is on ultra-long context rather than retrieval-augmented generation (RAG). Their proprietary LTM architecture replaces standard transformer attention with a mechanism that is dramatically more efficient at long sequences:

- **LTM-2-mini** (their publicly discussed model) supports a 100 million token context window.
- For a 100M-token context, LTM-2-mini's sequence-dimension algorithm is approximately **1,000x cheaper** than the attention mechanism in Llama 3.1 405B.
- Running Llama 3.1 405B at 100M tokens would require 638 H100 GPUs per user just for the KV cache; LTM requires a small fraction of a single H100's memory per user.
- Magic is training a larger LTM-2 model on dedicated supercomputers.

The thesis is that with enough context, the model can see and reason over an organization's entire codebase -- including proprietary code, documentation, and internal libraries not on the public internet -- enabling it to complete large, multi-step engineering tasks autonomously.

## Infrastructure: Google Cloud Partnership

Magic has partnered with Google Cloud as its preferred cloud provider and is building two supercomputers on Google Cloud's AI Hypercomputer architecture:

- **Magic-G4**: Powered by NVIDIA H100 Tensor Core GPUs (A3 Mega VMs).
- **Magic-G5**: Will use NVIDIA GB200 NVL72 (Grace Blackwell platform), with the ability to scale to tens of thousands of Blackwell GPUs.

## Business Model

Magic's business model details are not fully public. As of mid-2024 reporting, the company had minimal revenue (one source cited ~$2M in 2023 with a 23-person team). The company appears to be in a research-heavy, pre-commercial or very early commercial phase, investing heavily in model training and infrastructure. The broader AI coding tool market is projected to reach $27 billion by 2032 (Polaris Research estimate).

**[Uncertainty note]:** Specific pricing, packaging, or go-to-market strategy for 2025-2026 could not be confirmed from public sources. It is unclear whether Magic has launched a generally available product or remains in limited access/pilot mode as of March 2026.

## What Makes Magic Interesting

1. **Contrarian technical bet on context over RAG.** While most competitors use retrieval-augmented generation to handle large codebases, Magic is building custom architectures (LTM) that can natively ingest entire repositories. If the approach works at scale, it could yield qualitatively different capabilities in code understanding and generation.

2. **Extraordinary capital efficiency in fundraising.** Nearly half a billion dollars raised by a team that was ~23 people through 2023 and ~97 by early 2026. The investor roster (Eric Schmidt, Sequoia, CapitalG, Jane Street, Nat Friedman/Daniel Gross) is unusually strong.

3. **Founder profile.** Steinberger's trajectory -- FAIR researcher as a teenager, RL/poker AI work with Noam Brown, Cambridge CS, climate nonprofit founder -- is distinctive. He has publicly framed Magic's mission as building toward AGI, not just a developer tool.

4. **Dedicated compute infrastructure.** The Google Cloud partnership with two purpose-built supercomputers (scaling to tens of thousands of Blackwell GPUs) positions Magic with serious training capacity, unusual for a startup of this size.

5. **Efficiency claims.** The 1,000x efficiency improvement over standard attention at 100M tokens, if it holds at scale with competitive quality, would represent a meaningful architectural breakthrough.

## Competitive Landscape

Magic competes with a crowded field of AI coding tools:

- **GitHub Copilot** (Microsoft/OpenAI) -- market leader by adoption
- **Cursor** -- AI-native code editor, strong developer following
- **Codeium / Windsurf** -- free-tier competitor
- **Cognition (Devin)** -- autonomous AI software engineer
- **Augment** -- enterprise AI coding assistant

Magic differentiates primarily on context length and its ambition to build an autonomous engineer (not just an autocomplete tool).

## Key Risks

- Pre-revenue or minimal-revenue status despite ~$466M raised creates pressure to demonstrate commercial viability.
- The LTM architecture's quality at 100M-token scale versus RAG-based or shorter-context competitors is not yet independently benchmarked at production scale.
- The AI coding tools market is intensely competitive, with well-funded incumbents (Microsoft, Google) and fast-moving startups.
- AGI framing may attract talent and capital but could also set unrealistic expectations.

## Sources

- [TechCrunch: Magic lands $320M investment (Aug 2024)](https://techcrunch.com/2024/08/29/generative-ai-coding-startup-magic-lands-320m-investment-from-eric-schmidt-atlassian-and-others/)
- [SiliconANGLE: Magic seeking $1.5B valuation (Jul 2024)](https://siliconangle.com/2024/07/02/generative-ai-coding-assistant-startup-magic-ai-looking-raise-200m-1-5b-valuation/)
- [Sequoia: Eric Steinberger on Magic's Approach to AGI (podcast)](https://sequoiacap.com/podcast/training-data-eric-steinberger/)
- [Sequoia: Eric Steinberger founder profile](https://sequoiacap.com/founder/eric-steinberger/)
- [Magic Blog: 100M Token Context Windows](https://magic.dev/blog/100m-token-context-windows)
- [Google Cloud Blog: Magic partnership](https://cloud.google.com/blog/products/ai-machine-learning/magic-ai-100m-tokens-cloud-supercomputer)
- [CapitalG: Magic -- Reimagining Software Engineering with AI](https://www.capitalg.com/insights/magic-reimagining-software-engineering-with-ai)
- [The Decoder: LTM-2-mini record for context processing](https://the-decoder.com/ltm-2-mini-sets-new-record-for-ai-context-processing-handling-10-million-lines-of-code/)
- [Tracxn: Magic AI company profile](https://tracxn.com/d/companies/magic-ai/__Y_4iQlpPq65_ZP9qNeWGuLLPBlVaGm7gJxWQH5i6arA)
- [Crunchbase: Magic AI funding](https://www.crunchbase.com/organization/magic-5c3e)
- [AIX Expert Network: Magic profile](https://aiexpert.network/magic/)
- [Maginative: Magic secures $320M, partners with Google Cloud](https://www.maginative.com/article/magic-secures-320m-funding-partners-with-google-cloud-for-ai-supercomputers/)
- [Data Center Dynamics: Magic + Google Cloud](https://www.datacenterdynamics.com/en/news/gen-ai-startup-magic-partners-with-google-cloud-closes-320m-funding-round/)
