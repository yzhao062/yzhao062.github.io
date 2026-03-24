# Selection Guide

## Source Map

- Master CV: `cv/cv-full.tex`
- Auto-generated source fragment: `cv/open-source.tex` (from `data/open-source.json`)
- Generator script: `scripts/generate_cv_open_source.py`
- Ignore as source: `cv/*.pdf`, and LaTeX intermediate files

Re-read the current master before editing. Do not rely on stale line numbers or old page counts.

## Default Outputs

- `cv/cv-1page.tex`
- `cv/cv-2page.tex`

Keep the master file unchanged unless the user explicitly asks to refactor the source layout itself.

## Page Budgets

### 1 Page

- Header and contact: at most 15%
- Summary: 10-15%
- Current role or experience snapshot: 15-20%
- Education: around 10%
- Selected publications: 20-25%
- Selected software/projects: 20-25%
- Awards/extra: at most 10%

### 2 Pages

- Header and contact: at most 8%
- Summary: 8-10%
- Experience: 15-20%
- Education: 8-10%
- Awards/funding: 10-15%
- Selected publications: 20-25%
- Selected software/projects: 15-20%
- Optional audience-specific section: at most 10%

## Pruning Order

Drop or compress sections in this order:
1. Full publications, full service, talks, committees, and teaching
2. Older internships and older awards that do not change the story
3. Secondary bullets within experience or summary
4. Formatting density, only after content is already focused

## Audience Presets

### Academia

Keep:
- research summary
- employment
- education
- selected publications
- grants, awards, and advising if strong

Drop first:
- broad software lists unless they support research leadership
- generic service details

### Industry Research / ML

Keep:
- concise research identity
- current role and prior high-signal roles
- open-source systems, libraries, benchmarks, and impact metrics
- selected publications tied to deployed or reusable work

Drop first:
- long student and committee sections
- most talks and teaching

### AI Security / Agent Safety

Keep:
- AI auditing, assurance, safety, and security framing
- agent-audit, Aegis, TrustLLM, and related security papers
- systems evidence over broad historical lists

Drop first:
- anomaly detection items that do not support the target role

### Anomaly Detection / Data Mining

Keep:
- PyOD, ADBench, AD-AGENT, NLP-ADBench, anomaly-detection resources
- anomaly detection papers and benchmark contributions
- data mining venues and reusable libraries

Drop first:
- agent security items unless the role explicitly values them
