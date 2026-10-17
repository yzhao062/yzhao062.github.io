"""Export the approved USC-color logo as three reusable components."""

from copy import deepcopy
from pathlib import Path
import json
import xml.etree.ElementTree as ET
import zipfile

import cairosvg
from fontTools.pens.boundsPen import BoundsPen
from fontTools.svgLib.path import parse_path
from PIL import Image


ROOT = Path(__file__).resolve().parent
OUT = ROOT / "brand-kit"
OUT.mkdir(exist_ok=True)
NS = "http://www.w3.org/2000/svg"
ET.register_namespace("", NS)
tag = lambda name: f"{{{NS}}}{name}"
source = ET.parse(ROOT / "variants/fortis-original-flat.svg").getroot()
original = {p.get("id"): p.get("d") for p in source.iter(tag("path"))}


def bounds(root):
    pen = BoundsPen(None)
    for path in root.iter(tag("path")):
        parse_path(path.get("d"), pen)
    return pen.bounds


full_box = bounds(source)
square_side = max(full_box[2] - full_box[0], full_box[3] - full_box[1]) + 64
specs = [
    ("fortis-logo", {"mascot", "motion-lines", "fortis-wordmark"}, "FORTIS logo with bottom wordmark", True),
    ("fortis-symbol", {"mascot", "motion-lines"}, "FORTIS symbol with motion lines", True),
    ("fortis-wordmark", {"fortis-wordmark"}, "FORTIS wordmark", False),
]
manifest = {"colors": {"USC Cardinal": "#990000", "USC Gold": "#FFCC00"},
            "color_source": "https://identity.usc.edu/identity/color/",
            "editing": "SVG paths are editable outlines; letters are individually grouped, not live font text.",
            "geometry": "Original paths and relative sizes preserved. Symbol retains every motion line. No scaling or distortion within assets.",
            "files": {}}
trees = []
for name, keep, title, square in specs:
    root = deepcopy(source)
    for group in root.findall(tag("g")):
        if group.get("id") not in keep:
            root.remove(group)
    box = bounds(root)
    if square:
        width = height = square_side
        left = (box[0] + box[2] - width) / 2
        top = (box[1] + box[3] - height) / 2
    else:
        left, top = box[0] - 16, box[1] - 16
        width, height = box[2] - box[0] + 32, box[3] - box[1] + 32
    root.set("viewBox", f"{left:.6f} {top:.6f} {width:.6f} {height:.6f}")
    root.set("width", f"{width:.6f}")
    root.set("height", f"{height:.6f}")
    root.find(tag("title")).text = title
    root.find(tag("desc")).text = manifest["geometry"] + " USC Cardinal #990000 and USC Gold #FFCC00. Transparent background."
    paths = list(root.iter(tag("path")))
    assert all(p.get("d") == original[p.get("id")] for p in paths)
    assert not any(n.get("transform") for n in root.iter())
    assert {p.get("fill") for p in paths} == {"#990000", "#FFCC00"}
    payload = ET.tostring(root, encoding="utf-8", xml_declaration=True)
    (OUT / f"{name}.svg").write_bytes(payload)
    cairosvg.svg2png(bytestring=payload, write_to=str(OUT / f"{name}.png"), output_width=2048 if square else 1600)
    with Image.open(OUT / f"{name}.png") as image:
        assert image.mode == "RGBA"
        assert image.getchannel("A").getextrema() == (0, 255)
        png_size = image.size
    manifest["files"][name] = {"groups": sorted(keep), "unchanged_paths": len(paths), "square": square,
                               "viewBox": root.get("viewBox"), "png_size": png_size}
    trees.append(root)

assert manifest["files"]["fortis-logo"]["unchanged_paths"] == len(original)
assert (manifest["files"]["fortis-symbol"]["unchanged_paths"] +
        manifest["files"]["fortis-wordmark"]["unchanged_paths"]) == len(original)
board = '<rect width="1200" height="510" fill="white"/>'
board += '<g font-family="Arial, sans-serif" fill="#990000" font-size="20">'
labels = ["01 / LOGO", "02 / SYMBOL", "03 / WORDMARK"]
for x, label in zip([200, 600, 1000], labels):
    board += f'<text x="{x}" y="48" text-anchor="middle">{label}</text>'
board += '</g>'
for index, root in enumerate(trees):
    clone = deepcopy(root)
    for node in clone.iter():
        if node.get("id"):
            node.set("id", f"kit-{index}-" + node.get("id"))
    box = bounds(clone)
    center_x, center_y = (box[0] + box[2]) / 2, (box[1] + box[3]) / 2
    content = ''.join(ET.tostring(child, encoding="unicode") for child in clone)
    board += f'<g transform="translate({200 + index * 400} 258) scale(0.68) translate({-center_x} {-center_y})">{content}</g>'
board += '<g font-family="Arial, sans-serif" font-size="15" fill="#666"><text x="600" y="480" text-anchor="middle">USC Cardinal #990000 + USC Gold #FFCC00 / Original paths and relative sizes preserved</text></g>'
preview = f'<svg xmlns="{NS}" width="1200" height="510" viewBox="0 0 1200 510">{board}</svg>'
(OUT / "preview.svg").write_text(preview)
cairosvg.svg2png(bytestring=preview.encode(), write_to=str(OUT / "preview.png"), output_width=1800)
(OUT / "manifest.json").write_text(json.dumps(manifest, indent=2) + "\n")
with zipfile.ZipFile(OUT / "fortis-brand-kit.zip", "w", zipfile.ZIP_DEFLATED) as archive:
    for name, *_ in specs:
        for extension in ("svg", "png"):
            archive.write(OUT / f"{name}.{extension}", f"{name}.{extension}")
    for name in ("manifest.json", "preview.png"):
        archive.write(OUT / name, name)
print(json.dumps(manifest, indent=2))
