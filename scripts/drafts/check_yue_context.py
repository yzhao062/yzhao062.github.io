"""Show full context for Yue Zhao matches in a PDF."""
import fitz
import re
import sys


doc = fitz.open(sys.argv[1])
for pno in range(len(doc)):
    text = doc[pno].get_text("text")
    for m in re.finditer(r"Yue Zhao", text):
        start = max(0, m.start() - 300)
        end = min(len(text), m.end() + 300)
        ctx = text[start:end].replace("\n", " ")
        print(f"p{pno+1}:", ctx)
        print("---")
doc.close()
