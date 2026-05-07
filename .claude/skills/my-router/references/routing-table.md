# Routing Table — Quick Reference

## Shipped Skills

| Skill | Triggers on | What it does |
|---|---|---|
| `implement-review` | staged changes + review request | Structured review loop with a reviewer agent (e.g., Codex); content-aware lenses for code, paper, proposal, or general |
| `my-router` | any task (this skill) | Detects context and dispatches to the right skill |
| `ci-mockup-figure` | "mockup", "HTML figure", "dashboard mockup", "timeline figure", "Gantt", "TikZ figure", "arrow routing" | Build HTML mockups of systems, dashboards, and timelines, then capture as space-efficient PNG/PDF figures; use TikZ or skia-canvas for abstract diagrams needing arrow routing |
| `readme-polish` | "polish README", "modernize README", "README audit", "README rewrite", "README badges", "README hero image" | Audit a GitHub README and rewrite using modern 2025-2026 patterns (centered header, badges, hero image, GitHub alert callouts, emoji feature bullets, collapsibles, Mermaid diagrams) |

The shipped routing table covers the four skills above. Extend it in your fork (or in consuming projects) with rows for your own skills.

## Extension Template

Copy this section and extend it with your own skills. When a user's prompt matches keywords or files, the router will dispatch to the corresponding skill.

### Keyword-based routing

| Keywords in prompt | Skill | Source |
|---|---|---|
| "review staged", "review changes", "review the diff" | `implement-review` | shipped |
| "mockup", "HTML figure", "HTML mockup", "interactive figure", "dashboard mockup", "Gantt", "screenshotable figure", "capture mode", "skia-canvas", "TikZ figure", "arrow routing" | `ci-mockup-figure` | shipped |
| "polish README", "modernize README", "README audit", "README rewrite", "README badges", "README hero image", "GitHub README patterns" | `readme-polish` | shipped |
| `<your-keywords>` | `<your-skill-name>` | `skills/` (local) or shared |

### File-type routing

If prompt keywords are ambiguous, inspect the files being worked on:

| Files present | Likely context | Default skill |
|---|---|---|
| Staged git changes | Review needed | `implement-review` |
| HTML mockup files for systems, dashboards, or timelines | Figure source | `ci-mockup-figure` |
| Top-level `README.md` flagged for audit or rewrite | Public-facing README | `readme-polish` |
| `<your-file-type>` | `<your-context>` | `<your-skill>` |

### Directory-hint routing

Some projects declare their type via directory naming:

| Directory pattern | Likely context | Default skill |
|---|---|---|
| `<your-directory-pattern>` (e.g., `proposals/`, `papers/`) | `<your-context>` | `<your-skill>` |

## Lens Selection for implement-review

When the router dispatches to `implement-review`, it also selects a review lens. The lens is content-type-aware:

| Context | Lens | Criteria source |
|---|---|---|
| `.py`, `.js`, `.ts`, `.go`, `.rs`, code files | Code | Google eng-practices, Microsoft Engineering Fundamentals |
| `.tex`/`.bib` in paper directory | Paper | NeurIPS, ICLR, ICML, ACL review guidelines |
| `.tex`/`.bib`/`.md` in proposal directory | Proposal | NSF Merit Review or NIH Simplified Peer Review (ask user which agency) |
| Mixed or unclear | General | Completeness, correctness, consistency, clarity |

See `implement-review/references/review-lenses.md` for full lens definitions.

## Local-first Rule

If a project has a more specific local skill (e.g., a project-local variant under `skills/` that overrides a shared skill), prefer the local version. Local skills are customized for the project context and should win over generic shared copies.
