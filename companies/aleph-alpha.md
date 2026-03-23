---
name: "Aleph Alpha"
founded: 2019
headquarters: "Heidelberg, Germany"
website: "https://aleph-alpha.com"
sector: ["sovereign AI", "enterprise AI", "foundation models"]
one_liner: "Germany's leading sovereign AI company building enterprise AI platform PhariaAI for government and regulated industries."
status: active
employees: 351

founders:
  - name: Jonas Andrulis
    role: Founder; Chairman of Advisory Board (as of Jan 2026; stepped down as CEO Oct 2025)
    nationality: German
    education:
      - Industrial Engineering, Karlsruhe Institute of Technology (KIT), specialization in AI and modeling
    prior_experience:
      - Apple, Special Projects Group - Senior AI R&D Manager (multiple years in California)
      - Pallas Ludens - Founder & CEO (machine learning / computer vision startup)
    source: https://www.deutschland.de/en/topic/business/portrait-of-jonas-andrulis-founder-of-aleph-alpha

  - name: Samuel Weinbach
    role: Co-Founder; Co-Chief Research Officer
    nationality: German (unconfirmed)
    education:
      - Unknown (details not publicly available)
    prior_experience:
      - Deloitte - AI Expert
    notes: Leads Aleph Alpha Research alongside Yasser Jadidi. Key contributor to the company's work on LLM explainability.
    source: https://theorg.com/org/aleph-alpha/org-chart/samuel-weinbach

current_leadership:
  - name: Reto Spoerri
    role: Co-CEO (installed summer 2025)
    prior_experience: Former divisional head at Schwarz Group
    source: https://sifted.eu/articles/aleph-alpha-founder-quits-as-ceo
  - name: Ilhan Scheer
    role: Co-CEO / Chief Growth Officer (joined 2025)
    prior_experience: Accenture
    source: https://sifted.eu/articles/aleph-alpha-founder-quits-as-ceo
  - name: Lucie Prinz
    role: Chief People Officer
  - name: Yasser Jadidi
    role: Co-Chief Research Officer

funding_rounds:
  - stage: Seed
    date: 2020
    amount_eur: ~5.3M
    notes: Early-stage funding to begin LLM development.
    source: https://www.clay.com/dossier/aleph-alpha-funding

  - stage: "Series A"
    date: "2021"
    amount_m: 25
    lead_investors: ["Earlybird Venture Capital"]
    source: "https://en.wikipedia.org/wiki/Aleph_Alpha"
  - stage: "Series B"
    date: "2023-11"
    amount_m: 500
    lead_investors: ["Schwarz Group", "Innovation Park AI (IPAI)"]
    source: "https://sifted.eu/articles/ai-startup-aleph-alpha-raises-500m"
    notes: "Only ~110M EUR was equity; rest was research grants and order commitments."

total_raised_m: 533

confidence: medium
last_updated: 2026-03-23
---

# Aleph Alpha

## Overview

Aleph Alpha is Germany's most prominent sovereign AI company, headquartered in Heidelberg. Founded in 2019 by Jonas Andrulis (ex-Apple AI) and Samuel Weinbach (ex-Deloitte), the company initially positioned itself as a European competitor to OpenAI, developing its own large language models (Luminous family). It has since executed a significant strategic pivot away from competing on foundation models and toward becoming an enterprise AI platform company, targeting government and regulated industries with its PhariaAI operating system.

## What Makes Aleph Alpha Interesting

**1. The "European Sovereign AI" thesis, tested and evolved.** Aleph Alpha is the highest-profile case study of a non-US company trying to build an independent AI stack and then confronting the economic reality of competing with OpenAI, Anthropic, and Google on foundation models. Rather than collapse, the company pivoted to a platform play -- arguably a more defensible position given European regulatory and data-sovereignty requirements.

**2. The unusual $500M round.** The November 2023 Series B headline was $500M, making it one of Europe's largest AI rounds. But only ~110M EUR was equity. The remainder comprised ~300M EUR in research grants (to subsidiary Aleph Alpha Research) and ~60M EUR in pre-committed customer orders. This structure reflects the German industrial ecosystem's preference for de-risked, project-linked investment rather than pure venture-style equity bets. It also means the company's true equity valuation (~500M EUR) is far lower than the headline suggests.

