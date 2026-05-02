"""Apply yellow highlight to [CONFIRM:...] blockquote regions in a pandoc-generated docx.

Usage: python highlight_confirm.py <docx_path>

Strategy:
1. Walk paragraphs.
2. Track whether we are inside a [CONFIRM:] blockquote region.
3. A region starts when a paragraph contains "[CONFIRM:".
4. The region continues across paragraphs whose style is "Block Text" (pandoc's
   default blockquote style) or contains "Quote", and across list paragraphs whose
   text begins with "(a)", "(b)", "-", or similar markers nested under a blockquote.
5. The region ends at the first paragraph that is a heading, a normal paragraph
   without quote / list markers, or an empty paragraph followed by a heading.
"""

from __future__ import annotations

import sys
from docx import Document
from docx.enum.text import WD_COLOR_INDEX


def is_blockquote_style(para) -> bool:
    name = (para.style.name or "").lower()
    return ("block text" in name) or ("quote" in name)


def is_blockquote_continuation(para) -> bool:
    """A paragraph that visually belongs to the previous blockquote region.

    Pandoc-generated docx puts list items inside a blockquote on "List Paragraph"
    style, but they still belong to the blockquote visually. Match those by
    detecting that we are still inside a contiguous Block Text or List Paragraph
    sequence whose surrounding context began with [CONFIRM:].
    """
    name = (para.style.name or "").lower()
    if "block text" in name or "quote" in name:
        return True
    if "list paragraph" in name and para.text.strip():
        return True
    return False


def apply_yellow(para) -> None:
    for run in para.runs:
        run.font.highlight_color = WD_COLOR_INDEX.YELLOW


def main(path: str) -> int:
    doc = Document(path)
    paras = doc.paragraphs

    in_region = False
    highlighted = 0
    for para in paras:
        text = para.text
        if text.lstrip().startswith("[CONFIRM:"):
            in_region = True
            apply_yellow(para)
            highlighted += 1
            continue
        if in_region:
            if is_blockquote_continuation(para):
                apply_yellow(para)
                highlighted += 1
                continue
            in_region = False

    doc.save(path)
    print(f"Highlighted {highlighted} paragraphs in {path}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1]))
