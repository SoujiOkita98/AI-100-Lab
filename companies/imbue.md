---
company: Imbue
former_name: Generally Intelligent
founded: 2020
headquarters: San Francisco, CA
website: https://imbue.com
sector: AI Agents / Reasoning / Foundation Models
stage: Series B
founders:
- name: Kanjun Qiu
  role: CEO
  origin: Chinese-American
- name: Josh Albrecht
  role: CTO
  origin: American
team_size: ~20-30 (estimated; sources vary from 15-50)
status: Active
tags:
- AI agents
- reasoning
- foundation models
- coding agents
- unicorn
last_updated: 2026-03-20
funding_rounds:
- stage: Series A
  date: 2022-10
  amount_m: 20.0
  lead_investors:
  - Astera Institute
  source: https://tracxn.com/d/companies/imbue/
- stage: Series B
  date: 2023-09
  amount_m: 200.0
  valuation_m: 1000.0
  lead_investors:
  - Astera Institute
  source: https://techcrunch.com/2023/09/07/imbue-raises-200m/
- stage: Series B Extension
  date: 2023-10
  amount_m: 12.0
  lead_investors:
  - Alexa Fund
  - Eric Schmidt
  source: https://www.crunchbase.com/funding_round/generally-intelligent-series-b--9dbecc7f
one_liner: Imbue is an independent AI research lab that trains its own large foundation models (>100B parameters) optimized
  for reasoning, with the initial application being AI agents that can code
website_verified: true
linkedin: https://www.linkedin.com/company/imbue-ai
crunchbase: https://www.crunchbase.com/organization/imbue
crunchbase_verified: true
twitter: '@imbue_ai'
name: Imbue
linkedin_verified: true
total_raised_m: 232.0
latest_valuation_m: 1000.0
---

# Imbue

**Formerly Generally Intelligent** | Building foundation models optimized for reasoning to power AI agents

## Overview

Imbue is an independent AI research lab that trains its own large foundation models (>100B parameters) optimized for reasoning, with the initial application being AI agents that can code. The company rebranded from Generally Intelligent to Imbue in September 2023 alongside its Series B announcement. Imbue operates as a small, research-heavy team and is one of the few independent labs training its own large-scale models outside of the major frontier labs.

## Founders

### Kanjun Qiu (CEO)

- **Education:** BS in Computer Science from MIT; graduate researcher at the MIT Media Lab.
- **Prior roles:**
  - First Chief of Staff at **Dropbox**, joining when the company had ~200 employees and helping scale it to ~1,200.
  - Co-founder and CEO of **Sourceress**, an ML-powered recruiting startup that went through Y Combinator and raised ~$13M from Lightspeed Venture Partners, OpenAI researchers, YC, and Dropbox founders Drew Houston and Arash Ferdowsi.
  - Sequoia Capital Scout.
  - Co-author of *Sew Electric*, a book teaching computer science through sewing for middle and high school students.
- Kanjun is also a co-founder of **Outset Capital**, a venture fund.

### Josh Albrecht (CTO)

- Published ML researcher with academic papers in the field.
- **Thiel Fellow** mentor.
- Early engineer at **Addepar** (wealth management fintech platform).
- Founded an AI recruiting company (through YC) and a 3D injection molding software company (acquired).
- Started programming as a child and began working professionally as a software engineer in high school.
- Leads all technical work at Imbue: research direction, foundation model development, and backend product development.

**Notable pattern:** Both founders have deep experience at the intersection of AI research and company-building. Their shared background in AI recruiting (Sourceress) likely informed their understanding of practical agent workflows.

## Funding History

| Round | Date | Amount | Key Investors |
|-------|------|--------|---------------|
| Seed | August 2021 | Undisclosed | Not publicly detailed |
| Series A | October 2022 | ~$20M | Not publicly detailed |
| Series B | September 2023 | $200M | Astera Institute (lead), Nvidia, Kyle Vogt (Cruise CEO), Simon Last (Notion co-founder) |
| Series B Extension | October 2023 | $12M | Alexa Fund, Eric Schmidt |

**Total raised:** ~$232M across all rounds.

**Valuation:** $1B post-money after the Series B, achieving unicorn status.

The Series B was led by the **Astera Institute**, a nonprofit founded by Jed McCaleb (co-founder of Ripple and Stellar). Imbue counts approximately 13 known investors: 6 institutional and 7 angel investors.

## Compute Infrastructure

In November 2023, Imbue announced a **$150M deal with Dell Technologies** to build a high-performance computing cluster using Dell PowerEdge XE9690 servers with Nvidia H100 GPUs. The system was designed with smaller clusters for rapid experimentation on novel architectures plus the ability to network into a large cluster for training large-scale models. This is a significant capital commitment for a company of Imbue's size and signals serious intent to remain an independent model trainer.

## Business Model & Product

### Research Approach (Full Stack)

Imbue takes a "full stack" approach to AI:
1. **Foundation model training** -- Pre-training large (>100B parameter) models optimized for internal reasoning benchmarks.
2. **Agent prototyping** -- Building experimental agents used internally, primarily for coding but extending to general-purpose agent work.
3. **Infrastructure & tooling** -- Developing robust tools and systems for agent orchestration.
4. **Theoretical research** -- Investigating the fundamentals of how models learn and reason.

