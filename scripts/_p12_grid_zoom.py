# -*- coding: utf-8 -*-
"""Render p12 with a finer grid (every 20 points) and label each grid step.
Zoom to the right side where logos are."""
from pathlib import Path
import fitz
from PIL import Image, ImageDraw, ImageFont

NEW_PDF = Path(r"c:\Users\Josvier\Desktop\Copia de Propuesta diseño DLCI (1).pdf")
OUT = Path(r"c:\Users\Josvier\Desktop\erick_ingeniero\dlci-web\public\dlci\_reimport_staging\logo_diag")
OUT.mkdir(parents=True, exist_ok=True)

DPI = 2.0


def render(page_no: int, dpi=DPI):
    doc = fitz.open(NEW_PDF)
    page = doc[page_no - 1]
    pix = page.get_pixmap(matrix=fitz.Matrix(dpi, dpi), alpha=False)
    img = Image.frombytes("RGB", (pix.width, pix.height), pix.samples).copy()
    doc.close()
    return img


img = render(12, dpi=DPI)
# Crop to right portion (x=380 to 1440)
crop_x0 = int(380 * DPI)
crop = img.crop((crop_x0, 0, img.width, img.height))
draw = ImageDraw.Draw(crop)
H, W = crop.size[1], crop.size[0]

# Vertical lines every 20 points
for x_pt in range(380, 1440, 20):
    px = int((x_pt - 380) * DPI)
    if x_pt % 100 == 0:
        col = (255, 0, 0)
        draw.line([(px, 0), (px, H)], fill=col, width=2)
        draw.text((px + 2, 5), str(x_pt), fill=col)
    else:
        col = (255, 200, 200)
        draw.line([(px, 0), (px, H)], fill=col, width=1)
        if x_pt % 50 == 0:
            draw.text((px + 1, 5), str(x_pt), fill=(180, 0, 0))

# Horizontal lines every 20 points
for y_pt in range(0, 810, 20):
    py = int(y_pt * DPI)
    if y_pt % 100 == 0:
        col = (0, 0, 255)
        draw.line([(0, py), (W, py)], fill=col, width=2)
        draw.text((5, py + 2), str(y_pt), fill=col)
    else:
        col = (200, 200, 255)
        draw.line([(0, py), (W, py)], fill=col, width=1)
        if y_pt % 50 == 0:
            draw.text((5, py + 1), str(y_pt), fill=(0, 0, 180))

crop.save(OUT / "p12_grid_zoomed.png")
print("Saved:", OUT / "p12_grid_zoomed.png", "size:", crop.size)
