> If this file was fetched into `.agent-config/AGENTS.md`, treat the bootstrap block below as copy-paste setup for project repos, not as runtime instructions to execute again.
> In the fetched copy, read and follow the shared rules starting at `## User Profile`.

## Bootstrap — Shared Config and Skills

This file is the shared agent configuration hosted at `https://github.com/yzhao062/agent-config`.
Project repos should include the following bootstrap block in their own `AGENTS.md` so that agents automatically pull the latest shared defaults and skills before starting any task.

### Bootstrap block for project repos

Copy the block below into the top of each project repo's `AGENTS.md`. Project-local rules written after the bootstrap block override anything fetched here.

````
## Shared Agent Config (auto-fetched)

Before starting any task, fetch the shared agent configuration and skills. Use the block for your shell.

PowerShell (Windows):

```powershell
New-Item -ItemType Directory -Force -Path .agent-config, .claude, .claude/commands | Out-Null
Invoke-WebRequest -UseBasicParsing -Uri https://raw.githubusercontent.com/yzhao062/agent-config/main/bootstrap/bootstrap.ps1 -OutFile .agent-config/bootstrap.ps1
& .\.agent-config\bootstrap.ps1
```

Bash (macOS/Linux):

```bash
mkdir -p .agent-config .claude/commands
curl -sfL https://raw.githubusercontent.com/yzhao062/agent-config/main/bootstrap/bootstrap.sh -o .agent-config/bootstrap.sh
bash .agent-config/bootstrap.sh
```

This bootstrap flow refreshes the consuming repo's root `AGENTS.md` to match the shared copy. If a project later needs repo-local overrides, put them in `AGENTS.local.md`.

Read and follow the rules in `.agent-config/AGENTS.md` as baseline defaults. Any rule defined later in this file overrides the shared default.
When a skill is invoked, read its SKILL.md from `.agent-config/repo/skills/<skill-name>/SKILL.md`.
If a local `skills/<skill-name>/SKILL.md` exists in the project repo, the local copy takes precedence.
Copying `.agent-config/repo/.claude/commands/*.md` only overwrites command files with the same name as the shared repo and does not delete unrelated project-local commands.
Merge shared Claude project defaults (e.g., `effortLevel`, `permissions`) from `.agent-config/repo/.claude/settings.json` into the project `.claude/settings.json`. Shared keys are updated on every bootstrap run; project-only keys are preserved. Merge requires Python; if unavailable the existing file is left untouched.
Add `.agent-config/` to the project's `.gitignore` so fetched files are not committed.
````

### What gets shared

| Content | Source | How fetched |
|---------|--------|-------------|
| User profile, writing defaults, formatting rules, environment notes | `AGENTS.md` (this file) | `curl` raw file |
| Shared skills (`dual-pass-workflow`, etc.) | `skills/` directory (committed only) | sparse `git clone` |
| Claude pointer commands for shared skills | `.claude/commands/` | sparse `git clone` plus non-destructive copy into the project `.claude/commands/` |
| Claude project defaults (`effortLevel`, `permissions`, etc.) | `.claude/settings.json` | sparse `git clone` plus key-level merge into the project `.claude/settings.json` on every run |

### Override rules

- If `AGENTS.local.md` exists in the project root, read and follow it after `AGENTS.md`. Rules in `AGENTS.local.md` override the shared defaults.
- Project-local `AGENTS.md` rules always win over shared defaults.
- Project-local `skills/<name>/SKILL.md` always wins over the shared copy of the same skill.
- Shared keys in `.claude/settings.json` are updated on every bootstrap run. Project-only keys are preserved. To override a shared key locally, use `.claude/settings.local.json`.
- If a shared skill does not exist locally, the agent should use the fetched copy from `.agent-config/repo/skills/`.

---

<!-- Everything above this line is bootstrap setup instructions. -->
<!-- Everything below this line contains the shared rules that agents should read and follow. -->

## User Profile

- These are user-level defaults that can be reused across projects unless a local repo rule or task-specific instruction is stricter.
- The user is a computer scientist and professor working in machine learning and AI.
- Common tasks include research papers, funding proposals, scientific writing, and administrative writing.

## Writing Defaults

