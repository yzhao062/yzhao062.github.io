"""Trace the original FORTIS artwork without changing its composition.

Requires Pillow, NumPy, SciPy, CairoSVG, and potracer.
The SVG is the editable master; rerunning this script replaces generated files.
"""

from pathlib import Path
import base64
import json
import xml.etree.ElementTree as ET

import cairosvg
import numpy as np
from PIL import Image
from scipy import ndimage
import potrace


OUT = Path(__file__).resolve().parent
SOURCE = OUT / "fortis-original-raster.png"
rgba = np.asarray(Image.open(SOURCE).convert("RGBA"))
alpha = rgba[:, :, 3] > 127
components, count = ndimage.label(alpha)
rgb = rgba[:, :, :3].astype(float)
gold = (rgb[:, :, 1] > rgb[:, :, 0] * 0.42) & alpha
gold_labels, _ = ndimage.label(gold)
gold_sizes = np.bincount(gold_labels.ravel())
gold = (gold_sizes[gold_labels] > 100) & (gold_labels > 0)
ns = "{http://www.w3.org/2000/svg}"


def trace(mask):
    curves = potrace.Bitmap(~mask).trace(turdsize=2, alphamax=1.0, opttolerance=0.12)
    def point(p):
        return f"{p.x:.3f},{p.y:.3f}"
    parts = []
    for curve in curves:
        parts.append(f"M{point(curve.start_point)}")
        for segment in curve:
            if segment.is_corner:
                parts.append(f"L{point(segment.c)} L{point(segment.end_point)}")
            else:
                parts.append(f"C{point(segment.c1)} {point(segment.c2)} {point(segment.end_point)}")
        parts.append("Z")
    return " ".join(parts)


def path(mask, identity, fill):
    return f'<path id="{identity}" d="{trace(mask)}" fill="{fill}" fill-rule="evenodd"/>'


def gradient(mask, identity):
    # Fit a smooth color field to interior pixels, leaving edge antialiasing out.
    interior = ndimage.binary_erosion(mask, iterations=3)
    y, x = np.nonzero(interior)
    colors = rgb[interior]
    features = np.column_stack((np.ones(len(x)), x / 512, y / 512))
    coefficients = np.linalg.lstsq(features, colors, rcond=None)[0]
    u, _, _ = np.linalg.svd(coefficients[1:], full_matrices=False)
    direction = u[:, 0]
    corners = np.array([[0, 0], [1, 0], [0, 1], [1, 1]])
    projections = corners @ direction
    start, end = projections.min(), projections.max()
    anchor = np.array([0.5, 0.5])
    p0 = anchor + (start - anchor @ direction) * direction
    p1 = anchor + (end - anchor @ direction) * direction
    stops = []
    for t in np.linspace(0, 1, 9):
        point = p0 * (1 - t) + p1 * t
        color = np.clip(np.rint(np.array([1, *point]) @ coefficients), 0, 255).astype(int)
        stops.append(f'<stop offset="{t:.3f}" stop-color="#{color[0]:02x}{color[1]:02x}{color[2]:02x}"/>')
    return f'<linearGradient id="{identity}" gradientUnits="userSpaceOnUse" x1="{p0[0]*512:.3f}" y1="{p0[1]*512:.3f}" x2="{p1[0]*512:.3f}" y2="{p1[1]*512:.3f}">{"".join(stops)}</linearGradient>'


objects = []
for identity in range(1, count + 1):
    mask = components == identity
    if mask.sum() < 10:
        continue
    y, x = np.nonzero(mask)
    objects.append((identity, int(mask.sum()), int(x.min()), int(y.min())))
body_id = max(objects, key=lambda item: item[1])[0]
body_mask = components == body_id
body_gold = gold & body_mask
filled_body_gold = ndimage.binary_fill_holes(body_gold)
shield = filled_body_gold & ~body_gold
shield_labels, _ = ndimage.label(shield)
shield_sizes = np.bincount(shield_labels.ravel())
shield = (shield_labels > 0) & (shield_sizes[shield_labels] > 100)

defs = gradient(alpha & ~gold, "original-red") + gradient(gold, "original-gold")
art = '<g id="mascot"><title>Original mascot silhouette and chest shield</title>'
art += path(body_mask, "body-red-outline", "url(#original-red)")
art += path(filled_body_gold, "body-gold-fill", "url(#original-gold)")
art += path(shield, "chest-shield", "url(#original-red)") + '</g>'

