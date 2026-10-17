"""Derive layout and color variants without changing the traced paths."""

from copy import deepcopy
from pathlib import Path
import hashlib
import json
import xml.etree.ElementTree as ET
import zipfile

import cairosvg
from fontTools.pens.boundsPen import BoundsPen
from fontTools.svgLib.path import parse_path


ROOT = Path(__file__).resolve().parent
OUT = ROOT / "variants"
OUT.mkdir(exist_ok=True)
SOURCE = ROOT / "fortis-original-editable.svg"
SOURCE_HASH = hashlib.sha256(SOURCE.read_bytes()).hexdigest()
NS = "http://www.w3.org/2000/svg"
ET.register_namespace("", NS)
TAG = lambda name: f"{{{NS}}}{name}"
original = ET.parse(SOURCE).getroot()


def bounds(elements):
    pen = BoundsPen(None)
    for element in elements:
        for node in element.iter(TAG("path")):
            parse_path(node.get("d"), pen)
    return pen.bounds


def group(root, identity):
    return next(node for node in root.findall(TAG("g")) if node.get("id") == identity)


def frame(root, box, margin=32):
    left, top, right, bottom = box
    values = (left - margin, top - margin, right - left + 2 * margin, bottom - top + 2 * margin)
    root.set("viewBox", " ".join(f"{v:.4f}" for v in values))
    root.set("width", f"{values[2]:.4f}")
    root.set("height", f"{values[3]:.4f}")


def title(root, value):
    root.find(TAG("title")).text = value


canonical = deepcopy(original)
for node in canonical.iter(TAG("path")):
    node.set("fill", {"url(#original-red)": "#990000", "url(#original-gold)": "#FFCC00"}[node.get("fill")])
canonical.remove(canonical.find(TAG("defs")))
canonical.find(TAG("desc")).text = "Original traced paths and relative sizes preserved. USC web HEX colors: Cardinal #990000 and Gold #FFCC00. Source: https://identity.usc.edu/identity/color/"

safe = deepcopy(canonical)
frame(safe, bounds(safe.findall(TAG("g"))))
title(safe, "FORTIS original logo with equal 32-unit clear space")

horizontal = deepcopy(canonical)
mascot_bounds = bounds([group(horizontal, "mascot"), group(horizontal, "motion-lines")])
word_bounds = bounds([group(horizontal, "fortis-wordmark")])
gap = 48
dx = mascot_bounds[2] + gap - word_bounds[0]
dy = (mascot_bounds[1] + mascot_bounds[3] - word_bounds[1] - word_bounds[3]) / 2
group(horizontal, "fortis-wordmark").set("transform", f"translate({dx:.6f} {dy:.6f})")
frame(horizontal, (
    mascot_bounds[0], min(mascot_bounds[1], word_bounds[1] + dy),
    word_bounds[2] + dx, max(mascot_bounds[3], word_bounds[3] + dy),
))
title(horizontal, "FORTIS horizontal layout, original relative sizes retained")

flat = deepcopy(safe)
flat.find(TAG("desc")).text = "Original traced paths and relative sizes preserved. Uniform red #990000 and gold #FFCC00 fills. Equal 32-unit clear space."
title(flat, "FORTIS original logo, flat red and gold comparison")

variants = {
    "fortis-original-clearspace": safe,
    "fortis-original-horizontal": horizontal,
    "fortis-original-flat": flat,
}
original_paths = {node.get("id"): node.get("d") for node in original.iter(TAG("path"))}
checks = {}
for name, root in variants.items():
    actual = {node.get("id"): node.get("d") for node in root.iter(TAG("path"))}
    assert actual == original_paths, f"Geometry changed in {name}"
    fills = {node.get("fill") for node in root.iter(TAG("path"))}
    assert fills == {"#990000", "#FFCC00"}
    assert len(root.findall(f".//{TAG('image')}")) == 0
    transforms = {node.get("id"): node.get("transform") for node in root.iter() if node.get("transform")}
    if root is horizontal:
        assert list(transforms) == ["fortis-wordmark"]
        assert transforms["fortis-wordmark"].startswith("translate(")
    else:
        assert not transforms
    payload = ET.tostring(root, encoding="utf-8", xml_declaration=True)
    (OUT / f"{name}.svg").write_bytes(payload)
    cairosvg.svg2png(bytestring=payload, write_to=str(OUT / f"{name}.png"), scale=2)
    checks[name] = {"identical_paths": len(actual), "transforms": transforms, "viewBox": root.get("viewBox"), "fills": sorted(fills)}


def preview_art(root, x, y, scale=0.72, suffix=""):
    clone = deepcopy(root)
    left, top, width, height = map(float, clone.get("viewBox").split())
    for node in clone.iter():
        identity = node.get("id")
        if identity:
            node.set("id", identity + suffix)
        fill = node.get("fill", "")
        if fill.startswith("url(#"):
            node.set("fill", fill[:-1] + suffix + ")")
    content = "".join(ET.tostring(child, encoding="unicode") for child in clone)
    return f'<g transform="translate({x} {y}) scale({scale}) translate({-left} {-top})">{content}</g>'


board = '<rect width="1200" height="720" fill="white"/>'
board += '<g font-family="Arial, sans-serif"><text x="70" y="48" fill="#990000" font-size="22">FORTIS / USC CARDINAL + USC GOLD</text>'
board += '<text x="70" y="78" fill="#666666" font-size="15">All 32 paths unchanged. Same character, motion lines, lettering, and relative sizes.</text></g>'
board += '<path d="M70 100 H1130" stroke="#E5E5E5"/>'
board += '<g font-family="Arial, sans-serif" font-size="17" fill="#555555"><text x="100" y="139">VERTICAL / EVEN CLEAR SPACE</text><text x="540" y="139">HORIZONTAL / WORDMARK MOVED ONLY</text></g>'
board += preview_art(safe, 100, 153, suffix="-safe")
board += preview_art(horizontal, 540, 200, scale=0.6, suffix="-horizontal")
board += '<path d="M70 595 H1130" stroke="#E5E5E5"/>'
board += '<rect x="100" y="625" width="52" height="52" rx="4" fill="#990000"/><rect x="540" y="625" width="52" height="52" rx="4" fill="#FFCC00"/>'
board += '<g font-family="Arial, sans-serif" font-size="18" fill="#333333"><text x="170" y="657">USC Cardinal / #990000</text><text x="610" y="657">USC Gold / #FFCC00</text></g>'
preview = f'<svg xmlns="{NS}" width="1200" height="720" viewBox="0 0 1200 720">{board}</svg>'
(OUT / "comparison.svg").write_text(preview)
cairosvg.svg2png(bytestring=preview.encode(), write_to=str(OUT / "comparison.png"), output_width=1800)
assert hashlib.sha256(SOURCE.read_bytes()).hexdigest() == SOURCE_HASH
(OUT / "geometry-check.json").write_text(json.dumps(checks, indent=2) + "\n")
with zipfile.ZipFile(OUT / "fortis-three-variants.zip", "w", zipfile.ZIP_DEFLATED) as archive:
    for name in variants:
        archive.write(OUT / f"{name}.svg", f"{name}.svg")
print(json.dumps(checks, indent=2))
