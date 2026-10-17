from pathlib import Path
import base64
import xml.etree.ElementTree as ET

import cairosvg


OUT = Path(__file__).resolve().parent
RED = "#990000"
GOLD = "#FFCC00"

# The silhouette and shield are separate editable vector paths.
BODY = """M 177,87
Q 174,81 174,93
L 179,169
Q 180,175 173,178
L 90,211
Q 84,214 85,221
L 94,277
L 72,289
Q 65,293 74,296
Q 92,299 108,287
Q 112,284 111,278
L 106,237
L 165,217
L 170,271
Q 173,310 202,332
L 228,351
L 195,395
L 259,408
Q 273,411 267,400
L 239,374
L 278,319
Q 284,311 275,305
L 254,288
L 314,279
L 345,344
Q 349,353 358,347
L 411,315
Q 422,306 409,305
L 365,322
L 335,256
Q 332,249 324,248
L 281,245
L 273,206
L 359,182
L 397,242
Q 401,249 409,244
L 443,222
Q 451,214 440,215
L 417,223
L 379,156
Q 375,149 367,151
L 253,177
L 357,121
L 350,98
L 246,145
L 323,65
Q 328,59 323,53
L 311,42
Q 306,37 301,43
L 218,130
Z"""
SHIELD = "M 222,225 Q 233,225 240,219 Q 247,225 258,225 L 257,239 Q 255,251 240,260 Q 225,251 223,239 Z"


def symbol(mono=False, micro=False):
    body = f'<path id="mascot-body" d="{BODY}" fill="{RED if mono else GOLD}" stroke="{RED}" stroke-width="14" stroke-linejoin="round" stroke-linecap="round"/>'
    shield = "" if micro else f'<path id="chest-shield" d="{SHIELD}" fill="{"#FFFFFF" if mono else RED}"/>'
    return f'<g id="mascot">{body}{shield}</g>'


def svg(content, width, height, title):
    return f'<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img"><title>{title}</title>{content}</svg>'


def save(name, data, png_width=None):
    ET.fromstring(data)
    (OUT / f"{name}.svg").write_text(data)
    cairosvg.svg2png(bytestring=data.encode(), write_to=str(OUT / f"{name}.png"), output_width=png_width)


def icon(x, y, size, mono=False, micro=False):
    return f'<g transform="translate({x},{y}) scale({size / 408}) translate(-56,-25)">{symbol(mono, micro)}</g>'


def wordmark(x, y, size, text="FORTIS", color=RED):
    return f'<text x="{x}" y="{y}" fill="{color}" font-family="Arial, sans-serif" font-size="{size}" font-weight="900" letter-spacing="{size * 0.045}">{text}</text>'


def label(x, y, text, size=14, color="#777777"):
    return f'<text x="{x}" y="{y}" fill="{color}" font-family="Arial, sans-serif" font-size="{size}">{text}</text>'


save("fortis-mark-v1", svg(icon(0, 0, 408), 408, 408, "FORTIS mascot, simplified draft v1"), 1224)
save("fortis-mark-micro-v1", svg(icon(0, 0, 408, micro=True), 408, 408, "FORTIS small-size mascot"), 408)
save("fortis-mark-mono-v1", svg(icon(0, 0, 408, mono=True), 408, 408, "FORTIS one-color mascot"), 816)
horizontal = svg(icon(0, 0, 144) + wordmark(170, 91, 57) + label(174, 116, "LAB", 16, RED), 436, 144, "FORTIS Lab horizontal logo")
save("fortis-horizontal-v1", horizontal, 1308)
save("fortis-stacked-v1", svg(icon(46, 0, 316) + wordmark(34, 376, 76), 408, 408, "FORTIS stacked logo"), 816)
cairosvg.svg2pdf(bytestring=horizontal.encode(), write_to=str(OUT / "fortis-horizontal-v1.pdf"))

old = base64.b64encode((OUT.parent / "fortis-logo-vectorized" / "fortis-original-raster.png").read_bytes()).decode()
board = '<rect width="1200" height="900" fill="#FAFAF7"/>'
board += label(54, 51, "FORTIS / LOGO STUDY 01", 18, RED)
board += label(54, 79, "Same character. Fewer details. Editable vector paths.", 17, "#555555")
board += '<path d="M54 105 H1146" stroke="#DEDED7"/>'
board += label(68, 147, "CURRENT", 13)
board += f'<image x="65" y="181" width="220" height="220" xlink:href="data:image/png;base64,{old}"/>'
board += label(370, 147, "SIMPLIFIED / PRIMARY MARK", 13)
board += icon(369, 157, 320)
board += label(804, 147, "HORIZONTAL / WEBSITE + LETTERHEAD", 13)
board += icon(789, 218, 114) + wordmark(919, 289, 40) + label(922, 311, "LAB", 13, RED)
board += label(806, 399, "Cardinal  #990000", 15)
board += '<rect x="806" y="417" width="28" height="28" rx="5" fill="#990000"/>'
board += label(860, 438, "Gold  #FFCC00", 15)
board += '<rect x="1003" y="417" width="28" height="28" rx="5" fill="#FFCC00"/>'
board += '<path d="M54 507 H1146" stroke="#DEDED7"/>'
board += label(68, 549, "SMALL-SIZE CHECK", 13)
for x, size in [(70, 32), (150, 48), (247, 60)]:
    board += icon(x, 588, size, micro=size == 32)
    board += label(x, 681, f"{size}px", 13)
board += label(68, 727, "32px uses the shield-free micro mark.", 13)
board += label(427, 549, "ONE-COLOR COMPANION", 13)
board += icon(454, 580, 154, mono=True)
board += label(765, 549, "LETTERHEAD / PLACEMENT STUDY", 13)
board += '<rect x="765" y="572" width="375" height="215" fill="white" stroke="#E1E1DB"/>'
board += icon(786, 588, 52) + wordmark(849, 619, 23) + label(850, 635, "LAB", 8, RED)
board += '<path d="M788 654 H1117" stroke="#990000" stroke-width="1.5"/>'
for y, w in [(679, 240), (692, 301), (705, 287), (728, 303), (741, 260), (754, 282)]:
    board += f'<rect x="788" y="{y}" width="{w}" height="3" fill="#DEDEDB"/>'
board += label(54, 855, "DRAFT 01  /  Simplified silhouette + independent shield + editable wordmark", 14)
save("preview-v1", svg(board, 1200, 900, "FORTIS logo draft comparison and size checks"), 1800)
print(f"Saved editable SVGs and previews to {OUT}")
