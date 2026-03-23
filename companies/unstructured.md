---
company: Unstructured (Unstructured Technologies, Inc.)
website: https://unstructured.io
founded: July
headquarters: Rocklin, California (Sacramento metro area)
sector: AI Infrastructure / Data ETL & Preprocessing
stage: Series B
total_funding: ~$65M
latest_round: Series B ($40M, March 2024)
employees_est: ~84-150 (as of late 2025)
revenue_est: ~$7.7M (estimated, unconfirmed)
founders:
  - name: "Brian S. Raymond"
    role: "Founder & CEO"
    background: "Former CIA officer; founded Primer AI before starting Unstructured in 2022"
    origin: "American"
founder_ceo: Brian S. Raymond
status: Private
last_updated: 2026-03-20
confidence: high
website_verified: true
crunchbase: https://www.crunchbase.com/organization/unstructured
crunchbase_verified: true
total_raised_m: 65
funding_rounds:
  - stage: "Seed"
    date: "2023"
    amount_m: 5
    lead_investors: ["New Enterprise Associates"]
    source: "https://www.crunchbase.com/organization/unstructured"
  - stage: "Series A"
    date: "2023"
    amount_m: 20
    lead_investors: ["Menlo Ventures"]
    source: "https://www.crunchbase.com/organization/unstructured"
  - stage: "Series B"
    date: "2024-03"
    amount_m: 40
    lead_investors: ["Menlo Ventures"]
    source: "https://www.crunchbase.com/organization/unstructured"
---

# Unstructured

## One-Liner

Unstructured builds the data preprocessing and ETL layer that converts messy enterprise documents (PDFs, HTML, DOCX, slides, images, etc.) into clean, structured, AI-ready data for LLMs and RAG pipelines.

## Founding Story & Origin

Brian Raymond and his founding engineering team had spent years in the NLP space encountering the same recurring problem: unstructured data was everywhere but unusable for machine learning. In July 2022, they founded Unstructured and released an open-source toolkit in September 2022 to clean and preprocess text data for NLP tasks like named entity recognition and relation extraction.

Weeks later, ChatGPT launched and transformed the landscape. Suddenly, thousands of developers wanted to "chat with their data," and Unstructured's library was perfectly positioned. The team pivoted focus from traditional NLP workflows to integrations with the emerging LLM stack -- vector databases (Weaviate, Pinecone), orchestration frameworks (LangChain), and RAG architectures. This timing proved decisive.

