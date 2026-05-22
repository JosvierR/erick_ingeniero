# -*- coding: utf-8 -*-
"""Locate logos by analyzing horizontal extent of dark content in each row."""
from pathlib import Path
import fitz
from PIL import Image, ImageDraw
import numpy as np

NEW_PDF = Path(r"c:\Users\Josvier\Desktop\Copia de Propuesta diseño DLCI (1).pdf")
OUT = Path(r"c:\Users\Josvier\Desktop\erick_ingeniero\dlci-web\public\dlci\_reimport_staging\logo_diag")
OUT.mkdir(parents=True, exist_ok=True)

DPI = 3.0


def render(page_no: int):
    doc = fitz.open(NEW_PDF)
    page = doc[page_no - 1]
    pix = page.get_pixmap(matrix=fitz.Matrix(DPI, DPI), alpha=False)
    img = Image.frombytes("RGB", (pix.width, pix.height), pix.samples).copy()
    doc.close()
    return img


img = render(12)
arr = np.array(img)
gray = arr.mean(axis=2)
H, W = gray.shape
mask = gray < 230

# For each vertical band, find left and right extents of content
bands = [
    ("clients_row1", 160, 290),
    ("clients_row2", 285, 380),
    ("clients_row3", 390, 480),
    ("providers_row1", 500, 600),
    ("providers_row2", 590, 680),
    ("providers_row3", 660, 770),
]

# Also dump the page into the logo_diag folder for visual reference
img_small = img.resize((img.width // 3, img.height // 3))
img_small.save(OUT / "p12_render.png")

# For each band, find column positions where content appears
for name, y0, y1 in bands:
    sub = mask[int(y0*DPI):int(y1*DPI), :]
    col_has = sub.sum(axis=0)
    threshold = 5  # at least 5 dark pixels in column
    # Find continuous runs of "has content"
    runs = []
    in_run = False
    start = 0
    for x in range(W):
        if col_has[x] > threshold:
            if not in_run:
                start = x
                in_run = True
        else:
            if in_run:
                if (x - start) > int(15 * DPI):  # at least 15 points wide
                    runs.append((start, x))
                in_run = False
    if in_run:
        runs.append((start, W))

    # Group close runs together (gaps < 8 points are part of same logo)
    grouped = []
    if runs:
        cur_start, cur_end = runs[0]
        for s, e in runs[1:]:
            if (s - cur_end) < int(8 * DPI):
                cur_end = e
            else:
                grouped.append((cur_start, cur_end))
                cur_start, cur_end = s, e
        grouped.append((cur_start, cur_end))

    print(f"\n[{name}] y={y0}..{y1}: {len(grouped)} groups")
    for s, e in grouped:
        print(f"   x={s/DPI:6.1f}..{e/DPI:6.1f}  (w={(e-s)/DPI:.0f}pt)")
