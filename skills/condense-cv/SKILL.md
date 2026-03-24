---
name: condense-cv
description: Create 1-page or 2-page CV variants from a longer master LaTeX CV. Use when the user asks for a short CV, concise CV, one-page CV, two-page CV, resume-style version, or a role-specific application CV derived from `cv/cv-full.tex` or another master CV source.
---

# Condense CV

Read the master source first. In this repo, treat `cv/cv-full.tex` as the master CV and `cv/open-source.tex` as an auto-generated fragment included by the master (generated from `data/open-source.json` by `scripts/generate_cv_open_source.py`). Ignore generated PDFs and LaTeX intermediate files.

Ask for the target page limit and audience if either is missing. Good defaults:
- `1 page` for strict application portals and industry roles
- `2 pages` for research, faculty, and senior technical roles

Prefer creating derived files instead of overwriting the master source. Default output paths:
- `cv/cv-1page.tex`
- `cv/cv-2page.tex`

Add a short header comment to each derived file stating the source file, target page budget, and intended audience.

If both page lengths are requested, derive both from the master source rather than deriving one from the other.

Cut content before tightening formatting. Use this order:
1. Remove entire low-priority sections.
2. Replace exhaustive lists with selected lists.
3. Merge repeated narrative into one-line entries.
4. Tighten spacing or typography only if the document is still slightly over budget.

Use `references/selection-guide.md` for page budgets, pruning order, and audience presets.

Keep these rules:
- Preserve factual accuracy. Do not invent claims, counts, or dates.
- Keep the contact block, current affiliation, and the most relevant research identity.
- Prefer recent, high-signal, role-relevant items over completeness.
- Keep dates, affiliations, named recognitions, and venue names intact.
- Favor selected publications, software, benchmarks, and systems over exhaustive lists.
- Remove teaching, service, student committees, talks, and older internships unless directly relevant.
- The open-source section in cv/open-source.tex is auto-generated from data/open-source.json. For condensed variants, select items inline rather than editing the generated file.

For a `1-page` output:
- Keep contact, a 2-4 line summary, current role, education, and 2-4 strongest evidence sections.
- Limit publications to 2-4 items.
- Limit software/projects to 2-4 items.
- Keep awards or funding only if they materially strengthen the application.
- Prefer dense one-line entries and selected lists.

For a `2-page` output:
- Keep contact, summary, employment, education, selected awards/funding, selected publications, and selected software/systems.
- Limit publications to 4-8 items.
- Limit software/systems to 3-6 items.
- Add service, teaching, advising, or talks only if the audience values them and space allows.

When the audience is specified, bias selection accordingly:
- `academia`: publications, grants, students, invited talks
- `industry research / ML`: systems, libraries, benchmarks, impact metrics, selected papers
- `AI security / agent safety`: agent-audit, Aegis, TrustLLM, agent security and auditing work
- `anomaly detection / data mining`: PyOD, ADBench, AD-AGENT, anomaly detection papers

If a LaTeX toolchain is available, compile and confirm the final page count. If compilation is unavailable, state that the source was prepared but the page count was not verified locally.
