"""Reconcile news-search-candidates.jsonl status fields against the schema lifecycle.

Round 2 reconciled 13 specific rows that were promoted/held/demoted in this sweep.
Round 3 normalizes the remaining schema drift Codex flagged:

- 5 undocumented statuses (counted_as_row_expansion x2, deferred_not_counted,
  upcoming_not_counted, candidate_not_counted) -> map to canonical statuses
- 19 blank statuses -> set based on tier_guess (drops -> dropped; otherwise -> candidate)
- 7 lingering candidate-promote rows (Amazon Science/Salesforce/Microsoft/Databricks x3/
  Walmart Labs lower-star code-adoption rows) -> dropped with subsumed-by-aggregate note
- Line 28 OpenAI Careers stale ledger pointer #66cy -> #8g; add tier_guess T0(b)
- Line 120 Wells Fargo tier_guess T2 -> T3 to match new non-FM-co-careers Ledger 3 rule

The JSONL is gitignored scratch, but the schema is committed: the contract is one-way
(JSONL must follow schema). Older entries pre-status-lifecycle are normalized here so
the next Phase B run does not see drift.
"""
import json
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
PATH = REPO / "news-search-candidates.jsonl"

SUBSUMED_NOTE = (
    "Subsumed by Ledger 3 #66di PyOD GitHub Dependents aggregate row "
    "(5,493 repos + 139 packages, 2026-05-07 snapshot). "
    "Snapshot evidence preserved here; not individually counted in any ledger."
)
SUBSUMED_LEDGER = "Ledger 3 #66di (aggregate)"

raw = PATH.read_text(encoding="utf-8").splitlines()
out = []
changes = 0

for i, line in enumerate(raw, start=1):
    if not line.strip():
        out.append(line)
        continue

    rec = json.loads(line)
    status = rec.get("status", "")
    tier_guess = rec.get("tier_guess", "")
    src = rec.get("source", "")
    changed = False

    # 1) Line-specific fixes Codex called out by row number
    if i == 28 and "OpenAI Careers" in src:
        # Stale ledger pointer #66cy -> #8g; add tier_guess T0(b)
        if rec.get("ledger") != "Ledger 1 #8g":
            rec["ledger"] = "Ledger 1 #8g"
            changed = True
        if rec.get("tier_guess") != "T0(b)":
            rec["tier_guess"] = "T0(b)"
            changed = True

    if i == 120 and "Wells Fargo" in src:
        # Non-FM careers now classified Ledger 3 per SKILL.md rev; tier_guess T2 -> T3
        if rec.get("tier_guess") != "T3":
            rec["tier_guess"] = "T3"
            changed = True

    # 2) Map undocumented statuses to canonical schema values
    if status == "counted_as_row_expansion":
        rec["status"] = "counted"  # Already has ledger field per schema's `counted` definition
        changed = True
    elif status == "deferred_not_counted":
        rec["status"] = "dropped"
        rec["notes"] = (rec.get("notes", "").rstrip(". ") + ". " if rec.get("notes") else "") + (
            "Status normalized from legacy 'deferred_not_counted' to canonical 'dropped' "
            "in Codex Round 3; deferral reason preserved above."
        )
        changed = True
    elif status == "upcoming_not_counted":
        rec["status"] = "dropped"
        rec["notes"] = (rec.get("notes", "").rstrip(". ") + ". " if rec.get("notes") else "") + (
            "Status normalized from legacy 'upcoming_not_counted' to 'dropped' in Codex Round 3; "
            "tracked in news-coverage-audit.md Upcoming Visibility Opportunities, not coverage."
        )
        changed = True
    elif status == "candidate_not_counted":
        rec["status"] = "dropped"
        rec["notes"] = (rec.get("notes", "").rstrip(". ") + ". " if rec.get("notes") else "") + (
            "Status normalized from legacy 'candidate_not_counted' to 'dropped' in Codex Round 3."
        )
        changed = True

    # 3) Subsume 7 lingering candidate-promote (lower-star MS/Databricks/Salesforce/Walmart code rows)
    elif status == "candidate-promote":
        # Round 2 already moved Apache/PostHog/MLflow/Genentech/dependents to counted.
        # Anything still candidate-promote is the lower-star code-adoption tail
        # that Codex Round 1 said to fold into the aggregate.
        rec["status"] = "dropped"
        rec["ledger"] = SUBSUMED_LEDGER
        rec["notes"] = (rec.get("notes", "").rstrip(". ") + ". " if rec.get("notes") else "") + (
            "Codex Round 3 disposition: " + SUBSUMED_NOTE
        )
        changed = True

    # 4) Fill blank statuses from tier_guess
    elif status == "":
        if tier_guess == "dropped":
            rec["status"] = "dropped"
            changed = True
        elif tier_guess in {"T0", "T0(b)", "T1", "T2", "T3", "T4", "T5", "topic-validation"}:
            rec["status"] = "candidate"
            changed = True
        else:
            # Unknown tier_guess + blank status -> default to candidate (schema Phase A default)
            rec["status"] = "candidate"
            changed = True

    if changed:
        out.append(json.dumps(rec, ensure_ascii=False))
        changes += 1
    else:
        out.append(line)

trailing_newline = "\n" if raw and raw[-1] == "" else ""
PATH.write_text("\n".join(out) + trailing_newline, encoding="utf-8")
print(f"Updated {changes} rows in {PATH}")
