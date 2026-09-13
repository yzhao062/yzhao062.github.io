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

## Failure 6: The Worker Is Never Told Where to Write

**What happened.** A five-unit wave on 2026-08-30 came back with three `FALLBACK` results. Every one of
those three workers had finished its analysis. One announced `Counts: 21 NEW, 5 MIRROR, 1 UNVERIFIABLE`,
another `NEW 7, MIRROR 1, TOPIC-ONLY 37`, and the third `All 73 candidates now have evidence-backed
verdicts and the counts reconcile to 73. Writing is blocked only by the omitted result path.` The work
was done and could not be delivered.

**The cause.** `dispatch-task.sh` takes `--result-file`, records it at `<state-dir>/result-file`, and uses
it for its own salvage. It does **not** put that path into the prompt. A worker sees the prompt text and
nothing else. The prompt template said "write to the result path given to you", naming a path the worker
had never been given. Two of the three guessed the same conventional location, `out/news-search-phase-b-
verification.md`, so the second guess overwrote the first; the third refused to guess and was reaped.

**Why it looked like a capacity problem.** The one genuine infrastructure failure in the same wave
(`ERROR: Selected model is at capacity`) produced an identical `FALLBACK` header, so all four looked alike
until the salvaged tails were read. Only the tail distinguishes a worker that could not start from one
that finished and had nowhere to put the answer.

**The rules.**

- Put the **absolute result path as a literal string** in the prompt body, and say that it appears there
  and nowhere else. Never write "the path given to you".
- Tell the worker not to write anywhere else, naming the repository explicitly. Two units that guess
  alike will silently overwrite each other, which makes a guessed path inside the repo worse than no
  file at all.
- Before re-dispatching a `FALLBACK`, read its salvaged tail. A finished-but-undeliverable unit is
  recovered by copying the file it did write; only a genuinely failed one needs the tokens spent again.

## Failure 7: Suppressing Against the Ledger Tables but Not the Round Write-Ups

**What happened.** A dedicated lane round on 2026-09-12 was given a suppression list built from the
Ledger 6 rows and the 1,929-entry known-URL index. It reported seven confirmed new external citers.
One of them, arXiv:2608.18351, was already recorded in the immediately preceding pass section of
`news-coverage-audit.md`, which had already used that same paper to falsify the same standing
negative. The round re-announced a two-week-old finding as new, and a reviewer caught it.

Rebuilding the suppression set from the **entire text** of `news-coverage-audit.md` and
`citation-affiliation-audit.md`, rather than their tables, yielded 412 URLs and 98 arXiv identifiers.
Applied to the next round's 630 candidates it suppressed **210** that the narrow list had let through
as new: 196 by URL and 14 by arXiv identifier.

**The rule.** Build the suppression set by extracting every URL and every arXiv identifier from the
whole audit file, not from the ledger tables. A finding recorded in a pass write-up but not yet
promoted to a numbered ledger row is still a finding, and prose is where most of a round's evidence
lives before it settles.

**One exception, and it matters.** Suppress an arXiv identifier only when the candidate's own URL is
that arXiv page. A citation record legitimately names the *cited* work's identifier, and most citing
surfaces (GitHub, YouTube, CSDN, Zhihu) carry no identifier of their own. Testing identifiers found
anywhere in a record wrongly discarded 131 genuine third-party findings in one pass, including two
comparison benchmarks, and the fresh-candidate count moved from 58 to 175 once the test looked at the
URL instead.

## Failure 8: Reading a Reference List Through a Summarizing Fetch

**What happened.** Six citation candidates were verified on 2026-09-12 by downloading each paper and
grepping the raw bytes. A parallel summarizing fetch was run on two of them as a cross-check and got
both wrong. On arXiv:2608.30478, a 557 KB page, it reported "MemoHarness, not found" and "no
bibliography entry"; the entry is there. On arXiv:2608.12761 it re-rendered an author-year
bibliography as a numbered list of 1 to 25 and reported "17" as the printed reference number. That
number does not exist in the document. A verification that trusted it would have published a
fabricated locator.

