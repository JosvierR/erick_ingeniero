# -*- coding: utf-8 -*-
from pathlib import Path
import fitz
from PIL import Image, ImageDraw, ImageFont

PDF = Path(r"c:\Users\Josvier\Desktop\Untitled design.pdf")
OUT = Path(r"c:\Users\Josvier\Desktop\erick_ingeniero\dlci-web\public\dlci\_untitled_probe")
OUT.mkdir(parents=True, exist_ok=True)

DPI = 3.0
doc = fitz.open(PDF)
print(f"pages: {doc.page_count}")

for i in range(doc.page_count):
    page = doc[i]
    pix = page.get_pixmap(matrix=fitz.Matrix(DPI, DPI), alpha=False)
    img = Image.frombytes("RGB", (pix.width, pix.height), pix.samples).copy()
    img.save(OUT / f"p{i+1}_raw.png")

    annotated = img.copy()
    draw = ImageDraw.Draw(annotated)
    try:
        font = ImageFont.truetype("arial.ttf", 20)
    except Exception:
        font = ImageFont.load_default()

    for x in range(0, int(page.rect.width), 50):
        draw.line([(x * DPI, 0), (x * DPI, img.height)], fill=(200, 0, 0), width=1)
        draw.text((x * DPI + 2, 4), str(x), fill=(200, 0, 0), font=font)
    for y in range(0, int(page.rect.height), 50):
        draw.line([(0, y * DPI), (img.width, y * DPI)], fill=(0, 0, 200), width=1)
        draw.text((4, y * DPI + 2), str(y), fill=(0, 0, 200), font=font)

    annotated.save(OUT / f"p{i+1}_grid.png")
    pix_thumb = page.get_pixmap(matrix=fitz.Matrix(1.5, 1.5), alpha=False)
    Image.frombytes("RGB", (pix_thumb.width, pix_thumb.height), pix_thumb.samples).save(
        OUT / f"p{i+1}_thumb.png"
    )
    print(f"p{i+1}: {page.rect.width}x{page.rect.height}, images={len(page.get_images(full=True))}")

doc.close()
print("done")