**3. Deep integration with German industrial giants.** The Schwarz Group (parent of Lidl and Kaufland, and one of the world's largest retailers) is not just an investor but the company's strategic infrastructure partner via its STACKIT cloud platform. SAP and Bosch are also investor-customers. This "customer-as-investor" model provides revenue visibility but also raises questions about independence and whether the company is becoming a captive IT vendor for the Schwarz ecosystem.

**4. The founder transition.** Jonas Andrulis stepped down as CEO in October 2025, replaced by Schwarz Group executive Reto Spoerri and Accenture alumnus Ilhan Scheer as co-CEOs. This leadership change -- from a visionary AI researcher to operators from the investor's orbit -- signals a shift from research ambition to commercial execution. COO Carsten Dirks also departed. Andrulis remains as advisory board chairman, but the operational direction is now firmly in the hands of the Schwarz-aligned leadership.

**5. Government traction at scale.** Deploying an AI assistant to 80,000 government users is meaningful real-world adoption, particularly given the compliance and data-sovereignty requirements of the German public sector. This is a market where US hyperscalers face genuine structural disadvantages due to GDPR, Schrems II, and German federal IT security standards (C5 certification).

## The Pivot: From OpenAI Competitor to Enterprise Platform

Aleph Alpha's original Luminous models (13B-70B parameters) were positioned as European alternatives to GPT. By 2024, the company acknowledged it could not match the compute budgets and talent pools of US frontier labs. The strategic response was PhariaAI: a sovereign AI "operating system" that can integrate both Aleph Alpha's own smaller, optimized models (Pharia-1-LLM-7B) and third-party open-source models via a vLLM-based worker architecture.

This pivot reframed the company from "we build the best models" to "we provide the compliant, sovereign infrastructure layer on which any model can run for European enterprises and governments." The acquisition of thingsTHINKING (and its semantha platform) added domain-specific NLP capabilities for industrial and financial services use cases.

## Risks and Open Questions

- **Schwarz Group dependency:** With Schwarz acquiring Bosch's stake (Feb 2026) and installing its executive as co-CEO, Aleph Alpha increasingly resembles an internal AI division of the Schwarz Group rather than an independent startup. Whether this is a strength (stable backing) or a limitation (loss of startup agility and broader market appeal) remains to be seen.
- **Competitive moat:** The platform pivot is rational but not unique. Competitors like Mistral AI, various open-source model providers, and even US cloud providers with EU data regions could challenge the sovereign AI positioning.
- **Revenue opacity:** The company does not publicly disclose revenue. The conflation of equity, research grants, and order commitments in the Series B makes it difficult to assess commercial traction independently.
- **Headcount volatility:** The ~50-person layoff in January 2026 (reducing headcount from ~400 to ~351) suggests ongoing cost optimization as the company transitions to its new strategy.
- **Model competitiveness:** The Pharia-1-LLM-7B models are small by frontier standards. The company's value proposition now rests on platform and compliance capabilities, not model performance.

## Timeline of Key Events

| Date | Event |
|------|-------|
| 2019 | Founded by Jonas Andrulis and Samuel Weinbach in Heidelberg |
| 2020 | Seed round (~5.3M EUR) |
| 2021 | Series A (~23M EUR) |
| 2021-2023 | Development and release of Luminous model family (13B/30B/70B) |
| Nov 2023 | Series B: $500M headline (110M EUR equity + 300M EUR research + 60M EUR orders) |
| 2024 | Launch of PhariaAI platform; strategic pivot away from foundation model competition |
| 2024 | Acquisition of thingsTHINKING (semantha platform) |
| Mid-2024 | Release of Pharia-1-LLM-7B model family under Open Aleph License |
| May 2025 | PhariaAI-as-a-Service partnership with STACKIT announced |
| Summer 2025 | Reto Spoerri (Schwarz Group) installed as Co-CEO |
| Oct 2025 | Jonas Andrulis steps down as CEO; transitions to advisory board chairman |
| Jan 2026 | ~50-person layoff; organizational realignment |
| Feb 2026 | Schwarz Group acquires Bosch Ventures' shareholding, consolidating ownership |

## Sources

- [Portrait of Jonas Andrulis - deutschland.de](https://www.deutschland.de/en/topic/business/portrait-of-jonas-andrulis-founder-of-aleph-alpha)
- [Aleph Alpha Wikipedia](https://en.wikipedia.org/wiki/Aleph_Alpha)
- [Aleph Alpha raises $500M Series B - Sifted](https://sifted.eu/articles/ai-startup-aleph-alpha-raises-500m)
- [European OpenAI Competitor Aleph Alpha Raises $500M - Crunchbase News](https://news.crunchbase.com/ai/openai-anthropic-competitor-germany-aleph-alpha/)
- [Aleph Alpha founder quits as CEO - Sifted](https://sifted.eu/articles/aleph-alpha-founder-quits-as-ceo)
- [Upheaval at Aleph Alpha: Founder leaves, Schwarz Group moves up - Heise](https://www.heise.de/en/news/Upheaval-at-Aleph-Alpha-Founder-leaves-Schwarz-Group-moves-up-10750654.html)
- [Schwarz Group expands influence over Aleph Alpha - European Cloud](https://european.cloud/2026/02/schwarz-group-aleph-alpha/)
- [Is Aleph Alpha no longer one of the most promising AI start-ups? - European Cloud](https://european.cloud/2025/10/aleph-alpha-no-longer-promising/)
- [Aleph Alpha Announces PhariaAI - Maginative](https://www.maginative.com/article/aleph-alpha-announces-phariaai-a-sovereign-enterprise-grade-ai-operating-system/)
- [Aleph Alpha launches Pharia-1-LLM - CDO Magazine](https://www.cdomagazine.tech/aiml/aleph-alpha-launches-pharia-1-llm-model-family)
- [Aleph Alpha acquires thingsThinking - Sifted](https://sifted.eu/articles/aleph-alpha-acquires-thingsthinking)
- [Aleph Alpha's open-source LLMs comply with AI Act - Techzine](https://www.techzine.eu/blogs/privacy-compliance/123863/aleph-alphas-open-source-llms-fully-comply-with-the-ai-act/)
- [Luminous: the language model that wasn't - European Open Source AI Index](https://osai-index.eu/news/aleph-alpha-pivot/)
- [Aleph Alpha Public Sector](https://aleph-alpha.com/public-sector/)
- [Aleph Alpha IPAI Collaboration](https://aleph-alpha.com/lighthouse-for-sovereign-ai-development-in-germany-aleph-alpha-strengthens-collaboration-with-the-ipai-ecosystem-for-open-and-application-oriented-research-and-development-in-genai/)
- [Alpha ONE Data Center](https://aleph-alpha.com/alpha-one-opens-aleph-alpha-ai-data-centre-closes-infrastructure-gap-at-federal-state-and-local-level/)
- [Aleph Alpha cuts ~50 jobs - Startbase](https://www.startbase.com/news/aleph-alpha-baut-rund-50-stellen-ab/)
- [Aleph Alpha Funding - Clay](https://www.clay.com/dossier/aleph-alpha-funding)
