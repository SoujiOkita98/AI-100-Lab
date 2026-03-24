---
name: Weights & Biases (W&B)
founded: 2017
headquarters: San Francisco, CA
website: https://wandb.ai
sector: AI Infrastructure / MLOps / Developer Tools
one_liner: ML experiment tracking and model management platform, acquired by CoreWeave for $1.7B in 2025.
status: 'Acquired by CoreWeave (Nasdaq: CRWV) - acquisition completed May 5, 2025'
founders:
- name: Lukas Biewald
  role: Co-founder & CEO
  background: Born 1981 in Boston, MA. Attended Cambridge Rindge and Latin School. Earned both BS and MS in Computer Science
    from Stanford University. Worked at Yahoo as an engineer on machine translations and led the Search Relevance Team for
    Yahoo Japan. Joined Powerset as Senior Scientist (acquired by Microsoft in 2008). Co-founded CrowdFlower (later renamed
    Figure Eight), a human-in-the-loop ML data labeling platform, which was acquired by Appen in 2019 for ~$300M. Had a stint
    at OpenAI where he observed firsthand the poor state of ML experiment tooling, inspiring W&B. Inc Magazine Top 30 Entrepreneurs
    Under 30 (2010).
  origin: American
- name: Chris Van Pelt
  role: Co-founder & CISO
  background: Co-founded CrowdFlower/Figure Eight with Biewald, spending nearly a decade building it. Transitioned to Weights
    & Biases in 2017 as co-founder. Currently serves as Chief Information Security Officer (CISO). Inc Magazine Top 30 Entrepreneurs
    Under 30 (2010, alongside Biewald).
  origin: American
- name: Shawn Lewis
  role: Co-founder & CTO
  background: Studied at Virginia Tech (2002-2006). Worked as Software Engineer at the Naval Research Laboratory (2004-2006),
    then as Senior Software Engineer at Google (2006-2010). Founded Beep Networks (2012-2017). Described as a Y Combinator
    alum. Known for building an OpenAI o1-based AI programming agent that achieved state-of-the-art results on SWE-Bench-Verified
    (64.6% resolution rate).
  origin: American
employee_count: ~300-310 (as of early 2026)
acquisition_price: ~$1.7B (reported; not officially disclosed)
funding_rounds:
- stage: Series A
  date: 2018-05-31
  amount_m: 5.0
  valuation_m: null
  lead_investors:
  - Trinity Ventures
  - Bloomberg Beta
  source: https://techcrunch.com/2018/05/31/weights-biases-raises-5m-to-build-development-tools-for-machine-learning/
  notes: First institutional round. Trinity Ventures GP Daniel Scholnick joined the board.
- stage: Series B1
  date: 2019-05-30
  amount_m: 15.0
  valuation_m: null
  lead_investors:
  - Coatue Management
  source: https://techcrunch.com/2019/05/30/machine-learning-startup-weights-biases-raises-15m/
  notes: Sometimes grouped with the 2021 Series B as a single series.
- stage: Series B2
  date: 2021-02-01
  amount_m: 45.0
  valuation_m: null
  lead_investors:
  - Insight Partners
  source: https://techcrunch.com/2021/02/01/weights-and-biases-series-b/
  notes: 'Continued support from Coatue, Trinity Ventures, and Bloomberg Beta. Total raised to date reached ~$65M.

    '
- stage: Series C
  date: 2021-10-13
  amount_m: 135.0
  valuation_m: 1000.0
  lead_investors:
  - Felicis Ventures
  - BOND
  source: https://techcrunch.com/2021/10/13/weights-biases-raises-new-capital-as-developer-tools-remain-a-venture-focus-ml-matures/
  notes: 'Insight Partners and Coatue also participated. Brought total raised to ~$200M. Over 100,000 ML practitioners using
    the platform at time of raise.

    '
- stage: Corporate Round
  date: 2022-05-17
  amount_m: null
  valuation_m: null
  lead_investors:
  - Undisclosed
  source: https://www.crunchbase.com/funding_round/weights-biases-corporate-round--852ba88f
  notes: Limited public information available on this round.
