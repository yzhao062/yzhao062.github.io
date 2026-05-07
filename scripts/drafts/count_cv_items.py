"""Count \\item entries inside each benumerate block in cv-full.tex to derive numbering ranges."""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CV = ROOT / "cv" / "cv-full.tex"
text = CV.read_text(encoding="utf-8")
lines = text.split("\n")

HEADER_RE = re.compile(r"\\textbf\{\\color\{uscred\}\s*([^}]+)\}")
BEGIN_RE = re.compile(r"\\begin\{benumerate\}\{(\d+)\}")
END_RE = re.compile(r"\\end\{benumerate\}")
ITEM_RE = re.compile(r"^\s*\\item")

current_header = ""
in_section = False
start_num = None
items = 0

for i, line in enumerate(lines, 1):
    m = HEADER_RE.search(line)
    if m and any(s in m.group(1) for s in ["Preprints", "Peer-reviewed", "Conference"]):
        current_header = m.group(1).strip()
    m2 = BEGIN_RE.search(line)
    if m2:
        in_section = True
        start_num = int(m2.group(1))
        items = 0
        begin_line = i
    if in_section and ITEM_RE.match(line):
        items += 1
    if in_section and END_RE.search(line):
        end_num = start_num - items + 1
        print(f"{current_header} :: starts at line {begin_line}, items={items}, range {start_num} -> {end_num}")
        in_section = False
