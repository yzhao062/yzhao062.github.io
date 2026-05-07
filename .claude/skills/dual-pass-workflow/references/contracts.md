# Contracts

## Task Packet

Use `workflow.yaml` to declare the collaboration contract when you need explicit control. Keep it short.

Required fields:

- `task_type`
- `goal`
- `selected_skills`
- `task_root`
- `primary_result`
- `artifact_dir`
- `sources_of_truth`
- `constraints`
- `acceptance_criteria`
- `verification`

Recommended optional fields:

- `pass_mode`
- `builder_agent`
- `checker_agent`
- `skill_roles`
- `workspace_contract`
- `protected_regions`
- `notes`
- `workflow_artifacts`

Recommended shape:

```yaml
task_type: ""
goal: ""
selected_skills: []
pass_mode: ""
builder_agent: ""
checker_agent: ""
task_root: "."

# String for single-file output; list for multi-file coordinated output.
primary_result: ""
# primary_result:
#   - file: "00-project-summary.tex"
#     role: "summary"
#   - file: "00-project-description.tex"
#     role: "main-narrative"

artifact_dir: ""
sources_of_truth: []
constraints: []
acceptance_criteria: []

# Flat list for simple tasks; ordered pipeline for staged preflight.
verification: []
# verification:
#   - step: "integrity-check"
#     artifact: "outputs/pdf-safety-check.md"
#     blocking: true
#   - step: "extraction-quality"
#     artifact: "outputs/pdf-extraction-check.md"
#     blocking: true

# Optional: role-based multi-skill coordination.
# skill_roles:
#   primary: "nsf-proposal-composer"
#   compliance: "nsf-proposal-guardrail"
#   refinement: "nsf-thrust-refiner"
#   citation: "<citation-skill>"

# Optional: paths that must exist before first-pass.
# workspace_contract:
#   required_paths:
#     - "templates/paper-deck-base.tex"
#     - "theme/beamerthemeuscmoloch.sty"
#   check_before: "first-pass"

# Optional: regions the second-pass must not rewrite.
# protected_regions:
#   marker_prefix: "refiner:body"
#   policy: "audit-only"

workflow_artifacts:
  build_note: ""
  handoff_note: ""
  audit_note: ""
  reconcile_note: ""
notes: ""
```

## Field Details

### `primary_result` — String Or List

When a single file is the canonical output, use a string:

```yaml
primary_result: "outputs/review.md"
```

When the task produces a coordinated file set with no single dominant file, use a list:

```yaml
primary_result:
  - file: "00-project-summary.tex"
    role: "summary"
  - file: "00-project-description.tex"
    role: "main-narrative"
  - file: "11-aim1.tex"
    role: "unit"
  - file: "20-evaluation.tex"
    role: "evaluation"
```

When `primary_result` is a list, the second-pass agent audits all listed files. Reconciliation must update all files that the audit touched. The `role` field is optional but helps the auditor understand which file serves which function.

### `verification` — Flat List Or Ordered Pipeline

A flat list is the default and remains valid for simple tasks:

```yaml
verification:
  - "run tests"
  - "check formatting"
```

An ordered pipeline expresses multi-stage preflight where some steps must pass before drafting begins:

```yaml
verification:
  - step: "integrity-check"
    artifact: "outputs/pdf-safety-check.md"
    blocking: true
  - step: "extraction-quality"
    artifact: "outputs/pdf-extraction-check.md"
    blocking: true
  - step: "packet-consistency"
    artifact: "outputs/packet-consistency-check.md"
    blocking: false
```

Steps marked `blocking: true` must pass before the first-pass draft begins. Steps marked `blocking: false` produce advisory artifacts. Run steps in the declared order.

### `skill_roles` — Multi-Skill Coordination

Use `skill_roles` instead of the flat `selected_skills` list when the task involves coordinated multi-skill work:

```yaml
skill_roles:
  primary: "nsf-proposal-composer"
  compliance: "nsf-proposal-guardrail"
  refinement: "nsf-thrust-refiner"
  citation: "<citation-skill>"
```

The `primary` role is the main domain skill. Other roles are consulted by the primary skill at defined escalation points. The dual-pass workflow does not orchestrate inter-skill calls; it records which skill fills which role so the second-pass agent understands the coordination structure.

`selected_skills` remains valid as the simple case.

### `workspace_contract` — Environment Precondition

Declare paths that must exist before work starts:

```yaml
workspace_contract:
  required_paths:
    - "README.md"
    - "templates/paper-deck-base.tex"
    - "theme/beamerthemeuscmoloch.sty"
  check_before: "first-pass"
```

If any required path is missing at the step named in `check_before`, stop and ask instead of improvising.

### `protected_regions` — Second-Pass Boundaries

Declare file regions that the second-pass must not rewrite:

```yaml
protected_regions:
  marker_prefix: "refiner:body"
  policy: "audit-only"
```

When `policy` is `audit-only`, the second-pass agent may reference and comment on protected regions in the audit, but reconciliation must not modify content between matching markers. Use `read-write` only when the user explicitly unlocks protected regions.

## When `workflow.yaml` Is Optional

You do not need `workflow.yaml` when all of the following are already obvious from the task layout or domain skill:

- the task root
- the canonical output
- the artifact directory
- the source-of-truth files
- the verification steps

Example in this repo:

- a review folder already implies `outputs/review.md` as the canonical result
- `outputs/` is already the artifact directory
- `review.yaml` and the `intake/` files already define most of the packet

In that case, create workflow notes directly under the existing artifact directory and use `workflow.yaml` only if you want to pin agent roles, acceptance criteria, or non-default checks.

## Pass Modes

Preferred external language:

- `first-pass`: create the main result and stop if it is good enough
- `second-pass`: audit the first pass and optionally reconcile it

Internal files may still use names such as `build.<agent>.md`, `handoff.<agent>.md`, `audit.<agent>.md`, and `reconcile.md`.

## Output Contract

The domain skill keeps control of the canonical output. The workflow adds only supporting artifacts.

Required decisions:

- `task_root`: the folder that contains the task packet and task-local outputs
- `primary_result`: the canonical file or file set that represents the final answer
- `artifact_dir`: the directory for workflow notes
- `verification`: the checks that must run after build and after reconcile

Optional decision:

- `pass_mode`: `first-pass` or `second-pass`

Default artifact names:

- `workflow.yaml`
- `build.<agent>.md`
- `handoff.<agent>.md`
- `audit.<agent>.md`
- `reconcile.md`

## Integration Rule

Do not move the main output just to satisfy the workflow.

Examples:

- Review packet: keep `outputs/review.md` as canonical, add workflow notes under `outputs/`.
- Code task in a repo: keep the edited source files as canonical, add workflow notes under `.agent/<task-id>/` or an existing task-local artifact directory.
- Writing task: keep the requested draft file as canonical, add workflow notes next to it or under an existing `outputs/` directory.
- NSF proposal: keep the `.tex` file set as canonical, add workflow notes under `<proposal-dir>/` or an existing artifact directory.

## Builder Handoff Contract

`handoff.<agent>.md` should answer:

- What changed?
- Which assumptions might fail?
- What verification actually ran?
- What is still unresolved?
- What should the checker focus on first?

## Audit Contract

`audit.<agent>.md` should separate:

- factual or behavioral issues
- unsupported claims or assumptions
- missed requirements
- clarity or structure issues
- citation integrity issues (key resolves but paper does not support the claim) — include when the task involves citations

For high-stakes tasks, order findings by severity.

If no second pass is used, `audit.<agent>.md` and `reconcile.md` are not required.
