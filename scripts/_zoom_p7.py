# -*- coding: utf-8 -*-
"""Render page 7 at higher DPI with grid for fine inspection."""
from pathlib import Path
import fitz
from PIL import Image, ImageDraw, ImageFont

PDF = Path(r"c:\Users\Josvier\Desktop\Copia de Propuesta diseño DLCI.pdf")
OUT = Path(r"c:\Users\Josvier\Desktop\erick_ingeniero\dlci-web\public\dlci\_reimport_staging\zoom")
OUT.mkdir(parents=True, exist_ok=True)

doc = fitz.open(PDF)
for p in (7, 8):
    page = doc[p - 1]
    pix = page.get_pixmap(matrix=fitz.Matrix(2.0, 2.0), alpha=False)
    img = Image.frombytes("RGB", (pix.width, pix.height), pix.samples).copy()
    draw = ImageDraw.Draw(img)
    try:
        font = ImageFont.truetype("arial.ttf", 18)
    except OSError:
        font = ImageFont.load_default()
    # grid every 50 page units (each unit = 2 px due to 2x DPI)
    step = 50
    for x in range(0, 1441, step):
        px = x * 2
        color = (200, 60, 60, 150) if x % 200 == 0 else (220, 220, 240, 100)
        draw.line([(px, 0), (px, pix.height)], fill=color, width=2)
        draw.text((px + 3, 4), str(x), fill=(20, 20, 80), font=font)
    for y in range(0, 811, step):
        py = y * 2
        color = (200, 60, 60, 150) if y % 200 == 0 else (220, 220, 240, 100)
        draw.line([(0, py), (pix.width, py)], fill=color, width=2)
        draw.text((4, py + 3), str(y), fill=(20, 20, 80), font=font)
    img.save(OUT / f"p{p:02d}_zoom.png")
    print(f"p{p:02d} {pix.width}x{pix.height}")
doc.close()
