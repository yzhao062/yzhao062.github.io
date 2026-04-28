<!-- Quick start: In Claude Code, read @AGENTS.md to run bootstrap, session checks, and task routing -->

> **Claude Code / Codex / other agents -- determine your context before proceeding:**
>
> **Source repo test:** If `bootstrap/bootstrap.sh`, `bootstrap/bootstrap.ps1`, and `skills/` all exist at the repo root, you are in the `anywhere-agents` source repo (or a fork with the same layout). **Skip the bootstrap block below** and proceed directly to `## Session Start Check`. Do not execute the bootstrap script in the source repo; it would try to bootstrap itself.
>
> **Consumer repo path:** Otherwise, you are in a project that consumes the shared config. **You MUST execute the matching bootstrap block below at the start of every session, before responding to any user request or running session checks.** Use the PowerShell block on Windows and the Bash block on macOS/Linux. Bootstrap is idempotent: run it every session even if `.agent-config/` already exists, so shared config, skills, and settings are refreshed from upstream before any work begins. Do not treat the block below as reference documentation -- it is a required runtime command. After running, report the refresh result in one line (for example, "bootstrap: refreshed AGENTS.md, skills, settings").

## Bootstrap: Shared Config and Skills

This file is the shared agent configuration hosted at `https://github.com/yzhao062/anywhere-agents`.
Project repos should include the following bootstrap block in their own `AGENTS.md` so that agents automatically pull the latest shared defaults and skills before starting any task. Because bootstrap overwrites the consumer's root `AGENTS.md` with this source on every run, the block below ends up serving two roles in consumer repos: it is both the embedded reference for how the setup works and the runtime command the agent executes each session (see the top-of-file note for the source-vs-consumer test that decides which role applies in the current repo).

### Bootstrap block for project repos

Copy the block below into the top of each project repo's `AGENTS.md`. Because bootstrap overwrites `AGENTS.md` on every run, put project-local overrides in `AGENTS.local.md`.

````
## Shared Agent Config (auto-fetched)

Before starting any task, fetch the shared agent configuration and skills. Use the block for your shell.

PowerShell (Windows):

```powershell
New-Item -ItemType Directory -Force -Path .agent-config, .claude, .claude/commands | Out-Null
Invoke-WebRequest -UseBasicParsing -Uri https://raw.githubusercontent.com/yzhao062/anywhere-agents/main/bootstrap/bootstrap.ps1 -OutFile .agent-config/bootstrap.ps1
& .\.agent-config\bootstrap.ps1
```

Bash (macOS/Linux):

```bash
mkdir -p .agent-config .claude/commands
curl -sfL https://raw.githubusercontent.com/yzhao062/anywhere-agents/main/bootstrap/bootstrap.sh -o .agent-config/bootstrap.sh
bash .agent-config/bootstrap.sh
```

This bootstrap flow refreshes the consuming repo's root `AGENTS.md` on every run: by default it composes the shared upstream copy with the `agent-style` rule pack (requires Python 3 + PyYAML; bootstrap attempts a best-effort `pip install --user pyyaml` when missing). When rule-pack composition is disabled (`rule_packs: []` in `agent-config.yaml`) or unavailable (Python or PyYAML absent after the auto-install attempt), the root `AGENTS.md` is written verbatim from the shared upstream copy. If a project later needs repo-local overrides, put them in `AGENTS.local.md`.

Read and follow the rules in `.agent-config/AGENTS.md` as baseline defaults. Any rule in `AGENTS.local.md` overrides the shared default.
When a skill is invoked, read its SKILL.md from `.agent-config/repo/skills/<skill-name>/SKILL.md`.
If a local `skills/<skill-name>/SKILL.md` exists in the project repo, the local copy takes precedence.
Copying `.agent-config/repo/.claude/commands/*.md` only overwrites command files with the same name as the shared repo and does not delete unrelated project-local commands.
Merge shared Claude project defaults (e.g., `permissions`, `attribution`) from `.agent-config/repo/.claude/settings.json` into the project `.claude/settings.json`. Shared keys are updated on every bootstrap run; project-only keys are preserved. Merge requires Python; if unavailable the existing file is left untouched.
Add `.agent-config/` to the project's `.gitignore` so fetched files are not committed.
Bootstrap also sets up user-level config: it copies `scripts/guard.py` to `~/.claude/hooks/` (a PreToolUse hook that guards against destructive commands) and merges `user/settings.json` into `~/.claude/settings.json` (shared permissions, hook wiring, and the `CLAUDE_CODE_EFFORT_LEVEL=max` env entry that sets the default effort level). Remove the user-level section from the bootstrap script if this is not wanted.
````

### What gets shared

| Content | Source | How fetched |
|---------|--------|-------------|
| User profile, writing defaults, formatting rules, environment notes | `AGENTS.md` (this file) | `curl` raw file |
| Per-agent rule files (`CLAUDE.md`, `agents/codex.md`) | Generated from `AGENTS.md` by `scripts/generate_agent_configs.py` | Regenerated locally on every bootstrap; hand-authored files preserved + warned |
| Shared skills (`implement-review`, `my-router`, `ci-mockup-figure`, `readme-polish`) | `skills/` directory (committed only) | sparse `git clone` |
| Claude pointer commands for shared skills | `.claude/commands/` | sparse `git clone` plus non-destructive copy into the project `.claude/commands/` |
| Claude project defaults (`permissions`, `attribution`, etc.) | `.claude/settings.json` | sparse `git clone` plus key-level merge into the project `.claude/settings.json` on every run |
| User-level hooks (`guard.py`, `session_bootstrap.py`) + settings | `scripts/` + `user/settings.json` | Scripts copied to `~/.claude/hooks/`; settings merged into `~/.claude/settings.json` (shared permissions, PreToolUse guard, SessionStart bootstrap hook, `CLAUDE_CODE_EFFORT_LEVEL=max`) |

### Override rules

- If `AGENTS.local.md` exists in the project root, read and follow it after `AGENTS.md`. Rules in `AGENTS.local.md` override the shared defaults.
- Rules in `AGENTS.local.md` always win over shared defaults. Do not edit the root `AGENTS.md` for local overrides, as bootstrap will overwrite it.
- Project-local `skills/<name>/SKILL.md` always wins over the shared copy of the same skill.
- Shared keys in `.claude/settings.json` are updated on every bootstrap run. Project-only keys are preserved. To override a shared key locally, use `.claude/settings.local.json`.
- If a shared skill does not exist locally, the agent should use the fetched copy from `.agent-config/repo/skills/`.

### Configuration Precedence

Three independent configuration layers, each with its own precedence rules. When two rules conflict, the more specific source wins.

**1. Agent rule files (Markdown)** — most specific wins:

| Layer | File | Scope |
|---|---|---|
| 1 | `CLAUDE.local.md` / `agents/codex.local.md` | Per-agent + project-local. Hand-authored; never touched by bootstrap. |
| 2 | `AGENTS.local.md` | Cross-agent + project-local. Hand-authored; never touched by bootstrap. |
| 3 | `CLAUDE.md` / `agents/codex.md` | Per-agent, generated from `AGENTS.md` by `scripts/generate_agent_configs.py`. |
| 4 | `AGENTS.md` | Cross-agent, synced from upstream on every bootstrap. |

The generated `CLAUDE.md` and `agents/codex.md` carry a `GENERATED FILE` header. If a consumer project has a hand-authored `CLAUDE.md` (or `agents/codex.md`) without that header, the generator preserves it and warns loudly — it never silently overrides user work. To adopt upstream rules in that case, rename the hand-authored file to `CLAUDE.local.md` (which still wins via layer 1).

**2. Claude Code settings (`settings.json`)** — follow Claude Code's own precedence: `managed policy` > `command-line arguments` > `.claude/settings.local.json` > `.claude/settings.json` > `~/.claude/settings.json`. Bootstrap only writes to the project-shared and user-level layers, and merges shared keys while preserving project-only keys.

**3. Environment variables** — for effort level specifically: `managed policy > CLAUDE_CODE_EFFORT_LEVEL env var > persisted effortLevel > default`.

---

<!-- Everything above this line is bootstrap setup instructions. -->
<!-- Everything below this line contains the shared rules that agents should read and follow. -->

## Session Start Check

**Mandatory turn-start procedure.** Before generating the first content of any response, apply the branch that matches your runtime.

**In Claude Code:** the flag files are per-project. `<project-root>` is the consumer-repo root: walk up from `cwd` until a directory with `.agent-config/bootstrap.sh` or `.agent-config/bootstrap.ps1` is found. Read `<project-root>/.agent-config/session-event.json` and `<project-root>/.agent-config/banner-emitted.json`.

1. If `session-event.json.ts > banner-emitted.json.ts`, OR `session-event.json` exists but `banner-emitted.json` does not: emit the session start banner as the **literal first content of your response**, then write the event `ts` into `<project-root>/.agent-config/banner-emitted.json`. Only after the banner text may you address the user's request on the same turn.
2. Otherwise (emitted `ts` is already current, or neither file exists): skip the banner this turn.

`session_bootstrap.py` writes `session-event.json` on every SessionStart hook fire (fresh startup, resume, clear, compact), so the banner reappears across all four lifecycle events. Flag files are per-project, so opening multiple Claude Code windows in different consumer repos does not cause cross-session interference.

**In a source repo (`agent-config` or `anywhere-agents`, no `.agent-config/` at the root):** the banner gate in `guard.py` is not active and the flag-file mechanism does not apply. Emit the banner on the first response of the session (turn with no prior assistant turns in context); skip on subsequent turns. Compact / resume / clear cannot be mechanically distinguished here.

**In Codex:** Codex has no `SessionStart` hook equivalent; `session-event.json` is not written during a Codex invocation. Each Codex invocation is a new session. Emit the banner as the literal first content of your response on the turn where there are no prior assistant turns in context (i.e., the first response of the invocation). On subsequent turns in the same invocation, skip. No flag files are involved for Codex.

**Both runtimes:** this procedure overrides any other "skill-first" or "task-first" behavior. Even when the user's first message is a task prompt like "read the project" or "fix this bug," or when a skill such as `superpowers:using-superpowers` would otherwise fire before the response, emit the banner first; the task response or skill output comes after the banner on the same turn. Do not let task pressure, skill invocations, or brevity guidance suppress the banner.

### Format

```
📦 anywhere-agents active
   ├── OS: <platform>
   ├── Claude Code: <version>[ → <latest>] (auto-update: <on|off>) · <model> · effort=<level>
   ├── Codex: <version>[ → <latest>] · <model> · <reasoning> · <tier> · fast_mode=<bool>
   ├── Skills: <N> local (<names>) + <M> shared (<names>)
   ├── Hooks: PreToolUse <guard.py>, SessionStart <session_bootstrap.py>
   └── Session check: all clear
```

If anything is off, replace `all clear` with a semicolon-separated list of concrete issues, each actionable in one short clause (e.g., `⚠ actions/checkout@v4 in .github/workflows/validate.yml:17 — bump to v5; Codex config.toml missing model key`). Keep the whole banner to six lines plus the check line. The skills row may wrap visually when many names are present; do not omit a local or shared bucket just to preserve terminal width.

### How to populate each field

1. **OS** — read from the session environment (`win32`, `darwin`, `linux`). Use this elsewhere to pick platform-specific behavior (terminal review path on Windows, MCP on macOS/Linux, `.ps1` vs `.sh`).
2. **Claude Code** — format: `Claude Code <current>[ → <latest>] (auto-update: <on|off>) · <model> · effort=<level>`. Current version comes from Claude Code's startup header or `claude --version`. Read `~/.claude/hooks/version-cache.json` for `claude_latest`; render ` → <latest>` **only when current differs** from latest. Determine `auto-update: on` when `DISABLE_AUTOUPDATER` is not `1` in the effective env (OS env or `env` block in `~/.claude/settings.json`) AND `~/.claude.json` top-level `autoUpdates` is not explicitly `false` — a missing key counts as `on` because native installs auto-update by default. Only explicit `autoUpdates: false` (which bootstrap heals on the next run) or the disable env var means `off`. User prefers the highest available model at max effort; flag any drift once in the banner, not every turn.
3. **Codex** — format: `Codex <current>[ → <latest>] · <model> · <reasoning> · <tier> · fast_mode=<bool>`. Current version from `codex --version`. Latest from `~/.claude/hooks/version-cache.json` `codex_latest` (render ` → <latest>` only when current differs). Config from `~/.codex/config.toml` (or `%USERPROFILE%\.codex\config.toml` on Windows): `model` · `model_reasoning_effort` · `service_tier` · `[features].fast_mode`. Expected values: `model = "gpt-5.4"` (or latest), `model_reasoning_effort = "xhigh"`, `service_tier = "fast"`, `[features] fast_mode = true`. If the binary is not on PATH, show `Codex: not installed`. If the binary exists but `config.toml` is missing, show version + `not configured` in place of the config summary.
4. **Skills** — list both active sets. Count directories under `skills/` (project-local) and `.agent-config/repo/skills/` (bootstrapped). For the shared count/list, exclude any shared skill whose name also exists under project-local `skills/`, because project-local overrides shared on name conflict. Format: `<N> local (<names>) + <M> shared (<names>)`. Omit either half if empty (e.g., `4 shared (...)` when the consumer has no project-local `skills/`).
5. **Hooks** — check `~/.claude/hooks/` for `guard.py` (PreToolUse) and `session_bootstrap.py` (SessionStart). If one is missing, include it in the Session check line as an issue.
6. **Session check** — scan `.github/workflows/*.yml` for action version pins below the minimums in the GitHub Actions Standards section. Combine with any Codex-config or hook drift detected above. Emit `all clear` only when nothing needs attention.

7. **Pack deployment** — perform this check exactly:

    a. Read user-level config: on Windows `%APPDATA%\anywhere-agents\config.yaml`; on POSIX `$XDG_CONFIG_HOME/anywhere-agents/config.yaml`, default `~/.config/anywhere-agents/config.yaml`. If absent, `user_packs = []`.

    b. Read durable project config: `agent-config.yaml` then merge `agent-config.local.yaml` overrides by name. `AGENT_CONFIG_PACKS` env var is **excluded**. If both files absent, `project_packs = []`.

    c. For each pack `u` in `user_packs`, normalize its identity tuple `(u.name, normalize_pack_source_url(u.source.url), u.source.ref)`. Find any pack `p` in `project_packs` with the same `u.name` (case-sensitive name match). If `project_packs` contains duplicate-named entries (e.g., the same name in both `agent-config.yaml` and `agent-config.local.yaml`), apply local-overrides-tracked: keep only the local entry. Count `u` toward `gap_count` if either: no matching `p` exists, OR `p`'s normalized identity tuple differs from `u`'s.

    d. Read `.agent-config/pack-lock.json` (the project-local lock written by the composer). For each entry in `data.packs`, count it toward `update_count` when **both** `latest_known_head` and `resolved_commit` are non-empty strings AND `latest_known_head != resolved_commit`. The optional `latest_known_head` / `fetched_at` fields land via `pack verify` (which runs `git ls-remote` opportunistically and lock-bracket-merges the result) and via composer fetches at install time. Old locks predating v0.5.2 omit both fields and contribute zero — no migration needed.

    e. Compose the banner contribution from both counts. Each is a half-clause; drop the half whose count is 0; emit `all clear` only when both are 0:

       - `gap_count > 0` → ``⚠ <gap_count> user-level pack(s) not deployed (run `anywhere-agents pack verify --fix`)``
       - `update_count > 0` → ``ℹ <update_count> pack update(s) available (run `anywhere-agents pack verify --fix`)``

       Append the surviving half-clauses to the Session check line, semicolon-separated. The CLI command differs from v0.5.1: v0.5.2 collapses the verify-then-bootstrap dance into `pack verify --fix`, which now invokes the composer subprocess after writing config rows.