- stage: Venture Round (sometimes called Series C extension)
  date: 2023-08-09
  amount_m: 50.0
  valuation_m: 1250.0
  lead_investors:
  - Daniel Gross
  - Nat Friedman
  source: https://techcrunch.com/2023/08/09/weights-biases-who-counts-openai-as-a-customer-lands-50m/
  notes: 'Sapphire Ventures participated as a new investor. Existing investors Coatue, Insight Partners, Felicis, BOND, and
    Bloomberg Beta also participated. User base had grown from 100K to 700K+ since Series C. W&B Prompts (LLMOps tool) announced
    alongside the round.

    '
- stage: Acquisition by CoreWeave
  date: 2025-03-04 (announced) / 2025-05-05 (completed)
  amount_m: 1700.0
  valuation_m: 1700.0
  lead_investors:
  - CoreWeave
  source: https://techcrunch.com/2025/03/04/coreweave-acquires-ai-developer-platform-weights-biases/
  notes: Evercore and Morgan Stanley advised CoreWeave. Qatalyst Partners advised W&B. Davis Polk & Wardwell (CoreWeave legal);
    Orrick, Herrington & Sutcliffe (W&B legal).
linkedin: https://www.linkedin.com/company/wandb/
linkedin_verified: true
total_raised_m: 250.0
latest_valuation_m: 1250.0
---

# Weights & Biases (W&B)

## Overview

Weights & Biases is a San Francisco-based AI developer platform that provides experiment tracking, model management, and MLOps tooling for machine learning practitioners. Founded in 2017 by Lukas Biewald, Chris Van Pelt, and Shawn Lewis -- all veterans of the ML tooling space -- W&B became the de facto standard for ML experiment tracking across both academic research labs and production AI teams. The company was acquired by CoreWeave in 2025 for a reported $1.7 billion.

The founding insight came directly from Biewald's experience at OpenAI: the tooling available for tracking ML experiments, visualizing training runs, and collaborating on model development was woefully inadequate. W&B set out to build "GitHub for machine learning" -- a system of record for the entire ML development lifecycle.

## Origin Story

All three founders had deep prior experience in ML infrastructure. Biewald and Van Pelt spent nearly a decade building CrowdFlower (later Figure Eight), a pioneering data labeling platform. Lewis came from Google engineering and had founded his own startup (Beep Networks). The trio recognized that while data labeling (their previous domain) was well-served, the experiment tracking and model development workflow was still shockingly manual -- researchers were tracking hyperparameters in spreadsheets and losing track of which model checkpoint corresponded to which configuration.

W&B launched with a simple but powerful value proposition: add a few lines of code to your training script, and every experiment is automatically logged, versioned, and visualized in a collaborative dashboard.

## Business Model

W&B operates a **freemium SaaS** model:

- **Free Tier:** Personal accounts with unlimited experiments on the cloud-hosted platform. This drove massive bottom-up adoption in the research community.
- **Teams Tier:** $50/user/month (billed annually) for cloud-hosted team collaboration, up to 10 seats.
- **Enterprise Tier:** Custom pricing for large organizations. Supports both cloud-hosted and on-premises / private cloud deployment. Designed for organizations with strict data governance requirements who need W&B running inside their own infrastructure.

### Core Product Suite

| Product | Description |
|---------|-------------|
| **W&B Experiments** | Core experiment tracking -- log metrics, hyperparameters, model outputs, system resource usage |
| **W&B Sweeps** | Automated hyperparameter optimization |
| **W&B Artifacts** | Dataset and model versioning |
| **W&B Tables** | Interactive data visualization and exploration |
| **W&B Reports** | Collaborative, Jupyter-like documents for sharing results |
| **W&B Models** | Model registry and lifecycle management |
| **W&B Launch** | Job scheduling and infrastructure management for training runs |
| **W&B Weave** | LLM application development and evaluation framework (newer product) |
| **W&B Prompts** | LLMOps tooling for prompt engineering and chain debugging (launched 2023) |

