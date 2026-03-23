---
name: Patronus AI
slug: patronus-ai
domain: AI Evaluation, Safety Testing & LLM Reliability
founded: 2023
headquarters: San Francisco, CA (registered address in Dublin, CA)
founders:
- name: Anand Kannappan
  role: Co-Founder & CEO
  background: Former Head of Engineering & ML at Vertis; ML explainability lead at Meta Reality Labs; Data Scientist at Facebook;
    Co-Founder of Kyber Technologies; BS in Economics, Computer Science & Statistics from University of Chicago
  origin: Indian-American
- name: Rebecca Qian
  role: Co-Founder & CTO
  background: Former Facebook AI researcher; trained FairBERTa (fairness-focused LLM); built semantic parsing for robotic
    assistants at Meta; created Continuous Contrast Set Mining (adopted across Facebook infra, presented at ICSE); University
    of Chicago CS graduate
  origin: Chinese-American
team_size: ~34 employees (estimated as of late 2025)
total_funding: ~$40M
funding_rounds:
- round: Seed
  date: September 2023
  amount: $3M
  lead: Lightspeed Venture Partners
  participants:
  - Factorial Capital
  - Amjad Masad (Replit CEO)
  - Gokul Rajaram
- round: Series A
  date: May 2024
  amount: $17M
  lead: Notable Capital
  participants:
  - Lightspeed Venture Partners
  - Datadog
  - Factorial Capital
  - Gokul Rajaram
- round: Additional equity (SEC filing)
  date: ~2024
  amount: ~$20.5M
  notes: SEC exempt offering filing; may represent Series A extension or follow-on round
latest_round: Series A (May 2024)
key_investors:
- Lightspeed Venture Partners
- Notable Capital
- Datadog (strategic)
- Factorial Capital
status: Private
last_updated: 2026-03-20
confidence: medium-high
crunchbase: https://www.crunchbase.com/organization/patronus-ai
crunchbase_verified: true
---

# Patronus AI

## Overview

Patronus AI is an AI evaluation and safety testing company that provides automated tools for enterprises to detect hallucinations, security vulnerabilities, and other failure modes in large language model (LLM) outputs. The company builds what amounts to a quality assurance and monitoring layer for generative AI deployments -- enabling organizations to test, score, benchmark, and monitor LLM performance before and after production deployment.

Founded in 2023 by two University of Chicago classmates who later worked at Meta, Patronus AI has positioned itself at the center of one of the most critical problems in enterprise AI adoption: **how do you trust that an LLM is producing accurate, safe, and compliant outputs at scale?**

## Founders and Origin Story

**Anand Kannappan (CEO)** and **Rebecca Qian (CTO)** studied computer science together at the University of Chicago and later both worked at Meta, where they independently encountered the challenge of evaluating and interpreting ML outputs -- Anand from an applied/product engineering perspective at Meta Reality Labs, and Rebecca from a research perspective at Facebook AI.

Rebecca's research background is notably strong in NLP fairness and robustness. At Facebook AI, she trained FairBERTa (a large language model designed with fairness objectives), developed demographic-perturbation models for rewriting Wikipedia content, and led semantic parsing for robotic assistants. She also created "Continuous Contrast Set Mining," an infrastructure tool that was adopted across Facebook's engineering teams and was presented at the ICSE conference.

Anand led ML explainability and advanced experimentation efforts at Meta Reality Labs and previously served as Head of Engineering and ML at Vertis. He also co-founded Kyber Technologies.

Their shared frustration with the lack of robust evaluation tooling for LLMs -- especially as enterprises began adopting generative AI in 2023 -- led them to found Patronus AI.

