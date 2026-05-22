# -*- coding: utf-8 -*-
"""Try a few y0 values for media.jpg and suministro.jpg to find clean crop without title bleed."""
from pathlib import Path
import fitz
from PIL import Image

NEW_PDF = Path(r"c:\Users\Josvier\Desktop\Copia de Propuesta diseño DLCI (1).pdf")
OUT = Path(r"c:\Users\Josvier\Desktop\erick_ingeniero\dlci-web\public\dlci\_reimport_staging\service_crops")
OUT.mkdir(parents=True, exist_ok=True)

DPI = 3.0


def render(page_no: int):
    doc = fitz.open(NEW_PDF)
    page = doc[page_no - 1]
    pix = page.get_pixmap(matrix=fitz.Matrix(DPI, DPI), alpha=False)
    img = Image.frombytes("RGB", (pix.width, pix.height), pix.samples).copy()
    doc.close()
    return img


def crop_box(img, x0, y0, x1, y1):
    return img.crop((int(x0 * DPI), int(y0 * DPI), int(x1 * DPI), int(y1 * DPI)))


img22 = render(22)
img23 = render(23)

# Media tension: try different y0 values
for y0 in [540, 555, 565, 575, 585, 600]:
    crop = crop_box(img22, 861, y0, 1276, 770)
    crop.save(OUT / f"media_y0_{y0}.jpg", "JPEG", quality=90)
    print(f"media y0={y0}: {crop.size}")

# Suministro: try different y0 values
for y0 in [490, 505, 520, 535, 545, 555]:
    crop = crop_box(img23, 896, y0, 1258, 730)
    crop.save(OUT / f"suministro_y0_{y0}.jpg", "JPEG", quality=90)
    print(f"suministro y0={y0}: {crop.size}")

print("\nOutputs:", OUT)
