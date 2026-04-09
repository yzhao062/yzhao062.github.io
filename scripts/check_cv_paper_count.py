"""Check that benumerate start numbers match cumulative paper counts in cv-full.tex.

The CV uses three benumerate sections with reverse numbering:
  benumerate{N1} for Preprints (N1 = total papers)
  benumerate{N2} for Journals (N2 = journals + conference/workshop)
  benumerate{N3} for Conference/Workshop (N3 = conference/workshop only)
"""
import re, os

cv_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "cv", "cv-full.tex")
with open(cv_path, encoding="utf-8") as f:
    lines = f.readlines()

in_section = False
current_start = 0
current_count = 0
sections = []  # list of (start_number, item_count)

for line in lines:
    m = re.search(r"begin\{benumerate\}\{(\d+)\}", line)
    if m:
        in_section = True
        current_start = int(m.group(1))
        current_count = 0
    elif "end{benumerate}" in line and in_section:
        sections.append((current_start, current_count))
        in_section = False
    elif in_section and re.match(r"\s+\\item\s", line):
        current_count += 1

# Compute expected start numbers (cumulative from bottom)
counts = [s[1] for s in sections]  # item counts per section
expected = []
cumulative = 0
for c in reversed(counts):
    cumulative += c
    expected.insert(0, cumulative)

ok = True
labels = ["Preprints", "Journals", "Conference/Workshop"]
for i, (start, count) in enumerate(sections):
    label = labels[i] if i < len(labels) else f"Section {i}"
    exp = expected[i]
    status = "OK" if start == exp else f"MISMATCH (starts at {start}, should be {exp}, has {count} items)"
    if start != exp:
        ok = False
    print(f"  {label}: benumerate({start}), {count} items, expected start={exp} -- {status}")

print(f"\nTotal papers: {sum(counts)}")
if not ok:
    print("FIX NEEDED: update benumerate start numbers.")
else:
    print("All counts match.")