- Use scientifically accessible language.
- Do not oversimplify unless the user asks for simplification.
- Keep meaningful technical detail.
- Keep factual accuracy and clarity high in scientific contexts.
- Use consistent terms. If an abbreviation is defined once, do not define it again later.
- If citing papers, verify that they exist.
- When paper citations are requested, provide BibTeX entries that can be copied into a `.bib` file.
- Provide code only when necessary. Confirm that the code is correct and can run as written.
- For NSF or other federal proposal work, do not introduce DEI-related terms unless the solicitation explicitly requires them.
- For non-federal proposals or calls that explicitly request DEI framing or terminology, follow the call requirements instead of applying a blanket ban.
- Avoid the following words and close variants unless the user explicitly asks for them: `encompass`, `burgeoning`, `pivotal`, `realm`, `keen`, `adept`, `endeavor`, `uphold`, `imperative`, `profound`, `ponder`, `cultivate`, `hone`, `delve`, `embrace`, `pave`, `embark`, `monumental`, `scrutinize`, `vast`, `versatile`, `paramount`, `foster`, `necessitates`, `provenance`, `multifaceted`, `nuance`, `obliterate`, `articulate`, `acquire`, `underpin`, `underscore`, `harmonize`, `garner`, `undermine`, `gauge`, `facet`, `bolster`, `groundbreaking`, `game-changing`, `reimagine`, `turnkey`, `intricate`, `trailblazing`, `unprecedented`.

## Formatting Defaults

- Preserve the original format when the input is in LaTeX, Markdown, or reStructuredText.
- Do not convert paragraphs into bullet points unless the user asks for that format.
- Prefer full forms such as `it is` and `he would` rather than contractions.
- `e.g.,` and `i.e.,` are fine when appropriate.
- Do not use Unicode character `U+202F`.
- Avoid heavy dash use.

## Git Safety

- **Never run `git commit` or `git push` without explicit user approval.** Always show the proposed action and ask for confirmation before executing.
- This rule is non-negotiable and applies to all projects that consume this shared config.
- This includes any variant: `git commit -m`, `git commit --amend`, `git push`, `git push --force`, `gh pr create` (which pushes), etc.

## Environment Notes

- Prefer a Miniforge-managed Python interpreter.
- If a `py312` environment or launcher exists, use it first.
- Do not conclude that Python is unavailable just because `python`, `python3`, or `py` fails in `PATH`; those may resolve to shims, store aliases, or the wrong interpreter.
- On Windows, a common Miniforge pattern is `%USERPROFILE%\\miniforge3\\envs\\py312\\python.exe`.
- On macOS or Linux, a common Miniforge pattern is `$HOME/miniforge3/envs/py312/bin/python`.
- If interpreter selection is still unclear, inspect Miniforge environments and local IDE settings before reporting that Python is missing.
- GitHub CLI (`gh`) is used for PR and issue workflows. If `gh` is not found, remind the user to install it (`winget install GitHub.cli` on Windows, `brew install gh` on macOS) and authenticate with `gh auth login`.

## Local Skills Precedence

- If the workspace contains a `skills/` directory, treat repo-local skills as the default source of truth for that project.
- When a task matches a skill name and both a repo-local `skills/<skill-name>/SKILL.md` and an installed global skill exist, prefer the repo-local skill.
- When using a repo-local skill, read `skills/<skill-name>/SKILL.md` and its local `references/`, `scripts/`, and `assets/` before falling back to any globally installed copy.
- Do not modify a globally installed skill when a repo-local skill of the same name exists, unless the user explicitly asks to update the global copy too.
- If a repo-local skill overrides a global skill, state briefly that the local project copy is being used.

## Cross-Tool Skill Sharing

- Skills under `skills/` are shared between coding agents (Codex, Claude Code, and any future agent).
- `skills/<skill-name>/SKILL.md` is the single source of truth for each skill. Agent-specific config files (e.g., `agents/openai.yaml`) are thin wrappers and must not duplicate or override the logic in `SKILL.md`.
- Claude Code accesses these skills via pointer commands in `.claude/commands/`. Each pointer file references the corresponding `SKILL.md` rather than duplicating its content.
- Bootstrap sync should copy only the shared repo's `.claude/commands/*.md` files into the project `.claude/commands/` directory and should not delete unrelated project-local commands.
- When editing a skill, modify `SKILL.md` and its `references/` or `scripts/` directly. Do not create agent-specific forks of the same content.
- If a new skill is added, create both the `skills/<skill-name>/SKILL.md` structure and a matching `.claude/commands/<skill-name>.md` pointer so both agents can use it immediately.
