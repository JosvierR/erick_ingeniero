# -*- coding: utf-8 -*-
"""Annotate select pages of the NEW proposal PDF with coord grid."""
from pathlib import Path
import fitz
from PIL import Image, ImageDraw, ImageFont

PDF = Path(r"c:\Users\Josvier\Desktop\Copia de Propuesta diseño DLCI (1).pdf")
OUT = Path(r"c:\Users\Josvier\Desktop\erick_ingeniero\dlci-web\public\dlci\_reimport_staging\annotated_new")
OUT.mkdir(parents=True, exist_ok=True)

doc = fitz.open(PDF)
for p in (15, 16, 17, 18):
    page = doc[p - 1]
    pix = page.get_pixmap(matrix=fitz.Matrix(1.0, 1.0))
    img = Image.frombytes("RGB", (pix.width, pix.height), pix.samples)
    draw = ImageDraw.Draw(img)
    try:
        font = ImageFont.truetype("arial.ttf", 11)
    except OSError:
        font = ImageFont.load_default()
    step = 50
    for x in range(0, pix.width, step):
        color = (200, 80, 80) if x % 200 == 0 else (210, 210, 240)
        draw.line([(x, 0), (x, pix.height)], fill=color, width=1)
        draw.text((x + 2, 4), str(x), fill=(20, 20, 80), font=font)
    for y in range(0, pix.height, step):
        color = (200, 80, 80) if y % 200 == 0 else (210, 210, 240)
        draw.line([(0, y), (pix.width, y)], fill=color, width=1)
        draw.text((4, y + 2), str(y), fill=(20, 20, 80), font=font)
    img.save(OUT / f"p{p:02d}_grid.png")
    print(f"p{p:02d} {pix.width}x{pix.height}")
doc.close()
