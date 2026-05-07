<!-- Round 2 -->

# Review

Verification notes: I reviewed the staged diff, rechecked the original NSF-ACCESS proposal task/budget language in `examples/proposals/NSF-ACCESS/<previous-proposal>.zip` (`main.tex` lines 86, 105-112, 131-134, 179-188), and compiled `progress_report.tex` locally. The LaTeX source compiles cleanly on the second pass to a 2-page letter PDF with no overfull/underfull or undefined-reference warnings after rerun.

File/diff scope: staged changes from `git diff --cached` for `proposals/registry.yaml`, `proposals/<project>/README.md`, `proposals/<project>/reason.txt`, `proposals/<project>/progress_report.tex`, `proposals/<project>/progress_report.pdf`, and `template/context/team/<pi>/nsf-access-acknowledgements.md`.

Review lens: `proposal/nsf` plus common proposal dimensions, with extra focus on ACCESS Progress Report / Supplement expectations, remaining-month feasibility, Table 2 to narrative consistency, skim clarity, and formatting compliance.

## New

None.

## Previously raised

### Fixed

1. T3 mislabeled as the largest compute line. This is fixed. `proposals/<project>/progress_report.tex:122-127`, `proposals/<project>/progress_report.tex:143-145`, and `proposals/<project>/reason.txt:16-18` now describe T3 as the largest unfinished workstream rather than the largest original budget line, and Table 2 has been rebalanced to keep T3 at $X00k while shifting T2 to $Y00k at `proposals/<project>/progress_report.tex:158-178`.

2. Burn-rate mismatch unexplained. This is fixed. `proposals/<project>/progress_report.tex:75-85` now gives two concrete causes, expanded open-weight model coverage and less favorable Delta exchange rates, and the short form carries the same explanation at `proposals/<project>/reason.txt:4-10`. For an ACCESS reviewer, this now reads as a real utilization explanation rather than an empty claim of "used everything."

3. Tracker acknowledgement text baked in both allocations verbatim. This is fixed. `template/context/team/<pi>/nsf-access-acknowledgements.md:21-54` is now a real template with an explicit "insert only the allocations actually used" instruction, plus one-allocation and two-allocation examples. That rewrite materially lowers the chance of future over-claiming.

### Still open

1. The publication-evidence issue is improved but not fully closed, because the README still overstates the AAAI paper's acknowledgement status and now contradicts the tracker's own stricter rule. `proposals/<project>/README.md:23` tells the user to add three papers that "acknowledge <ALLOC_A> compute," including the AAAI paper. But the tracker says the AAAI paper published with stale `<ALLOC_B>` boilerplate at `template/context/team/<pi>/nsf-access-acknowledgements.md:82-91`, and its process rule says ACCESS reports should list only papers that cite the target allocation in the camera-ready at `template/context/team/<pi>/nsf-access-acknowledgements.md:129-131`. This is now the only material inconsistency left in the submission instructions.

   Recommended change: revise the README publications step so it matches the tracker exactly. Two clean options:
   - If the ACCESS form should list only papers whose published camera-ready cites `<ALLOC_A>`, tell the user to list only the two ACL 2026 papers and keep the AAAI paper only in the attached progress report with the stale-boilerplate caveat.
   - If the ACCESS form allows papers that used `<ALLOC_A>` compute even when the published acknowledgement is stale, say that explicitly: two papers cite `<ALLOC_A>` directly, while the AAAI paper used `<ALLOC_A>` compute but published with stale `<ALLOC_B>` boilerplate.

### Deferred

None.

### Reopened

None.

## Additional notes

The burn-rate explanation is now concrete and credible. Section 5 and Table 2 are internally consistent after the T2/T3 rebalance. The `reason.txt` caveat reads honest rather than hedged.

There is now page headroom if you want to add one more sentence, but I would spend it only on clarifying the README/publications rule above, not on expanding the narrative elsewhere.