Source: [How We Got Started - Unstructured Blog](https://unstructured.io/blog/how-we-got-started)

## Founder & Leadership

### Brian S. Raymond -- Founder & CEO

Raymond has an unusually diverse background spanning intelligence, policy, finance, and AI:

- **CIA Intelligence Officer** (2009-2014)
- **White House National Security Council** -- Director for Iraq, advising on foreign policy related to Iraq, ISIL, and the Middle East (2014-2015)
- **MBA, Tuck School of Business at Dartmouth** (2015-2017)
- **Harris Williams & Co.** -- Investment Banker (2016-2018)
- **Primer.ai** -- VP, Global Public Sector (2018-2022), an NLP/AI company focused on intelligence analysis
- **BA & MA in Political Science, UC Davis**

His intelligence community and defense background is directly relevant to Unstructured's growing government business and likely informed the company's early focus on document intelligence.

Sources: [The Org](https://theorg.com/org/unstructured-technologies-inc/org-chart/brian-s-raymond), [Madrona Featured Leader](https://www.madrona.com/featuredleader/unstructured/)

### Other Known Executives
- **Drew Messersmith** -- VP of Commercial Sales & Partnerships
- **James Reid** -- Head of Operations

## Funding History

| Round | Date | Amount | Lead Investor | Notable Participants |
|-------|------|--------|---------------|---------------------|
| Seed + Series A (combined announcement) | July 2023 | $25M | Madrona (Series A), Bain Capital Ventures (Seed) | M12 Ventures, Mango Capital, MongoDB Ventures, Shield Capital. Angels: Harrison Chase (LangChain), Bob van Luijt (Weaviate), Josh Lefkowitz (Flashpoint) |
| Series B | March 2024 | $40M | Menlo Ventures | Databricks Ventures, IBM Ventures, NVentures (NVIDIA), Vivek Ranadive (Sacramento Kings), Chet Kapoor (Datastax CEO), Allison Pickens (New Normal Fund), plus existing investors |

**Total raised: ~$65M.** Valuation not publicly disclosed for either round.

Board members include Tim Tully (Menlo Ventures), Karan Mehandru (Madrona), and Enrique Salem (Bain Capital Ventures).

Sources: [BusinessWire - Series B](https://www.businesswire.com/news/home/20240314620374/en/Unstructured-Raises-$40M-Series-B-From-Menlo-Ventures-Databricks-Ventures-IBM-Ventures-and-NVIDIA-to-Make-Enterprise-Data-LLM-ready), [BusinessWire - Seed/A](https://www.businesswire.com/news/home/20230719773647/en/Unstructured-Secures-%2425-Million-in-Seed-and-Series-A-Funding-to-Enable-Enterprises-to-Use-LLMs-With-their-Data), [Menlo Ventures](https://menlovc.com/perspective/backing-the-stack-why-menlo-invested-in-unstructured/)

## Business Model

**Open-core / usage-based SaaS + enterprise contracts + government contracts.**

- **Open-source library** (`unstructured` on PyPI): Free. Provides document parsing, partitioning, chunking across 65+ file types. Serves as the top-of-funnel and community flywheel.
- **Unstructured Platform (SaaS)**: Pay-as-you-go usage-based pricing for managed ETL pipelines. Includes 30+ source/destination connectors, VLM-based partitioning, enrichment via LLMs (GPT-4o, Claude), and orchestration.
- **Enterprise tier**: Custom pricing with SLAs, dedicated support, advanced security, and on-prem/VPC deployment options.
- **Government/Defense**: FedRAMP High and IL-5 authorized deployments; direct contracts with federal agencies.

Source: [Unstructured Pricing](https://unstructured.io/pricing), [Unstructured Enterprise](https://unstructured.io/enterprise)

## Product & Technology

Unstructured's core capability is converting raw, messy documents into clean structured data that LLMs can consume. The pipeline:

1. **Ingest** -- 30+ connectors (S3, Azure Blob, Google Drive, SharePoint, Dropbox, databases, etc.)
2. **Partition** -- Extract text, tables, images from 65+ file types using a combination of traditional parsers and vision-language models (VLMs)
3. **Transform & Enrich** -- Chunking strategies, metadata extraction, summarization, entity extraction via LLMs
4. **Embed** -- Generate vector embeddings
5. **Load** -- Output to vector databases (Pinecone, Weaviate, Chroma, etc.), data lakes, or any destination

The key differentiator is handling the "dirty work" -- scanned PDFs, PowerPoint slides with floating text boxes, complex HTML, images with embedded text -- the edge cases that break naive parsers.

## Traction & Customers

- **Open-source adoption**: 6M+ PyPI downloads, 12,000+ dependent codebases, 45,000+ organizations using the library
- **Enterprise**: More than one-third of the Fortune 500 reportedly use Unstructured (per company claims; independently unverified)
- **Government/Defense**: Open-source powers NIPRGPT, CamoGPT, and other military/national security tools
- **Key partnerships**:
  - **IBM** -- OEM partnership integrating with watsonx.data (announced October 2025)
  - **Palantir** -- Joined FedStart program (August 2025) to accelerate FedRAMP/IL-5 compliance
  - **Databricks** -- Strategic investor and integration partner
  - **NVIDIA** -- Strategic investor (NVentures)

Sources: [Unstructured + IBM](https://unstructured.io/blog/unstructured-ibm-watsonx-data-a-new-oem-partnership-powering-the-future-of-enterprise-ai), [Palantir FedStart](https://www.businesswire.com/news/home/20250808482862/en/Unstructured.io-Joins-Palantir-FedStart-Program-to-Accelerate-Federal-Adoption-of-AI-Ready-Data-Solutions-Through-FedRAMP-High-and-IL-5-Authorizations)

## Government & Defense Milestones

- **FedRAMP High Authorization** (December 2025): One of very few AI infrastructure companies authorized at the High baseline, enabling work with the most sensitive unclassified federal data.
- **IL-5 Authority to Operate** (February 2026): Cleared for Department of Defense workloads involving Controlled Unclassified Information.
- **$1M DAF DTO Contract** (January 2026): Awarded by the Department of the Air Force Digital Transformation Office to build a vendor-agnostic data foundation for GenAI at the tactical edge.

Sources: [FedRAMP announcement](https://www.businesswire.com/news/home/20251212677557/en/Unstructured-Secures-FedRAMP-High-Authorization-to-Deliver-AI-Ready-Data-to-Federal-Agencies-and-Partners), [DAF contract](https://www.businesswire.com/news/home/20260116254624/en/Unstructured-Awarded-1-Million-DAF-DTO-Contract-to-Deliver-AI-Data-Layer-for-Scalable-Cost-Controlled-GenAI-at-the-Tactical-Edge), [IL-5 ATO](https://www.businesswire.com/news/home/20260204238090/en/Unstructured-Achieves-IL5-Authority-to-Operate)

## Competitive Landscape

Direct competitors in the unstructured data ETL / document processing space:

- **Reducto** -- AI-native document parsing
- **LlamaIndex** -- Overlaps on data ingestion/indexing for LLMs (more of a framework)
- **LangChain document loaders** -- Basic but widely used
- **Upstage** -- Document AI
- **Deasy Labs** -- Data preprocessing for AI

Broader competition from legacy ETL tools (Fivetran, dbt) that are adding AI capabilities, and from cloud providers building native document intelligence (Azure AI Document Intelligence, AWS Textract, Google Document AI). However, these tend to focus on structured extraction rather than full RAG-pipeline-ready preprocessing.

## What Makes Them Interesting

1. **Timing and positioning**: Launched an open-source document processing library weeks before ChatGPT, then rode the LLM wave perfectly. They occupy a critical but unglamorous layer of the AI stack -- the "plumbing" that everyone needs but nobody wants to build.

2. **Open-source moat**: 45,000+ organizations and deep integrations with LangChain, Weaviate, Databricks, and others create significant switching costs and network effects. The open-source library is a de facto standard for document ingestion in LLM workflows.

3. **Strategic investor alignment**: Databricks, IBM, and NVIDIA are not just financial investors -- they are distribution channels. The IBM OEM deal embeds Unstructured inside watsonx.data, giving it enterprise reach that a startup could not achieve alone.

4. **Government wedge**: Raymond's CIA/NSC background is rare in the startup world and gives Unstructured credibility and access in the defense/intelligence community. FedRAMP High + IL-5 authorization is a substantial barrier to entry that most competitors have not cleared. Government AI adoption is accelerating, and Unstructured is well-positioned to capture this market.

5. **The 80% problem**: An estimated 80% of enterprise data is unstructured. Every organization building RAG, fine-tuning LLMs, or deploying AI agents needs a way to ingest and clean this data. Unstructured sits at a chokepoint in the AI data pipeline.

6. **Dual-market strategy**: Simultaneously pursuing commercial enterprise (Fortune 500) and government/defense markets. Few AI infrastructure startups successfully serve both, and the combination provides revenue diversification and resilience.

## Open Questions & Uncertainties

- **Revenue scale**: The ~$7.7M revenue estimate is unverified and sourced from third-party trackers. Actual revenue and growth trajectory are not publicly disclosed.
- **Valuation**: No public valuation data for any round. A Series C or later-stage raise in 2026 would clarify market positioning.
- **Competitive durability**: As LLMs improve at direct document understanding (multimodal models reading PDFs natively), the preprocessing layer could be partially disintermediated. Unstructured's value depends on enterprise needs for structured, auditable, pipeline-grade data workflows remaining strong.
- **Employee count**: Estimates range from ~84 to ~150; exact headcount is unclear.
- **Path to profitability**: Not disclosed. The $65M raised should provide runway, but burn rate is unknown.

## Key Sources

- [Unstructured Official Website](https://unstructured.io/)
- [How We Got Started - Unstructured Blog](https://unstructured.io/blog/how-we-got-started)
- [Series B Announcement - BusinessWire](https://www.businesswire.com/news/home/20240314620374/en/Unstructured-Raises-$40M-Series-B-From-Menlo-Ventures-Databricks-Ventures-IBM-Ventures-and-NVIDIA-to-Make-Enterprise-Data-LLM-ready)
- [Seed/Series A Announcement - BusinessWire](https://www.businesswire.com/news/home/20230719773647/en/Unstructured-Secures-%2425-Million-in-Seed-and-Series-A-Funding-to-Enable-Enterprises-to-Use-LLMs-With-their-Data)
- [Why Menlo Invested in Unstructured - Menlo Ventures](https://menlovc.com/perspective/backing-the-stack-why-menlo-invested-in-unstructured/)
- [Madrona Investment in Unstructured](https://www.madrona.com/unstructured-io/)
- [FedRAMP High Authorization - BusinessWire](https://www.businesswire.com/news/home/20251212677557/en/Unstructured-Secures-FedRAMP-High-Authorization-to-Deliver-AI-Ready-Data-to-Federal-Agencies-and-Partners)
- [DAF DTO Contract - BusinessWire](https://www.businesswire.com/news/home/20260116254624/en/Unstructured-Awarded-1-Million-DAF-DTO-Contract-to-Deliver-AI-Data-Layer-for-Scalable-Cost-Controlled-GenAI-at-the-Tactical-Edge)
- [IL-5 ATO - BusinessWire](https://www.businesswire.com/news/home/20260204238090/en/Unstructured-Achieves-IL5-Authority-to-Operate)
- [Palantir FedStart - BusinessWire](https://www.businesswire.com/news/home/20250808482862/en/Unstructured.io-Joins-Palantir-FedStart-Program-to-Accelerate-Federal-Adoption-of-AI-Ready-Data-Solutions-Through-FedRAMP-High-and-IL-5-Authorizations)
- [IBM OEM Partnership - Unstructured Blog](https://unstructured.io/blog/unstructured-ibm-watsonx-data-a-new-oem-partnership-powering-the-future-of-enterprise-ai)
- [TechCrunch - Series A Coverage](https://techcrunch.com/2023/07/19/unstructured-which-offers-tools-to-prep-enterprise-data-for-llms-raises-25m/)
- [SiliconANGLE - Series B Coverage](https://siliconangle.com/2024/03/14/ai-focused-big-data-startup-unstructured-raises-40m-make-data-llm-ready/)
- [Dynamic Business - Company Profile](https://dynamicbusiness.com/ai-tools/unstructured-data-preprocessing-leader-in-ai-transformation.html)
