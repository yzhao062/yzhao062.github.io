# Pitfalls

Each entry is a mistake made in a real run on 2026-08-25, what it cost, and the check that
catches it. Read this before designing a probe, not after.

## 1. HTTP 200 does not mean you got results

Five scraper units reported that the subject appeared for none of sixteen audit-related
queries. The number looked like a finding. It was a collection failure.

Bing had returned HTTP 200 with a page that had nothing to do with the query. It listed
generic AI destinations: OpenAI, ChatGPT, Gemini, DeepAI, a Chinese AI-tool directory, a
Zhihu thread. Every unit recorded those rows as the top ten organic results.

A sixth unit, given a control term, tried nine engines, found eight blocked or degraded,
located one that worked, and returned real data that contradicted the other five.

**Check:** issue one query whose correct top result you already know. If it does not appear,
the engine is degraded for this run. Record the query and its expected result in the unit
prompt so the worker cannot skip it.

**Second-order lesson:** the five bad units and the one good unit used the same code. Only
the engine differed. Never generalize a scrape result from one engine.

## 2. A missing control makes zeros unreadable

The first forward probe returned zero hits across every term, including the one the subject
is a definitional figure for. That should have stopped the run immediately. Instead the
zeros were nearly reported as a finding about the audit terms.

**Check:** include a term the subject owns beyond argument. Read the control first. If it
fails, the probe is invalid and its other numbers carry no information.

Put this in the output contract as an explicit verdict, so a worker has somewhere to put a
failed control. A unit reporting "no engine passed the control, so this is unmeasurable"
is worth more than one reporting five confident zeros. Zeros from a degraded source cannot
be told apart from real ones, and they get read as findings. The one unit in that
run that withheld preserved the integrity of the whole result set.

## 3. Query wording selects the population, not the ranking

"Leading international researchers working on X" returned the same names whatever X was:
public AI-ethics figures. It measures media salience.

Rewording it to "university professors, tenure-track or tenured, whose group publishes on X
at NeurIPS, ICML, ICLR, KDD, ACL, or IEEE and ACM journals" returned the working field. The
term X had not changed.

**Check:** run two wordings of the same question and compare the returned populations. If
they differ, the wording is doing the work.

## 4. Optimizing a measurable proxy in place of the real question

This one repeated three times in a single session, each time with a different proxy.

- Round one scored how much of the paper corpus a name covered, and concluded no name works.
- Round two scored how cleanly a name partitioned the corpus, and picked the best partition.
- Round three scored search-term ownership, and picked the best-ranking terms.

Each round was correct about its proxy. None of the proxies contained the constraint that
actually decided the question, which was whether the phrase reads like something a scholar
puts at the top of a homepage. That test was available from the start and cost almost nothing.

**Check:** before spending on measurement, write down the constraint that would overturn a
high score. If it is not one of the things being measured, measure it first, cheaply.

## 5. Corpus coverage and conceptual parenting are different tests

A candidate umbrella was rejected on the grounds that it "covers 7 of 55 papers". That is a
coverage number: how many papers are literally about the topic. It was then reused to argue
the term could not be the conceptual parent of a sub-area.

Those are different claims. The subject's own published framework already defined the
sub-area as one mechanism class inside the umbrella, so the parenting was sound even though
the coverage was low.

**Check:** when rejecting a parent term, say which test failed. Coverage failure is an
argument about emphasis. Parenting failure is an argument about meaning.

## 6. Common names collapse into the wrong person

The prompt named the subject's institution and lab and asked what they are known for. Three
of eight models answered with a different person's field entirely: systems security,
healthcare machine learning, federated learning, polymer chemistry.

The models were not confusing two candidates. They lacked the entity and fell back to the
nearest well-known holder of the name.

**Consequence for naming:** the headline's first job is to make the name resolve. A generic
umbrella cannot do that, whereas a distinctive term can. Adding the institution to the prompt moved
correct answers from one in six to three in six, so the institution belongs in the page's
identity strings.

**Check:** run the reverse probe with and without qualifiers and compare. Report the wrong
attributions, since they are the finding.

## 7. A conjunction of two eras reads as neither

`Current Direction and Legacy Direction` was proposed to widen coverage and rejected on
sight as stitched together. Both halves were real assets and both ranked. What failed was the
conjunction.

**Check:** does the phrase name one thing? If a reader has to hold two unrelated topics at
once, it fails, whatever each half scores.

## 8. Generalizing from one term's decline

