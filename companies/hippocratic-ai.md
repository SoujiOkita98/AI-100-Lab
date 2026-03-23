---
company: Hippocratic AI
sector: Healthcare AI / Agentic AI
founded: 2023
headquarters: Palo Alto, CA
ceo: Munjal Shah
employees: ~200-260 (estimates vary by source; ~211 as of Dec 2025)
latest_valuation: $3.5B (Series C, Nov 2025)
total_funding: $404M
stage: Series C
status: Private
website: https://hippocraticai.com
last_updated: 2026-03-20
funding_rounds:
- stage: Seed
  date: 2023-05
  amount_m: 50
  lead_investors:
  - General Catalyst
  - Andreessen Horowitz
  source: https://www.globenewswire.com/en/news-release/2023/05/16/2670039/0/en/
- stage: Seed Extension
  date: 2023-07
  amount_m: 15
  lead_investors:
  - General Catalyst
  - Andreessen Horowitz
  source: https://hippocraticai.com/press/
- stage: Series A
  date: 2024-03
  amount_m: 53
  valuation_m: 500
  lead_investors:
  - Premji Invest
  - General Catalyst
  source: https://www.globenewswire.com/news-release/2024/03/18/2848237/0/en/
- stage: Series A Extension
  date: 2024-09
  amount_m: 17
  lead_investors:
  - NVentures (NVIDIA)
  source: https://vator.tv/news/2024-09-20-hippocratic-ai-adds-17m-to-its-series-a-funding-partners-with-nvidia
- stage: Series B
  date: 2025-01
  amount_m: 141
  valuation_m: 1640
  lead_investors: []
  source: https://www.fiercehealthcare.com/ai-and-machine-learning/hippocratic-ai-banks-141m-series-b-hits-unicorn-status-it-rolls-out-ai
- stage: Series C
  date: 2025-11
  amount_m: 126
  valuation_m: 3500
  lead_investors:
  - Avenir Growth
  source: https://hippocraticai.com/hippocratic-ai-announces-series-c-funding-126-million/
one_liner: Hippocratic AI builds safety-focused generative AI agents for healthcare
website_verified: true
twitter: '@hippocraticai'
linkedin: https://www.linkedin.com/company/hippocratic-ai-health
crunchbase: https://www.crunchbase.com/organization/hippocratic-ai
crunchbase_verified: true
---

# Hippocratic AI

## Overview

Hippocratic AI builds safety-focused generative AI agents for healthcare. The company deploys AI agents that handle non-diagnostic, patient-facing tasks -- chronic care management, post-discharge follow-ups, pre-operative preparation, clinical trial coordination, and more -- at a fraction of the cost of human staff. Named after the Hippocratic Oath ("first, do no harm"), the company's core thesis is that healthcare AI must be held to a higher safety standard than general-purpose AI, and that staffing shortages across global healthcare create an enormous addressable market for safe, scalable AI agents.

As of early 2026, the company reports 150+ million clinical interactions across 1,000+ use cases with 50+ partners worldwide, with no reported safety incidents.

## Founders & Team

### Munjal Shah -- Co-Founder & CEO

- **Education:** BS in Computer Science from UC San Diego (senior thesis on neural networks for protein ligand binding prediction); MS in Computer Science from Stanford, focused on AI.
- **Prior companies:**
  - **Andale Inc. (1999):** One of the first cloud-based SaaS companies for small businesses. Acquired by Vendio, later sold to Alibaba.
  - **Like.com:** Early consumer AI company using computer vision and ML to search inside digital photographs. Acquired by Google in 2010.
  - **Health IQ (~2014-2022):** Spent ~10 years as co-founder/CEO of a healthcare startup using AI to analyze health records to help seniors select Medicare Advantage plans.
- **Angel investing:** Backed 42+ companies and 23+ venture funds, including multiple unicorn outcomes.
- Shah is a serial entrepreneur with deep roots in both AI and healthcare -- an unusual combination that gives him credibility in both VC and health system circles.

### Other Co-Founders & Key Leaders

- **Vishal (Co-Founder & CPO):** Leads product and engineering. Background in building and scaling high-growth technology companies across AI, engineering, and operations. *(Full last name not confirmed in public sources.)*
- **Subho (Co-Founder & CSO):** Chief Science Officer. Previously Principal Researcher at Microsoft Research, leading large-scale foundation model efforts. PhD from Max Planck Institute, Germany. Spearheads multimodal AI model development. *(Full last name not confirmed in public sources.)*
- **Dr. Ahad Wahid:** Appointed President of Life Sciences (Jan 2026) to lead the new Life Sciences Division following the Grove AI acquisition.

### Team Origins

The founding team is drawn from physicians, hospital administrators, healthcare professionals, and AI researchers from institutions including El Camino Health, Johns Hopkins, Washington University in St. Louis, Stanford, Google, and NVIDIA. The company also maintains a clinical validation network of 6,000+ licensed nurses and 300+ licensed physicians who evaluate AI agent safety.

## Technology: Polaris Constellation Architecture

