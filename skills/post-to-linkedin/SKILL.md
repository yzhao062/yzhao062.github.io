---
name: post-to-linkedin
description: Draft, preview, publish, and record Yue Zhao's research announcements on his personal LinkedIn feed. Use for papers, talks, grants, releases, and research-program updates; supports browser document posts and API text or image posts. Do not use for DMs or Company Page posts.
---

# Post to LinkedIn

Create a source-checked LinkedIn post in Yue Zhao's established voice, show the
complete preview, publish only within the user's authorization, and record the final
public result. LinkedIn commentary is limited to 3,000 characters.

Read [references/yue-style.md](references/yue-style.md) before drafting a personal
post. The shared scaffolds and hashtag vocabulary remain in
`skills/post-to-x/references/`, but LinkedIn copy should not be a verbatim X draft.

## Choose the delivery path

Use the **browser composer** when the post attaches a PDF or other LinkedIn document,
when a real mention or visual spacing matters, or when API credentials are absent and
the user has a logged-in session. Otherwise prefer the API path for text or image posts.
If a computer-use or browser skill is installed, follow it for the mechanics. Whichever
browser tooling is used, do not click `Post` until the user has approved a screenshot
of the exact final composer in this conversation. Approval of an earlier draft does
not carry over.

Use `scripts/post_to_linkedin.py` for repeatable text or image posts when LinkedIn API
credentials are configured. Its media path uses LinkedIn's image endpoint and does not
support PDF document posts. Never pass a PDF to `--media`.

This skill posts only to the authenticated user's personal feed. It does not cover
messages, connection requests, comments, or Company Page publishing.

## Workflow

1. **Verify the source.** Read the current paper, project data, event record, or
   user-provided fact. Check venue, status, author names, URLs, and every number.
2. **Choose one story.** Lead with the most concrete event, consequence, question, or
   finding. Use the attached artifact for detail instead of restating all of it.
3. **Draft and save.** Store only the post body in `scripts/drafts/<slug>.md`; the API
   path posts that file verbatim, so it must contain nothing else. Put links,
   attachment path and title, proposed mentions, hashtag rationale, character count,
   and claim checks in `scripts/drafts/<slug>.notes.md`. The post record in step 6 goes
   in the notes file under a `## Published` heading.
4. **Preview the actual surface.** For API posts, run `--dry-run` and show the output.
   For browser posts, prepare the full composer and show a screenshot. In both cases,
   stop until the user approves that exact preview.
5. **Publish once.** Use the approved API draft or the inspected browser composer. On
   an ambiguous failure, first check whether the post already exists; do not silently
   retry.
6. **Record the public result.** Read the published post back from LinkedIn. Save to
   `scripts/drafts/<slug>.notes.md` its permanent URL, observed time, exact public copy,
   attachment, and the differences between the preview and the user's final edits.
   Leave `scripts/drafts/<slug>.md` unchanged so it still matches the dry-run. Preserve
   the public copy verbatim, including incidental errors, but do not turn those errors
   into future style rules. When the sibling `../research-impact` repository is
   available, add or update the post record under `social/YYYY-MM-DD-<slug>/` and link
   it from `social/README.md`; commit that repository separately.

## Browser composer rules

- Treat a PDF poster or slide as a LinkedIn document. Upload the finished PDF, add a
  descriptive title within the limit shown by the composer, and verify the preview.
- Plain pasted `@Name` text is not a mention. Type `@`, continue the name slowly, and
  select the exact person from LinkedIn's typeahead. Verify that the editor stores a
  structured, non-editable mention object. If no exact account appears, keep a plain
  name or omit the mention. Do not choose a similar person.
- Hashtags can remain visually plain in the composer. Type them normally and verify
  after publication that LinkedIn rendered them as hashtag links.
- LinkedIn can collapse ordinary empty lines inserted through automation. Inspect a
  screenshot. If major blocks run together, use a line containing only U+200B between
  those blocks, then inspect again. Do not scatter invisible characters inside words,
  links, mentions, or hashtags.
- Keep `Post to Anyone` and comment settings visible in the final preview so the user
  knows the distribution scope.
- A browser tab returning to the feed is not enough evidence. Require the success
  notice or find the new public post and capture its URL.

## Draft rules

- Voice, structure, links, and hashtag count follow
  [references/yue-style.md](references/yue-style.md).
- Preserve honest limits. Distinguish separately validated components from a complete
  end-to-end system, and a proposed framework from a measured result.
- Apply repository writing rules: no casual em dash or en dash, no U+202F, no banned
  AI-tell words, and full forms where natural.
- Stay at or below 3,000 characters including full literal URL length.

## API path

The Python environment needs `requests` and `python-dotenv`; install from
`scripts/requirements-post.txt`. A real API post requires these `.env` values:

- `LINKEDIN_CLIENT_ID`
- `LINKEDIN_CLIENT_SECRET`
- `LINKEDIN_ACCESS_TOKEN`
- `LINKEDIN_TOKEN_EXPIRES_AT`
- `LINKEDIN_USER_URN`

`LINKEDIN_REFRESH_TOKEN` is optional. When the access token expires without a refresh
token, run:

```powershell
python scripts/post_to_linkedin.py --auth
```

First-time setup: create an app at <https://developer.linkedin.com>. LinkedIn requires
a Company Page to own the app. Add the products **Share on LinkedIn** and **Sign In
with LinkedIn using OpenID Connect**, register `http://localhost:8765/callback` as a
redirect URL, and copy the client ID and secret into `.env` using the keys in
`.env.example`. Access tokens normally last 60 days. Keep all credentials in `.env`.

Preview:

```powershell
python scripts/post_to_linkedin.py --dry-run --draft scripts/drafts/<slug>.md
```

Publish the approved preview:

```powershell
python scripts/post_to_linkedin.py --yes --draft scripts/drafts/<slug>.md
```

Attach images with repeatable `--media <path>` arguments. Run a successful dry-run for
the exact draft and attachments before using `--yes`.

`--draft` reads the whole file as commentary. Never point it at a notes or record file.
The API image path currently publishes an empty alt-text field.

The API path cannot create mentions; `@` is escaped and publishes as plain text. If a
mention matters, use the browser composer.

## Output record

A completed post record should contain:

- permanent LinkedIn URL and publication time;
- exact published text and resolved destinations for each link;
- attachment path, document title, and alt text when supported;
- verified claims and public source revisions;
- whether mentions became profile links and hashtags became hashtag links;
- user edits that reveal a reusable voice preference;
- an initial analytics observation and planned follow-up window when impact is being
  measured.

First API post retained for regression reference:
<https://www.linkedin.com/feed/update/urn:li:share:7472734205077053440/>.
