# AI-100-Lab

**一个研究级的全球 750+ AI 与机器人初创企业数据库 — 融资轮次、创始人背景、投资者网络及创始人来源分析。**

以研究级标准构建：每项数据可追溯来源，不确定性明确标注，质量优先于完整性。

---

## 数据概览

| 指标 | 数量 |
|------|-----:|
| 企业数量 | 767 |
| 融资轮次 | 1,635 |
| 创始人档案 | 1,737 |
| 2025年种子轮 | 180+ |
| 2026年种子轮 | 30+ |
| 覆盖国家 | 20+ |

## 数据质量

| 字段 | 覆盖率 | 说明 |
|------|:------:|------|
| 公司名称 | 100% | |
| 行业分类 | 98% | 多标签分类体系 |
| 一句话简介 | 97% | 可从叙述正文自动提取 |
| 成立年份 | 100% | |
| 总融资额 | 94% | 统一换算为百万美元 |
| 单轮金额 | 97% | 1,045轮详细数据 |
| 领投方 | 92% | 每轮记录 |
| 创始人档案 | 100% | 姓名、职务、背景、来源 |
| LinkedIn | 100% | 615个经HTTP验证的公司主页链接 |
| 来源链接 | 73% | 可追溯至原始报道 |
| 总部所在地 | 95% | 城市+国家 |
| 官网 | 96% | 经HTTP验证 |
| 最新估值 | 32% | 种子轮/早期通常不公开（市场常态）|
| 营收信号 | 8% | 仅限公开披露的数据 |

---

## 目录结构

```
AI-100-Lab/
  companies/           # 767个Markdown文件 — 每家企业一个
  exports/             # 清洗后的CSV + JSON导出（按需重新生成）
    companies_clean.csv
    rounds_clean.csv
    founders_clean.csv
    companies_clean.json
  schema/              # 数据模式定义、行业分类、字段说明
  scripts/             # 数据管道脚本（解析器、爬虫、导出器）
  logos/               # 企业Logo（已收集部分）
  data/                # 原始数据文件
```

---

## 分类体系

### 行业分类

| 类别 | 代表企业 | 数量 |
|------|---------|-----:|
| **基础模型** | OpenAI、Anthropic、Mistral、DeepSeek、xAI | 30+ |
| **AI基础设施/云** | Baseten、Together AI、Lambda、CoreWeave、Nscale | 25+ |
| **AI芯片/半导体** | Etched、Cerebras、d-Matrix、Groq、Celestial AI | 25+ |
| **AI开发者工具** | Cursor、Augment Code、Windsurf、Cognition AI | 20+ |
| **AI智能体/自动化** | Sierra、/dev/agents、LangChain、Braintrust | 20+ |
| **AI医疗/生物科技** | Hippocratic AI、Abridge、OpenEvidence、Rad AI | 25+ |
| **AI网络安全** | 7AI、Sola Security、Cylake、Tenzai | 15+ |
| **人形机器人** | Figure AI、1X Technologies、Apptronik、宇树科技、智元机器人 | 15+ |
| **AI药物研发** | Xaira、Chai Discovery、英矽智能、晶泰科技 | 12+ |
| **AI语音/音频** | ElevenLabs、Deepgram、Gradium、Wispr AI | 10+ |
| **AI视频/媒体** | Runway、Pika、Luma AI、Synthesia、Fal | 10+ |
| **AI法律** | Harvey AI、Luminance、Paxton、Eudia | 8+ |
| **AI国防/政府科技** | Anduril、Shield AI、Overland AI、NODA AI | 10+ |
| **AI科学研究** | Periodic Labs、CuspAI、Lila Sciences | 8+ |

### 创始人来源分布

| 来源 | 创始人数 |
|------|--------:|
| 美国 | 178 |
| 印度裔美国人 | 42 |
| 以色列 | 41 |
| 华裔美国人 | 35 |
| 中国 | 26 |
| 德国 | 22 |
| 印度 | 21 |
| 法国 | 19 |
| 英国 | 18 |
| 荷兰 | 11 |
| 加拿大 | 8 |
| 瑞典 | 7 |

### 地理分布