Hippocratic AI's proprietary system, **Polaris**, uses a "constellation" of multiple specialized LLMs rather than a single model:

- **Architecture:** 22+ models working together -- one large (~400B parameter) conversational model does the talking, while 21+ smaller task-specific models (70B+ parameters each) supervise it in real-time, checking for hallucinations, unsafe outputs, and clinical accuracy.
- **Safety validation:** Every agent undergoes a three-step process -- licensure verification, development testing, and clinical review by the nurse/physician network.
- **NVIDIA partnership:** Optimized using TensorRT-LLM for faster, cheaper inference. Collaboration with NVIDIA on inference performance for on-demand deployment.
- **Patented:** The safety-focused LLM architecture is patented.
- **Evolution:** Now at Polaris 3.0 as of the latest public information.

In head-to-head evaluations with 1,100+ nurses and 130+ physicians acting as simulated patients, Polaris performed on par with human nurses across medical safety, clinical readiness, patient education, conversational quality, and bedside manner.

## Funding History

| Round    | Date       | Amount   | Valuation | Lead Investors                                    |
|----------|------------|----------|-----------|---------------------------------------------------|
| Seed     | May 2023   | $50M     | Undisclosed | General Catalyst, Andreessen Horowitz (a16z)    |
| Seed Ext.| Jul 2023   | +$15M    | Undisclosed | (Extension of seed round)                       |
| Series A | Mar 2024   | $53M     | $500M     | Premji Invest, General Catalyst                   |
| Series B | Jan 2025   | $141M    | $1.64B    | *(Lead not confirmed; likely General Catalyst)*   |
| Series C | Nov 2025   | $126M    | $3.5B     | Avenir Growth                                     |

**Total raised: ~$404M**

