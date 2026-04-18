# Draft patterns

These are scaffolds, not rigid forms. Always keep the hard rules: lead with the one-line core value, include install/docs/repo links when applicable, end with 3 to 5 hashtags, no em dashes as casual punctuation. Drop a section when the line above already says what it would say; for example, omit the explicit `What's new in {VERSION}:` heading if the first paragraph already announces the core change (see `scripts/drafts/pyod-3.0.md` for an acceptable compact variant).

## Open-source release

```
🚀 {NAME} {VERSION} is out, and the big change is {ONE-LINE-CORE-VALUE}.

{ONE-SENTENCE-POSITIONING: what this library is, who uses it}

What's new in {VERSION}:
• {POINT-1}
• {POINT-2}
• {POINT-3}

Still a one-liner:
{SHORT-CODE-SNIPPET}

{SOCIAL-PROOF-LINE: downloads, stars, user segments}

Install: pip install {pkg}
Docs: {docs-url}
Repo: {repo-url}

{3 to 5 hashtags}
```

**Rules for this pattern**:
- Line 1 must carry the **one** biggest change. If the user says the core is X, do not bury X under secondary features.
- Max 3 bullets under "What's new". More than 3 dilutes.
- Only include a code snippet if the API is genuinely simple (one line). Otherwise skip.
- Social proof must cite real numbers from `data/open-source.json` or user statement. Do not round up.

## Academic paper

```
📄 New paper: "{TITLE}" ({VENUE} {YEAR})

{ONE-SENTENCE-RESEARCH-QUESTION-OR-FINDING}

Why it matters: {IMPACT-OR-USE-CASE}

Highlights:
• {METHOD-1}
• {FINDING-2}
• {CONTRIBUTION-3}

Paper: {arxiv-url}
Code: {repo-url}
With {COAUTHOR-HANDLES}

{hashtags}
```

**Rules**:
- Include the venue in line 1 when accepted.
- Tag coauthor X handles when they have public accounts; ask the user if unsure.
- Use `arxiv-url` as the stable link; venue URLs change.

## Grant / award

```
🎉 {HEADLINE-ONE-LINE}

{ONE-SENTENCE-CONTEXT: what the grant funds, how much if public}

Thanks to {FUNDER} for supporting our work on {TOPIC}. Co-PIs: {NAMES}.

{Optional next line: what this enables}

{hashtags}
```

**Rules**:
- Do not disclose grant amounts or internal details unless the user confirms they are public.
- Tag co-PIs only with their explicit permission (or if they are public X users who have tagged each other before on related work).

## Talk / keynote

```
🎤 Speaking {WHEN} at {VENUE} on "{TITLE}".

{ONE-SENTENCE-TEASER}

{Optional: session link or time}

{CTA: come say hi / will share slides after}

{hashtags}
```

**Rules**:
- Post within 1 week of the event, not 3 months ahead (stale by go-time).
- Always include venue hashtag if the conference has one.

## Student / hiring / lab news

```
🎓 {HEADLINE}

{ONE-SENTENCE-DETAIL}

{OPTIONAL: congrats, link, more info}

{hashtags}
```

**Rules**:
- Get the student's permission before naming them publicly.
- Keep tone congratulatory but not hyperbolic.

## General guardrails for all patterns

- First line = one-sentence hook with the single biggest point.
- Never start several consecutive sentences with the same word.
- No em dashes (`—`) or en dashes (`–`) as sentence punctuation. Use `,`, `:`, `;`, or parentheses.
- Prefer `it is` over `it's`, `does not` over `doesn't`, where natural.
- 3 to 5 hashtags at the end. Always.