The run that started this work found that a modifier had been dropped from the subject's own
titles at a career boundary, seven occurrences to zero. It had named a scarcity that ended.

A term tied to a current system architecture often dates the same way when that
architecture is superseded, and renaming costs the accumulated equity again. One case does
not establish a lifespan for the category, and this one was a single term in a single
career.

**Check:** name the event that would make the term stale, and give the evidence that the
event is likely. Require field-specific or longitudinal evidence before assigning a general
lifespan to a whole class of terms.

## 9. Engine verdicts expire in hours, not months

Two scrapeability runs on the same machine, three hours apart, disagreed completely. The
engine the first run called the only working one came back degraded. One the first run
called blocked came back at rank 1 with the smallest response body of any engine tested.

No engine changed in three hours. The client did: a different user agent, a different curl
binary, different compression headers.

**Check:** re-run the control every session. Never reuse a verdict, including one written
down by a careful previous run. Treat a stored matrix as a list of engines to try, never as
a list of engines that work.

**Environment note that cost three crashes:** on Windows, the `curl` first on `PATH` may be
the Git for Windows build, which crashed with an access violation on one engine. The system
binary at `C:\Windows\System32\curl.exe` handled the same request. Use the absolute path.

## 10. The agent's own folklore is the hardest thing to catch

A fact-check unit was pointed at claims the agent had made confidently while advising. Three
came back unsupported, two of them the agent's own.

One was a character limit for a page title, quoted as a constraint through several rounds of
advice. The documentation says there is no limit and that truncation depends on the device.

The other was worse, because it had already been recommended: put keywords in a
visually-hidden heading, on the reasoning that no reader sees it and only crawlers read it.
That reasoning is close to a verbatim description of what the relevant spam policy targets,
which permits screen-reader text by intent and lists off-screen positioning as an abuse
example. The recommendation was withdrawn.

Both had survived because they sounded like settled knowledge and neither the agent nor the
reader had reason to question them.

**Check:** list the load-bearing claims made during a run and check them against primary
documentation, including the ones that feel too basic to check. Run this as a separate unit
so the checker is not the author. Require NOT-VERIFIED as a distinct verdict from false;
conflating them turns silence in the docs into permission.

## 11. A reviewer checks your reasoning, not your premises

Two wrong calls in one session traced to the same shape. Each began with a statement written
into a review prompt as though it were established, and each reviewer reasoned correctly from
it to a wrong conclusion.

The first ran: "the biography is the only place on the homepage carrying the institution,
the awards, and the third-party validation." The reviewer accepted it. It then prescribed a
visible summary paragraph to compensate for collapsing the biography. One grep showed the
institution appeared six times elsewhere on that page, the flagship library five times, and
every other claim but one at least once. That paragraph was pure duplication, and it worked
against the stated goal of a shorter page. The page owner caught it, not the reviewer.

The second: a scholarly profile was called merge-polluted because its top-cited paper looked
like another person's work. It was the subject's own paper, and it was listed in the
repository's own authoritative publication file the whole time. The conclusion to exclude the
profile happened to survive, but for an unrelated reason found later by a third party.

A reviewer treats a stated premise as a given. That is what makes review cheap, and it is
what makes a false premise expensive: it is laundered into a confident recommendation, and it
now carries a second signature.

**Check:** before writing a factual claim into a prompt, run the command that would falsify
it. If no such command exists, mark the claim as an assumption in the prompt and ask the
reviewer to test it first. Prefer handing over the raw counts and letting the reviewer
conclude.

## 12. A rename reaches the pages and misses everything else

A full-site rename inventory reported 56 occurrences across nine files and was treated as
complete. It was built by globbing HTML in the repository root and the data directory.

It missed two tracked files. One was a shared sidebar fragment injected into every page by a
script, so the old term stayed visible site-wide. The other was the machine-readable site
summary that exists specifically to tell crawlers what the site is about. It defined the old
term as the umbrella and the new one as a subordinate approach. Publishing that would
have announced the opposite of the change to exactly the audience the change was aimed at.

Both were found by a reviewer running a content grep over the tracked tree rather than a
glob over one extension.

**Check:** enumerate surfaces first and grep by content across everything tracked. Include
shared includes, script-injected fragments, generated regions and their source files,
structured data, `llms.txt` and similar crawler summaries, plain-text deliverables, and CV or
publication pipelines. A count from a glob is a count of what the glob matched, never a count
of what exists.