### Revenue Estimates

| Year | Estimated Revenue | Source |
|------|------------------|--------|
| 2023 | ~$10.8M | [Latka](https://getlatka.com/companies/weights-biases) |
| 2024 | ~$13.6M | [Latka](https://getlatka.com/companies/weights-biases) |

**Note:** These revenue figures seem low relative to the valuation and customer base, suggesting either significant undercounting by third-party estimators, or that W&B's valuation was driven more by strategic value and growth trajectory than current revenue. The company does not publicly disclose financials. Post-acquisition by CoreWeave, revenue is no longer reported independently.

## Key Customers

W&B serves over 1,400 enterprise organizations and claims 700,000+ individual users (as of mid-2023).

**AI Labs & Research:**
- OpenAI (one of the most prominent customers)
- Meta AI
- NVIDIA
- Cohere
- AstraZeneca (AI for drug discovery)

**Enterprises:**
- Toyota
- Volkswagen
- Square (Block)
- Snowflake
- Canva
- Samsung

**Research Institutions:**
- Broadly adopted across top ML research labs globally, with significant penetration in academic settings due to the free tier.

## What Makes Weights & Biases Interesting

1. **Developer-first adoption flywheel:** W&B achieved extraordinary bottom-up adoption by offering a genuinely useful free tier and requiring only 3-5 lines of code to integrate. ML researchers adopted it personally, brought it to new labs and companies, and eventually championed enterprise purchases. This mirrors the playbooks of GitHub, Slack, and Datadog.

2. **System of record for ML:** W&B positioned itself as the "single pane of glass" for ML development. Once a team's entire experiment history lives in W&B, switching costs become very high. Every model checkpoint, every hyperparameter sweep, every training curve is stored there -- creating deep lock-in.

3. **Timing the deep learning wave:** Founded in 2017, W&B rode the explosive growth in deep learning experimentation. As models grew from millions to billions of parameters, the need for systematic experiment tracking became critical rather than optional.

4. **Expansion into LLMOps:** With the rise of LLMs in 2023-2024, W&B expanded beyond traditional ML experiment tracking into prompt engineering, LLM evaluation (Weave), and production monitoring -- broadening the addressable market significantly.

5. **Strategic acquisition by CoreWeave:** The $1.7B acquisition by CoreWeave (a GPU cloud infrastructure provider) represents a vertical integration play -- combining compute infrastructure with the developer workflow layer. CoreWeave gains a software moat and direct relationship with ML developers; W&B gains distribution and deep integration with GPU infrastructure. This mirrors the logic of cloud providers bundling developer tools with infrastructure.

6. **Founder credibility:** The founding team's prior experience building CrowdFlower/Figure Eight (a successful ML tools exit) gave them unusually deep domain knowledge and credibility in the ML community. Biewald's time at OpenAI provided direct insight into the pain points of frontier AI development.

7. **Massive integration ecosystem:** W&B integrates with 19,000+ ML libraries and frameworks, including PyTorch, TensorFlow, Hugging Face, LangChain, and all major cloud ML platforms (SageMaker, Azure ML, Vertex AI). This broad compatibility makes it the "neutral" experiment tracker in a fragmented ecosystem.

## Competitive Landscape

| Competitor | Differentiation |
|-----------|----------------|
| **MLflow** (Databricks) | Open-source; tightly integrated with Databricks. W&B offers superior UX and visualization. |
| **Neptune.ai** | Similar SaaS model but smaller scale and less community adoption. |
| **Comet ML** | Direct competitor; W&B has stronger market position and larger user base. |
| **TensorBoard** (Google) | Free and open-source but limited collaboration features; W&B often used alongside it. |
| **Hugging Face** | Overlapping in model registry/sharing; complementary more than competitive. |
| **Databricks MLflow** | Strong in enterprise data teams; W&B stronger with pure ML/DL practitioners. |

## Risks and Open Questions

- **Revenue-to-valuation disconnect:** Third-party revenue estimates (~$13.6M in 2024) seem very low relative to the $1.7B acquisition price, implying CoreWeave paid a large strategic premium. Whether W&B can generate meaningful revenue relative to the acquisition cost is an open question.
- **Post-acquisition independence:** As a CoreWeave subsidiary, W&B's ability to remain a neutral, multi-cloud developer tool is uncertain. Customers running on AWS or Azure may be wary of a tool owned by a competing cloud/GPU provider.
- **Open-source competition:** MLflow continues to gain ground as an open-source alternative, especially within the Databricks ecosystem. The "good enough" open-source option is a persistent threat to paid developer tools.
- **LLMOps market maturity:** The expansion into LLM tooling (Weave, Prompts) puts W&B in competition with a crowded field of LLM evaluation and observability startups (LangSmith, Braintrust, etc.).

## Timeline

| Date | Event |
|------|-------|
| 2017 | Founded by Lukas Biewald, Chris Van Pelt, and Shawn Lewis |
| 2018-05 | Series A ($5M; Trinity Ventures, Bloomberg Beta) |
| 2019-05 | Series B1 ($15M; Coatue) |
| 2021-02 | Series B2 ($45M; Insight Partners) |
| 2021-10 | Series C ($135M; Felicis, BOND); $1B valuation; unicorn status |
| 2023-08 | Venture Round ($50M; Daniel Gross, Nat Friedman); $1.25B valuation; W&B Prompts launched |
| 2023-2024 | Expansion into LLMOps with Weave and Prompts; NVIDIA integrations |
| 2025-03 | CoreWeave announces acquisition of W&B for ~$1.7B |
| 2025-05 | Acquisition completed; W&B becomes a CoreWeave subsidiary |

## Sources

- [TechCrunch: W&B raises $5M Series A (2018)](https://techcrunch.com/2018/05/31/weights-biases-raises-5m-to-build-development-tools-for-machine-learning/)
- [TechCrunch: W&B raises $15M (2019)](https://techcrunch.com/2019/05/30/machine-learning-startup-weights-biases-raises-15m/)
- [TechCrunch: W&B raises $45M Series B (2021)](https://techcrunch.com/2021/02/01/weights-and-biases-series-b/)
- [TechCrunch: W&B raises $135M Series C (2021)](https://techcrunch.com/2021/10/13/weights-biases-raises-new-capital-as-developer-tools-remain-a-venture-focus-ml-matures/)
- [TechCrunch: W&B lands $50M (2023)](https://techcrunch.com/2023/08/09/weights-biases-who-counts-openai-as-a-customer-lands-50m/)
- [TechCrunch: CoreWeave acquires W&B (2025)](https://techcrunch.com/2025/03/04/coreweave-acquires-ai-developer-platform-weights-biases/)
- [CoreWeave: Acquisition completion press release](https://www.coreweave.com/blog/coreweave-completes-acquisition-of-weights-biases)
- [PR Newswire: Series C announcement](https://www.prnewswire.com/news-releases/weights--biases-raises-its-series-c-at-a-billion-dollar-valuation-301399022.html)
- [W&B: $50M round press release](https://wandb.ai/site/press-release/weights-biases-raises-50-million-round-led-by-daniel-gross-and-nat-friedman-announces-wb-prompts/)
- [Insight Partners: Lukas Biewald profile](https://www.insightpartners.com/ideas/weights-and-biases-ceo-lukas-biewald-on-building-an-ai-developer-powerhouse/)
- [Contrary Research: W&B Business Breakdown](https://research.contrary.com/company/weights--biases)
- [Latka: W&B revenue estimates](https://getlatka.com/companies/weights-biases)
- [Wikipedia: Lukas Biewald](https://en.wikipedia.org/wiki/Lukas_Biewald)
- [Tracxn: W&B funding profile](https://tracxn.com/d/companies/weights-biases/__uVC3y5h56PSBeov63SBmKNjSxWpMaR4hyT-qaotxi5Q/funding-and-investors)
