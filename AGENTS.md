## User Profile

- These are user-level defaults that can be reused across projects unless a local repo rule or task-specific instruction is stricter.
- The user is a computer scientist and professor working in machine learning and AI.
- Common tasks include research papers, funding proposals, scientific writing, and administrative writing.

## Writing Defaults

- Use scientifically accessible language.
- Do not oversimplify unless the user asks for simplification.
- Keep meaningful technical detail.
- Keep factual accuracy and clarity high in scientific contexts.
- Use consistent terms. If an abbreviation is defined once, do not define it again later.
- If citing papers, verify that they exist.
- When paper citations are requested, provide BibTeX entries that can be copied into a `.bib` file.
- Provide code only when necessary. Confirm that the code is correct and can run as written.
- For NSF or other federal proposal work, do not introduce DEI-related terms unless the solicitation explicitly requires them.
- For non-federal proposals or calls that explicitly request DEI framing or terminology, follow the call requirements instead of applying a blanket ban.
- Avoid the following words and close variants unless the user explicitly asks for them: `encompass`, `burgeoning`, `pivotal`, `realm`, `keen`, `adept`, `endeavor`, `uphold`, `imperative`, `profound`, `ponder`, `cultivate`, `hone`, `delve`, `embrace`, `pave`, `embark`, `monumental`, `scrutinize`, `vast`, `versatile`, `paramount`, `foster`, `necessitates`, `provenance`, `multifaceted`, `nuance`, `obliterate`, `articulate`, `acquire`, `underpin`, `underscore`, `harmonize`, `garner`, `undermine`, `gauge`, `facet`, `bolster`.

## Formatting Defaults

- Preserve the original format when the input is in LaTeX, Markdown, or reStructuredText.
- Do not convert paragraphs into bullet points unless the user asks for that format.
- Prefer full forms such as `it is` and `he would` rather than contractions.
- `e.g.,` and `i.e.,` are fine when appropriate.
- Do not use Unicode character `U+202F`.
- Avoid heavy dash use.

## Environment Notes

- Prefer a Miniforge-managed Python interpreter.
- If a `py312` environment or launcher exists, use it first.
- Do not conclude that Python is unavailable just because `python`, `python3`, or `py` fails in `PATH`; those may resolve to shims, store aliases, or the wrong interpreter.
- On Windows, a common Miniforge pattern is `%USERPROFILE%\\miniforge3\\envs\\py312\\python.exe`.
- On macOS or Linux, a common Miniforge pattern is `$HOME/miniforge3/envs/py312/bin/python`.
- If interpreter selection is still unclear, inspect Miniforge environments and local IDE settings before reporting that Python is missing.
