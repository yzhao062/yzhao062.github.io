from pathlib import Path
import base64
import xml.etree.ElementTree as ET

import cairosvg


OUT = Path(__file__).resolve().parent
RED, GOLD = "#990000", "#FFCC00"
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
L 188,211
L 194,260
Q 197,285 219,302
L 240,333
L 201,390
L 253,400
Q 263,402 257,394
L 233,373
L 273,317
Q 277,311 270,305
L 245,283
L 319,274
L 349,339
Q 352,345 358,341
L 410,313
Q 420,306 409,307
L 363,327
L 332,259
Q 330,254 323,253
L 266,250
L 259,210
L 363,179
L 401,239
Q 404,244 410,240
L 442,221
Q 450,215 440,217
L 415,228
L 377,158
Q 374,153 367,155
L 253,177
L 355,119
L 350,101
L 246,145
L 320,64
Q 324,59 320,55
L 311,46
Q 307,42 303,47
L 218,130
Z"""
SHIELD = "M 221,226 Q 230,226 236,221 Q 242,226 251,226 L 250,237 Q 248,247 236,254 Q 224,247 222,237 Z"


def mark(x=0, y=0, size=408, mono=False, micro=False):
    shield = "" if micro else f'<path id="chest-shield" d="{SHIELD}" fill="{"white" if mono else RED}"/>'
    return f'<g id="mascot" transform="translate({x},{y}) scale({size / 408}) translate(-56,-25)"><path id="mascot-body" d="{BODY}" fill="{RED if mono else GOLD}" stroke="{RED}" stroke-width="9" stroke-linejoin="round" stroke-linecap="round"/>{shield}</g>'


def text(x, y, value, size=15, color="#666666", weight=400, spacing=0):
    return f'<text x="{x}" y="{y}" fill="{color}" font-family="Arial, sans-serif" font-size="{size}" font-weight="{weight}" letter-spacing="{spacing}">{value}</text>'


def svg(content, w, h, title):
    return f'<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="{w}" height="{h}" viewBox="0 0 {w} {h}"><title>{title}</title>{content}</svg>'


def save(name, content, w, h, png_width):
    data = svg(content, w, h, name)
    ET.fromstring(data)
    (OUT / f"{name}.svg").write_text(data)
    cairosvg.svg2png(bytestring=data.encode(), write_to=str(OUT / f"{name}.png"), output_width=png_width)
    return data


save("fortis-mark-v2", mark(), 408, 408, 1224)
save("fortis-mark-micro-v2", mark(micro=True), 408, 408, 408)
save("fortis-mark-mono-v2", mark(mono=True), 408, 408, 816)
horizontal = mark(size=144) + text(170, 91, "FORTIS", 57, RED, 900, 2.565) + text(174, 116, "LAB", 16, RED)
data = save("fortis-horizontal-v2", horizontal, 436, 144, 1308)
cairosvg.svg2pdf(bytestring=data.encode(), write_to=str(OUT / "fortis-horizontal-v2.pdf"))
save("fortis-stacked-v2", mark(46, 0, 316) + text(34, 376, "FORTIS", 76, RED, 900, 3.42), 408, 408, 816)

prior = base64.b64encode((OUT / "fortis-mark-v1.png").read_bytes()).decode()
board = '<rect width="1100" height="770" fill="#FAFAF7"/>'
board += text(50, 52, "FORTIS / PROPORTION REVISION", 18, RED)
board += text(50, 83, "Narrower torso, lighter outline, more open space between limbs.", 16)
board += '<path d="M50 110 H1050" stroke="#DEDED7"/>'
board += text(120, 153, "V1 / PREVIOUS", 14)
board += text(620, 153, "V2 / SLIMMER", 14, RED)
board += f'<image x="100" y="174" width="360" height="360" xlink:href="data:image/png;base64,{prior}"/>'
board += mark(600, 174, 360)
board += '<path d="M50 563 H1050" stroke="#DEDED7"/>'
board += mark(75, 604, 104) + text(196, 671, "FORTIS", 41, RED, 900, 1.8) + text(199, 693, "LAB", 12, RED)
board += text(610, 601, "SMALL-SIZE CHECK", 13)
for x, size in [(618, 32), (724, 48), (849, 60)]:
    board += mark(x, 624, size, micro=size == 32)
    board += text(x, 717, f"{size}px", 13)
save("preview-v2", board, 1100, 770, 1650)
print("Saved v2. V1 files retained.")
