# -*- coding: utf-8 -*-
"""Render p12 full page with fine grid for logo positioning."""
from pathlib import Path
import fitz
from PIL import Image, ImageDraw

NEW_PDF = Path(r"c:\Users\Josvier\Desktop\Copia de Propuesta diseño DLCI (1).pdf")
OUT = Path(r"c:\Users\Josvier\Desktop\erick_ingeniero\dlci-web\public\dlci\_reimport_staging\logo_diag")
OUT.mkdir(parents=True, exist_ok=True)

DPI = 1.5


def render(page_no: int, dpi=DPI):
    doc = fitz.open(NEW_PDF)
    page = doc[page_no - 1]
    pix = page.get_pixmap(matrix=fitz.Matrix(dpi, dpi), alpha=False)
    img = Image.frombytes("RGB", (pix.width, pix.height), pix.samples).copy()
    doc.close()
    return img


img = render(12, dpi=DPI)
draw = ImageDraw.Draw(img)
W, H = img.size

for x_pt in range(0, 1440, 20):
    px = int(x_pt * DPI)
    if x_pt % 100 == 0:
        draw.line([(px, 0), (px, H)], fill=(255, 0, 0), width=2)
        draw.text((px + 2, 5), str(x_pt), fill=(255, 0, 0))
    else:
        draw.line([(px, 0), (px, H)], fill=(255, 200, 200), width=1)
        if x_pt % 50 == 0:
            draw.text((px + 1, 5), str(x_pt), fill=(180, 0, 0))

for y_pt in range(0, 810, 20):
    py = int(y_pt * DPI)
    if y_pt % 100 == 0:
        draw.line([(0, py), (W, py)], fill=(0, 0, 255), width=2)
        draw.text((5, py + 2), str(y_pt), fill=(0, 0, 255))
    else:
        draw.line([(0, py), (W, py)], fill=(200, 200, 255), width=1)
        if y_pt % 50 == 0:
            draw.text((5, py + 1), str(y_pt), fill=(0, 0, 180))

img.save(OUT / "p12_full_grid.png")
print("Saved:", OUT / "p12_full_grid.png", "size:", img.size)
