# FORTIS Lab Website and CV

This repository hosts the [FORTIS Lab website](https://viterbi-web.usc.edu/~yzhao010/) and the LaTeX source for Yue Zhao's academic CV.

## How to Update Your Info on the Lab Page

Member sections are data-driven. Update JSON files instead of editing `lab.html` directly.

### Files to edit

- `data/lab-current-phd.json` for current Ph.D. students
- `data/lab-members.json` for current Master/Undergrad members and all past members

### Workflow

1. **Fork and clone** this repository.
2. **Add your photo** under `images/others/` (square, `.webp` preferred).
3. **Update the correct JSON file** (do **not** manually edit `lab.html`).
4. **Preview locally** by opening `lab.html` in a browser.
5. **Keep commits clean** (no `.DS_Store`, `.idea/*.xml`, etc.).
6. **Open a PR**.

### JSON Examples

#### Current Ph.D. student (`data/lab-current-phd.json`)

```json
{
  "name": "Jane Doe",
  "profile_url": "https://example.com",
  "image": "images/others/jane_doe.webp",
  "alt": "Jane Doe",
  "year_info": "1st year, Joined Fortis in Aug 2026",
  "research": "LLM Safety, Robustness",
  "awards": ["Example Fellowship"],
  "email": "janedoe@usc.edu",
  "co_advised_by": {
    "name": "Prof. X",
    "url": "https://example.com/prof-x"
  }
}
```

`awards` and `co_advised_by` are optional.

#### Current Master/Undergrad (`data/lab-members.json`)

```json
{
  "group": "current",
  "name": "Jane Doe",
  "profile_url": "https://example.com",
  "image": "images/others/jane_doe.webp",
  "alt": "Jane Doe",
  "research": "Multimodal / Generative AI",
  "status_text": "Master Student",
  "email": "janedoe@usc.edu",
  "awards": ["Example Fellowship"],
  "publications": ["Paper title, Venue 2026"]
}
```

`awards` and `publications` are optional.

#### Past member (`data/lab-members.json`)

```json
{
  "group": "past",
  "name": "Jane Doe",
  "profile_url": "https://example.com",
  "status_text": "Master Student → Now Ph.D. Student at XYZ",
  "email": "janedoe@xyz.edu",
  "publications": ["Paper title, Venue 2026"]
}
```

#### Moving someone from current to past

Change `"group": "current"` to `"group": "past"` in `data/lab-members.json`. Optionally update `status_text` and `email`. That single field change moves the member automatically.

---

## Maintainer Reference

The rest of this document is for the repo maintainer (Yue Zhao).

### Repository Structure

```
├── index.html, lab.html, publications.html, ...   Website HTML pages
├── data/                           Shared data (single source of truth)
│   ├── publications.json           Publication list (website)
│   ├── open-source.json            Open-source projects (website + CV)
│   ├── lab-current-phd.json        Current PhD students
│   └── lab-members.json            Other lab members (current + past)
├── cv/                             LaTeX CV sources
│   ├── cv-full.tex                 Full academic CV
│   ├── cv-1page.tex                1-page condensed CV
│   ├── open-source.tex             Auto-generated from data/open-source.json
│   └── res.cls                     Document class
├── files/                          PDFs, bib file, bio
│   ├── ZHAO_YUE_CV.pdf             Compiled CV (auto-updated by CI)
│   └── yue-zhao.bib                BibTeX file
├── scripts/
│   ├── generate_cv_open_source.py  Generates cv/open-source.tex from JSON
│   ├── sync_open_source_metadata.mjs  Refreshes stars/dates from GitHub API
│   ├── fetch_paper_metadata.py     Batch-fetches abstracts from arXiv/S2
│   └── ci_check_site.py            CI site validation
├── skills/                         Agent skills (shared by Claude Code + Codex)
│   ├── dual-update/                Update content on both website and CV
│   └── condense-cv/                Generate short CV variants
├── .github/workflows/              CI/CD pipelines
├── css/, assets/, images/          Website static assets
└── includes/                       Shared HTML fragments (navbar, footer, sidebar)
```

### How Content Flows

#### Open-source projects (fully automated)

```
GitHub API
  → scripts/sync_open_source_metadata.mjs   (refreshes stars, dates)
  → data/open-source.json                   (single source of truth)
  → scripts/generate_cv_open_source.py      (generates LaTeX)
  → cv/open-source.tex                      (included by cv-full.tex)
  → files/ZHAO_YUE_CV.pdf                   (compiled by CI)
```

CI runs this chain daily. To run locally:

```bash
node scripts/sync_open_source_metadata.mjs
python scripts/generate_cv_open_source.py
```

#### Publications abstracts

`data/publications.json` contains abstracts for all 100 papers. When adding new papers (via `/dual-update` or manually), include the abstract in the JSON entry. If abstracts are missing in bulk, run:

```bash
python scripts/fetch_paper_metadata.py
```

This fetches abstracts from arXiv (for papers with arXiv URLs) and Semantic Scholar (fallback), with title validation to prevent wrong-paper matches.

#### Other shared content (manual, skill-assisted)

Use the `/dual-update` agent skill to update both website and CV in one pass.

| Content | Website | CV |
|---|---|---|
| Publications | `data/publications.json` | `cv/cv-full.tex` |
| Awards and Grants | `index.html` | `cv/cv-full.tex` |
| Services | `services.html` | `cv/cv-full.tex` |
| Teaching | `teaching.html` | `cv/cv-full.tex` |
| PhD Students | `data/lab-current-phd.json` | `cv/cv-full.tex` |
| Open-source | `data/open-source.json` | `cv/open-source.tex` (auto-generated) |

### Building the CV Locally

```bash
cd cv
latexmk -pdf -interaction=nonstopmode cv-full.tex
latexmk -pdf -interaction=nonstopmode cv-1page.tex
```

### CI Workflows

| Workflow | Trigger | What it does |
|---|---|---|
| `build-cv.yml` | Daily + push to `cv/` or `data/open-source.json` | Syncs GitHub metadata, regenerates tex, compiles CV PDF, commits |
| `site-checks.yml` | Push / PR | Runs `scripts/ci_check_site.py` |
| `lighthouse.yml` | Push / PR | Lighthouse performance audit |
| `sync-profile-assets-to-template.yml` | Push to `files/yue-zhao.bib` or `files/ZHAO_YUE_CV.pdf` | Syncs bib and CV PDF to USC proposal template repo |