## User Profile

- These are user-level defaults that can be reused across projects unless a local repo rule or task-specific instruction is stricter.
- **Customize this section in your fork of `anywhere-agents`** to describe your role, domain, and common task types. Agents read this to tailor their work (e.g., a researcher vs. a backend engineer vs. a data scientist will get different defaults).
- If your fork serves multiple use cases, keep the description general ("developer working on infrastructure and research tooling") rather than overspecifying.

## Agent Roles

- **Claude Code** is the primary workhorse: drafting, implementation, research, and heavy-lifting tasks.
- **Codex** is the gatekeeper: review, feedback, and quality checks on work produced by Claude Code or the user.
- When both agents are available, default to this division of labor unless the user overrides it.

## Task Routing

- Before starting a task, read the router skill to determine which domain skill to use. Look for it in this order: `skills/my-router/SKILL.md` (repo-local), then `.agent-config/repo/skills/my-router/SKILL.md` (bootstrapped from shared config).
- The router inspects prompt keywords, file types, and project structure to dispatch automatically. Do not ask the user which skill to use when the routing table provides a clear match.
- If the `superpowers` plugin is active, the router operates during the execution phase. Superpowers handles the outer workflow (brainstorm, plan, execute, verify); the router handles inner dispatch to the right domain skill.
- If routing is ambiguous (multiple skills could apply), state the detected context and proposed skill, then ask the user to confirm.

<!-- agent:codex -->
## Codex MCP Integration

- Codex is available to Claude Code as an MCP server. Register it once at the user level so it applies to all projects and terminals (including PyCharm):
  ```
  claude mcp add codex -s user -- codex mcp-server -c approval_policy=on-failure
  ```
- This writes to `~/.claude.json` top-level `mcpServers`. A session restart is required after registration for `/mcp` to pick it up.
- **Migrating an existing registration:** If Codex was registered without `-c approval_policy=on-failure`, remove and re-add:
  ```
  claude mcp remove codex -s user
  claude mcp add codex -s user -- codex mcp-server -c approval_policy=on-failure
  ```
  On Windows, adjust the path as shown below.
- **Gotcha:** Do not register under a project scope (e.g., from a specific working directory without `-s user`). That creates a project-scoped entry under `projects["<path>"].mcpServers` in `~/.claude.json`, which does not propagate to other directories.
- Prerequisites: Node.js installed, Codex CLI installed (`npm install -g @openai/codex`), and `OPENAI_API_KEY` set.
- **Recommended Codex defaults (as of April 2026):** Add or update these keys in `~/.codex/config.toml` on macOS/Linux or `%USERPROFILE%\.codex\config.toml` on Windows (create the file if it does not exist) so that both interactive sessions and the MCP server use the recommended default model with fast inference:
  ```toml
  model = "gpt-5.4"
  model_reasoning_effort = "xhigh"
  service_tier = "fast"

  [features]
  fast_mode = true
  ```
  `service_tier = "fast"` selects the fast inference tier (1.5x speed, no quality reduction). For ChatGPT-authenticated users this costs 2x credits; API-key users pay standard API pricing. The `[features].fast_mode` flag gates the feature and defaults to `true`; set it explicitly alongside `service_tier` to persist the default in `config.toml`. Omit both if you prefer lower cost over latency. The MCP server reads the same `config.toml`, so these settings apply to both interactive sessions and MCP. These settings work identically on macOS, Linux, and Windows.
- MCP tools available after registration: `codex` (new prompt) and `codex-reply` (continue an existing session).
- **Windows note:** Claude Code launches MCP servers through bash, not cmd or PowerShell. This means `.cmd` wrappers and PowerShell variables like `$env:APPDATA` do not work. If `codex` is not on `PATH`, use the full path with forward slashes and **no `.cmd` extension** (npm installs a bash-compatible script alongside the `.cmd`):
  ```
  claude mcp add codex -s user -- C:/Users/<you>/AppData/Roaming/npm/codex mcp-server -c approval_policy=on-failure
  ```
  Run `where codex` (cmd) or `Get-Command codex` (PowerShell) to find the actual path.
- **MCP approval policy:** By default the Codex MCP server prompts for approval on every shell command, which surfaces as "MCP server requests your input" dialogs in Claude Code. Pass `-c approval_policy=on-failure` in the registration command (shown above) so commands auto-approve and only prompt on failures. The same key can be set in `config.toml` (`approval_policy = "on-failure"`) for interactive sessions.
- **Bitdefender false positives (Windows):** Bitdefender Advanced Threat Defense may flag Codex and Claude Code shell commands as "Malicious command lines detected." To suppress this, add exceptions in Bitdefender → Protection → Manage Exceptions. For each exception, enable the **Advanced Threat Defense** toggle (not just Antivirus). Recommended exceptions:
  - `C:\Program Files\nodejs\node.exe` (process)
  - `C:\Users\<you>\.local\bin\claude.exe` (process)
  - `C:\Users\<you>\AppData\Roaming\npm\codex` (process)
  - `C:\Users\<you>\AppData\Roaming\npm\codex.cmd` (process)
  - `C:\WINDOWS\System32\WindowsPowerShell\v1.0\powershell.exe` (process, if Codex invokes PowerShell)
- **Windows recommendation: use the terminal path.** On Windows (11 Build 26200+), the MCP path still has rough edges — residual approval prompts and Bitdefender false positives add friction even after the mitigations above. The terminal path (relay reviews via the Codex interactive terminal window) avoids both issues. Prefer the terminal path on Windows; use MCP on macOS/Linux where it works smoothly.
<!-- /agent:codex -->

## Writing Defaults

- Use scientifically accessible language.
- Do not oversimplify unless the user asks for simplification.
- Keep meaningful technical detail.
- Keep factual accuracy and clarity high in scientific contexts.
- Use consistent terms. If an abbreviation is defined once, do not define it again later.
- If citing papers, verify that they exist.
- When paper citations are requested, provide BibTeX entries that can be copied into a `.bib` file.
- Provide code only when necessary. Confirm that the code is correct and can run as written.
- Avoid the following words and close variants unless the user explicitly asks for them (a default AI-tell list; trim or extend in your fork): `encompass`, `burgeoning`, `pivotal`, `realm`, `keen`, `adept`, `endeavor`, `uphold`, `imperative`, `profound`, `ponder`, `cultivate`, `hone`, `delve`, `embrace`, `pave`, `embark`, `monumental`, `scrutinize`, `vast`, `versatile`, `paramount`, `foster`, `necessitates`, `provenance`, `multifaceted`, `nuance`, `obliterate`, `articulate`, `acquire`, `underpin`, `underscore`, `harmonize`, `garner`, `undermine`, `gauge`, `facet`, `bolster`, `groundbreaking`, `game-changing`, `reimagine`, `turnkey`, `intricate`, `trailblazing`, `unprecedented`.

## Formatting Defaults

- Preserve the original format when the input is in LaTeX, Markdown, or reStructuredText.
- Do not convert paragraphs into bullet points unless the user asks for that format.
- Prefer full forms such as `it is` and `he would` rather than contractions.
- `e.g.,` and `i.e.,` are fine when appropriate.
- Do not use Unicode character `U+202F`.
- Avoid heavy dash use. Do not use em dashes (`—`) or en dashes (`–`) as casual sentence punctuation. Prefer commas, semicolons, colons, or parentheses instead. En dashes in numeric ranges (e.g., `1–3`, `2020–2025`), paired names, or citations are fine. Normal hyphenation in compound words and technical terms (e.g., `command-line`, `co-PI`, `zero-shot`) is fine and should not be avoided.
- Break extremely long or complex sentences into shorter, more readable ones. If a sentence has multiple clauses or nested qualifications, split it.
- Vary sentence length and structure. Prefer not to start several consecutive sentences with the same word or phrase. Avoid overusing transition words like "Additionally" or "Furthermore." Not every paragraph needs a tidy summary sentence at the end. Mix short, direct sentences with longer ones to keep the writing natural.

## Git Safety

- **Never run `git commit` or `git push` without explicit user approval.** Always show the proposed action and ask for confirmation before executing.
- This rule is non-negotiable and applies to all projects that consume this shared config.
- This includes any variant: `git commit -m`, `git commit --amend`, `git push`, `git push --force`, `gh pr create` (which pushes), etc.

## Mechanical Enforcement

Bootstrap deploys `scripts/guard.py` to `~/.claude/hooks/guard.py` and wires it as a `PreToolUse` hook in `~/.claude/settings.json`. The hook runs before every tool call and mechanically enforces the following:

| Gate | Tool scope | Trigger | Action |
|---|---|---|---|
| Writing-style | `Write`, `Edit`, `MultiEdit` on `.md` / `.tex` / `.rst` / `.txt` | Outgoing content contains a banned AI-tell word (see Writing Defaults list) | **deny** with hit list |
| Banner emission | Any tool except `Read`, `Grep`, `Glob`, `Skill`, `Task`, `TodoWrite`, `BashOutput`, `WebFetch`, `WebSearch`, `ToolSearch`, `LS`, `NotebookRead`; plus `Write`/`Edit`/`MultiEdit` whose target path exactly equals `<project-root>/.agent-config/banner-emitted.json` after absolute-path normalization and Windows case folding | `<project-root>/.agent-config/session-event.json.ts > <project-root>/.agent-config/banner-emitted.json.ts`. `<project-root>` is found by walking up from `cwd` until `.agent-config/bootstrap.{sh,ps1}` is present. Source repos (no `.agent-config/`) and unrelated directories skip the gate entirely | **deny** with instruction to emit banner + write acknowledgment to the per-project ack file |
| Compound `cd` | `Bash` | Command contains `cd <path> && <cmd>` or `cd <path>; <cmd>` | **deny** with suggestion to use `git -C` or path arguments |
| Destructive git | `Bash` | `git push`, `git commit`, `git merge`, `git rebase`, `git reset --hard`, `git clean`, `git branch -d/-D`, `git tag -d`, `git stash drop/clear` | **ask** (user confirms) |
| Destructive gh | `Bash` | `gh pr create`, `gh pr merge`, `gh pr close`, `gh repo delete` | **ask** (user confirms) |

**Escape hatch:** set env var `AGENT_CONFIG_GATES=off` (or `0`/`disabled`/`false`) via the `env` block in `~/.claude/settings.json` to disable the two new gates (writing-style and banner). The compound-cd / destructive-git / destructive-gh checks remain active regardless, since they guard against muscle-memory mistakes that do not tolerate false positives.

Setting the escape hatch is the right move when a legitimate write has a banned word in *meta-discussion* context (for example, a style-guide document that quotes banned words as examples of what to avoid), or when a prompt-layer failure is blocking legitimate work. Fix the false positive, then remove the override.

## Shell Command Style

- **Avoid compound `cd <path> && <command>` chains.** Claude Code's hardcoded compound-command protection prompts for approval on these even when both commands are individually allowed. Use alternatives that keep each tool call to a single command:
  - For git in another repo: use `git -C <path> <subcommand>` instead of `cd <path> && git <subcommand>`.
  - For non-git commands: pass the target path as an argument (e.g., `ls <path>`, `python <path>/script.py`) or use separate tool calls.
- Examples of read-only invocations that should not require approval: `git status`, `git diff`, `git log`, `git branch` (no flags), `git show`, `git stash list`, `git remote -v`, `git submodule status`, `git ls-files`, `git tag --list`. Filesystem reads (`ls`, `cat`) and benign local operations (`mkdir`) are also fine.
- Examples of invocations that always require explicit approval: `git commit`, `git push`, `git reset`, `git checkout`, `git rebase`, `git merge`, `git branch -d`, `git remote add/remove`, `git tag <name>` (creating/deleting), `git stash drop`.
- Filesystem commands like `cp` and `mv` are fine for scratch and temporary files. Moves or renames that affect git-tracked files should be reviewed before executing.
- **Avoid inline Python with `#` comments in quoted arguments.** Claude Code flags "newline followed by `#` inside a quoted argument" as a path-hiding risk and prompts for approval. Instead, write the code to a `.py` file and run `python <script>.py`.

## GitHub Actions Standards

GitHub is deprecating Node.js 20 actions. Runners begin using Node.js 24 by default on June 2, 2026, and GitHub's public changelog currently says Node.js 20 removal will happen later in fall 2026. Keep workflow action pins at or above the first Node.js 24 major for the GitHub-maintained actions below:

| Action | Minimum version (Node.js 24) | Replaces |
|--------|------------------------------|----------|
| `actions/checkout` | **v5** | v3, v4 |
| `actions/setup-python` | **v6** | v5 |
| `actions/setup-node` | **v5** | v4 |
| `actions/upload-artifact` | **v6** | v4, v5 |
| `actions/download-artifact` | **v7** | v4, v5, v6 |

When the session start check (item 4) detects older versions, list the affected files and suggest the minimum Node.js 24 version from this table. If a repository intentionally wants the latest major instead of the minimum compatible major, flag that as a separate manual upgrade because later majors can include behavior changes. If a workflow pins a SHA instead of a tag (e.g., `actions/checkout@abc123`), flag it for manual review rather than auto-suggesting a tag. For self-hosted runners, also remind the user that these Node.js 24 actions require an Actions Runner version that supports Node.js 24.

## Environment Notes

- Do not conclude that Python is unavailable just because `python`, `python3`, or `py` fails in `PATH`; those may resolve to shims, store aliases, or the wrong interpreter. Inspect common environment managers (Miniforge/Conda, pyenv, uv, venv) before reporting Python as missing.
- If the user's fork sets a preferred Python interpreter path in `AGENTS.local.md`, use that first.
- GitHub CLI (`gh`) is used for PR and issue workflows. If `gh` is not found, remind the user to install it (`winget install GitHub.cli` on Windows, `brew install gh` on macOS, `gh` from the distro package manager on Linux) and authenticate with `gh auth login`.
<!-- agent:claude -->
- **Claude Code installation**: Prefer the **native installer**. Migrate off npm and winget when possible.
  - macOS: `curl -fsSL https://claude.ai/install.sh | sh`
  - Windows (PowerShell, no admin): `irm https://claude.ai/install.ps1 | iex` (requires Git for Windows)
  - To migrate from npm: `npm uninstall -g @anthropic-ai/claude-code` first. From winget: `winget uninstall Anthropic.ClaudeCode` first.
  - Native installs auto-update in the background by default. Use `/config` inside Claude Code to set the release channel (`latest` or `stable`). Run `claude doctor` to inspect updater status, and `claude update` to force an immediate update check.
  - To disable auto-updates, set `DISABLE_AUTOUPDATER=1` in the environment or add `"env": {"DISABLE_AUTOUPDATER": "1"}` to `~/.claude/settings.json`. The env var takes precedence regardless of other flags. **Caveat:** if you migrated from npm or winget, an earlier install may have left `"autoUpdates": false` at the top level of `~/.claude.json`. Observed behavior is that the native updater daemon never spawns when that flag was already false at launch, even with `autoUpdatesProtectedForNative: true`. Bootstrap now heals this by flipping the stale flag to `true` on every run, so the env-var path is the only supported way to opt out.
