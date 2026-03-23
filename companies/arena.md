---
name: Arena
former_names:
- Chatbot Arena
- LMArena
- LMSYS Chatbot Arena
domain: AI Model Evaluation
founded: '2023'
incorporated: 2025
headquarters: San Francisco Bay Area, CA (originated from UC Berkeley)
website: https://arena.ai
headcount: 11-50 (estimated, early 2026)
founders:
- name: Anastasios Nikolas Angelopoulos
  role: CEO
  origin: Greek-American
- name: Wei-Lin Chiang
  role: CTO
  origin: Taiwanese-American
- name: Ion Stoica
  role: Co-founder & Advisor
  origin: Romanian-American
funding:
  total_raised: $250M
  latest_round: Series A
  latest_round_date: 2026-01-06
  latest_valuation: $1.7B (post-money)
  rounds:
  - stage: Seed
    date: 2025-05
    amount: $100M
    valuation: $600M (post-money)
    lead_investors:
    - Andreessen Horowitz (a16z)
    - UC Investments
    other_investors:
    - Lightspeed Venture Partners
    - Felicis Ventures
    - Kleiner Perkins
  - stage: Series A
    date: 2026-01
    amount: $150M
    valuation: $1.7B (post-money)
    lead_investors:
    - Felicis
    - UC Investments
    other_investors:
    - Andreessen Horowitz
    - The House Fund
    - LDVP
    - Kleiner Perkins
    - Lightspeed Venture Partners
    - Laude Ventures
status: Unicorn
tags:
- AI evaluation
- LLM benchmarking
- crowdsourced evaluation
- model leaderboards
- enterprise AI
last_updated: 2026-03-20
one_liner: Arena (formerly LMArena, originally Chatbot Arena) is a community-powered AI model evaluation platform
website_verified: true
crunchbase: https://www.crunchbase.com/organization/arena
crunchbase_verified: true
total_funding: 250
---

# Arena

## Overview

Arena (formerly LMArena, originally Chatbot Arena) is a community-powered AI model evaluation platform. It is best known for its crowdsourced leaderboard in which users compare outputs from two anonymous AI models side-by-side and vote on which response is better. The results feed an Elo-style ranking system that has become one of the most widely cited benchmarks in the AI industry. The company rebranded from LMArena to Arena on January 28, 2026.

## Origin Story

Arena began in 2023 as an academic side project at UC Berkeley. Anastasios Angelopoulos and Wei-Lin Chiang, both PhD students in EECS, built "Chatbot Arena" under the LMSYS (Large Model Systems Organization) research group, which was closely associated with Professor Ion Stoica's SkyLab. The premise was simple: let users test two anonymous chatbots, compare their answers, and vote for the better one. The project rapidly gained traction among AI researchers and practitioners, becoming the de facto community benchmark for LLM quality.

In May 2025, the team spun the project out of Berkeley into a commercial venture under the name LMArena, raising a $100M seed round at a $600M valuation. By January 2026 -- less than eight months later -- the company closed a $150M Series A at $1.7B, achieving unicorn status.

## Founders & Key People

### Anastasios Nikolas Angelopoulos -- CEO
- PhD in EECS, UC Berkeley
- Research focus: trustworthy AI systems, black-box decision-making, medical machine learning
- Former student researcher at Google DeepMind
- Brings the statistical rigor and reliability focus to the platform