motion = [item for item in objects if item[0] != body_id and item[3] < 440]
art += '<g id="motion-lines"><title>17 original motion lines</title>'
for index, (identity, *_) in enumerate(motion, 1):
    art += path(components == identity, f"motion-{index:02d}", "url(#original-red)")
art += '</g><g id="fortis-wordmark"><title>Original FORTIS lettering, editable outlines</title>'
letters = sorted((item for item in objects if item[3] >= 440), key=lambda item: item[2])
for letter, (identity, *_) in zip("FORTIS", letters, strict=True):
    mask = components == identity
    art += f'<g id="letter-{letter}">'
    art += path(mask, f"letter-{letter}-outline", "url(#original-red)")
    art += path(gold & mask, f"letter-{letter}-fill", "url(#original-gold)") + '</g>'
art += '</g>'

svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="512" height="512" viewBox="0 0 512 512">
<title>FORTIS original logo, faithful editable vector trace</title>
<desc>Traced from lab-logo.png at its original 512 by 512 coordinates. Original silhouette, 17 motion lines, shield, and six custom letters retained. All artwork is vector paths. Smooth gradients approximate original colors; pixel grain is omitted.</desc>
<defs>{defs}</defs>{art}</svg>'''
ET.fromstring(svg)
(OUT / "fortis-original-editable.svg").write_text(svg)
cairosvg.svg2png(bytestring=svg.encode(), write_to=str(OUT / "fortis-original-vector.png"), output_width=1536, output_height=1536)
cairosvg.svg2png(bytestring=svg.encode(), write_to=str(OUT / "trace-512.png"))

rendered = np.asarray(Image.open(OUT / "trace-512.png").convert("RGBA"))
traced_alpha = rendered[:, :, 3] > 127
intersection = np.count_nonzero(alpha & traced_alpha)
union = np.count_nonzero(alpha | traced_alpha)
metrics = {
    "source": str(SOURCE), "canvas": [512, 512],
    "motion_lines": len(motion), "letter_groups": len(letters),
    "paths": len(ET.fromstring(svg).findall(f".//{ns}path")),
    "alpha_intersection_over_union": intersection / union,
    "alpha_disagreement_pixels": int(np.count_nonzero(alpha ^ traced_alpha)),
    "raster_images_in_master": len(ET.fromstring(svg).findall(f".//{ns}image")),
}
(OUT / "trace-check.json").write_text(json.dumps(metrics, indent=2) + "\n")

original_b64 = base64.b64encode(SOURCE.read_bytes()).decode()
vector_b64 = base64.b64encode((OUT / "fortis-original-vector.png").read_bytes()).decode()
preview = f'''<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="1120" height="650" viewBox="0 0 1120 650">
<rect width="1120" height="650" fill="#ffffff"/>
<g font-family="Arial, sans-serif" fill="#555555" font-size="17">
<text x="55" y="44">ORIGINAL PNG</text><text x="605" y="44">EDITABLE SVG / FAITHFUL TRACE</text>
</g><path d="M560 65 V595" stroke="#eeeeee"/>
<image x="35" y="67" width="500" height="500" xlink:href="data:image/png;base64,{original_b64}"/>
<image x="585" y="67" width="500" height="500" xlink:href="data:image/png;base64,{vector_b64}"/>
<text x="55" y="620" font-family="Arial, sans-serif" fill="#777777" font-size="14">Original proportions, motion lines, shield, and lettering retained. Transparent vector master.</text>
</svg>'''
cairosvg.svg2png(bytestring=preview.encode(), write_to=str(OUT / "original-vs-vector.png"), output_width=1680)

# Magenta identifies original-only pixels; cyan identifies vector-only pixels.
overlay = np.full((512, 512, 3), 255, dtype="uint8")
overlay[alpha & traced_alpha] = [100, 100, 100]
overlay[alpha & ~traced_alpha] = [220, 0, 130]
overlay[traced_alpha & ~alpha] = [0, 180, 200]
Image.fromarray(overlay).save(OUT / "contour-overlay.png")
print(json.dumps(metrics, indent=2))