- **Claude Code effort level**: As of Claude Code v2.1.111, the `/effort` slider exposes five levels: `low`, `medium`, `high`, `xhigh`, `max`. The persisted `effortLevel` key in `settings.json` accepts `low`, `medium`, `high`, and `xhigh` (v2.1.111 added `xhigh` as a valid persisted value). `max` remains session-only: selecting `max` via `/effort` silently does not persist. To get `max` as a persistent default across every project and session, set the env var `CLAUDE_CODE_EFFORT_LEVEL=max` in `~/.claude/settings.json` under `"env"`. The shared `user/settings.json` in this repo sets the env var, and bootstrap merges it into `~/.claude/settings.json`, so running bootstrap once on any consuming project lands the user-level default. Runtime precedence: managed policy > `CLAUDE_CODE_EFFORT_LEVEL` env var > persisted `effortLevel` (local > project > user) > Claude Code's built-in default. When the env var is set, it outranks `--effort` at launch and `/effort` inside a session; the slash command prints a warning that the env var is overriding the live effort. When the env var is unset, `--effort <level>` at launch is a session-only override, `/effort low|medium|high|xhigh` updates the persisted user setting, and `/effort max` is session-only.
<!-- /agent:claude -->

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

<!-- rule-pack:agent-style:begin version=v0.3.2 sha256=f175e39b0047d7dd8f7c047cce31c476dcc79e4f0452183b47b03baf3d4511bb -->
<!-- SPDX-License-Identifier: CC-BY-4.0 -->

<!--
Canonical rule-pack source consumed by anywhere-agents' rule-pack composer.

This file mirrors RULES.md at the repo root verbatim. agent-style's own
installer reads RULES.md; anywhere-agents fetches this file at
docs/rule-pack.md via the rule-pack convention. See
https://github.com/yzhao062/anywhere-agents for the composer spec.
-->

# The Elements of Agent Style — Rules

For each rule, this document provides:

- metadata (source citation, agent-instruction evidence, severity, scope, enforcement tier)
- directive (command-form sentence, negative for anti-patterns, positive for constructive placement)
- BAD → GOOD examples (5 or more per rule, with at least one non-paper context such as API docs, runbooks, proposals, release notes, postmortems, changelogs, or issue reports)
- rationale for AI agent (why the rule matters for LLM output specifically)

## Severity Rubric

Each rule has a severity from this four-level scale:

- **critical** — reader cannot understand or trust the prose if the rule is violated.
- **high** — externally visible AI-tell, or a recurring clarity failure that breaks skim-reading.
- **medium** — local readability cost, felt by the reader but not a trust issue.
- **low** — polish or preference; flagged for consistency rather than comprehension.

## Escape Hatch (Meta-Principle)

> *"Break any of these rules sooner than say anything outright barbarous."*
> — George Orwell, "Politics and the English Language" (1946), Rule 6

Rules are guides to clarity, not ends in themselves. When a rule fights the sentence, drop the rule.

## The 12 Rules

### Audience and Reader State

#### RULE-01: Do Not Assume the Reader Shares Your Tacit Knowledge (Resist the Curse of Knowledge)

- **source**: Pinker 2014, Ch. 3 "The Curse of Knowledge" (the entire chapter is devoted to this failure mode).
- **agent-instruction evidence**: Zhang et al. 2026 supports negative phrasing for anti-pattern directives in coding-agent instruction files (does not validate mechanical enforcement). Bohr 2025 supports pairing directives with examples for stronger initial style control over a paired two-turn code-generation workflow (not open-ended prose).
- **severity**: critical. Most common reviewer complaint on AI-generated technical prose is "reads like you forgot the reader doesn't know X yet."
- **scope**: `.md`, `.tex`, `.rst`, `.txt`, and prose sections of source files.
- **enforcement**: Tier-3 agent self-check (judgment rule; not mechanical); Tier-4 Codex review as primary gate.

##### Directive

Do not use technical terms or acronyms that have not been established for the reader's background level. Do not launch into mechanics before naming the purpose. Do not write a multi-paragraph argument without a one-sentence map first. Before writing, name the intended reader for this artifact: adjacent-field graduate student for research papers, junior engineer for API docs, on-call engineer for runbooks, cross-panel reviewer for proposals, release reader for changelogs, or another concrete reader. If that reader would pause to infer what a term means, define it or rewrite around it.

##### BAD → GOOD

- BAD: `We use contrastive learning with InfoNCE and a momentum encoder.`
- GOOD: `Our method trains a representation to separate similar from dissimilar image pairs (contrastive learning), with InfoNCE as the loss and a slowly-updating momentum encoder to stabilize training.`

- BAD: `The API uses JWT with RS256 refresh tokens rotated via the OIDC flow.`
- GOOD: `Authentication uses short-lived signed tokens (JWT with RS256) issued by our OIDC identity provider. Clients refresh these tokens before expiry through the standard OIDC refresh flow.`

- BAD: `We observed activation collapse in the final layer, resolved by adding LayerNorm before the projection head.`
- GOOD: `Final-layer activations collapsed to a near-constant vector during training (activation collapse). Adding a normalization step (LayerNorm) between the backbone and the projection head restored activation diversity.`

- BAD: `We set dropout=0.1, optimizer=AdamW, lr=3e-4, warmup=2000 steps, cosine decay.`
- GOOD: `We regularize with 10% dropout. Optimization uses AdamW (Adam with decoupled weight decay) at learning rate 3e-4, with a 2000-step linear warmup followed by cosine decay to zero.`

- BAD: `SGD converges faster here because of the Hessian conditioning.`
- GOOD: `SGD converges faster than Adam on this task because the loss surface is well-conditioned — the eigenvalues of the second-derivative matrix (Hessian) do not span many orders of magnitude, so a single learning rate suits all directions.`

- BAD (runbook): `If the queue is backed up, bounce the workers and clear the dead-letter.`
- GOOD (runbook): `If RabbitMQ queue depth exceeds 10k messages for more than 5 minutes, (1) drain and restart the Celery worker pool (bounce the workers) so new brokers pick up the rebalanced connections, then (2) drain the dead-letter queue so failed messages do not replay against the now-fresh workers.`

##### Rationale for AI Agent

LLMs absorb their training corpus at a near-expert register and reproduce that register by default. When an AI assistant writes about a technical subject, it does not know whether the current reader is a peer of the training distribution or a junior engineer, cross-team reviewer, external auditor, or grant panelist. The failure mode is almost invisible to the writer (whose knowledge is the baseline) and glaringly visible to the wrong-audience reader. Pinker 2014 Ch. 3 describes the phenomenon in depth; the practical fix compresses to: imagine a specific reader one level below your own expertise, and write for that reader. The concrete test before any technical paragraph is "would this sentence land for someone who has not opened this codebase / read this paper / sat in this meeting?" — if not, rewrite.

### Voice and Directness

#### RULE-02: Do Not Use Passive Voice When the Agent Matters

- **source**: Orwell 1946, "Politics and the English Language," Rule 3: *"Never use the passive where you can use the active."* Strunk & White §II.14 "Use the active voice."
- **agent-instruction evidence**: Zhang et al. 2026 supports negative phrasing for anti-pattern directives in coding-agent instruction files (does not validate mechanical enforcement). Bohr 2025 supports pairing directives with examples for stronger initial style control over a paired two-turn code-generation workflow (not open-ended prose).
- **severity**: high. Recurring AI-tell; passive constructions are the default register in technical prose generated from formal-training distributions.
- **scope**: `.md`, `.tex`, `.rst`, `.txt`, and prose sections of source files.
- **enforcement**: Tier-2 LanguageTool (`PASSIVE_VOICE` family) + Tier-3 agent self-check + Tier-4 Codex review. Not Tier-1 deny because passive-voice regex is high-recall, low-precision (flags many legitimate passives; scientific attribution and true agent-unknown cases remain valid).

##### Directive

Do not write "X was done by Y" when "Y did X" fits. Active voice names the agent, shortens the sentence, and makes the verb carry the action. When the agent is genuinely unknown or irrelevant (scientific attribution, observation of phenomena, general truths), passive is correct; use it deliberately, not by default. Before each passive construction, ask: is the agent known and worth naming? If yes, rewrite active.

##### BAD → GOOD

- BAD: `The experiments were conducted on eight NVIDIA A100 GPUs.`
- GOOD: `We ran the experiments on eight NVIDIA A100 GPUs.`

- BAD: `Errors are logged to /var/log/app.log when the service restarts.`
- GOOD: `The service logs errors to /var/log/app.log on restart.`

- BAD: `A significant improvement in recall was observed after the embedding model was swapped.`
- GOOD: `Swapping the embedding model raised recall@10 by 7 points.`

- BAD (release note): `Memory leaks have been fixed in the worker pool.`
- GOOD (release note): `The worker pool no longer leaks file descriptors on SIGTERM.`

- BAD (postmortem): `The incident was caused by a misconfigured load balancer rule.`
- GOOD (postmortem): ``A misconfigured load balancer rule (typo in the ingress-nginx path-rewrite regex) routed `/auth/*` to the wrong upstream and caused the incident.``

##### Rationale for AI Agent

LLMs trained on formal technical prose (abstracts, RFCs, corporate documentation) overproduce passive constructions by default. The training signal rewards "sounds authoritative" register, and passive constructions are over-represented in that register. The practical cost: passive hides the agent, drops responsibility, and forces the reader to reconstruct who did what. For debugging prose (postmortems, bug reports, root-cause analyses), this is actively harmful because "the error was raised" leaves the caller unnamed; "function `parse_token` raised the error at line 47" localizes the defect immediately. The rule does not ban passive. Scientific attribution ("participants were recruited") and true agent-unknown reports ("the service was restarted during the incident, reason unlogged") keep passive honestly. The rule bans passive-by-default when the agent is known and naming the agent would clarify the sentence.

### Word Choice

#### RULE-03: Do Not Use Abstract or General Language When a Concrete, Specific Term Exists

- **source**: Strunk & White §II.16: *"Use definite, specific, concrete language."* Pinker 2014 Ch. 3 frames abstraction as a primary vector of the curse of knowledge (writer has the specifics; reader does not, and cannot resolve abstract pointers like "factors" or "aspects").
- **agent-instruction evidence**: Zhang et al. 2026 supports negative phrasing for anti-pattern directives in coding-agent instruction files (does not validate mechanical enforcement). Bohr 2025 supports pairing directives with examples for stronger initial style control over a paired two-turn code-generation workflow (not open-ended prose).
- **severity**: high. Recurring clarity failure; generic nouns (`factors`, `aspects`, `considerations`, `issues`, `elements`) are an AI-tell because the model names a category without naming what the category contains.
- **scope**: `.md`, `.tex`, `.rst`, `.txt`, and prose sections of source files.
- **enforcement**: Tier-2 partial (claim-without-number heuristic for "improved", "enhanced", "optimized") + Tier-3 agent self-check + Tier-4 Codex review as primary gate.

##### Directive

Do not use abstract nouns when concrete ones exist. "The system has performance issues" says nothing; "the checkout endpoint p95 latency rose from 120ms to 450ms at 14:00 UTC" names what, when, and how much. Replace category words ("factors", "aspects", "considerations", "issues", "elements") with the specific items they refer to. If you reach for a category word, ask: what exactly? If the answer takes longer than one clause to give, the sentence was hiding the work.

##### BAD → GOOD

- BAD: `The model shows improvements across various metrics.`
- GOOD: `The model improves F1 by 3.2 points (0.812 to 0.844) on FEVER and cuts hallucination rate from 11.3% to 6.8% on TruthfulQA.`

- BAD: `Several architectural considerations influenced our design decisions.`
- GOOD: `We chose a two-tower retrieval architecture over cross-encoding because (1) the query-side embedding is cached across sessions, and (2) the document-side index is updated nightly without re-running inference on the query side.`

- BAD: `Ingestion is affected by data quality factors.`
- GOOD: ``When upstream vendors send records with malformed UTF-8, ingestion drops the record and increments the `malformed_input` counter on the `/metrics` endpoint.``

- BAD (API doc): `Authentication handles multiple scenarios.`
- GOOD (API doc): `Authentication supports three flows: OIDC authorization code (first-party web), client_credentials (service-to-service), and refresh-token rotation (long-lived mobile sessions). Each flow returns a signed JWT with a 15-minute TTL.`

- BAD (runbook): `Scale up the backend if traffic is high.`
- GOOD (runbook): ``If p95 latency on `/search` exceeds 300ms for more than 2 minutes, scale the search worker pool from 8 to 16 replicas via `kubectl scale deployment/search-worker --replicas=16`.``

##### Rationale for AI Agent

LLMs absorb abstract prose from grant abstracts, executive summaries, and position-paper genres where specifics are hidden for competitive or rhetorical reasons. The default output carries that register: "improvements across metrics", "multiple factors", "various considerations". A careful reader processes these phrases, notices nothing has been said, and discounts the rest of the document. The operational test before any factual-claim sentence: can I point at the exact number, file, commit, user action, or mechanism behind each phrase in this sentence? If not, the phrase is filler, and the LLM has hidden the absence of substance behind pleasant-sounding abstraction. Strunk & White §II.16 gives the rule; Pinker 2014 Ch. 3 identifies abstraction as one primary vector of the curse of knowledge (the writer knows the specifics, so "factors" reads as a pointer to them, but the reader has no pointer and cannot resolve it).

#### RULE-04: Do Not Include Needless Words

- **source**: Strunk & White §II.17: *"Omit needless words. Vigorous writing is concise."* Orwell 1946 Rule 3: *"If it is possible to cut a word out, always cut it out."*
- **agent-instruction evidence**: Zhang et al. 2026 supports negative phrasing for anti-pattern directives in coding-agent instruction files; the filler-phrase deny list is our separate mechanical enforcement choice because these specific phrases are directly detectable without a parse. Bohr 2025 supports pairing directives with examples for stronger initial style control over a paired two-turn code-generation workflow (not open-ended prose).
- **severity**: high. Filler phrases are among the most visible AI tells after clichés; wordiness signals a register shift that careful readers detect immediately.
- **scope**: `.md`, `.tex`, `.rst`, `.txt`, and prose sections of source files.
- **enforcement**: Tier-1 `deny` (filler-phrase list in `enforcement/deny-phrases.txt`: "it is important to note that", "in order to", "due to the fact that", "at this point in time", "may potentially", "could possibly", "in the event that", "it may be necessary to") + Tier-2 ProseLint (`terms.denizen_labels`) + Tier-3 agent self-check.

##### Directive

Do not stretch phrases. "In order to" is "to"; "due to the fact that" is "because"; "at this point in time" is "now"; "it is important to note that" is (delete and state the fact); "may potentially" and "could possibly" are redundant hedges (use "may" or "could", not both). Every filler phrase signals to the reader that substance is about to arrive; delete the phrase and let the substance arrive directly.

##### BAD → GOOD

- BAD: `It is important to note that the learning rate was reduced in order to prevent divergence.`
- GOOD: `We reduced the learning rate to prevent divergence.`

- BAD: `Due to the fact that the data pipeline may potentially fail under high load, we have added retry logic.`
- GOOD: `Because the data pipeline can fail under load, we added retry logic.`

