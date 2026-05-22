# -*- coding: utf-8 -*-
"""Diagnose service image crops to remove title text bleed."""
from pathlib import Path
import fitz
from PIL import Image
import numpy as np

NEW_PDF = Path(r"c:\Users\Josvier\Desktop\Copia de Propuesta diseno DLCI (1).pdf")
if not NEW_PDF.exists():
    NEW_PDF = Path(r"c:\Users\Josvier\Desktop\Copia de Propuesta diseño DLCI (1).pdf")
OUT = Path(r"c:\Users\Josvier\Desktop\erick_ingeniero\dlci-web\public\dlci\_reimport_staging\diag_services")
OUT.mkdir(parents=True, exist_ok=True)

DPI = 3.0


def render(page_no: int):
    doc = fitz.open(NEW_PDF)
    page = doc[page_no - 1]
    pix = page.get_pixmap(matrix=fitz.Matrix(DPI, DPI), alpha=False)
    img = Image.frombytes("RGB", (pix.width, pix.height), pix.samples).copy()
    doc.close()
    return img


def find_photo_bands(img: Image.Image, x0: int, x1: int):
    """Look for horizontal bands of photo content in the right column."""
    arr = np.array(img)
    right = arr[:, int(x0 * DPI):int(x1 * DPI), :]
    gray = right.mean(axis=2)
    h = gray.shape[0]
    nonwhite = (gray < 230).sum(axis=1)
    threshold = (x1 - x0) * DPI * 0.2  # at least 20% of width is non-white
    print(f"  threshold for content row: {threshold:.0f}")
    in_band = False
    start = 0
    bands = []
    for y in range(h):
        if nonwhite[y] > threshold:
            if not in_band:
                start = y
                in_band = True
        else:
            if in_band:
                end = y
                if end - start > 30:
                    bands.append((start / DPI, end / DPI))
                in_band = False
    if in_band:
        bands.append((start / DPI, h / DPI))
    return bands


for page_no in [21, 22, 23]:
    print(f"\n== page {page_no} ==")
    img = render(page_no)
    print(f"  rendered size: {img.size}")
    print(f"  page width in points: {img.width / DPI:.0f}")
    print(f"  page height in points: {img.height / DPI:.0f}")
    bands = find_photo_bands(img, 800, 1280)
    print(f"  photo bands (y0,y1) in points:")
    for y0, y1 in bands:
        print(f"    y={y0:.0f} to y={y1:.0f}  (height={y1-y0:.0f})")
    img.save(OUT / f"p{page_no}_full.png")

print("\n  written full pages to:", OUT)