**The rule.** Reference-list checks are grepped from raw PDF text and raw HTML, never from a
summarizing fetch. Download, extract, search the bytes. Two false negatives in six candidates is too
high a rate to accept, and one of the two invented a citation detail rather than merely missing one.

## Failure 9: Treating a Printed Reference Number as Format-Independent

**What happened.** A round recorded Audita's citation of Auditable Agents as reference [62] and
HANSARD's as [20], and stated that every number had been established by grepping HTML. Fresh PDF
downloads print [17] on Audita page 16 and [5] on HANSARD page 6. The [62] came from nothing in
either format; `bib.bib76` is Audita's HTML element id, which is positional and unrelated to any
printed number.

Worse, most bibliographies in this subfield carry no printed numbers at all. Five of the six papers
verified in the following pass use author-year style, where the correct locator is a page number plus
an author-year label.

**The rule.** Record the format alongside the locator: "PDF [17], page 16" or "HTML element id
`bib.bib76`" or "author-year, no printed number, PDF page 57". Never present an HTML element id as a
printed reference number, and never assume a number exists.

## Failure 10: Letting a Search That Found Nothing Outrank a Document

**What happened.** Two rounds disagreed about whether Implicit Execution Tracing (arXiv:2603.17445)
had any external citer. A search lane reported the zero falsified and named two documents. A
cross-vendor sweep reported a hard zero across eight citation indexes, 879 full texts, and
`site:arxiv.org`. The round recorded the question as open, reasoning that the sweep had covered more
surfaces.

Fetching one of the two named documents settled it in a single request. The Crew Scaler response to
the NIST CAISI RFI carries the bibliography entry "When only the final text survives: implicit
execution tracing for multi-agent attribution. External Links: 2603.17445". The zero was false and
the sweep was blind, which is exactly what the sweep's own findings predicted: two of the strongest
citations that round confirmed cite a repository URL with no identifier for an index to match.

**The rule.** A search that finds nothing is weak evidence; a fetched bibliography entry is strong
evidence. When they conflict, fetch the document. Surface count does not convert absence of evidence
into evidence of absence, and this subfield's citations routinely carry no identifier at all.

**The corollary for fan-out caps.** The same round named six candidates it had located but could not
verify within its cap. All six were later confirmed, with independent authors, a 6 of 6 rate. A cap
does not merely cost time when the queue is already triaged; it defers findings the round had already
found. Log what the cap dropped, by identifier, so the next round starts there.

## Failure 11: Reading a Phase A Tier as an Estimate Rather Than a Ceiling

**What happened.** A Phase B round verified all 420 candidates two Phase A rounds had left over and
compared each final tier against the Phase A guess. 310 held, **110 moved down, and none moved up**.
A 26.2% error rate that runs entirely in one direction is not noise, because noise misses in both
directions.

The bias is worst where it costs most. Six candidates arrived as Tier 0 and one survived. One was a
third-party adapter registry misread as the institution whose framework it indexes, three tiers of
difference on a real document. Four were topic-validation: pages about the subject matter naming no
work and no person.

**The rule.** Treat a Phase A tier as an upper bound on what verification will support, never as an
estimate. Report high-tier Phase A counts as "claims" and reserve tier language for verified rows. A
round that publishes Phase A tier counts as findings publishes a number that will fall by a quarter.

## Failure 12: A Lane That Knows the Document and Invents Its Address

**What happened.** Five candidate addresses in one round did not exist: four GitHub repositories and
one Hugging Face Space, all 404. Four of the five had already been written up as findings.

What makes this failure hard is that the lanes were right about everything except the address. For
each of the four, the project, the document type, the mechanism and the comparison all checked out
once the real document was found, under a different owner: `AgentShield-Security/AgentShield` is
`affaan-m/agentshield`, `HandoffGraph/handoffgraph` is `arbazkhan971/handoffgraph`,
`onelive-ai/onelive-engine` is `schubertsean-ui/onelive`, and `mcp-data/platform` issue #142 is
`txn2/mcp-data-platform` issue #1163. An invented `AgentShield-Security` organisation is exactly what
a plausible owner for a project called AgentShield would be named.

**The one detectable signal** was that the same lane emitted both URLs. The worklist carried a
near-duplicate pair per case: same project name, same document type, different owner. Nothing else
about the fabricated row read as wrong.

