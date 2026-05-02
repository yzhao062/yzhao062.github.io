"""Inspect a docx to print each paragraph's style and a snippet of text. Used to
debug which paragraphs are inside vs. outside blockquote regions."""

import sys

from docx import Document


def main(path: str) -> int:
    doc = Document(path)
    for i, para in enumerate(doc.paragraphs):
        style = (para.style.name or "")
        text = para.text.replace("\n", " ")[:100]
        print(f"{i:3d} | {style!r:30s} | {text!r}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1]))