- BAD: `At this point in time, the service is able to process approximately 1000 requests per second.`
- GOOD: `The service processes ~1000 requests per second.`

- BAD (PR description): `This PR makes some minor adjustments in order to fix an issue that was causing failures in certain test cases.`
- GOOD (PR description): ``Fixes a null-pointer crash in `test_checkout_flow` when the cart has a single item.``

- BAD (runbook): `In the event that the database connection pool is exhausted, it may be necessary to restart the service in order to recover.`
- GOOD (runbook): `If the connection pool is exhausted, restart the service.`

- BAD (commit message): `Some small changes have been made that may potentially improve the overall performance of the system in certain scenarios.`
- GOOD (commit message): `Cache product lookups in the hot path; reduces p99 from 310ms to 180ms.`

##### Rationale for AI Agent

LLM training rewards formal-sounding, hedge-laden completions because they sit closer to the modal output of the training corpus (press releases, whitepapers, academic abstracts, corporate documentation) than terse technical writing does. The specific filler phrases ("in order to", "due to the fact that", "it is important to note", "may potentially", "could possibly") are consensus cliché of that register. They lengthen sentences without carrying information. Human readers skim past them and infer the writer had little to say; downstream consumers (search indices, RAG pipelines, summarization chains) also suffer from the diluted signal-per-token ratio. The exact-phrase deny list is mechanically enforceable (Tier-1) because these phrases have no legitimate technical function: "in order to" is always replaceable by "to" with no loss of meaning, so denying the phrase outright has near-zero false-positive risk. Strunk & White §II.17 gives the principle; Orwell 1946 Rule 3 gives the cut-if-possible operational test.

#### RULE-05: Do Not Use Dying Metaphors or Prefabricated Phrases

- **source**: Orwell 1946, "Politics and the English Language," Rule 1: *"Never use a metaphor, simile, or other figure of speech which you are used to seeing in print."*
- **agent-instruction evidence**: Zhang et al. 2026 supports negative phrasing for anti-pattern directives in coding-agent instruction files; the exact-phrase deny list is our separate mechanical enforcement choice because these phrases are directly detectable. Bohr 2025 supports pairing directives with examples for stronger initial style control over a paired two-turn code-generation workflow.
- **severity**: high. The most externally visible AI-tell signal in generated prose.
- **scope**: `.md`, `.tex`, `.rst`, `.txt`, and prose sections of source files.
- **enforcement**: Tier-1 `deny` (exact-phrase list in `enforcement/deny-phrases.txt`) + Tier-2 ProseLint (`misc.phrasal_adjectives`, `airlinese.misc`, `cliches.misc`) + Tier-4 Codex review for anything the phrase list misses.

##### Directive

Do not use metaphors, similes, or phrases you have seen often in print. When a phrase feels off-the-shelf — ready-made framing for work-in-general rather than for this work — either restate in plain technical terms with specific numbers or a specific mechanism, or delete the sentence. If the sentence is paraphrasing what other people write about work like yours rather than stating what is true about yours, it is a dying metaphor and should go.

##### BAD → GOOD

- BAD: `This work pushes the boundaries of what's possible in large language model alignment.`
- GOOD: `This work reduces harmful-completion rate on HarmBench from 14.1% to 3.2% without degrading MMLU accuracy.`

- BAD: `Our system delivers industry-leading performance on the ImageNet benchmark.`
- GOOD: `On ImageNet-1k, our system reaches 88.3% top-1 accuracy, 1.2 points above the previous best (Wang et al. 2025).`

- BAD: `This paves the way for a new era of retrieval-augmented agents.`
- GOOD: (delete the sentence; if the work genuinely establishes a new method, the specific results paragraph already said that.)

- BAD: `We leverage state-of-the-art embedding models to unlock the full potential of the retrieval pipeline.`
- GOOD: `We use OpenAI text-embedding-3-large for document embedding. This raised retrieval recall@10 by 7 points over our previous choice (text-embedding-ada-002).`

- BAD: `Our groundbreaking approach to interpretability represents a paradigm shift in the field.`
- GOOD: `Our attention-probing method identifies which transformer layer each factual-recall head first activates. We validate this on 12 known facts from Meng et al. 2022 and observe consistent attribution for 10 of them.`

- BAD (release note): `This release delivers significant improvements to user experience and performance.`
- GOOD (release note): `Reduce p99 dashboard load latency from 820ms to 240ms. Fix a crash in CSV export when a cell contains an embedded newline. Add keyboard shortcut (Shift+E) for the filter-reset action requested in #1847.`

##### Rationale for AI Agent

LLMs trained on web text — press releases, blog posts, grant introductions, paper abstracts, corporate marketing — disproportionately reproduce clichéd phrases from that corpus. Readers who have processed many such sources recognize "pushes the boundaries" and "paradigm shift" as filler and skip the sentence; the distinctiveness of AI-written prose suffers in direct proportion. Orwell 1946 Rule 1 names the failure mode directly, predating LLMs by eighty years. Zhang et al. 2026 give empirical support for phrasing this class of rule as a negative directive in coding-agent instruction files; the phrase-list deny is our separate mechanical enforcement choice, independent of the Zhang paper, motivated by the observation that these specific phrases are directly detectable without a parse. The LLM-specific corollary — which the six BAD/GOOD examples above illustrate — is that if you cannot quote a specific number, comparison, or mechanism in place of the cliché, the cliché was hiding the absence of substance. Deleting the cliché and finding you cannot replace it with specifics is itself useful information.

#### RULE-06: Do Not Use Avoidable Jargon Where an Everyday English Word Exists

- **source**: Orwell 1946, "Politics and the English Language," Rule 5: *"Never use a foreign phrase, a scientific word, or a jargon word if you can think of an everyday English equivalent."* Pinker 2014 Ch. 2 treats concrete everyday language as the classic-style baseline; specialized terms are reserved for when they carry distinct information.
- **agent-instruction evidence**: Zhang et al. 2026 supports negative phrasing for anti-pattern directives in coding-agent instruction files (does not validate mechanical enforcement). Bohr 2025 supports pairing directives with examples for stronger initial style control over a paired two-turn code-generation workflow (not open-ended prose).
- **severity**: medium. Local readability cost; readers still understand "utilize" and "methodology" but parse them as register markers rather than content. Distinguish technical jargon (necessary, carries distinct meaning) from corporate-speak jargon (substitutable, signals register only).
- **scope**: `.md`, `.tex`, `.rst`, `.txt`, and prose sections of source files.
- **enforcement**: Tier-1 `ask` (heuristic substitutions: "leverage" → "use", "utilize" → "use", "methodology" → "method", "functionality" → "function" or "feature", "operationalize" → "start" or "build") + Tier-2 ProseLint (`airlinese.misc`) + Tier-3 agent self-check.

##### Directive

Do not use "leverage" where "use" fits. Do not use "utilize" where "use" fits. Do not use "methodology" where "method" fits. Do not use "functionality" where "function" or "feature" fits. Reserve the longer word for when it carries information the shorter word does not. Technical jargon with distinct meaning ("backpropagation", "quantization", "deserialization") is fine and often necessary. Corporate-speak jargon ("leverage", "utilize", "operationalize") is substitutable by shorter everyday words without loss of meaning.

##### BAD → GOOD

- BAD: `We leverage transformer architectures to facilitate cross-lingual transfer.`
- GOOD: `We use transformers for cross-lingual transfer.`

- BAD: `The methodology utilized for optimization employs gradient descent techniques.`
- GOOD: `We optimize with gradient descent.`

- BAD: `Functionality for CSV export will be operationalized in the next release.`
- GOOD: `CSV export ships in the next release.`

- BAD (API doc): `This endpoint enables users to interact with the underlying data store through a REST interface.`
- GOOD (API doc): `GET /documents lists documents in the store. Paginated; default 50 per page.`

- BAD (changelog): `The system has been optimized to efficiently utilize available resources in a more performant manner.`
- GOOD (changelog): `Reduce memory footprint from 1.2GB to 380MB at idle by lazy-loading the embedding cache.`

- BAD (proposal): `We will operationalize a novel methodology for the efficient utilization of computational resources.`
- GOOD (proposal): `We will build a scheduler that packs GPU jobs by estimated memory and runtime, aiming for >85% cluster utilization (current baseline: 62%).`

##### Rationale for AI Agent

LLMs reproduce the corporate-technical register disproportionately because it is over-represented in training corpora (whitepapers, blog posts, grant abstracts, vendor documentation). Words like "leverage", "utilize", "operationalize", "methodology", "functionality" do not carry more information than "use", "use", "start", "method", "feature"; they signal a register rather than refine meaning. Readers experienced in technical prose mentally substitute the shorter word as they read, which means the longer word has bought nothing and has cost reading time. The rule does not ban polysyllabic terms outright. Technical terms with distinct meaning are fine and necessary. The rule bans substitutions where a shorter everyday word carries the same information and the longer word adds only register.

### Claims and Calibration

#### RULE-07: Use Affirmative Form for Affirmative Claims ("Trivial" Instead of "Not Important")

- **source**: Strunk & White §II.15: *"Put statements in positive form."*
- **agent-instruction evidence**: Zhang et al. 2026 supports negative phrasing for anti-pattern directives in coding-agent instruction files; RULE-07 carries a positive directive because the target is a constructive placement (choose the affirmative word) rather than an anti-pattern to flag. Bohr 2025 supports pairing directives with examples for stronger initial style control over a paired two-turn code-generation workflow.
- **severity**: medium. Readability cost rather than clarity failure; readers parse "not important" correctly, just slower than "trivial".
- **scope**: `.md`, `.tex`, `.rst`, `.txt`, and prose sections of source files.
- **enforcement**: Tier-3 agent self-check + Tier-4 Codex review. No Tier-1 deny (requires judgment about whether the positive form exists and fits). Empty-hedge phrases ("may potentially", "could possibly") live under RULE-04, not here, because they are redundant hedges rather than double negations.

##### Directive

Replace "not important" with "trivial"; "did not remember" with "forgot"; "did not pay attention to" with "ignored"; "is not often" with "rarely"; "is not large" with "small"; "does not succeed" with "fails". Prefer one affirmative word over two negating words. When the sentence genuinely negates something (the proposition is true only in the negative), a single "not" is fine and necessary. The rule targets two-word negations that have a one-word affirmative equivalent. The operational test: can I replace "not X" with a single positive word that names the state directly? If yes, do so.

##### BAD → GOOD

- BAD: `The variance was not large.`
- GOOD: `The variance was small.`

- BAD: `He did not remember to set the flag.`
- GOOD: `He forgot to set the flag.`

- BAD: `This method is not as accurate as the baseline.`
- GOOD: `This method is less accurate than the baseline (81.7% vs 88.3% top-1 on ImageNet-1k).`

- BAD (bug report): `The function does not return a value in some cases.`
- GOOD (bug report): ``The function returns `undefined` when the input array is empty (missing branch in `parse_row` at `utils/parse.py:47`).``

- BAD (release note): `Startup time is not as slow as in the previous release.`
- GOOD (release note): `Startup time drops from 4.2s to 1.8s (57% faster) by deferring the plugin scan to first interactive action.`

- BAD: `The cache is not frequently invalidated.`
- GOOD: `The cache is rarely invalidated, roughly once per deploy.`

##### Rationale for AI Agent

Double-negation phrasing ("not insignificant", "not uncommon", "not unlike") pervades academic and journalistic prose, and LLMs absorb the pattern from training. The cognitive cost is real: the reader holds "not" in working memory, parses the negated adjective, then negates again to recover the intended meaning. For simple affirmative states, this is wasted work. The rule does not ban honest negation; when something is genuinely absent, "no X" or "not X" is correct. The rule bans avoidable compound negation where a positive-form word already names the state. A downstream concern for AI-generated prose: double-negation also defeats tone and sentiment detection in downstream tooling, so in contexts where the text feeds another model (summarization, classification, moderation), positive form is operationally safer.

#### RULE-08: Do Not Linguistically Overstate or Understate Claims Relative to the Evidence

- **source**: Pinker 2014 Ch. 6 (calibrated claims; hedge calibration treated as a skill with verbs matched to evidence strength). Gopen & Swan 1990 (scientific attribution: the source of a claim should be visible in the sentence, and the verb should match the evidence).
- **agent-instruction evidence**: Zhang et al. 2026 supports negative phrasing for anti-pattern directives in coding-agent instruction files (does not validate mechanical enforcement). Bohr 2025 supports pairing directives with examples for stronger initial style control over a paired two-turn code-generation workflow (not open-ended prose).
- **severity**: high. Externally visible AI-tell; overclaim patterns ("revolutionary", "transforms", "dramatic") and reflexive weasel ("it might be worth considering") are both recognized by technical readers as filler register, each eroding trust differently.
- **scope**: `.md`, `.tex`, `.rst`, `.txt`, and prose sections of source files.
- **enforcement**: Tier-3 agent self-check + Tier-4 Codex review as primary gate. Not Tier-1 because calibration requires judgment about what the evidence actually supports.

##### Directive

Do not overclaim (saying "proves X" when the evidence is "suggests X"). Do not underclaim via reflexive weasel (saying "it might be worth considering" when you mean "we should do X"). Calibrate verbs to evidence: experimental results "suggest" or "show"; theoretical derivations "imply" or "prove"; user reports "indicate" (pending verification); benchmarks "measure". Use "best" only when you have compared against the strongest alternative; use "only" only when you have ruled out alternatives. When the evidence is uncertain, say so in one clause; do not weaken the main verb beyond what the evidence supports.

##### BAD → GOOD

- BAD: `Our method revolutionizes language model alignment.`
- GOOD: `Our method reduces harmful-completion rate on HarmBench from 14.1% to 3.2% without degrading MMLU accuracy. (Generalization to other alignment benchmarks is future work.)`

- BAD: `Dramatic improvement in inference speed was observed.`
- GOOD: `Inference latency at batch size 1 drops from 142ms to 118ms (17% faster) on A100. Batch size 32 and larger show no measurable speedup.`

- BAD: `It might be worth considering whether some form of input validation could be beneficial.`
- GOOD: ``Add input validation at `/users`: the endpoint crashes on non-UTF-8 query parameters (observed twice last week).``

- BAD (paper abstract): `Our model proves the superiority of attention-based retrieval over sparse methods.`
- GOOD (paper abstract): `Our attention-based retriever reaches MRR@10 = 0.412 on MS MARCO Dev, compared to 0.395 for BM25 and 0.398 for ColBERT. The improvement is within one standard deviation on out-of-domain queries (BEIR).`

- BAD (issue report): `Everything is broken; nothing works.`
- GOOD (issue report): ``/auth/login returns 500 for all requests after the 2026-04-18 deploy. /auth/logout and /auth/refresh unaffected. Logs show a KeyError on `iat` in token parsing.``

- BAD (grant proposal): `This research will transform our understanding of neural network interpretability.`
- GOOD (grant proposal): `This research tests whether attention-probing generalizes beyond the 12 factual-recall circuits reported in Meng et al. 2022. If yes, the method applies to a class of interpretability questions currently intractable; if no, we localize the method's scope.`

##### Rationale for AI Agent