Notable investors across rounds: General Catalyst, Andreessen Horowitz (a16z), Premji Invest, Kleiner Perkins, CapitalG (Google's growth fund), SV Angel, Universal Health Services (UHS), Cincinnati Children's Hospital, WellSpan Health, Memorial Hermann Health System, John Doerr, Rick Klausner.

The investor base is notable for mixing top-tier tech VCs with actual health systems -- a deliberate strategy that gives the company both capital and built-in design partners/customers.

## Business Model

- **B2B, usage-based pricing:** Sells AI agent services directly to health systems, payers, and pharma companies.
- **Price point:** ~$9/hour per agent, compared to ~$45/hour average cost for a human nurse (2024 figures). This cost differential is the core value proposition.
- **AI Agent App Store (launched Jan 2025):** 300+ AI agents spanning 25 medical specialties. Introduces a platform revenue model where Hippocratic takes a share of revenue from third-party-developed agents -- a potentially significant long-term margin expansion lever.
- **Consulting partnerships:** Strategic collaborations with KPMG and BCG to deploy agents within their healthcare consulting engagements, effectively using Big Four/MBB as distribution channels.

## Customers & Partners

### Health Systems (Selected)
- **Universal Health Services (UHS):** Deployed post-discharge follow-up agents at Summerlin Hospital (Las Vegas) and Texoma Medical Center (TX). Patient ratings averaged 9.0/10. Expanding to additional facilities. UHS also invested in the Series C.
- **WellSpan Health:** One of the first health systems to launch Hippocratic AI agents (Sep 2024). Also a Series C investor.
- **Cincinnati Children's Hospital Medical Center:** Partner and investor.
- **Memorial Hermann Health System:** Series A investor and partner.

### Consulting & Enterprise
- **KPMG (Jul 2025):** Global collaboration to deploy AI agents to address healthcare workforce shortages.
- **BCG / BCG X (Jan 2026):** Strategic collaboration to deploy agentic AI across biopharma and medtech.

### Life Sciences / Pharma
- **Grove AI acquisition (Jan 2026):** Brought agentic AI capabilities for pharma R&D and clinical trial operations. Grove AI had powered 10M+ patient interactions for enterprises including two of the top five global pharma companies.

The company reports 50+ partners total across health systems, payers, and pharma.

## What Makes Hippocratic AI Interesting

1. **Safety-first architecture in a safety-critical domain.** The constellation approach -- multiple models supervising a primary model -- is a genuinely differentiated technical bet. Most AI companies optimize for capability; Hippocratic optimizes for not making mistakes. This is the right priority ordering for healthcare.

2. **Valuation trajectory.** $0 to $3.5B in under three years. The 2x+ jump from $1.64B (Jan 2025) to $3.5B (Nov 2025) in just 10 months signals strong commercial traction, not just hype.

3. **Health systems as investors.** UHS, WellSpan, Cincinnati Children's, and Memorial Hermann are not just customers -- they are equity holders. This creates alignment and stickiness that pure software sales cannot match.

4. **Unit economics pitch.** $9/hr vs. $45/hr is a compelling and easy-to-understand value proposition for budget-strained health system CFOs. The nursing shortage (projected to worsen through 2030+) creates sustained demand.

5. **Platform ambitions via the App Store.** Moving from selling agents to hosting a marketplace of 300+ agents across 25 specialties is an attempt to become the "iOS of healthcare AI agents." If it works, it shifts the business from linear services revenue to platform economics.

6. **Life sciences expansion.** The Grove AI acquisition and BCG/KPMG partnerships extend the TAM from health systems into pharma R&D, clinical trials, and medtech -- a much larger revenue pool.

7. **Founder-market fit.** Munjal Shah combines a Stanford AI background, three prior exits (including one to Google), a decade in healthcare, and prolific angel investing. The co-founding team bridges AI research (Microsoft Research, Max Planck) and clinical practice (Johns Hopkins, El Camino Health).

## Risks & Open Questions

- **Regulatory uncertainty.** AI agents making patient-facing calls exist in a regulatory gray area. FDA and state-level regulations could impose new compliance burdens.
- **Safety at scale.** 150M+ interactions with no reported safety issues is impressive, but one high-profile adverse event could be existential for a company whose brand is built on safety.
- **Revenue vs. valuation.** At $3.5B, the company needs substantial revenue to justify the valuation. Actual revenue figures are not publicly disclosed. *(Uncertainty: it is unclear whether the company is profitable or what current ARR is.)*
- **Competitive landscape.** Google (Med-PaLM), Microsoft/Nuance, Amazon Health, and well-funded startups (Abridge, Nabla, etc.) are all investing heavily in healthcare AI, though most focus on clinician-facing tools rather than patient-facing agents.
- **Customer concentration risk.** With 50+ partners, concentration may not be extreme, but the depth of deployment at each partner is unclear.

## Recent Milestones (2026)

- **Jan 2026:** Acquired Grove AI; appointed Dr. Ahad Wahid as President of Life Sciences; launched Life Sciences Executive Advisory Council.
- **Jan 2026:** Strategic collaboration with BCG/BCG X for biopharma and medtech deployment.
- **Mar 2026:** Named to Forbes America's Best Startup Employers 2026.
- **Mar 2026:** Featured at NVIDIA GTC 2026 as a key agentic AI healthcare partner.

---

## Sources

- [Hippocratic AI Series C Announcement](https://hippocraticai.com/hippocratic-ai-announces-series-c-funding-126-million/)
- [Fierce Healthcare: Series C Coverage](https://www.fiercehealthcare.com/ai-and-machine-learning/hippocratic-ai-lands-126m-series-c-expand-patient-facing-ai-agents-fuel-ma)
- [SiliconANGLE: Valuation to $3.5B](https://siliconangle.com/2025/11/03/hippocratic-ais-valuation-soars-3-5b-raising-126m-new-funding/)
- [GlobeNewsWire: $53M Series A](https://www.globenewswire.com/news-release/2024/03/18/2848237/0/en/Hippocratic-AI-Raises-53-Million-Series-A-at-a-500-Million-Valuation.html)
- [GlobeNewsWire: $50M Seed Round](https://www.globenewswire.com/en/news-release/2023/05/16/2670039/0/en/Hippocratic-AI-Launches-With-50-Million-Seed-Round-Co-Led-by-General-Catalyst-and-Andreessen-Horowitz-to-Build-Safety-Focused-Large-Language-Model-for-Healthcare.html)
- [Fierce Healthcare: Series B $141M](https://www.fiercehealthcare.com/ai-and-machine-learning/hippocratic-ai-banks-141m-series-b-hits-unicorn-status-it-rolls-out-ai)
- [Munjal Shah Bio](https://munjalshah.com/about-munjal-shah/)
- [Hippocratic AI Team Page](https://hippocraticai.com/team/)
- [NVIDIA Case Study: Hippocratic AI](https://www.nvidia.com/en-us/case-studies/hippocratic-ai/)
- [Polaris Architecture Paper (arXiv)](https://arxiv.org/html/2403.13313v1)
- [Hippocratic AI App Store Launch](https://www.businesswire.com/news/home/20250109618459/en/Hippocratic-AI-Launches-AI-Agent-App-Store-for-Healthcare)
- [UHS Partnership Announcement](https://uhs.com/news/universal-health-services-launches-hippocratic-ais-generative-ai-healthcare-agents-to-assist-with-post-discharge-patient-engagement/)
- [KPMG Collaboration](https://kpmg.com/xx/en/media/press-releases/2025/07/kpmg-and-hippocratic-ai-announce-collaboration-to-transform-healthcare.html)
- [BCG Strategic Collaboration](https://www.bcg.com/news/8january2026-strategic-collaboration-agentic-ai-across-biopharma-medtech)
- [Grove AI Acquisition](https://www.businesswire.com/news/home/20260112959357/en/Hippocratic-AI-Consolidates-Life-Sciences-Leadership-with-Acquisition-of-Grove-AI-and-Key-Executive-Appointments)
- [Forbes Best Startup Employers 2026](https://www.businesswire.com/news/home/20260303030987/en/Hippocratic-AI-Included-on-Forbes-Americas-Best-Startup-Employers-2026)
- [Contrary Research: Business Breakdown](https://research.contrary.com/company/hippocratic-ai)
- [Sacra: Valuation & Funding](https://sacra.com/c/hippocratic-ai/)