### Product: Sculptor

Imbue's primary public-facing product is **Sculptor**, a UI for running parallel coding agents:

- Runs multiple coding agents in **isolated Docker containers** so they cannot interfere with each other or the developer's local environment.
- Features **Pairing Mode**: bidirectional real-time sync between the agent's container and the developer's local IDE.
- Use cases: resolving bugs, writing tests, adding features, improving docs, fixing style issues.
- Supports **Claude Code** and **Codex** as underlying agents.
- **Free while in beta**; requires Anthropic API access or Claude Pro/Max subscription.
- Available on macOS and Linux (Windows via WSL).
- Open source: [github.com/imbue-ai/sculptor](https://github.com/imbue-ai/sculptor)

**Business model note:** As of March 2026, Sculptor is free in beta and Imbue has not publicly announced a monetization strategy for it. The company's long-term vision is to enable anyone to build robust, custom AI agents. Revenue model remains unclear -- it may evolve toward enterprise tooling, model licensing, or agent-as-a-service. [This is an area of uncertainty.]

### Reasoning Philosophy

Imbue's core thesis is that **reasoning is the primary blocker to effective AI agents**. Their definition of reasoning includes:
- Dealing with uncertainty
- Knowing when to change approach
- Asking questions and gathering new information
- Playing out scenarios and making decisions
- Self-critiquing and analyzing outputs
- Breaking down goals into executable plans

## Current Status (as of March 2026)

- Sculptor has been released and rebuilt based on community feedback, now in active beta.
- The company pre-trained a **70B-parameter model** and fine-tuned it on multiple-choice reasoning benchmarks (reported in 2025).
- Named a "Highflier" in the coding assistance market.
- No new funding rounds publicly announced since October 2023. [It is unclear whether Imbue is seeking or has closed additional funding.]
- Team remains small (~20-30 people, though exact headcount is hard to confirm).

## What Makes Imbue Interesting

1. **Unusual capital efficiency story:** A ~20-30 person team controlling $232M in funding plus $150M in compute infrastructure. One of the highest funding-per-employee ratios in AI.

2. **Independent model training:** One of very few startups outside the frontier labs (OpenAI, Anthropic, Google DeepMind) that pre-trains its own large foundation models. Most agent startups build on top of existing APIs.

3. **Reasoning-first thesis:** While many companies rushed to build agent products on top of GPT-4 or Claude, Imbue bet that reasoning quality at the model level is what matters most for reliable agents. This is a deeper, longer-horizon bet.

4. **Pivot to open tooling:** Sculptor represents an interesting strategic shift -- rather than keeping everything proprietary, Imbue open-sourced an agent orchestration tool that works with other companies' models (Claude, Codex). This could be a funnel for future products or a sign that the pure model-training strategy evolved.

5. **Founder pedigree:** Kanjun's operational experience scaling Dropbox combined with Josh's deep technical ML background is a complementary pairing. Their shared background in AI recruiting (practical ML applications) adds grounding.

6. **Stealth-to-unicorn trajectory:** Founded in 2020, operated in stealth as Generally Intelligent, then emerged with a $1B valuation in under 3 years.

## Key Uncertainties

- **Revenue and monetization path** are not publicly disclosed. It is unclear how or when Imbue plans to generate meaningful revenue.
- **Competitive positioning** against frontier labs (which now all offer reasoning-optimized models) and well-funded agent startups is an open question.
- **Whether independent model training remains viable** at their scale as compute costs and capability gaps relative to the largest labs continue to evolve.
- **No confirmed new funding since late 2023.** Burn rate with a $150M compute cluster and a small team could be significant.
- **Exact team size is uncertain** -- sources range from 15 to 50 employees.

## Sources

- [Imbue official site](https://imbue.com/)
- [Imbue - Introducing Imbue (Series B announcement)](https://imbue.com/company/introducing-imbue/)
- [TechCrunch: Imbue raises $200M](https://techcrunch.com/2023/09/07/imbue-raises-200m-to-build-ai-models-that-can-robustly-reason/)
- [Crunchbase: AI Lab Imbue Gets $200M](https://news.crunchbase.com/ai-robotics/new-ai-unicorn-imbue-astera-nvidia/)
- [Bloomberg: AI Startup Imbue Tops $1 Billion Valuation](https://www.bloomberg.com/news/articles/2023-09-07/ai-startup-imbue-tops-1-billion-valuation-after-funding-from-nvidia)
- [Dell: Imbue $150M HPC System](https://investors.delltechnologies.com/news-releases/news-release-details/imbue-develop-next-generation-ai-models-150-million-dell-high)
- [Kanjun Qiu - Wikipedia](https://en.wikipedia.org/wiki/Kanjun_Qiu)
- [Imbue on Y Combinator](https://www.ycombinator.com/companies/imbue)
- [Sculptor product page](https://imbue.com/sculptor/)
- [Sculptor on GitHub](https://github.com/imbue-ai/sculptor)
- [Nvidia blog: Kanjun Qiu on building smarter AI agents](https://blogs.nvidia.com/blog/how-to-build-smarter-ai-agents/)
- [Crunchbase: Imbue funding profile](https://www.crunchbase.com/organization/generally-intelligent)