LLMs trained on mixed-register corpora (research abstracts, press releases, grant introductions, marketing copy) absorb both overclaiming and reflexive hedging from the genre patterns. Each fails predictably: overclaim trips the reader's calibration alarm (technical readers scan abstracts for unwarranted "proves" or "best" and discount the rest of the paper accordingly); reflexive under-hedging inflates trivially-true claims to sound important; over-hedging delays the main point across two clauses of pro-forma caution. The operational test before writing any result sentence: (a) what evidence supports this, and (b) does the verb match? "We observed" is weaker than "we showed" is weaker than "we proved." Pick the verb that matches your evidence exactly. Pinker 2014 Ch. 6 gives the calibration vocabulary; Gopen & Swan 1990 frame scientific attribution as a structural writing concern (the source of a claim should be visible, and the verb should match the evidence).

### Sentence Structure

#### RULE-09: Express Coordinate Ideas in Similar Form (Parallel Structure)

- **source**: Strunk & White §II.19: *"Express coordinate ideas in similar form."*
- **agent-instruction evidence**: Zhang et al. 2026 supports negative phrasing for anti-pattern directives in coding-agent instruction files; RULE-09 carries a positive directive because parallel structure is a constructive placement (match the form across items) rather than an anti-pattern to flag. Bohr 2025 supports pairing directives with examples for stronger initial style control over a paired two-turn code-generation workflow.
- **severity**: medium. Local readability cost; readers reparse mismatched items and lose rhythm, but still recover the meaning.
- **scope**: `.md`, `.tex`, `.rst`, `.txt`, and prose sections of source files.
- **enforcement**: Tier-2 partial (list-item POS check on bullet lists) + Tier-3 agent self-check + Tier-4 Codex review.

##### Directive

Write coordinate ideas in the same grammatical form. In a list of three items, if item 1 is a noun phrase, items 2 and 3 are also noun phrases; if item 1 is a verb-initial clause, items 2 and 3 are also verb-initial clauses. The rule applies to bullet lists, parallel predicates ("we measure X, improve Y, and validate Z"), and compound sentences connected by "and" / "or" / "but". Mismatched forms force the reader to reparse each item against a new expected structure.

##### BAD → GOOD

- BAD: `The pipeline cleans the data, feature extraction, and then trains the model.`
- GOOD: `The pipeline cleans the data, extracts features, and trains the model.`

- BAD: `We benchmark against three baselines: BM25, a sparse lexical retriever; dense retrieval using DPR; ColBERT.`
- GOOD: `We benchmark against three baselines: BM25 (sparse lexical), DPR (single-vector dense), and ColBERT (multi-vector dense).`

- BAD (API doc): `The endpoint accepts JSON input, you get XML back, and pagination is via cursor.`
- GOOD (API doc): `The endpoint accepts JSON input, returns XML output, and paginates by cursor.`

- BAD (runbook checklist item, in a list of verb-initial items): `Memory usage`
- GOOD (runbook checklist item, matching surrounding items): `Check memory (`free -h`)`

- BAD (changelog entry, in a list of verb-initial entries): `Faster startup`
- GOOD (changelog entry, matching surrounding entries): `Reduce startup time from 4.2s to 1.8s.`

##### Rationale for AI Agent

LLMs often produce lists where the first one or two items set a structure, then subsequent items drift because the model samples each next item conditional on the topic rather than on the established structure. The drift is subtle: a reader scans item 1, forms an expected shape for items 2 and 3, then hits a mismatch and backtracks. Simple cases are mechanically checkable (lists where item 1 starts with verb X should have items 2 and 3 starting with verbs of the same tense; lists of noun phrases should remain noun phrases), but the general case requires parse. The practical remedy for AI generation: when generating a list, first decide the structure (all verb phrases? all noun phrases? subject-verb-object?), then generate each item against that structure rather than sampling freely. Strunk & White §II.19 gives the rule and a diagnostic: read the list with "that" connecting items; if any item fails the read, parallelism is broken.

#### RULE-10: Keep Related Words Together

- **source**: Strunk & White §II.20: *"Keep related words together."* Gopen & Swan 1990 treat verb-subject proximity as a structural readability concern in scientific prose specifically (long subject-to-verb gaps are one of the most common causes of unreadable science writing).
- **agent-instruction evidence**: Zhang et al. 2026 supports negative phrasing for anti-pattern directives in coding-agent instruction files; RULE-10 carries a positive directive because the target is a constructive placement (keep X close to Y) rather than an anti-pattern to flag. Bohr 2025 supports pairing directives with examples for stronger initial style control over a paired two-turn code-generation workflow.
- **severity**: medium. Local readability cost; long subject-to-verb gaps cause reader working-memory overflow and backtracking, but the meaning remains recoverable with effort.
- **scope**: `.md`, `.tex`, `.rst`, `.txt`, and prose sections of source files.
- **enforcement**: Tier-2 partial (dep-parse distance between subject and verb) + Tier-3 agent self-check + Tier-4 Codex review.

##### Directive

Keep subject close to verb, verb close to object, and modifier close to modified. When a long parenthetical or relative clause must appear between subject and verb, move the clause to the end of the sentence or split into two sentences. The operational test: count words between subject and verb; if the gap exceeds 8, split. Readers hold the subject in working memory until the verb arrives; every intervening clause costs memory slots and increases misparsing risk.

##### BAD → GOOD

- BAD: `The model, which was pre-trained on a mixed corpus of English Wikipedia, Common Crawl, and a 400-million-token curated scientific dataset assembled by the authors over eight months, achieves 87.2% accuracy.`
- GOOD: `The model achieves 87.2% accuracy. It was pre-trained on a mixed corpus of English Wikipedia, Common Crawl, and a 400-million-token scientific dataset the authors curated over eight months.`

- BAD: `Users of the legacy authentication flow, which is being deprecated in Q3 2026 in favor of the new OIDC-based system described in the migration guide, must update their client libraries before the end-of-life date.`
- GOOD: `Users of the legacy authentication flow must update their client libraries before end-of-life. The legacy flow is being deprecated in Q3 2026; the replacement is OIDC-based (see migration guide).`

- BAD (API doc): `The /users endpoint returns, subject to the rate-limit and access-control constraints described below, a paginated list of user objects.`
- GOOD (API doc): `The /users endpoint returns a paginated list of user objects. Rate limits and access controls apply (see below).`

- BAD (postmortem): `The database replica, which had been failing its health checks intermittently for three days before the outage but was never promoted to primary during that period because of a misconfigured priority setting, was the direct cause of the outage.`
- GOOD (postmortem): `The database replica was the direct cause of the outage. It had been failing health checks intermittently for three days; a misconfigured priority setting prevented promotion to primary during that period.`

- BAD: `We found that the retrieval recall of our system, compared against the previously strongest baseline across all five evaluation datasets and using the same pre-processing pipeline, improved by 7 points at k=10.`
- GOOD: `Retrieval recall@10 improved by 7 points over the previously strongest baseline. The comparison used the same pre-processing pipeline across all five evaluation datasets.`

##### Rationale for AI Agent

LLMs generate text token-by-token conditional on prior context, which encourages completeness (every qualifier added inline) over readability (qualifiers deferred until the main clause lands). The result: sentences where the subject and verb are separated by 20+ words of parenthetical qualification. Readers experience this as working-memory overflow. By the time the verb arrives, the reader has lost the subject and must backtrack. The same logic applies to verb-object and modifier-modified pairs. Gopen & Swan 1990 frame long subject-to-verb gaps as one of the most common causes of unreadable scientific prose; Strunk & White §II.20 give the principle in general form. For AI generation specifically, the practical remedy is to split the sentence: the main claim lands in the first sentence, supporting qualifications follow in a second sentence.

#### RULE-11: Place New or Important Information in the Stress Position at the End of the Sentence

- **source**: Gopen & Swan 1990, "The Science of Scientific Writing" (stress-position framing; empirical treatment of reader expectation for new information at sentence end).
- **agent-instruction evidence**: Zhang et al. 2026 supports negative phrasing for anti-pattern directives in coding-agent instruction files; RULE-11 carries a positive directive because stress-position placement is a constructive structural rule rather than an anti-pattern to flag. Bohr 2025 supports pairing directives with examples for stronger initial style control over a paired two-turn code-generation workflow.
- **severity**: medium. Local readability cost; readers recover the claim from a front-loaded sentence but at the cost of re-reading, and skim-readers pick up the words before the final punctuation as the takeaway, so stress-position misuse dilutes the sentence's impact.
- **scope**: `.md`, `.tex`, `.rst`, `.txt`, and prose sections of source files.
- **enforcement**: Tier-3 agent self-check + Tier-4 Codex review. Not Tier-1 because identifying the "key fact" in a sentence requires judgment.

##### Directive

End sentences with the information you want the reader to remember. The beginning of a sentence (topic position) connects to what came before; the end (stress position) is where new or important information lands with maximum emphasis. If the key fact is in the middle, move it to the end or rebalance. The rule applies especially to result sentences in papers, conclusions in design docs, and root-cause lines in postmortems.

##### BAD → GOOD

- BAD: `A 3.2-point improvement in F1 over the previous best model was demonstrated by the new architecture on the SQuAD 2.0 test set.`
- GOOD: `On the SQuAD 2.0 test set, the new architecture improves F1 by 3.2 points over the previous best model.`

- BAD: `The outage was caused by a cron job that ran at the wrong time.`
- GOOD: ``The outage was caused by a cron job firing every minute instead of every hour (typo in the crontab: `* * * * *` instead of `0 * * * *`).``

- BAD (commit message): `Fix for issue where users occasionally see a blank page in the dashboard when their session has expired and they try to navigate to a protected route.`
- GOOD (commit message): `On expired-session navigation to protected routes, redirect to /login instead of rendering the blank dashboard frame.`

- BAD (release note): `Performance improvements in the search pipeline are included in this release, with p95 query latency improving from 340ms to 95ms and p99 from 870ms to 180ms.`
- GOOD (release note): `p95 search latency drops from 340ms to 95ms; p99 drops from 870ms to 180ms.`

- BAD (paper sentence): `The approach is to first train a contrastive embedder, and then the retrieval performance can be measured across the five benchmarks.`
- GOOD (paper sentence): `We first train a contrastive embedder, then measure retrieval performance across five benchmarks: MS MARCO, FEVER, HotpotQA, NQ, and TriviaQA.`

##### Rationale for AI Agent

Gopen & Swan 1990 show empirically (American Scientist study of sentence clarity) that readers unconsciously expect the stress position for new information. When a sentence front-loads the new information and tails off into background, readers experience the sentence as flat and re-read to recover the claim. LLMs often produce the BAD pattern because token-by-token generation rewards completing the sentence with whatever is most fluent, frequently a prepositional phrase that restates topic material already established rather than introducing new information. The operational rewrite: identify the sentence's key claim, then rebuild the sentence so that the claim lands at the end. For multi-sentence units (paragraphs), the same logic applies at the paragraph level: the opening sentence frames; the final sentence lands the main point; middle sentences support.

#### RULE-12: Break Long Sentences; Vary Length (Split Sentences over 30 Words)

