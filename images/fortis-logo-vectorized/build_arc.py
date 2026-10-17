"""Place the original FORTIS glyphs on an upper arc without scaling paths."""

from copy import deepcopy
from pathlib import Path
import json
import math
import xml.etree.ElementTree as ET

import cairosvg
from fontTools.pens.boundsPen import BoundsPen
from fontTools.pens.transformPen import TransformPen
from fontTools.svgLib.path import parse_path


ROOT = Path(__file__).resolve().parent
OUT = ROOT / "variants"
NS = "http://www.w3.org/2000/svg"
ET.register_namespace("", NS)
tag = lambda name: f"{{{NS}}}{name}"
source = ET.parse(OUT / "fortis-original-flat.svg").getroot()
root = deepcopy(source)
wordmark = next(n for n in root.findall(tag("g")) if n.get("id") == "fortis-wordmark")


def measure(node, transform=None):
    pen = BoundsPen(None)
    target = TransformPen(pen, transform) if transform else pen
    for path in node.iter(tag("path")):
        parse_path(path.get("d"), target)
    return pen.bounds


glyphs = wordmark.findall(tag("g"))
boxes = [measure(glyph) for glyph in glyphs]
widths = [b[2] - b[0] for b in boxes]
spacing = 10
length = sum(widths) + spacing * (len(glyphs) - 1)
radius = 260
center_x = (27.131369051957975 + 473.93403496553674) / 2
center_y = 220
cursor = -length / 2
all_bounds = [measure(n) for n in root.findall(tag("g")) if n is not wordmark]
placements = {}
for glyph, box, width in zip(glyphs, boxes, widths):
    angle = (cursor + width / 2) / radius
    x = center_x + radius * math.sin(angle)
    y = center_y - radius * math.cos(angle)
    origin_x = (box[0] + box[2]) / 2
    origin_y = box[3]
    cos, sin = math.cos(angle), math.sin(angle)
    matrix = (cos, sin, -sin, cos,
              x - cos * origin_x + sin * origin_y,
              y - sin * origin_x - cos * origin_y)
    glyph.set("transform", "matrix(" + " ".join(f"{v:.10f}" for v in matrix) + ")")
    all_bounds.append(measure(glyph, matrix))
    placements[glyph.get("id")] = {"rotation_degrees": math.degrees(angle), "matrix": matrix}
    assert abs(matrix[0] ** 2 + matrix[1] ** 2 - 1) < 1e-12
    cursor += width + spacing

left = min(b[0] for b in all_bounds) - 32
top = min(b[1] for b in all_bounds) - 32
width = max(b[2] for b in all_bounds) + 32 - left
height = max(b[3] for b in all_bounds) + 32 - top
root.set("viewBox", f"{left:.6f} {top:.6f} {width:.6f} {height:.6f}")
root.set("width", f"{width:.6f}")
root.set("height", f"{height:.6f}")
root.find(tag("title")).text = "FORTIS upper arc, original glyphs and mascot, USC colors"
root.find(tag("desc")).text = "Original 32 paths retained. Each letter is independently editable and only rotated and translated. No glyph or mascot scaling. Cardinal #990000; Gold #FFCC00."
paths = lambda tree: {n.get("id"): n.get("d") for n in tree.iter(tag("path"))}
assert paths(root) == paths(source)
assert {n.get("fill") for n in root.iter(tag("path"))} == {"#990000", "#FFCC00"}
payload = ET.tostring(root, encoding="utf-8", xml_declaration=True)
(OUT / "fortis-usc-upper-arc.svg").write_bytes(payload)
cairosvg.svg2png(bytestring=payload, write_to=str(OUT / "fortis-usc-upper-arc.png"), output_width=1000)
cairosvg.svg2png(bytestring=payload, write_to=str(OUT / "fortis-usc-upper-arc-preview.png"), output_width=900, background_color="white")
(OUT / "upper-arc-check.json").write_text(json.dumps({"identical_paths": len(paths(root)), "fills": ["#990000", "#FFCC00"], "letter_placements": placements}, indent=2) + "\n")
print("Verified 32 unchanged paths, rigid letter transforms, and two USC fills.")