**Source:** [AWS Startups Profile](https://aws.amazon.com/blogs/startups/how-patronus-ai-helps-enterprises-boost-their-confidence-in-generative-ai/), [Unite.AI Interview - Anand](https://www.unite.ai/anand-kannappan-ceo-co-founder-of-patronus-ai-interview-series/), [Unite.AI Interview - Rebecca](https://www.unite.ai/rebecca-qian-co-founder-and-cto-of-patronus-ai-interview-series/)

## Products

### Core Platform

The Patronus AI Platform enables engineering teams to:

- **Score and benchmark LLM performance** on real-world scenarios
- **Generate adversarial test cases** at scale to probe model weaknesses
- **Monitor hallucinations** and unsafe behavior in production (online and offline)
- **Evaluate models** across categories including accuracy, hallucination, brand alignment, PII leakage, toxicity, and copyright infringement

### Key Product Lines

1. **Patronus Evaluators** -- A suite of evaluation tools for assessing LLM outputs across multiple dimensions (accuracy, hallucination, brand alignment, PII leakage, etc.)

2. **Lynx** (open source, released July 2024) -- A state-of-the-art hallucination detection model, fine-tuned on Llama-3. The 70B variant outperformed GPT-4o on hallucination detection benchmarks. Released alongside HaluBench, a 15,000-sample hallucination evaluation benchmark. Available on Hugging Face in 8B and 70B parameter variants. Integrated into NVIDIA NeMo Guardrails.

3. **CopyrightCatcher** -- Industry-first copyright detection API for LLMs that can identify whether outputs contain copyrighted book content and even name the source.

4. **EnterprisePII** -- Evaluation API and dataset for detecting business-sensitive information leakage.

5. **Percival** (launched May 2025) -- The first scalable supervision solution for agentic AI systems. Automatically identifies 20+ failure modes in AI agent traces and suggests optimizations. Reduces agent workflow analysis time from ~1 hour to 1-1.5 minutes. Integrates with Hugging Face Smolagents, Pydantic AI, OpenAI Agent SDK, and LangChain.

6. **Generative Simulators** (launched December 2025) -- Simulated environments for testing AI agents that adapt on the fly, creating new tasks, scenarios, and rules. Supports Open Recursive Self-Improvement (ORSI), a training technique enabling agents to improve through interaction feedback without full retraining.

7. **TRAIL Benchmark** -- Trace Reasoning and Agentic Issue Localization benchmark for evaluating how well systems detect issues in AI agent workflows.

**Sources:** [Patronus Products Page](https://www.patronus.ai/products), [VentureBeat on Lynx](https://venturebeat.com/ai/meet-patronus-ais-lynx-the-open-source-bullshit-detector-outsmarting-gpt-4), [VentureBeat on Percival](https://venturebeat.com/ai/patronus-ai-debuts-percival-to-help-enterprises-monitor-failing-ai-agents-at-scale), [SiliconANGLE on Generative Simulators](https://siliconangle.com/2025/12/17/patronus-ais-debuts-generative-simulators-support-continuous-evolution-improvement-ai-agents/)

## Business Model

Patronus AI operates a **B2B SaaS / API platform** model targeting enterprise customers. Revenue appears to come from:

- **Platform subscriptions** for the Patronus AI evaluation and monitoring platform
- **API usage** for products like CopyrightCatcher and EnterprisePII
- **AWS Marketplace** distribution (listed as a product on AWS Marketplace)

The company automates what has traditionally been a manual, expensive process: human evaluation of LLM outputs. This positions it as a cost-saving and risk-reduction tool for enterprises deploying generative AI.

*Note: Specific revenue figures and pricing tiers are not publicly disclosed.*

## Customers and Partnerships

Patronus AI reports that its platform is used by "numerous Fortune 500 enterprises and leading AI companies." Customers have processed millions of requests through the platform and caught hundreds of thousands of hallucinations.

Notable partnerships include:

- **CARIAD (Volkswagen Group's software subsidiary)** -- Patronus AI partners with CARIAD to continuously enhance in-vehicle AI assistants
- **Databricks** -- Collaborated on training the Lynx hallucination detection model
- **Hugging Face** -- Co-created the Enterprise Scenarios Leaderboard, ranking open-source LLMs on 6 enterprise use cases (finance, legal, customer support, enterprise PII, toxicity, creative writing)
- **MongoDB** -- Partnership announced at Google Cloud Next
- **NVIDIA** -- Lynx integrated into NVIDIA NeMo Guardrails
- **Datadog** -- Strategic investor; Patronus also uses Datadog's observability platform

**Sources:** [Patronus CARIAD Announcement](https://www.patronus.ai/announcements/patronus-ai-partners-with-cariad-volkswagen-software-company), [Databricks Blog on Lynx](https://www.databricks.com/blog/patronus-ai-lynx)

## Funding Details

| Round | Date | Amount | Lead Investor |
|-------|------|--------|---------------|
| Seed | Sep 2023 | $3M | Lightspeed Venture Partners |
| Series A | May 2024 | $17M | Notable Capital |
| Additional equity (SEC filing) | ~2024 | ~$20.5M | Undisclosed |

**Total raised:** ~$40M across all rounds.

Datadog's participation as a strategic investor in the Series A is noteworthy -- it signals potential integration with the broader observability/monitoring ecosystem, where AI model monitoring is a natural extension.

*Note: No Series B announcement has been publicly confirmed as of March 2026. The ~$20.5M SEC filing may represent a Series A extension or separate equity round -- details are uncertain.*

**Sources:** [Series A Announcement](https://www.patronus.ai/blog/announcing-our-17-million-series-a), [Seed Announcement](https://www.patronus.ai/blog/patronus-launch), [Notable Capital Blog](https://www.notablecap.com/blog/why-notable-capital-is-excited-about-patronus-ai)

## What Makes Patronus AI Interesting

1. **Riding the most critical bottleneck in enterprise AI adoption.** The #1 concern enterprises have about deploying LLMs is trust -- hallucinations, data leakage, compliance risk, copyright exposure. Patronus AI is purpose-built to address this entire surface area.

2. **Open-source research credibility.** Releasing Lynx (which outperformed GPT-4o on hallucination detection) and HaluBench as open-source projects builds community trust and establishes technical authority. This is an unusually strong research contribution for a startup of this size.

3. **Rapid pivot to agentic AI evaluation.** The 2025 launches of Percival and Generative Simulators show the company is tracking the market shift from simple LLM chat applications toward autonomous AI agents -- and building evaluation tooling specifically for multi-step agent workflows, which is a much harder problem.

4. **Strategic investor alignment.** Having Datadog (the dominant observability platform) as both an investor and integration partner positions Patronus to become "the Datadog for AI model quality" -- a potentially very large market category.

5. **Deep Meta AI DNA.** Both founders bring production ML experience from Meta's most technically demanding teams (Reality Labs, Facebook AI Research). This is not a team building evaluation tools from the outside -- they experienced the pain of inadequate LLM evaluation firsthand.

6. **Volkswagen/CARIAD partnership.** Winning an automotive safety-critical customer (in-vehicle AI assistants) validates the platform for high-stakes, regulated use cases -- a strong signal for other industries like healthcare, finance, and legal.

## Competitive Landscape

Patronus AI competes with and is adjacent to several categories:

- **LLM evaluation platforms:** Arize AI, Weights & Biases, LangSmith (LangChain), Braintrust
- **AI safety/guardrails:** Guardrails AI, NVIDIA NeMo Guardrails, Lakera
- **AI observability:** Datadog (AI-specific features), Arize Phoenix, Galileo

Patronus differentiates through its focus on automated adversarial testing, proprietary evaluation models (Lynx), and its expanding agentic AI evaluation capabilities (Percival, Generative Simulators).

## Key Uncertainties

- Exact revenue figures and growth trajectory are not publicly available
- Whether the ~$20.5M SEC filing represents a separate round or Series A extension is unclear
- Team size (~34 employees) is an estimate from third-party sources and may have changed
- Long-term competitive moat vs. larger observability platforms (Datadog, Arize) adding native LLM evaluation features is an open question

---

*Profile compiled March 2026. Data sourced from public announcements, press coverage, and third-party databases. Marked uncertainties where information could not be independently verified.*