| 地区 | 企业数 |
|------|------:|
| 美国加州 | 192 |
| 美国纽约 | 28 |
| 美国其他 | 17 |
| 中国 | 31 |
| 英国 | 27 |
| 以色列 | 15 |
| 法国 | 10 |
| 德国 | 6 |
| 韩国 | 3 |
| 澳大利亚 | 3 |
| 其他 (20+国家) | 52 |

---

## 研究方法

### 数据来源

本数据库通过系统性多来源研究构建，而非依赖单一数据供应商：

| 来源 | 方法 | 捕获内容 |
|------|------|---------|
| **VC机构组合页面** | 浏览器自动化爬取（browser-use CLI）：a16z、Index Ventures、Khosla Ventures、Greylock、General Catalyst、Accel、Felicis、Bessemer、NEA、Thrive | 投资组合企业，包括隐形投资 |
| **TechCrunch汇总文章** | 权威的"$1亿+AI初创"榜单交叉验证 | 重大融资轮次的权威报道 |
| **Crunchbase News** | 免费文章及每周汇总 | 融资公告、估值信息 |
| **StartupHub.ai** | 结构化融资数据 | 2025年AI融资交易 |
| **Y Combinator目录** | W24、S24、W25、S25批次爬取 | 早期AI企业 |
| **SEC EDGAR Form D文件** | 通过FormDs.com获取公开融资文件 | 零媒体曝光的隐形企业 |
| **区域科技媒体** | Sifted（欧洲）、TechNode（中国）、KrASIA（亚洲）、YourStory（印度）等 | 被美国媒体遗漏的国际企业 |
| **每周融资汇总** | PYMNTS、SiliconANGLE、VentureBeat、Crescendo.ai | 未被单独报道的小额交易($3-20M) |
| **企业官网及新闻稿** | 直接核实 | 产品信息、团队简介 |

### 数据质量原则

1. **质量优于完整性** — 空字段好于编造的数据
2. **每项数据可追溯** — 融资金额尽可能链接到原始报道
3. **不确定性明确标注** — 每家企业标注 `confidence: low/medium/high`
4. **模式是指南而非牢笼** — 记录有趣的信息，跳过找不到的
5. **基于姓名的来源推断** — 创始人族裔从姓名+背景+公开信息推断，标注为推断而非确认事实

### 已知局限性

- **种子轮估值数据稀疏** — 大多数企业不公开种子轮估值（35%覆盖率）
- **营收数据稀少** — 仅11%的企业有营收信号（私营企业的现实）
- **偏向英语媒体** — 中日韩企业可能被低估
- **未使用付费数据库** — 无Crunchbase Pro或PitchBook访问权限；SEC EDGAR部分弥补
- **员工人数可能过时** — 仅42%覆盖率，通常来自最近融资公告

---

## 导出文件

分析就绪的导出文件位于 `exports/` 目录：

| 文件 | 行数 | 说明 |
|------|-----:|------|
| `companies_clean.csv` | 767 | 每行一家企业 — 所有标准化字段 |
| `rounds_clean.csv` | 1,635 | 每行一轮融资 — 阶段、日期、金额、估值、投资方 |
| `founders_clean.csv` | 1,737 | 每行一位创始人 — 姓名、职务、背景、来源 |
| `companies_clean.json` | 767 | 嵌套格式 — 企业+创始人+融资轮次合并 |

---

## 查询示例

利用CSV导出文件，您可以回答以下问题：

- **按融资金额排名2025年所有AI种子轮** → 筛选 `rounds_clean.csv` 中 `stage=Seed` 且 `date LIKE '2025%'`，按 `amount_m` 排序
- **哪些VC领投了最多AI轮次？** → 解析 `rounds_clean.csv` 中的 `lead_investors` 列
- **按行业分析创始人来源构成** → 将 `founders_clean.csv` 与 `companies_clean.csv` 通过 `company_slug` 连接
- **华人创立的AI企业及其总融资额** → 筛选创始人 `origin LIKE '%Chinese%'`
- **估值增长最快的企业** → 追踪每家企业各轮的 `valuation_m` 变化

---

## 许可证

本数据库采用 **CC BY 4.0** 许可证开源。数据来源于公开渠道——新闻稿、新闻报道、SEC文件和企业官网。

**如果您使用了本数据集，请注明出处并标注维护者 — 这对我意义重大。**

---

*使用 [Claude Code](https://claude.ai/claude-code)（Anthropic）构建。最后更新：2026年3月。*