### Wei-Lin Chiang -- CTO
- PhD in EECS, UC Berkeley (Stoica's SkyLab)
- Research focus: distributed systems and deep learning frameworks
- Prior research stints at Google Research, Amazon, and Microsoft
- Built the core technical infrastructure of Chatbot Arena

### Ion Stoica -- Co-founder & Advisor
- Professor of Computer Science, UC Berkeley
- Serial entrepreneur: co-founded Databricks (valued at $43B+), Anyscale, and Conviva
- Stoica's involvement lends significant credibility and investor access; his track record of spinning Berkeley research into massive companies (Databricks from Apache Spark) is a pattern Arena directly mirrors

The broader team draws from Google, DeepMind, Discord, Vercel, Berkeley, and Stanford.

## Business Model

Arena operates a **freemium / evaluation-as-a-service** model:

1. **Free public platform**: The consumer-facing website (arena.ai) lets anyone compare AI models anonymously. This drives community engagement and generates the massive dataset that powers the leaderboards. As of early 2026, the platform has 5M+ monthly users across 150 countries, generating 60M+ conversations per month.

2. **Commercial AI Evaluations service** (launched September 2025): Enterprises, AI model labs, and developers pay Arena to run custom evaluations using its community. Use cases include pre-release model testing, regression detection, and domain-specific benchmarking (coding, law, medicine, creative tasks, etc.).

3. **Revenue**: The company reported ~$30M annualized consumption rate (their term for ARR) as of December 2025, less than four months after launching the commercial product.

The flywheel is clear: free users generate evaluation data, which makes the leaderboard authoritative, which attracts AI labs as paying customers, which funds more infrastructure and community growth.

## Platform Scale & Capabilities

- 5M+ monthly active users (as of January 2026)
- 150+ countries
- 60M+ conversations per month
- Evaluation domains: coding, textual reasoning, professional domains (law, medicine), search and citation, creative tasks (image and video generation), and more
- Elo-based ranking methodology derived from millions of pairwise human preference votes

## What Makes Arena Interesting

**1. Academic credibility turned into commercial power.** Arena is a rare example of an open research project becoming a $1.7B company in under three years. The Berkeley pedigree, the Ion Stoica playbook (echoing the Spark-to-Databricks arc), and genuine community adoption give it a defensibility that purely commercial benchmarking companies would struggle to replicate.

**2. Network effects in evaluation.** The more users who vote, the more statistically robust the rankings become. The more robust the rankings, the more AI labs feel compelled to participate (and pay). This creates a self-reinforcing loop that is difficult to disrupt.

**3. Speed of commercialization.** From $0 to ~$30M ARR in under four months of commercial launch is exceptional. The company tripled its valuation (from $600M to $1.7B) in roughly seven months.

**4. Positioning as "the S&P of AI."** Arena is effectively building a ratings agency for AI models -- a trusted, third-party arbiter of quality. If this positioning holds, it becomes critical infrastructure for the AI industry, similar to how credit rating agencies became essential to financial markets.

## Risks & Controversies

**Conflict of interest.** Arena's most significant structural challenge is that it is funded by the same companies it ranks. OpenAI, Google, and Anthropic are all strategic investors or customers. While the company argues that taking money from all major players creates "structural neutrality" (no single backer can exert undue influence), critics note the inherent tension. A joint study by researchers at MIT, Stanford, and Cohere alleged that Arena allows certain companies to privately test multiple model variants before selecting the best performer for the public leaderboard -- for example, Meta reportedly tested 27 variants of Llama 4, and Google tested 10 variants of Gemini/Gemma. This practice could give well-resourced labs an unfair advantage in public rankings.

**Sustainability of crowdsourced quality.** As the platform scales, maintaining the quality and representativeness of human evaluations is non-trivial. Voter demographics, prompt sophistication, and gaming incentives all introduce potential biases.

**Market risk.** If major AI labs develop or adopt alternative evaluation standards, or if regulatory bodies mandate specific benchmarking frameworks, Arena's moat could narrow.

## Funding History Summary

| Round    | Date     | Amount | Valuation | Lead Investors                  |
|----------|----------|--------|-----------|---------------------------------|
| Seed     | May 2025 | $100M  | $600M     | a16z, UC Investments            |
| Series A | Jan 2026 | $150M  | $1.7B     | Felicis, UC Investments         |
| **Total**|          | **$250M** |        |                                 |

## Sources

- [LMArena lands $1.7B valuation four months after launching its product -- TechCrunch](https://techcrunch.com/2026/01/06/lmarena-lands-1-7b-valuation-four-months-after-launching-its-product/)
- [LMArena Raises $150 Million to Build the World's Most Trusted AI Evaluation Platform -- PR Newswire](https://www.prnewswire.com/news-releases/lmarena-raises-150-million-to-build-the-worlds-most-trusted-ai-evaluation-platform-302653012.html)
- [AI evaluation startup LMArena raises $150M at $1.7B valuation -- SiliconANGLE](https://siliconangle.com/2026/01/06/ai-evaluation-startup-lmarena-raises-150m-1-7b-valuation/)
- [How two Berkeley roommates built a $1.7B startup -- Founded](https://www.founded.com/lmarena-arena-ai-ranking-tool-startup-founders/)
- [LMArena Business Breakdown & Founding Story -- Contrary Research](https://research.contrary.com/company/lmarena)
- [Beyond Leaderboards: LMArena's Mission to Make AI Reliable -- a16z](https://a16z.com/podcast/beyond-leaderboards-lmarenas-mission-to-make-ai-reliable/)
- [Arena's LLM Leaderboard Raises Eyebrows: Funded by Those It Ranks -- TechBuzz](https://www.techbuzz.ai/articles/arena-s-llm-leaderboard-raises-eyebrows-funded-by-those-it-ranks)
- [LM Arena Under Fire: Allegations of Benchmark Bias -- OpenTools](https://opentools.ai/news/lm-arena-under-fire-allegations-of-benchmark-bias-stir-ai-industry)
- [As companies pour billions into AI, a ranking system by UC Berkeley students has all eyes on it -- Berkeley News](https://news.berkeley.edu/2025/05/06/as-companies-pour-billions-into-ai-a-ranking-system-by-uc-berkeley-students-has-all-eyes-on-it/)
- [LM Arena, the organization behind popular AI leaderboards, lands $100M -- TechCrunch](https://techcrunch.com/2025/05/21/lm-arena-the-organization-behind-popular-ai-leaderboards-lands-100m/)
- [Arena (AI platform) -- Wikipedia](https://en.wikipedia.org/wiki/Arena_(AI_platform))
- [Fueling the World's Most Trusted AI Evaluation Platform -- Arena Blog](https://arena.ai/blog/series-a/)