- **source**: Strunk & White §II.18 (arrangement of sentences; varied length across a paragraph). Pinker 2014 Ch. 4 (syntax and working-memory limits; long sentences with nested clauses tax the reader's parsing budget).
- **agent-instruction evidence**: Zhang et al. 2026 supports negative phrasing for anti-pattern directives in coding-agent instruction files; RULE-12 carries a positive directive because sentence-splitting and length-variation are constructive structural choices rather than anti-patterns to flag. Bohr 2025 supports pairing directives with examples for stronger initial style control over a paired two-turn code-generation workflow.
- **severity**: high. Long sentences are a recurring AI tell and a recurring clarity failure; time-constrained technical readers (on-call engineers, reviewers, release-note skimmers) cannot parse 40+ word sentences reliably.
- **scope**: `.md`, `.tex`, `.rst`, `.txt`, and prose sections of source files.
- **enforcement**: Tier-1 `ask` (sentence > 30 words; suggest split) + Tier-2 variance-of-sentence-length metric + Tier-3 agent self-check.

##### Directive

Split any sentence over 30 words into two or more sentences. Vary sentence length across a paragraph: a paragraph of five 25-word sentences reads less well than the same content in sentences of 8, 18, 22, 14, 30 words. Short sentences land points; long sentences carry qualification and detail. A paragraph that does only one of these reads as monotone. When a long sentence is unavoidable (single logical unit that resists splitting), make the previous and following sentences short to balance.

##### BAD → GOOD

- BAD (43 words, single sentence): `We evaluate our model on five standard benchmarks covering natural-language inference, reading comprehension, and factual-recall tasks, reporting both in-distribution accuracy on held-out splits of the training corpora and out-of-distribution accuracy on benchmarks not seen during training or fine-tuning.`
- GOOD (three sentences, 15 + 12 + 11 words): `We evaluate our model on five standard benchmarks: NLI, reading comprehension, and factual-recall. In-distribution accuracy uses held-out splits of the training corpora. Out-of-distribution accuracy uses benchmarks not seen during training.`

- BAD (monotone paragraph, four 22-word sentences): `The ingestion pipeline processes incoming records in batches of one thousand items and stores them in the primary document store. Each batch is processed by the ingest worker which runs on a schedule of every five minutes. The document store maintains an index on the timestamp field which enables range queries. Query performance is acceptable for batch sizes up to fifty thousand records per minute.`
- GOOD (varied, 8 + 22 + 14 + 11 words): `The ingest worker handles incoming records in batches. Every five minutes, it pulls up to a thousand records and writes them to the primary document store. The store keeps a timestamp index that supports range queries. At fifty thousand records per minute, performance holds.`

- BAD (runbook, 34 words): `If the primary database instance becomes unavailable for more than two minutes due to either a network partition or a full restart cycle, initiate failover to the replica using the promote_replica.sh script in the ops directory.`
- GOOD (split): ``Fail over to the replica if the primary is unavailable for more than two minutes. Unavailability includes both network partition and full restart cycle. Run `ops/promote_replica.sh` to promote.``

- BAD (paper abstract, 54 words): `In this work we investigate whether large language models pre-trained on code exhibit emergent understanding of algorithmic concepts, testing this hypothesis by measuring zero-shot performance on a suite of algorithm-design tasks and comparing the pattern of successes and failures to human performance on the same tasks collected from online programming forums over a period of six months.`
- GOOD (four sentences): `Do code-pretrained LLMs exhibit emergent understanding of algorithmic concepts? We test this by measuring zero-shot performance on a suite of algorithm-design tasks. We compare performance to human baselines collected from online programming forums over six months. We report the pattern of shared successes and failures across model size and task difficulty.`

- BAD (changelog, monotone): `This release adds support for OAuth 2.0 device flow authentication. This release also adds a new audit log for all API requests. This release introduces rate limiting on the free tier at 100 requests per minute. This release fixes a crash in CSV export when a cell contains an embedded newline.`
- GOOD (varied): `OAuth 2.0 device flow authentication ships in this release. A new audit log now captures all API requests. Free-tier clients see rate limiting at 100 req/min. CSV export no longer crashes on cells containing embedded newlines.`

##### Rationale for AI Agent

LLM decoding rewards well-formed completions; the next-token objective encourages sentences to continue with qualifications rather than stop and restart. The result is a tendency toward 30+ word sentences with multiple subordinate clauses. Readers, especially time-constrained readers of technical prose, read in chunks; chunks larger than working-memory capacity cause comprehension failure and re-reading. Short sentences also carry emphasis that long sentences dilute; a paragraph that never shifts sentence length reads as a flat surface, and the reader skims over the points that were meant to land. The operational guide for AI generation: after drafting, count words per sentence in each paragraph of technical prose; split anything over 30 words; vary lengths across the paragraph (no five similarly-sized sentences in a row). Pinker 2014 Ch. 4 frames the syntax/working-memory tradeoff; Strunk & White §II.18 give the variation principle.

## The 9 Field-Observed Rules

The following nine rules (RULE-A through RULE-I) come from my observation of LLM output across dozens of writing projects and code releases, 2022 to 2026. They are not drawn from cited writing authorities; each rule names a recurring pattern I saw frequently enough across distinct projects to warrant a named rule. They are treated as peer input to the 12 canonical rules in all adapter files; when an agent consumes the ruleset, both groups are binding.

### Observed LLM Patterns

#### RULE-A: Do Not Convert Prose into Bullet Points Unless the Content Is a Genuine List

- **source**: My observation of LLM output across dozens of writing projects and code releases, 2022–2026. Adjacent to `agent-config` / `anywhere-agents` AGENTS.md Formatting Defaults: "Do not convert paragraphs into bullet points unless the user asks for that format."
- **agent-instruction evidence**: Zhang et al. 2026 supports negative phrasing for anti-pattern directives in coding-agent instruction files (does not validate mechanical enforcement). Bohr 2025 supports pairing directives with examples for stronger initial style control over a paired two-turn code-generation workflow (not open-ended prose).
- **severity**: medium. Recurring structural AI-tell; bullet-ification fragments reasoning and signals "AI summary" register in proposals, design docs, and research-paper introductions.
- **scope**: `.md`, `.tex`, `.rst`, `.txt`, and prose sections of source files.
- **enforcement**: Tier-2 heuristic (flag consecutive bullet lists longer than 4 items with identical opener pattern, or bullets where subject-verb flow would connect the items into prose) + Tier-3 agent self-check + Tier-4 Codex review.

##### Directive

Keep prose in paragraphs when ideas connect by cause-and-effect, argument, or narrative. Use bullets only when items are genuinely parallel enumerations (API endpoints, config options, checklist steps). The test: if a reader reads only the first few words of each bullet, does the shape recover meaning? For a genuine list, yes (each bullet names a thing); for fragmented prose, no (bullets are sentence shards with connective tissue stripped). Do not force 3-item lists when 2 items or a sentence fit; LLMs over-produce "first, second, third" triads where 2 items would be natural. Resist the pattern.

##### BAD → GOOD

- BAD (proposal, bullet-ified argument):

    ```text
    Our approach consists of:
    - Training a contrastive embedder
    - Because this improves retrieval recall
    - Which is important for RAG pipelines
    - And enables downstream applications
    ```

- GOOD (proposal): `Our approach trains a contrastive embedder, which improves retrieval recall for downstream RAG pipelines.`

- BAD (design doc, bullet-ified causal chain):

    ```text
    The architecture decision:
    - We chose two-tower retrieval
    - Rather than cross-encoding
    - Because query embeddings cache across sessions
    - And document index updates nightly without re-inference
    ```

- GOOD (design doc): `We chose two-tower retrieval over cross-encoding because the query embedding caches across sessions, and the document index updates nightly without re-running inference on the query side.`

- BAD (API doc, fragmented single sentence):

    ```text
    Rate limits:
    - Free tier
    - 100 requests
    - Per minute
    - Per user
    ```

- GOOD (API doc): `Rate limits: the free tier allows 100 requests per minute per user.`

- BAD (postmortem, forced 3-item triad):

    ```text
    The outage had three causes:
    - A misconfigured load balancer rule
    - An outdated auth-v1 service
    - And insufficient alerting on auth-v1
    ```

- GOOD (postmortem): `A misconfigured load balancer rule routed /auth/* traffic to the outdated auth-v1 service. Insufficient alerting on auth-v1 delayed detection by 37 minutes.`

- BAD (README, forced "three strengths" triad):

    ```text
    Our framework has three key strengths:
    - It is fast
    - It is accurate
    - It is easy to use
    ```

- GOOD (README): `Our framework is fast (~2ms per query), accurate (94.3% top-1 on the benchmark suite), and ships as a drop-in Python library.`

##### Rationale for AI Agent

LLMs default to bullets whenever they present multiple ideas because bullets read as structured and signal "I am being organized." But bullets fragment reasoning: each bullet becomes an isolated shard, the connective tissue (because, therefore, however) disappears, and the reader reconstructs the argument from the shards. The specific 3-item triad is especially common; LLMs have learned that "first, second, third" structures feel balanced and complete, so they produce them even when the underlying content is two items or a flowing sentence. The fix: use bullets only when items are genuinely independent enumerations; use prose when ideas connect. The test sentence after drafting any list: can this become prose without loss? If yes, it probably should.

#### RULE-B: Do Not Use Em or En Dashes as Casual Sentence Punctuation

- **source**: My observation of LLM output across dozens of writing projects and code releases, 2022–2026. Adjacent to `agent-config` / `anywhere-agents` AGENTS.md Formatting Defaults: "Avoid heavy dash use. Do not use em dashes or en dashes as casual sentence punctuation. Prefer commas, semicolons, colons, or parentheses instead."
- **agent-instruction evidence**: Zhang et al. 2026 supports negative phrasing for anti-pattern directives in coding-agent instruction files; the dash-as-punctuation regex flag is our separate mechanical enforcement choice (Zhang does not validate mechanical enforcement). Bohr 2025 supports pairing directives with examples for stronger initial style control over a paired two-turn code-generation workflow (not open-ended prose).
- **severity**: medium. Recurring and externally visible AI-tell; LLMs produce em dashes at substantially higher rates than skilled human technical writers, producing a cadence that human readers recognize as AI-paced.
- **scope**: `.md`, `.tex`, `.rst`, `.txt`, and prose sections of source files.
- **enforcement**: Tier-1 `ask` (em-dash and en-dash regex, excluding ranges and paired names) + Tier-3 agent self-check + Tier-4 Codex review.

##### Directive

Do not use em dashes or en dashes as casual sentence punctuation. Prefer commas for appositives, semicolons for linked independent clauses, colons for expansions, and parentheses for asides. En dashes remain correct in numeric ranges (`1-3`, `2020-2026`), paired names ("the Stein-Strömberg theorem"), and bibliographic page ranges. Normal hyphens in compound words and technical terms (`command-line`, `co-PI`, `zero-shot`) are not dashes and should not be flagged.

##### BAD → GOOD

- BAD: `The model converges quickly — typically within 5000 training steps — on most datasets.`
- GOOD: `The model converges quickly, typically within 5000 training steps, on most datasets.`

- BAD: `We use three optimizers — AdamW, Lion, and SGD — in the ablation.`
- GOOD: `We use three optimizers in the ablation: AdamW, Lion, and SGD.`

- BAD (release note): `This release fixes the CSV export crash — the one reported last week — and adds a filter-reset shortcut.`
- GOOD (release note): `This release fixes the CSV export crash reported in issue #1847 and adds a filter-reset shortcut.`

- BAD (paper): `The method works well on in-distribution data — our primary evaluation target — and degrades gracefully on out-of-distribution inputs.`
- GOOD (paper): `The method works well on in-distribution data (our primary evaluation target) and degrades gracefully on out-of-distribution inputs.`

- BAD (blog post): `This is important — and somewhat surprising — because earlier work suggested the opposite.`
- GOOD (blog post): `This is important, and somewhat surprising, because earlier work suggested the opposite.`

##### Rationale for AI Agent

LLMs absorb the em dash as a favored connector from long-form journalism and essay prose (the register of magazine essays and essay-heavy blogs), where it carries rhythm and emphasis. In dense technical prose, every em dash is a pause the reader must hold in working memory while the parenthetical completes; two em dashes per sentence approach the working-memory ceiling for most readers. The recent public awareness of em dash overuse as an AI-tell is partly because LLMs produce them at several times the rate of skilled human technical writers, producing a cadence human readers recognize as AI-paced. Commas, semicolons, colons, and parentheses each carry a clearer semantic signal (list-separator, independent-clause break, expansion, aside); replacing em dashes with the punctuation that actually matches the relationship makes the sentence's logical structure explicit rather than rhythm-dependent. Normal hyphenation in compound words and technical terms remains correct; the rule targets dashes acting as punctuation, not hyphens joining words.

#### RULE-C: Do Not Start Consecutive Sentences with the Same Word or Phrase

- **source**: My observation of LLM output across dozens of writing projects and code releases, 2022–2026. Adjacent to `agent-config` / `anywhere-agents` AGENTS.md Formatting Defaults: "Prefer not to start several consecutive sentences with the same word or phrase."
- **agent-instruction evidence**: Zhang et al. 2026 supports negative phrasing for anti-pattern directives in coding-agent instruction files (does not validate mechanical enforcement). Bohr 2025 supports pairing directives with examples for stronger initial style control over a paired two-turn code-generation workflow (not open-ended prose).
- **severity**: medium. Local rhythm issue; paragraphs read as monotone and template-filled when same-starts accumulate.
- **scope**: `.md`, `.tex`, `.rst`, `.txt`, and prose sections of source files.
- **enforcement**: Tier-2 (first-word check across consecutive sentences in a paragraph; flag two or more consecutive identical openers) + Tier-3 agent self-check + Tier-4 Codex review.

##### Directive

Do not open two or more consecutive sentences with the same word. The pattern signals a drafting template that the generation process locked into (often `This ... This ... This ...`, `The ... The ... The ...`, or `We ... We ... We ...`). Vary the opener: topic-fronted versus subject-fronted versus connective. Pronoun subjects (`It`, `We`, `They`) are the most common offenders in LLM output because the model samples the next sentence conditional on the topic and re-picks the most fluent subject.

##### BAD → GOOD

- BAD (paper): `The method uses a contrastive loss. The method also applies dropout. The method converges in 5000 steps.`
- GOOD (paper): `The method uses a contrastive loss with 10% dropout, converging in 5000 steps.`

- BAD (release note): `This release adds OAuth support. This release fixes a CSV export bug. This release improves startup time.`
- GOOD (release note): `OAuth support lands in this release. A CSV export bug is fixed. Startup time drops from 4.2s to 1.8s.`

- BAD (paper, we-starts): `We trained the model. We evaluated on five benchmarks. We found improvements across all metrics.`
- GOOD (paper): `We trained the model and evaluated it on five benchmarks, finding improvements across all metrics.`

- BAD (API doc): `The API returns JSON. The API supports pagination. The API rate-limits at 100 req/min.`
- GOOD (API doc): `The API returns paginated JSON and rate-limits at 100 req/min.`

- BAD (postmortem, it-starts): `It started at 14:00 UTC. It lasted 37 minutes. It affected 12% of users.`
- GOOD (postmortem): `The incident started at 14:00 UTC, lasted 37 minutes, and affected 12% of users.`

##### Rationale for AI Agent

LLMs producing text token-by-token often lock into a successful opener and repeat it. Once `The method ...` works, the next-token distribution for the following sentence frequently starts with `The method ...` again because the prefix has become conditionally likely given the topic. The result: paragraphs with three or four identically-opened sentences. Human readers read these as template-filled rather than argued; even when the content is correct, the form signals a machine pattern. The fix at generation time: after a sentence is drafted, the next sentence's opener should vary, either by moving the new information to the subject position, combining the two sentences, or using a connective. This rule interacts with RULE-12 (sentence length variation); both aim at paragraph-level rhythm.

#### RULE-D: Do Not Overuse Transition Words ("Additionally", "Furthermore", "Moreover")

- **source**: My observation of LLM output across dozens of writing projects and code releases, 2022–2026. Adjacent to `agent-config` / `anywhere-agents` AGENTS.md Formatting Defaults: "Avoid overusing transition words like 'Additionally' or 'Furthermore.'"
- **agent-instruction evidence**: Zhang et al. 2026 supports negative phrasing for anti-pattern directives in coding-agent instruction files (does not validate mechanical enforcement). Bohr 2025 supports pairing directives with examples for stronger initial style control over a paired two-turn code-generation workflow (not open-ended prose).
- **severity**: medium. Recurring externally visible AI-tell; opening two or three consecutive sentences with "Additionally" / "Furthermore" / "Moreover" is one of the most distinctive cadences AI-generated text is recognized by.
- **scope**: `.md`, `.tex`, `.rst`, `.txt`, and prose sections of source files.
- **enforcement**: Tier-1 `ask` (sentence-initial transition word list: "Additionally", "Furthermore", "Moreover", "In addition", "What's more", "Notably"; flag when combined with paragraph-level frequency) + Tier-2 ProseLint + Tier-3 agent self-check.

##### Directive

Do not open sentences with "Additionally", "Furthermore", "Moreover", "In addition", "What's more", or "Notably" unless the sentence genuinely builds on the preceding clause in a way that a period or `And` would not convey. In most cases, a period ends the prior sentence and the next sentence makes the connection by content alone. Reserve explicit transitions for the rare case where the logical move (addition, contrast, concession) needs to be flagged for the reader.

##### BAD → GOOD

- BAD (paper): `The model outperforms BM25 on MS MARCO. Additionally, it outperforms DPR on Natural Questions. Furthermore, it reaches state-of-the-art on BEIR.`
- GOOD (paper): `The model outperforms BM25 on MS MARCO and DPR on Natural Questions, and reaches state-of-the-art on BEIR.`

- BAD (proposal): `The project addresses retrieval accuracy. Moreover, it addresses latency. In addition, it addresses interpretability.`
- GOOD (proposal): `The project addresses three targets: retrieval accuracy, latency, and interpretability.`

- BAD (design doc): `We cache embeddings for 24 hours. Additionally, we invalidate on source-document update. Furthermore, we rebuild the cache nightly.`
- GOOD (design doc): `We cache embeddings for 24 hours, invalidate on source-document update, and rebuild the cache nightly.`

- BAD (release note): `This release adds OAuth support. Additionally, it fixes the CSV export crash. Furthermore, it improves startup time.`
- GOOD (release note): `OAuth support lands in this release. The CSV export crash is fixed. Startup time drops from 4.2s to 1.8s.`

- BAD (blog): `The method is simple. Additionally, it is fast. Furthermore, it generalizes.`
- GOOD (blog): `The method is simple, fast, and generalizes to new domains.`

##### Rationale for AI Agent

LLM training on formal essay corpora (academic prose, Wikipedia, editorial writing) over-represents explicit transitions. "Additionally", "Furthermore", "Moreover" appear at higher frequency in LLM output than in skilled technical prose, producing the distinctive sentence-initial cadence AI-generated text is recognized by. The fix: connective tissue should usually be implicit (the next sentence is obviously an addition because of its content) rather than marked. Explicit transitions remain legitimate where the logical move is non-obvious, or where a paragraph-level contrast needs flagging for the reader. Related: RULE-04 catches word-level filler phrases ("in order to", "due to the fact that"); RULE-D catches the specific sentence-initial transition pattern that RULE-04's phrase list does not target. Both rules cut needless words; they target different positions in the sentence.

#### RULE-E: Do Not Close Every Paragraph with a Summary Sentence

- **source**: My observation of LLM output across dozens of writing projects and code releases, 2022–2026. Adjacent to `agent-config` / `anywhere-agents` AGENTS.md Formatting Defaults: "Not every paragraph needs a tidy summary sentence at the end."
- **agent-instruction evidence**: Zhang et al. 2026 supports negative phrasing for anti-pattern directives in coding-agent instruction files (does not validate mechanical enforcement). Bohr 2025 supports pairing directives with examples for stronger initial style control over a paired two-turn code-generation workflow (not open-ended prose).
- **severity**: medium. Structural throat-clearing; adds length without adding information. Pattern is externally visible because well-read technical readers skim past it, marking the prose as machine-generated or unedited.
- **scope**: `.md`, `.tex`, `.rst`, `.txt`, and prose sections of source files.
- **enforcement**: Tier-3 agent self-check (paragraph-level judgment) + Tier-4 Codex review.

##### Directive

Do not end every paragraph with a sentence that restates the paragraph's point ("In summary, ...", "Thus, the contribution is ...", "Overall, this means ...", "In conclusion, ..."). Summary closers are correct for the final paragraph of a piece, or for a long section that the reader will skim rather than read sequentially. For body paragraphs, trust the content to land its own point; a closer that restates the same claim in different words is noise. The test: if the closer sentence is deleted, does the paragraph still make its point? If yes, delete the closer.

##### BAD → GOOD

- BAD: `We trained the model on 50k query-passage pairs and evaluated on five benchmarks. The model reaches 0.79 recall@10 on our held-out set. Overall, these results demonstrate that our method is effective.`
- GOOD: `We trained the model on 50k query-passage pairs and evaluated on five benchmarks. The model reaches 0.79 recall@10 on our held-out set.`

- BAD (design doc): `We chose two-tower retrieval because query embeddings cache across sessions. Thus, the architecture is well-suited to our caching strategy.`
- GOOD (design doc): `We chose two-tower retrieval because query embeddings cache across sessions.`

- BAD (proposal): `The proposed work advances retrieval-augmented generation for medical question answering. In summary, the project combines several research directions into a unified framework.`
- GOOD (proposal): `The proposed work advances retrieval-augmented generation for medical question answering.`

- BAD (blog): `The bug was a single-character typo in the crontab (five asterisks instead of "0 hour"). In conclusion, this small typo caused a large outage.`
- GOOD (blog): `The bug was a single-character typo in the crontab: five asterisks instead of the intended hourly schedule.`

- BAD (paper): `Our method reaches 88.3% top-1 on ImageNet-1k, 1.2 points above Wang et al. 2025. Overall, our approach sets a new benchmark on ImageNet.`
- GOOD (paper): `Our method reaches 88.3% top-1 on ImageNet-1k, 1.2 points above Wang et al. 2025.`

##### Rationale for AI Agent

LLMs often add paragraph-closing summaries because academic and expository corpora include "topic sentence + body + summary sentence" structures prominently. The closer signals "I am finishing this thought" but adds no new information. Technical readers who skim skip the closer anyway (they read the topic sentence and the first specific claim); careful readers feel the redundancy as padding. Related: RULE-04 catches word-level filler phrases; RULE-E catches the paragraph-level padding pattern that RULE-04's word-level deny list does not reach. Both rules cut needless content; they operate at different structural levels (word versus paragraph).

#### RULE-F: Use Consistent Terms; Do Not Redefine Abbreviations Mid-Document

- **source**: My observation of LLM output across dozens of writing projects and code releases, 2022–2026. Adjacent to `agent-config` / `anywhere-agents` AGENTS.md Writing Defaults: "Use consistent terms. If an abbreviation is defined once, do not define it again later."
- **agent-instruction evidence**: Zhang et al. 2026 supports negative phrasing for anti-pattern directives in coding-agent instruction files (does not validate mechanical enforcement). Bohr 2025 supports pairing directives with examples for stronger initial style control over a paired two-turn code-generation workflow (not open-ended prose).
- **severity**: medium. Recurring clarity failure in long documents; varied terms force the reader to check whether each new term refers to the same concept or a new one.
- **scope**: `.md`, `.tex`, `.rst`, `.txt`, and prose sections of source files.
- **enforcement**: Tier-2 (first-use abbreviation tracking across document; flag later re-expansions and flag synonym drift when a defined abbreviation is replaced with a paraphrase without reason) + Tier-3 agent self-check + Tier-4 Codex review.

##### Directive

Once you introduce a term or abbreviation, keep using it. Do not alternate "large language model", "LLM", "language model", "LM", "neural language model", "foundation model" as synonyms for the same thing. Do not redefine an abbreviation: if `LLM` was defined as `large language model` in the introduction, do not expand it again in section 3. For the reader, a consistent term signals "this is the same concept I saw earlier"; varied terms signal "I should check whether this is something new."

##### BAD → GOOD

- BAD (paper, term drift): introduces "large language models (LLMs)" in §1, then writes in §3: "Neural language models achieve..."
- GOOD (paper): introduces "large language models (LLMs)" in §1, then writes in §3: "LLMs achieve..."

- BAD (doc, expansion re-emerges): "We use retrieval-augmented generation (RAG). ... / later / Retrieval-augmented-generation architectures..."
- GOOD (doc): "We use retrieval-augmented generation (RAG). ... / later / RAG architectures..."

- BAD (API doc, drift across synonyms): "The `/users` endpoint returns user objects. ... / later / The user endpoint supports filtering. ... / later / Our user resource accepts query parameters ..."
- GOOD (API doc): "The `/users` endpoint returns user objects. ... / later / `/users` supports filtering. ... / later / `/users` accepts query parameters ..."

- BAD (proposal, specific-aim drift): "Aim 1 focuses on retrieval. ... Aim 1 addresses document selection. ... The first aim investigates retrieval-augmented generation."
- GOOD (proposal): "Aim 1 focuses on retrieval. ... Aim 1 addresses document selection. ... Aim 1 investigates retrieval-augmented generation."

- BAD (runbook, system synonyms): "If the service is down, restart the service. If `app-v2` is offline, bounce the worker pool. If the backend stops responding, failover."
- GOOD (runbook): "If `app-v2` is offline, restart via `systemctl restart app-v2.service`. If `app-v2` still fails, failover to the replica."

##### Rationale for AI Agent

LLMs often vary terminology within a document because variety is mildly rewarded in the training distribution (reviewers and editors mark repetitive vocabulary as prose to be varied, and LLMs learn to alternate). But in technical writing, variety across terminology for the same entity masks the entity's identity and forces the reader to check whether each new term refers to the same concept. RULE-01 covers the first-use introduction of terms; RULE-F covers keeping them consistent thereafter. Gopen & Swan 1990 discuss this under "topic continuity", where subjects and entities should reappear as the same linguistic form across sentences. For documents produced in multi-turn generation, the risk is especially high because the model samples each new paragraph without guaranteed visibility into earlier-introduced terms, leading to drift. The fix at generation time: after defining a term, the agent should maintain a running glossary for the document and re-use the defined form consistently.

#### RULE-G: Use Title Case for Section and Subsection Headings

- **source**: My observation of LLM output across dozens of writing projects and code releases, 2022–2026. LLMs default to sentence case for Markdown and LaTeX headings; in academic and engineering contexts that call for title case, the sentence-case drift is a visible AI-tell.
- **agent-instruction evidence**: Zhang et al. 2026 supports negative phrasing for anti-pattern directives in coding-agent instruction files; RULE-G uses a positive directive because applying title case is a constructive placement rather than an anti-pattern to flag. Bohr 2025 supports pairing directives with examples for stronger initial style control over a paired two-turn code-generation workflow (not open-ended prose).
- **severity**: low. Polish rather than comprehension; readers recover meaning from either case. Pattern is high-visibility however because headings are the first thing a skimmer sees.
- **scope**: `.md`, `.tex`, `.rst`, `.txt`, and similar structural heading surfaces.
- **enforcement**: Tier-1 `ask` (heading-style check; H2/H3/H4 starting with sentence-case pattern flagged for title-case conversion, excluding question-style or full-sentence headings where sentence case is intended) + Tier-3 agent self-check.

##### Directive

Capitalize the first word, the last word, and all major words (nouns, verbs, adjectives, adverbs, pronouns) in section and subsection headings. Lowercase articles (`a`, `an`, `the`), coordinating conjunctions (`and`, `but`, `or`, `nor`), and short prepositions (`of`, `in`, `on`, `to`, `for`, `by`, `at`, `with`). This applies in Markdown (H1 through H6), LaTeX (`\section`, `\subsection`, `\subsubsection`), reStructuredText, and similar structural-heading surfaces. Does not apply to sentence-style titles (question-form headings or full-sentence article titles where sentence case is intended).

##### BAD → GOOD

- BAD (Markdown): `## Experimental results and analysis`
- GOOD (Markdown): `## Experimental Results and Analysis`

- BAD (LaTeX): `\subsection{Limitations and future work}`
- GOOD (LaTeX): `\subsection{Limitations and Future Work}`

- BAD (README): `## Getting started with the API`
- GOOD (README): `## Getting Started with the API`

- BAD: `### Related work in medical image retrieval`
- GOOD: `### Related Work in Medical Image Retrieval`

- BAD: `## Evaluating on out-of-distribution data`
- GOOD: `## Evaluating on Out-of-Distribution Data`

##### Rationale for AI Agent

LLMs default to sentence case for Markdown and LaTeX headings because their training data includes a substantial amount of modern blog and docs-site Markdown where sentence case is the convention (large platform developer documentation and docs-site prose). But academic and engineering venues (most conferences, most IEEE and ACM journals, most research groups' README conventions) use title case. A document with sentence-case headings inside a title-case context reads as machine-generated or unedited. The fix is mechanical: apply title case at heading write time. This rule is low-severity in terms of comprehension (readers recover meaning regardless) but high-visibility in terms of AI-tell detection, because headings are the first thing a skimmer sees, and miscased headings signal inattention.

#### RULE-H: Support Factual Claims with Citation or Concrete Evidence; Do Not Be Handwavy

- **source**: My observation of LLM output across dozens of writing projects and code releases, 2022–2026. Adjacent to `agent-config` / `anywhere-agents` AGENTS.md Writing Defaults: "If citing papers, verify that they exist." This rule is the flagship of the three-rule cluster against handwavy prose (RULE-03 on vague nouns, RULE-08 on uncalibrated verbs, RULE-H on unsupported claims).
- **agent-instruction evidence**: Zhang et al. 2026 supports negative phrasing for anti-pattern directives in coding-agent instruction files (does not validate mechanical enforcement). Bohr 2025 supports pairing directives with examples for stronger initial style control over a paired two-turn code-generation workflow (not open-ended prose).
- **severity**: critical. Uncited claims are a trust failure; fabricated citations are worse (permanent damage to reader trust once the fabrication is discovered). LLMs both default to citation-free hedges ("prior work shows", "recent studies suggest") and actively hallucinate plausible-looking citations that do not exist (Ji et al. 2023 survey of hallucination in NLG; Agrawal et al. 2024 empirical measurement).
- **scope**: `.md`, `.tex`, `.rst`, `.txt`, and prose sections of source files.
- **enforcement**: Tier-3 agent self-check (judgment about what needs attribution) + Tier-4 Codex review as primary gate. Supporting practice for agents: before writing any `Author Year` citation, verify via search (DBLP, arXiv, Google Scholar, or the cited paper's own bibliography) that the reference exists and supports the cited claim; otherwise mark `[UNVERIFIED]` placeholder or rewrite the sentence. Never generate a citation without verification.

##### Directive

When a sentence asserts a factual claim that warrants attribution (empirical result, published method, community consensus, comparative benchmark, historical fact), provide a verifiable citation, or name the specific source (a paper by author and year, a benchmark, a dataset, an observed experiment). Do not write handwavy attributions ("prior work shows", "it is well known that", "recent studies suggest", "many researchers believe") without naming the specific work. When the claim is the author's own observation, state the concrete evidence (number, dataset, experiment, condition). Never invent a citation; if the cited paper cannot be verified, remove the claim, soften it to the author's own observation, or mark `[UNVERIFIED]` and flag for review.

##### BAD → GOOD

- BAD (paper): `Prior work has shown that late-interaction retrieval improves over lexical retrieval.`
- GOOD (paper): `Khattab and Zaharia 2020 (ColBERT) report MS MARCO passage-ranking MRR@10 of 0.360 for ColBERT versus 0.187 for BM25-Anserini, using contextualized late interaction over BERT token embeddings.`

- BAD: `It is widely accepted that longer context improves RAG performance.`
- GOOD: `Liu et al. 2023/2024 (TACL, "Lost in the Middle") show that models answer less accurately when the relevant evidence is in the middle of a long context than near the beginning or end; Dsouza et al. 2024 report the same lost-in-the-middle pattern for GPT-4 and Claude 3 Opus.`

- BAD (paper): `Several studies have demonstrated the effectiveness of this approach.`
- GOOD (paper): `In our reproduced evaluation, the model improves GSM8K exact-match accuracy from 92.1% to 95.2% and MATH exact-match accuracy from 48.0% to 51.4% under the same decoding settings.`

- BAD (grant proposal): `Our pilot results look promising.`
- GOOD (grant proposal): `Our pilot (N=30 cohort, 3-month follow-up) shows AUROC 0.84 for the primary endpoint versus 0.72 for the standard-of-care baseline (p=0.012).`

- BAD (blog post): `Many researchers believe that contrastive learning produces better embeddings.`
- GOOD (blog post): `Chen et al. 2020 (SimCLR) report 76.5% ImageNet top-1 linear-evaluation accuracy for a self-supervised ResNet-50, a 7% relative gain over prior self-supervised methods and comparable to a supervised ResNet-50 baseline in their setup.`

- BAD (commit message): `Fix based on user feedback.`
- GOOD (commit message): `Fix null-pointer crash reported in issue #1847 (reproducible with empty cart).`

##### Rationale for AI Agent

LLMs produce handwavy, citation-free claims as a default register absorbed from formulaic abstract and review prose in the training corpus. Phrases like "prior work shows", "recent studies suggest", "it is well known that", "many researchers believe" appear at high frequency in academic introductions and review articles, where they serve as transition filler between specific claims. LLMs sample them at comparable rates without carrying the specific attributions that human authors have in mind when writing them. Additionally, LLMs hallucinate citations that look plausible (matching author conventions, year ranges, venue patterns) but point to non-existent papers; the hallucination rate is well-documented across domains. Both failures compound: an uncited claim is unverifiable, and a fabricated citation is worse than no citation because it damages reader trust permanently once discovered. The operational test before writing any factual-claim sentence: is there a specific, verifiable source, observation, or number behind this? If yes, state it by author and year, or by dataset and measurement. If no, either find the source before writing, or rewrite the sentence as a claim about the author's own experience (which must still be concrete: numbers, dataset, conditions). For LLMs specifically: never generate a citation without first verifying via DBLP, arXiv, Google Scholar, or the cited paper's own bibliography. If verification is not possible in the current session, mark `[UNVERIFIED]` and flag for review. Related: RULE-03 fights vague nouns; RULE-08 fights uncalibrated verbs; RULE-H fights unsupported claims. All three aim at specific, verifiable, honest prose; a single sloppy sentence often fires all three rules simultaneously.

#### RULE-I: Prefer Full Forms over Contractions in Technical Prose

- **source**: My observation of LLM output across dozens of writing projects and code releases, 2022–2026. Adjacent to `agent-config` / `anywhere-agents` AGENTS.md Formatting Defaults: "Prefer full forms such as 'it is' and 'he would' rather than contractions."
- **agent-instruction evidence**: Zhang et al. 2026 supports negative phrasing for anti-pattern directives in coding-agent instruction files; RULE-I uses a positive directive because preferring full forms is a constructive placement rather than an anti-pattern to flag. Bohr 2025 supports pairing directives with examples for stronger initial style control over a paired two-turn code-generation workflow (not open-ended prose).
- **severity**: low. Register rather than comprehension; readers parse contractions correctly. Flagged for consistency because register drift (a contraction in otherwise formal prose) reads as careless.
- **scope**: `.md`, `.tex`, `.rst`, `.txt`, and prose sections of source files.
- **enforcement**: Tier-1 `ask` (contraction list: "it's", "doesn't", "don't", "won't", "can't", "I'm", "you're", "we're", "they're", "that's"; flagged with expansion suggestion) + Tier-3 agent self-check.

##### Directive

In formal technical prose (research papers, grant proposals, API specifications, technical documentation), prefer "it is" over "it's", "does not" over "doesn't", "cannot" over "can't", "will not" over "won't", "I am" over "I'm", "you are" over "you're". Contractions are acceptable in informal registers (blog posts, release notes, commit messages, casual documentation), but even there, be deliberate: a contraction sets a register, and if the surrounding prose is formal, the contraction reads as a tonal break. The operational test: if the surrounding sentences use full forms, the contraction stands out; if the surrounding sentences use contractions, the full form stands out. Pick the register and hold it within the document.

##### BAD → GOOD

- BAD (paper): `It's worth noting that the model doesn't converge when the learning rate is too high.`
- GOOD (paper): `The model does not converge when the learning rate is too high.` (The "it is worth noting that" phrase is itself filler and should also be cut per RULE-04.)

- BAD (proposal): `We've shown in prior work that this approach isn't sensitive to initialization.`
- GOOD (proposal): `We have shown in prior work that this approach is not sensitive to initialization.`

- BAD (API spec): `If the request body can't be parsed, the endpoint won't return a 200 response.`
- GOOD (API spec): `If the request body cannot be parsed, the endpoint does not return a 200 response.`

- BAD (technical spec): `The client shouldn't retry on 4xx errors.`
- GOOD (technical spec): `The client must not retry on 4xx errors.`

- BAD (register drift in paper abstract): opens with full forms, then: `Our results show it's possible to achieve this with less compute.`
- GOOD (paper abstract): `Our results show that it is possible to achieve this with less compute.`

##### Rationale for AI Agent

LLMs produce contractions in technical prose at higher rates than skilled human writers do, because the training corpus mixes formal registers (papers, specifications, government documents) and informal registers (blog posts, forum answers, release notes), and LLMs sample across them without register-matching the surrounding prose. The effect: within a single formal paragraph, one or two contractions appear where a careful writer would have used full forms. Contractions are not wrong; they are register markers. In formal technical prose (the target scope of this ruleset), full forms are the expected register. In informal surfaces (release notes, blog posts, commit messages), contractions are acceptable and sometimes preferred for voice. The rule is about consistency with the surrounding register: pick one and hold it within a document, rather than drifting mid-paragraph.
<!-- rule-pack:agent-style:end -->

<!-- rule-pack:profile:begin version=main sha256=38203e4237b48b3f949dbfb3954c2e967364a48893ed1353ef0a2b62ab837831 -->
<!-- SPDX-License-Identifier: CC-BY-4.0 -->

<!--
Personal profile rule pack for Yue Zhao (yzhao062).

This file is composed as passive content into a consumer project's
AGENTS.md by the anywhere-agents bootstrap when the consumer references
this pack in agent-config.yaml. Any agent reading AGENTS.md
(Claude Code, Codex, others) gets this profile on session start.

Mirrors RULES.md / a single source of truth for the profile pack.
-->

# User Profile (yzhao062)

The following bullets describe the user the agent is working with. Use
this context to tailor tone, default tooling, terminology, and venue
conventions. Project-specific or task-specific instructions still
override these defaults when they conflict.

## Identity

- Yue Zhao, Computer Science faculty at the University of Southern California (USC).
- Research focus: machine learning, anomaly detection, outlier ensembles, automated tabular ML, and applied AI for science.
- Personal site: <https://yzhao062.github.io>.
- Public author identity for citations: "Yue Zhao" (Yue is the given name, Zhao is the family name).

## Public projects

- [PyOD](https://github.com/yzhao062/pyod): Python anomaly detection library. Around 9.8k GitHub stars, 38M+ total downloads, ~12k research citations.
- [PyGOD](https://github.com/pygod-team/pygod): graph outlier detection library, sister project to PyOD.
- [anywhere-agents](https://github.com/yzhao062/anywhere-agents): public AI agent configuration with pack architecture.
- [agent-style](https://github.com/yzhao062/agent-style): writing rule pack covering AI-tell vocabulary, formatting, and field-observed LLM patterns.
- [agent-config](https://github.com/yzhao062/agent-config): personal working dir and canonical source for anywhere-agents.
- [agent-pack](https://github.com/yzhao062/agent-pack): this repo, personal pack and reference example for third-party pack authors.

## Communication preferences

- Casual tone. "Yue" is preferred over "Dr. Zhao" for one-on-one work; use "Dr. Zhao" only in formal correspondence.
- Bilingual EN / ZH. Switch language by context; do not translate code, paths, or technical identifiers.
- Pacific Time (Los Angeles).
- Direct over diplomatic. Flag disagreements explicitly rather than soften them; the user prefers a fast back-and-forth over a cushioned monologue.

## Common tasks and venue conventions

- **Research papers.** NeurIPS, ICML, ICLR, KDD, NeurIPS-DB tracks default. ACL / EMNLP for NLP work; CVPR / ICCV for vision.
- **Funding proposals.** NSF Merit Review framework default; NIH Simplified Peer Review when the call is biomedical. DOE / DOD only on explicit request. Avoid DEI-related terms in NSF / federal proposals unless the solicitation explicitly requires them.
- **Reviews.** Code reviews use the [`implement-review`](https://github.com/yzhao062/anywhere-agents/blob/main/skills/implement-review/SKILL.md) skill (dual-agent: Claude Code implements, Codex reviews). Paper / proposal reviews follow the same pattern with content-type lenses.
- **Writing discipline.** Follows the [`agent-style`](https://github.com/yzhao062/agent-style) 21-rule pack: 12 classic rules (Strunk / White / Orwell / Pinker tradition) + 9 field-observed LLM patterns (em-dash overuse, summary-tail paragraphs, sentence-opener repetition, transition word overuse, and so on).

## Tools and stack

- Python primary. Miniforge `py312` environment as default; prefer `mamba` over `conda` for installs.
- LaTeX for papers and proposals; Markdown for documentation; reStructuredText where Sphinx is in play.
- Claude Code is the primary workhorse (drafting, implementation, research). Codex is the gatekeeper (review, feedback, quality checks).
- macOS / Windows / Linux all in active use. PyCharm and VS Code as editors.
- GitHub for source control; `gh` CLI for PR / issue work.

## Active focus snapshot

This block goes stale fastest. Treat as a snapshot of what the user is
likely working on at the time of bootstrap; if the date below is older
than a few months, recent context probably differs.

- Snapshot date: 2026-04 (post v0.4.0 release of `anywhere-agents`).
- `pyod` 3 — third major release, expanding modern detector coverage.
- `anywhere-agents` v0.4.x → v0.5.0 — wiring composer-side locks, startup reconciliation, and private-source pack support with auth chain.
- `agent-style` ongoing curation of the 21-rule pack as new LLM patterns surface.
- Active research themes: outlier-detection foundation models, automated detector selection, large-scale benchmark curation.

## Defaults agents should follow

- Confirm before any `git commit` or `git push`. This is non-negotiable across all projects.
- Use `git -C <path>` rather than `cd <path> && git ...` to avoid compound-command approval prompts.
- Verify cited papers actually exist before generating a citation; mark `[UNVERIFIED]` if unable to verify.
- For BibTeX, provide entries that copy cleanly into a `.bib` file; never invent venue / year fields.
- Treat the writing rules in [`agent-style`](https://github.com/yzhao062/agent-style) as binding for all `.md` / `.tex` / `.rst` / `.txt` writes.
<!-- rule-pack:profile:end -->

<!-- rule-pack:paper-workflow:begin version=main sha256=543fff3bbec608e808aaddef1e4bf44e9efde097400f93d97aa6ebe411a5b5ef -->
<!-- SPDX-License-Identifier: CC-BY-4.0 -->

<!--
Paper-workflow rule pack: conventions for paper / proposal repos that
use Overleaf submodules and co-PI collaboration. Composed as passive
content into the consumer AGENTS.md by anywhere-agents bootstrap
when the consumer references this pack in agent-config.yaml.

Load this pack on paper / proposal repos. Skip on prototype / OSS repos.
-->

# Paper and Proposal Workflow

Conventions for academic-writing repos that use Overleaf submodules and
co-PI collaboration. Apply when the project is a paper or proposal with
a `.gitmodules` file or an Overleaf-synced subdirectory.

## Submodule Workflow

- Some projects use git submodules for directories shared with collaborators (e.g., co-PI proposal repos, shared paper repos linked to Overleaf).
- At session start, if `.gitmodules` exists, run `git submodule status` to check submodule state. If submodules are uninitialized (prefix `-`), warn the user and suggest `git submodule update --init`.
- Submodule directories have their own `.git` and `origin` remote. Commits and pushes inside a submodule go to the submodule's upstream repo, not the parent.
- **Submodules are shared repos.** Pushes land directly in a collaborator's Overleaf project or co-PI repo. A careless force-push or overwrite can destroy someone else's work. Treat every write operation inside a submodule as high-risk.
- When the user asks to push or pull a submodule:
  1. Before writing, run `git -C <submodule-path> fetch` then `git -C <submodule-path> status` to check for uncommitted local changes. Review recent history with `git -C <submodule-path> log --oneline -5` to see local commits and `git -C <submodule-path> log --oneline -5 --remotes` to see recent remote-tracking activity. This is a quick sanity check, not a full divergence analysis; submodules are often in detached-HEAD state where branch comparisons do not apply cleanly.
  2. Use `git -C <submodule-path>` for git operations inside the submodule. Always confirm with the user before any commit, push, pull, or reset.
  3. Back in the parent repo, update the submodule pointer: `git add <submodule-path>` then commit (also requires confirmation).
- Submodules may have a `.gitignore` that excludes internal-only files (e.g., `.agent/`, `guardrail/`, `figure-spec/`, `figure-src/`). These files exist on disk but are not pushed to the collaborator repo. On a fresh clone, they will be missing. Warn the user if expected internal directories are absent.
- `context/` is synced to co-PI repos and will be available after submodule init.
- Project-specific submodule details (which directories, which upstream repos, which files are internal-only) belong in `CLAUDE.md` or `AGENTS.local.md` in each project repo, not here.

## Overleaf Merge Conflict Resolution

Overleaf-synced repos (usually submodules) require special care during merges. Overleaf's git bridge creates branches from its own snapshot, which may lag behind the latest local push. When a collaborator edits on Overleaf while we push structural changes locally, the Overleaf branch is based on the **pre-push** state. In a merge, "theirs" means "older base plus collaborator styling edits," not "collaborator's newer version." Using `git checkout --theirs` on such files silently discards our work.

**Co-PI changes are the priority.** Our own structural work (compaction, renames) can be redone in minutes because we know exactly what we changed. A co-PI's content changes on Overleaf -- new sentences, rewritten arguments, added references, terminology choices -- represent their intellectual contribution. If we silently drop their edits, we may not even know what was lost, and they may not notice until weeks later. Losing their work is an order of magnitude worse than losing ours. The merge must preserve both sides, but when in doubt, err toward preserving the co-PI's content.

### Rules for merging Overleaf branches with conflicts

1. **Never use `git checkout --theirs`** on files where we have local structural changes (compaction, renames, reorganization). This is the single most dangerous command in an Overleaf merge.
2. **Never use `git checkout --ours` and stop there.** Starting from our version is correct, but the merge is not done until the co-PI's content changes are accounted for. Treating `--ours` as the final answer silently drops their work.
3. **Inspect what the collaborator actually changed** before resolving. First find the merge base: `git merge-base HEAD <overleaf-branch>`. Then run `git diff <merge-base>..<overleaf-branch> -- <file>` to isolate the co-PI's edits relative to the common ancestor, without mixing in our structural changes. Classify each change as:
   - **Content** (new sentences, rewritten arguments, added references, deliberate deletions or shortenings, terminology changes) -- must be preserved. Treat co-PI deletions with the same care as additions; if they removed text, that was a deliberate editorial decision, not noise.
   - **Formatting** (spacing, font commands, styling) -- apply if consistent with our version.
   - **Stale reversions** (undoes our rename or compaction because they edited the pre-push snapshot) -- discard, but note that the co-PI has not seen our change yet. Be careful: a change that looks like a stale reversion may actually be a deliberate content choice. When ambiguous, ask the user.
4. **Apply their content changes onto our structural base.** Start from `git checkout --ours <file>`, then manually integrate every content change identified in step 3. Do not skip any co-PI content change without explicit user approval.
5. **Double-verify before committing** -- check both directions:
   - `git diff <pre-merge-commit> -- <file>` -- confirm our structural changes survived.
   - `git diff <overleaf-branch> -- <file>` -- confirm the only differences from the co-PI's version are our intended structural changes, not dropped content.
   - If the co-PI added entirely new paragraphs or sections, verify they appear in the merged file.
6. **Screen for binary artifacts before staging.** Overleaf branches often carry compiled PDFs, review screenshots (`out-review/`), or other build artifacts that should not be tracked. Use the same merge-base diff from pre-merge checklist step 2 to spot unexpected large files. Add them to `.gitignore` before staging the merge.

### Pre-merge checklist (run before `git merge <overleaf-branch>`)

1. `git fetch` to get the latest Overleaf branch.
2. `git diff --stat $(git merge-base HEAD <overleaf-branch>)..<overleaf-branch>` -- check which files the co-PI actually touched, spot binary artifacts.
3. `git log --oneline HEAD..<overleaf-branch>` -- understand what the collaborator did.
4. If any files we modified structurally appear in the diff, plan to resolve those conflicts manually using the rules above.
5. If the co-PI touched files we did not modify, those should auto-merge cleanly. After the merge, still spot-check them for unintended content loss.

### Recovery if `--theirs` was already used

Restore our structural version from the pre-merge commit with `git restore --source=<pre-merge-commit> --worktree -- <file>` (avoids encoding and line-ending issues from shell redirection on Windows). Then reapply the collaborator's content and formatting changes on top. Do not skip the reapply step -- their work matters too.

## Venue Conventions

For NSF / federal proposal work, do not introduce DEI-related terms unless the solicitation explicitly requires them. For non-federal proposals or calls that explicitly request DEI framing or terminology, follow the call requirements instead of applying a blanket ban.

NSF Merit Review framework defaults: intellectual merit + broader impacts. NIH Simplified Peer Review framework on biomedical proposals.

For paper venues, follow the venue's specific guidelines (NeurIPS / ICML / ICLR / KDD / ACL / EMNLP / CVPR). Do not generate venue-specific formatting (camera-ready, anonymous-version, etc.) unless asked.
<!-- rule-pack:paper-workflow:end -->
