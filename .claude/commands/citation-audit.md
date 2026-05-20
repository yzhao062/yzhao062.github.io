---
description: Run citation-affiliation audit across OpenAlex and Dimensions
argument-hint: "[--source openalex|dimensions|both] [--limit N] [--max-citing-pages-dimensions K] [--out PATH]"
---

Read and follow the skill definition. Look for it at `skills/citation-audit/SKILL.md` first, then `.agent-config/repo/skills/citation-audit/SKILL.md`.

Command arguments from the slash invocation: `$ARGUMENTS`

Treat the arguments as flags for `scripts/citation_affiliation_audit.py`. The skill owns the operational contract (default source, credential check, timing warnings, post-run summary, error surfacing).