**The rule.** Before spending verification budget, group candidates by project and document type and
flag any group whose owners disagree. A lane reporting a URL has not established that the URL
resolves, and a repository path is the part a lane is most likely to synthesize. A weaker sibling of
the same failure: a real repository with an invented file, such as a `setup.py` in a project that
ships `pyproject.toml`.

## Failure 13: A First-Party Filter That Matches Domains

**What happened.** A worklist builder excluded first-party material with a domain regex covering
`yzhao062`, `USC-FORTIS`, `pygod-team`, the lab site and the personal site. 47 first-party records
passed it, and Phase B dropped every one: 14 Hugging Face Daily Papers landing pages for the lab's own
papers, 7 alphaXiv preprint pages, 2 ACL Anthology publication records, PyPI release pages for the
lab's own packages, Hugging Face Spaces under a co-author's account, and a fork of a lab repository
under a third-party org. First-party material was the largest single reason a candidate was dropped,
46 of 63 drops.

**The rule.** First-party is a property of authorship, not of the host. Ask whether the page's subject
is the lab's own work, listed or announced by the lab or a co-author, and treat every aggregator that
mirrors preprints (Hugging Face Papers, alphaXiv, ACL Anthology, Semantic Scholar, a package index) as
a first-party surface for the lab's own artifacts. A fork of a lab repository is first-party wherever
it sits.

## Failure 14: One Document, Four URLs

**What happened.** Google Patents serves the same patent at `/en`, `/zh`, `/fr` and `/sk`. A
1,929-entry URL index held patent links in all four (23, 9, 2 and 1), so three patents already on file
re-entered verification because the new candidate carried a different language suffix than the indexed
copy. The same round re-verified a government report it had recorded hours earlier in its own ledger,
because that row names the document by OSTI accession number and carries no link, and re-surfaced two
already-counted items at a second surface: a podcast episode under an Apple Podcasts URL and a paper
under its workshop-hosted PDF rather than its arXiv page.

**The rule.** Key the suppression index by document identity, not by URL string. Store the URL and,
alongside it, every identifier the document has: arXiv ID, DOI, patent number with the language suffix
stripped, OSTI accession, ISBN, podcast episode number. A ledger row that names a document without a
link is invisible to a URL-keyed check, so require either a URL or an identifier in every row.

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
9. State the absolute result path literally in every prompt. `dispatch-task` does not pass it to the
   worker, so a prompt that refers to "the result path given to you" names nothing.
10. Read a `FALLBACK` tail before re-dispatching it. Three of five units in one wave had finished their
    analysis and only lacked somewhere to put it.
11. Build the suppression set from the whole audit file, not its ledger tables, and key an arXiv
    identifier against the candidate's own URL rather than against any identifier in the record.
12. Grep raw PDF text and raw HTML for every reference-list check. Never accept a summarizing
    fetch's account of a bibliography.
13. Record the format with every locator, and expect author-year bibliographies with no printed
    numbers at all.
14. Fetch the document when a search result and a document disagree. Log by identifier whatever a
    fan-out cap drops, because a triaged queue's deferred items verify at a high rate.
15. Read every Phase A tier as a ceiling. Measured on 420 candidates: 110 down, 0 up.
16. Group candidates by project and document type before verifying, and flag any group whose owners
    disagree. That pattern is what an invented repository URL looks like from the outside.
17. Decide first-party by authorship, not by host. Preprint aggregators and package indexes are
    first-party surfaces for the lab's own artifacts.
18. Key the suppression index by document identity: URL plus arXiv ID, DOI, language-stripped patent
    number, OSTI accession, podcast episode. Require a URL or an identifier in every ledger row.

`scripts/dispatch_lanes.sh` implements the mechanical parts of items 1, 3, 4, 5 and 8. Its
`result_complete` helper is the item 5 check, and it gates the skip-if-done branch and the launch
confirmation as well as the final reconcile, so a timed-out lane is re-dispatched rather than
counted. Items 2 and 6
are procedures that no script can enforce, and item 7 belongs to whoever writes the round up. Use the
script rather than writing a new launcher.
