# Draft Patterns

These are starting shapes, not forms to fill. The default post is brief and natural:
a few sentences that say what the thing is, what a reader can do with it, and why it
is useful, followed by a link and a few relevant hashtags. Do not pad a post to make it
longer. Every element below except the core sentence and the link is optional; add one
only when it carries information the reader needs.

See [example-prefixsim.md](example-prefixsim.md) for one short release post used as an
editorial reference (an example, not a template or a performance claim).

## Default Shape (Any Announcement)

```
{WHAT IT IS AND WHAT IS NEW, in one sentence}

{WHAT A READER CAN DO WITH IT, or WHY IT MATTERS, in one or two sentences}

{ONE LINK}

{A few relevant hashtags}
```

Nothing in this shape requires bullets, a feature list, a question, a research-program
link, a caveat, or a call to action. Use one of those only when the content calls for
it, for example a genuine list of three install targets, or a limitation that changes
what the post claims.

## Open-Source Release

```
{NAME} {VERSION} is out: {ONE-LINE CORE CHANGE OR PURPOSE}.

{WHAT A USER CAN NOW DO, and why that is useful}

{repo-url or docs-url}

{hashtags}
```

- Line 1 carries the **one** biggest change. If the user says the core is X, do not
  bury X under secondary features.
- Optional: a one-line code snippet when the API is genuinely that simple; an install
  line; real usage numbers from `data/open-source.json` or the user. Do not round up.
- A short list of new features is acceptable only when the release has several equally
  important changes and the user wants them listed. Keep it to three items.

## Academic Paper

```
New paper ({VENUE} {YEAR} if accepted): {TITLE or a plain-language name}.

{THE FINDING OR METHOD, and why someone would use or care about it}

{arxiv-url}

{hashtags}
```

- Include the venue when accepted. Use the arXiv URL as the stable link.
- Tag coauthor X handles only when they have public accounts; ask the user if unsure.
- A code link or a second finding is optional. Include a scoped limitation, at any
  length, when the post would otherwise overstate the result; otherwise omit it.

## Repost or Quote Caption

```
{ONE USEFUL ANGLE the original does not state: who should use it, the setting it fits,
a connection to a concrete problem, or a short takeaway}
```

- Add one angle. Do not restate the original post, its title, or its feature list.
- One to three sentences is usually enough. Hashtags are optional. Omit the original
  link only when the platform's native repost or quote attaches the original post;
  `post_to_x.py` and `post_to_linkedin.py` cannot do that, so a caption posted through
  either script must include the original URL and stand on its own.
- Verify any claim the caption adds about the original work.

## Grant or Award

```
{HEADLINE IN ONE SENTENCE}

{WHAT THE GRANT OR AWARD SUPPORTS, and thanks to the funder or co-PIs}

{hashtags}
```

- Do not disclose grant amounts or internal details unless the user confirms they are
  public.
- Tag co-PIs only with their explicit permission (or if they are public X users who
  have tagged each other before on related work).

## Talk or Keynote

```
Speaking {WHEN} at {VENUE} on "{TITLE}".

{ONE SENTENCE ON WHAT THE TALK COVERS}

{Optional: session link or time}

{hashtags}
```

- Post within one week of the event, not months ahead.
- Include the conference hashtag if it has one.

## Student, Hiring, or Lab News

```
{HEADLINE}

{ONE-SENTENCE DETAIL}

{hashtags}
```

- Get the student's permission before naming them publicly.
- Keep the tone congratulatory but not hyperbolic.

## When a Long Post Is Warranted

Write longer only when the user asks, or when the content cannot be understood in a
short post (a reflection with an argument, a release whose main change needs an
example to make sense). X Premium allows up to 25,000 characters; that is capacity,
not a target. Even then, cut anything that repeats the linked artifact.

## General Guardrails

- First line states the single biggest point.
- Prefer prose sentences over bullets unless the items are genuinely parallel.
- Do not start several consecutive sentences with the same word.
- No em dashes (`—`) or en dashes (`–`) as sentence punctuation. Use `,`, `:`, `;`, or
  parentheses.
- Prefer `it is` over `it's`, `does not` over `doesn't`, where natural.
- Hashtags: a few that name what the post is about, usually two to four, never more
  than five. Zero is fine for a repost caption. Choose for relevance; do not claim that
  a tag count helps or hurts reach.
