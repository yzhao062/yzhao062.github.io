# Fan-Out Reliability

A full news-search round dispatches thirty to forty worker lanes. Four separate times during the
2026-08-30 round, lanes were lost while the dispatcher reported success. Those lanes were never
the problem. The scaffolding around them was.

This file records what failed, what the evidence looked like, and the rules that follow. Read it
before building any launcher for a round.

## The One Rule That Covers All Four Failures

**An exit code is not evidence that work happened. A result file is.**

Three waves exited 0 while doing nothing, and two exited 2 while their workers ran to completion.
Neither direction of that signal was reliable. Reconcile every dispatched unit against a **complete**
result file before reporting a wave as finished, and before integrating anything. Complete means
present, non-empty, and not beginning with the `(FALLBACK, worker wrote no result file)` header that
`dispatch-task` writes over a reaped worker.

`prun`'s own flow already says most of this ("every dispatched unit must have a non-empty result").
Skipping it is what let the first failure stay invisible for a full lane generation. Non-empty alone
is too weak, because a salvaged tail is non-empty; see checklist item 5.

## Failure 1: A Unit List Written on Windows Carries CRLF

**What happened.** A generator wrote the unit list with Python's `pathlib.write_text`. On Windows
that translates `\n` to `\r\n`. A shell loop then read the file, and `\r` is absent from the default
`IFS`, so every unit id except the last carried a trailing carriage return. Each path built from
those ids missed. Twelve lanes died instantly on `dispatch-task: prompt file not found`, and the
wave exited 0.

**The tell.** `ls` showed the log files, and `od` could not open them. A filename ending in `\r`
renders as if it were clean. The one lane that worked was the last line of the file, which had no
line ending after it.

**The rules.**

- Write machine-read lists with `newline='\n'` explicitly.
- Strip `\r` from every unit id at the point of use as well, because the writer is not always the
  code you control: `u="${raw%$'\r'}"`.

## Failure 2: Editing a Bash Script That Is Currently Running

**What happened.** Three dispatcher shells were mid-flight when their script was edited to add a
reconciliation step. Bash reads a script lazily by byte offset rather than loading it whole, so the
edit shifted the offsets underneath the running shells. All three died on a fragment:
`line 28: syntax error near unexpected token 'do'`, where the reported text `S; do` is the tail of a
`while` line that had moved.

**Why the work survived anyway.** `dispatch-task.sh` re-executes from a private temp copy before it
does anything, so each worker is an independent process. When the parent died the workers orphaned
and ran to completion. The cost was monitoring, not results. That design is the reason this failure
was recoverable, and it is worth copying in any launcher.

**The rules.**

- Never edit a launcher while a wave is in flight. Copy it to a new name and edit the copy.
- Prefer a launcher that holds no long-lived supervising shell at all (see Failure 3).

## Failure 3: `setsid` Does Not Exist in Git Bash on Windows

**What happened.** After several supervising shells were killed, the launcher was rewritten to fire
and forget with `setsid nohup ... &`. Git Bash on Windows ships no `setsid`. Every launch failed with
`setsid: command not found`, and the script printed `DETACHED` for each unit regardless, because the
echo sat outside any check. Six lanes reported as running were not running.

**The rules.**

- `nohup ... &` is sufficient to outlive the launching shell here. Leave `setsid` out.
- Add `disown` only when the launcher will not wait. Disowning removes the worker from the shell job
  table, which a later review showed is both the concurrency cap's counter and what `wait` blocks on.
  Doing it unconditionally silently disabled the cap and made reconciliation fire against workers that
  had barely started.
- After launching, **verify** rather than assert. `dispatch-task` prints one `STATE-DIR` line once a
  worker is really running. Poll for that line, sample once more at the deadline, and report only the
  units still unconfirmed after it.

## Failure 4: Reading Buffered Output as a Complete Record

**What happened.** A killed wave's captured output showed eleven `DISPATCH` lines, so two lanes were
recorded as never dispatched. Both later produced full results. The shell had dispatched more than
its output had flushed before it died.

The same buffering made a later diagnosis wrong in the other direction: a batch that appeared to have
launched through one path had actually been launched by an earlier wave whose output was truncated.

**The rules.**

- Treat a killed process's captured stdout as a lower bound on what it did, never as a complete
  record.
- Determine what ran from the filesystem: the presence of a `prun-task-*` state directory and a
  growing `tail`, and the result file. Those are written by the worker, so they cannot be truncated
  by the launcher's death.

## Failure 5: Counting URLs Instead of Documents

Not a dispatch failure, and the one with the largest effect on the reported result.

**What happened.** The round reported nine new Tier 0 rows. Re-keying by document gave four. One BIS
paper appeared under four URLs (`/publications/ifc-bulletin-66-...`, `/ifc/publ/ifcb66_08.pdf`, and
`/2026-07/ifcb66_08.pdf` twice), and the International AI Safety Report appeared under three.

This is the same class of error the audit's 208 MIRROR verdicts exist to catch, applied one level up:
a fresh URL is not a fresh finding, and neither is a fresh row.

**The rule.** Before reporting any tier count, group by document identity rather than URL. Use the
DOI, the arXiv identifier, the PDF title-page string, or a hash of the fetched bytes. Report the
document count as the headline and the URL count only as supporting detail.

## Checklist for the Next Round

1. Write unit lists with `newline='\n'`, and strip `\r` at the point of use anyway.
2. Never edit a launcher that is running. Copy, then edit the copy.
3. Use `nohup`, never `setsid`. Disown a worker **only** when the launcher is not going to wait for
   it. The shell job table is both the concurrency cap's counter and what `wait` blocks on, so an
   unconditional `disown` makes the cap a no-op and makes `wait` return instantly. Leave the workers
   attached whenever the launcher intends to wait for them.
4. Verify every launch by polling for `STATE-DIR`, and take a final sample at the deadline before
   declaring any unit failed. Starting during the last interval still counts as starting.
5. Reconcile every dispatched unit against a result file that is present, non-empty, **and not a
   `FALLBACK` header**. A reaped worker is not a silent loss, because `dispatch-task` salvages its
   captured tail into the result file, but that file is non-empty and starts with
   `(FALLBACK, worker wrote no result file)`. Sizing it alone grades a timeout as a success.
6. Read the filesystem, not a killed process's stdout, to learn what actually ran.
7. Group by document before reporting any tier count.
8. Give the wait a finite wall clock. `dispatch-task` disables its hard timeout by default, so a
   worker that never finishes but keeps writing output resets the idle check forever. Setting the
   timeout is what makes item 5's `FALLBACK` check load-bearing: before it, no lane could time out.

`scripts/dispatch_lanes.sh` implements the mechanical parts of items 1, 3, 4, 5 and 8. Its
`result_complete` helper is the item 5 check, and it gates the skip-if-done branch and the launch
confirmation as well as the final reconcile, so a timed-out lane is re-dispatched rather than
counted. Items 2 and 6
are procedures that no script can enforce, and item 7 belongs to whoever writes the round up. Use the
script rather than writing a new launcher.
