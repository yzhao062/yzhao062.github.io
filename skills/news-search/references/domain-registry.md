# Domain Registry

Seed domains by source class. Phase A queries fan out to seeded domains in addition to the open dragnet, never instead of it. The registry is a recall floor, not a filter.

The registry is grown from each round's confirmed hits (see "Post-Round Harvest" in `SKILL.md`). Once a quarter, run a registry-disabled pass to surface outlet classes the registry has not seen yet.

## Class to outlet_class Field Value

The leftmost column gives the value Phase A writes to the `outlet_class` field of each candidate (see `references/candidate-schema.md`).

## Government / Policy PDFs (`gov-pdf`)

Highest priority for Tier 0 evidence. PDFs hosted at these domains are routinely missed by general web search; use Dimension 8 directly.

| Domain | Notes |
|---|---|
| dod.gov | DoD CDAO Generative AI RAI Toolkit lists PyOD and TrustLLM. |
| nist.gov | NIST AI RMF, AI 600-series. NIST AI 100-2e2025 cites TrustLLM. |
| nvlpubs.nist.gov | NIST special publications PDF host. |
| congress.gov | Bills, committee reports, hearings. |
| senate.gov | Senate committee report PDFs (HSGAC TrustLLM citation). |
| house.gov | House committee report PDFs. |
| crsreports.congress.gov | Congressional Research Service. |
| gao.gov | GAO accountability reports. |
| whitehouse.gov | Executive orders, OMB memos, OSTP reports. |
| federalregister.gov | RFIs, rules. |
| nsf.gov | NSF announcements, dear colleague letters, program solicitations, awards (path /awardsearch). |
| energy.gov | Department of Energy publications front-end. |
| osti.gov | DOE / national lab technical reports. |

## EU and International Government (`eu-gov`, `intl-gov`)

`eu-gov`:

| Domain | Notes |
|---|---|
| europa.eu | EU AI Act, EU AI Office. |
| ec.europa.eu | European Commission policy documents. |
| enisa.europa.eu | ENISA cybersecurity reports. |

`intl-gov`:

| Domain | Notes |
|---|---|
| oecd.ai | OECD AI Policy Observatory. |
| oecd.org | OECD reports. |
| internationalaisafetyreport.org | International AI Safety Report (cites TrustLLM). |
| gov.uk | UK government AI papers. |
| aisi.gov.uk | UK AI Safety Institute. |
| canada.ca | Canadian federal AI documents. |
| imda.gov.sg | Singapore IMDA Model AI Governance Framework. |

## EU Research Projects (`eu-research-project`)

EU Horizon and Framework Programme deliverables are PDFs hosted on project sites or aggregators. They cite open-source tools by name (PyOD, TODS) in toolkit descriptions. Discovered this round via SEDIMARK D3.1 p.18.

| Domain | Notes |
|---|---|
| cordis.europa.eu | EU research project metadata, deliverable links. |
| zenodo.org | Open-access repository for EU project deliverables. |
| sedimark.eu | SEDIMARK project (cites PyOD in D3.1 p.18). |
| swforum.eu | EU software-engineering project consortium pages. |

## Patents (`patent`)

Patents citing tool names appear via Google Patents and WIPO. Discovered this round via Actimize patent US20230267468A1 citing PyOD.

| Domain | Notes |
|---|---|
| patents.google.com | Google Patents full-text search and citation links. |
| patentscope.wipo.int | WIPO global patent database. |
| uspto.gov | USPTO patent search and PAIR. |

## China Tech Media (`china-tech-media`)

Editorial Chinese-language coverage of arXiv preprints. Distinct from machine-translated aggregators (which go in `ai-aggregator`). Discovered this round via Sina / 机器之心Pro DoxBench feature.

| Domain | Notes |
|---|---|
| sina.com.cn | Sina news (hosts 机器之心Pro and other tech media). |
| jiqizhixin.com | 机器之心 (Synced China). Editorial. |
| 36kr.com | 36氪 startup and tech media. |
| infoq.cn | InfoQ China. |
| paperweekly.site | PaperWeekly (curated paper highlights). |
| csdn.net | CSDN developer community. |
| zhihu.com | Zhihu Q&A platform; tool tutorials. |
| leiphone.com | 雷锋网 (Lei Feng Net). |

## Security Research Blogs (`security-blog`)

Vendor and independent security research blogs that publish original analyses naming tools or papers. Distinct from generic security press (which goes in `tier1-security-press`) and AI-generated security catalogs (which go in `ai-aggregator`).

| Domain | Notes |
|---|---|
| huntress.com | Huntress security research. |
| snyk.io | Snyk vulnerability research. |
| hiddenlayer.com | HiddenLayer ML security. |
| promptfoo.dev | Promptfoo prompt-injection research. |
| raxelabs.com | RAXE Labs RADAR. |
| protectai.com | Protect AI ML security research. |
| paloaltonetworks.com | Unit 42 threat research. |

## AI-Generated and Aggregator Sites (`ai-aggregator`)

Sites that auto-generate or auto-aggregate content about arXiv papers. Hard cap at Tier 3 by Phase B. See `references/disclaimer-patterns.md` for detection patterns.

| Domain | Notes |
|---|---|
| papers.cool | Cool Papers (auto-aggregated arXiv summaries). |
| chatpaper.com | ChatPaper (LLM-summarized papers). |
| goatstack.ai | GoatStack newsletter (auto-curated). |
| alphaxiv.org | alphaXiv (community + auto layer). |
| sectools.tw | SecTools.tw (本文由 AI 產生 disclaimer). |
| paperdigest.org | PaperDigest. |

## Tier 1 Press (`tier1-tech-press`, `tier1-security-press`, `tier1-business-press`)

The existing `outlet-registry.md` covers these in full. Cross-reference: that file lists all Tier 1 domains by category; this file gives Phase A a per-class outlet_class tag for the candidate record.

## Foundation Model Companies (`foundation-model`)

System cards and safety reports cite benchmarks like TrustLLM directly. Tier 0 if cited by name.

| Domain | Notes |
|---|---|
| openai.com | OpenAI system cards, preparedness framework. |
| anthropic.com | Anthropic model cards, RSP, safety reports. |
| deepmind.google | Google DeepMind technical reports. |
| ai.meta.com | Meta AI Llama documentation. |
| mistral.ai | Mistral model documentation. |
| x.ai | xAI Grok system cards. |
| cohere.com | Cohere model cards. |

## Adding New Entries

When a confirmed Phase B hit comes from a domain not in the registry:

1. Decide its class. If no class fits, create one (lowercase-hyphenated name).
2. Append a row under that class with a short note that anchors the round when it was added.
3. Commit the registry change with the audit. Future Phase A runs will seed queries against the new domain by default.

This is the post-round harvest step. Without it the registry freezes; with it, recall improves monotonically across rounds.
