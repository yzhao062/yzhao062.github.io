# Independent Patent Review

Disposition: pass all ten candidate families for the narrow claim that their patent text names the research methods. Exactly four families have a tool name inside a numbered claim. None of the reviewed evidence establishes commercial deployment.

I independently read all ten saved HTML documents, verified their SHA-256 hashes against parent-candidates.jsonl, extracted numbered claims, and checked the full audit for identifiers, publication stems, titles, and assignees. Seven additional country-member pages returned HTTP 200. Their publication histories expanded the deduplication check to 21 publication versions across ten families. All ten family IDs are distinct; no existing-audit duplicate was found.

Family membership was taken from Family Applications and Country Status, with Other Versions used only to expand publication histories. Citations, Cited By, Families Citing, and Family Cites Families were excluded from membership.

## Per-Family Findings

| Representative | Assignee | Family | Numbered Claims Naming the Tool | Verdict |
|---|---|---|---|---|
| CN115700673B | SF Technology | 85120788 | 1, 2, 3, 4, 6: COPOD | Pass. The description and claims also give tail/skewness calculations. |
| CN122264915A | Beijing Lingyan Technology | 100190914 | 1, 7, 8, 10: COPOD | Pass for name/claim evidence. The document expands COPOD as Copula-Based Outlier Detection. Preserve the qualification that its parameter-fitting adaptations are its own claims. |
| CN115720177B | Jinjing Yunhua / Beijing Jinjingyunhua | 85257968 | None | Pass, specification only. |
| CN120822140A | Zhejiang Huixie Digital Intelligent Technology | 97365247 | 1: COPOD | Pass, published application. |
| US20260018281A1 | Panasonic Well | 98387418 | None | Pass, broad optional-method list only. WO2026015718A1 is the same family. |
| US20260236645A1 | Greentech Korea | 97222121 | None | Pass, optional ECOD/COPOD mention. KR102864947B1 is the same family. The source's deep-learning label is technically inaccurate and should not be repeated as fact. |
| KR20240158693A | SK Innovation / SK Earthon | 93168052 | 3: COPOD | Pass. Korean original and English translation both place COPOD in claim 3. US20240361494A1, CN118861012A, and KR102908818B1 belong to this family. |
| EP4521278A1 | eBay | 92672105 | None | Pass, ECOD method description. US12641104B2, US20250088523A1, and CN119598242A belong to this family. No formal ECOD paper citation is established. |
| US20230237371A1 | Rockwell Automation Technologies | 87314160 | None | Pass, specification paragraph [0040] lists LSCP as an optional model. Keep the Google Patents abandoned-status qualification. |
| CN115424106B | Midea Group | 84202561 | None | Pass, specification lists LSCP, XGBOD, and COPOD. |

## Count and Metadata Checks

The proposed increase is ten distinct families, represented by five CN, three US, one KR, and one EP record. The increment in families with numbered-claim mentions is four, not the number of individual claims. Against the current public baseline of 97 and seven, the arithmetic would be 107 and eleven.

The parent records omit four older publication versions from their family-member arrays: CN115700673A, CN115720177A, CN115424106A, and US20250088523A1. These omissions do not change the family count or create an audit duplicate. Add them to the arrays if those fields are intended to be exhaustive. The expanded versions are saved in patent-review-checks.json.

Use wording such as patent text names or describes these methods when distinguishing formal paper citations from method mentions. Panasonic, Greentech, Rockwell, and Midea are optional-method mentions. A numbered claim is stronger textual evidence, but it does not demonstrate implementation.

## Review Artifacts

- patent-review-checks.json: per-family publication versions, audit hit results, exact numbered-claim matches, and reviewed audit hash.
- patent-extract.json: metadata, claim text, and tool contexts from the ten supplied pages.
- patent-family-versions.json: seven independently fetched country members plus publication histories.
- patent-family-evidence/: the seven additional raw HTML pages.

No repository file was edited. No speculative family was promoted and no duplicate was found.

## Coordinator Resolution

The four older publication versions listed above were added to the candidate family arrays before integration. The original review is preserved above. Its raw artifacts are under `/tmp/news-search-20261014-codex/institutional/`, including `patent-review-checks.json`, `patent-extract.json`, `patent-family-versions.json`, and `patent-family-evidence/`.
