# -*- coding: utf-8 -*-
"""Render page 13 (clean photo grid: Sorrento, Biventi3, Soria / DJ, Murcia, Bonsai)
with a coordinate grid overlay for visual coord finding."""
from pathlib import Path
import fitz
from PIL import Image, ImageDraw, ImageFont

NEW_PDF = Path(r"c:\Users\Josvier\Desktop\Copia de Propuesta diseño DLCI (1).pdf")
OUT = Path(r"c:\Users\Josvier\Desktop\erick_ingeniero\dlci-web\public\dlci\_p13_probe")
OUT.mkdir(parents=True, exist_ok=True)

DPI = 3.0

doc = fitz.open(NEW_PDF)
page = doc[12]
print(f"Page 13 size (points): {page.rect.width} x {page.rect.height}")
pix = page.get_pixmap(matrix=fitz.Matrix(DPI, DPI), alpha=False)
img = Image.frombytes("RGB", (pix.width, pix.height), pix.samples).copy()
img.save(OUT / "p13_raw.png")

annotated = img.copy()
draw = ImageDraw.Draw(annotated)
try:
    font = ImageFont.truetype("arial.ttf", 18)
except Exception:
    font = ImageFont.load_default()

for x in range(0, int(page.rect.width), 50):
    draw.line([(x * DPI, 0), (x * DPI, img.height)], fill=(200, 0, 0), width=1)
    draw.text((x * DPI + 2, 4), str(x), fill=(200, 0, 0), font=font)
for y in range(0, int(page.rect.height), 50):
    draw.line([(0, y * DPI), (img.width, y * DPI)], fill=(0, 0, 200), width=1)
    draw.text((4, y * DPI + 2), str(y), fill=(0, 0, 200), font=font)

annotated.save(OUT / "p13_grid.png")
print("done")
doc.close()
