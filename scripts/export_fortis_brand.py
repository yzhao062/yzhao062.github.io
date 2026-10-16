#!/usr/bin/env python3
"""Export images/fortis SVG masters to PNG/PDF. Requires cairosvg and Pillow."""

from pathlib import Path
import hashlib
import json
import xml.etree.ElementTree as ET

import cairosvg
from PIL import Image


ROOT = Path(__file__).resolve().parents[1]
BRAND = ROOT / "images" / "fortis"
NS = "{http://www.w3.org/2000/svg}"
COLORS = {"#990000", "#FFCC00"}


def main():
    assets = {}
    for name, path_count, width in (
        ("fortis-logo", 32, 2048),
        ("fortis-symbol", 20, 2048),
        ("fortis-wordmark", 12, 1600),
    ):
        source = BRAND / f"{name}.svg"
        payload = source.read_bytes()
        root = ET.fromstring(payload)
        paths = list(root.iter(NS + "path"))
        assert len(paths) == path_count
        assert {p.get("fill") for p in paths} == COLORS
        assert not list(root.iter(NS + "image"))
        cairosvg.svg2png(bytestring=payload, write_to=str(BRAND / f"{name}.png"), output_width=width)
        cairosvg.svg2pdf(bytestring=payload, write_to=str(BRAND / f"{name}.pdf"))
        with Image.open(BRAND / f"{name}.png") as image:
            assert image.mode == "RGBA"
            assert image.getchannel("A").getextrema() == (0, 255)
            size = image.size
        assets[name] = {"svg_sha256": hashlib.sha256(payload).hexdigest(), "paths": path_count, "png_size": size}
    (ROOT / "images/lab-logo.png").write_bytes((BRAND / "fortis-logo.png").read_bytes())
    manifest = {
        "source_repository": "https://github.com/yzhao062/yzhao062.github.io",
        "source_directory": "images/fortis",
        "masters": "The three SVG files are authoritative. Edit their paths, then run scripts/export_fortis_brand.py.",
        "colors": {"USC Cardinal": "#990000", "USC Gold": "#FFCC00"},
        "color_reference": "https://identity.usc.edu/identity/color/",
        "editing": "Paths and letter groups are editable; lettering is outlined, not live text.",
        "usage": {"fortis-logo": "Square logo with bottom wordmark.", "fortis-symbol": "Square symbol with all motion lines, for icons or placement beside a title.", "fortis-wordmark": "Separate outlined lettering for custom layouts."},
        "compatibility_alias": "images/lab-logo.png is exported from fortis-logo.svg for existing consumers and social previews.",
        "exports": "PNG files have transparent backgrounds. PDF files retain vector paths for LaTeX.",
        "assets": assets,
    }
    (BRAND / "brand.json").write_text(json.dumps(manifest, indent=2) + "\n")
    print(json.dumps(assets, indent=2))


if __name__ == "__main__":
    main()
