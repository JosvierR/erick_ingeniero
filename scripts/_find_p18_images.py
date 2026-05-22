# -*- coding: utf-8 -*-
"""Find image bounding boxes on p18 of NEW PDF by scanning for non-white regions."""
from pathlib import Path
import fitz
from PIL import Image
import numpy as np

PDF = Path(r"c:\Users\Josvier\Desktop\Copia de Propuesta diseño DLCI (1).pdf")
doc = fitz.open(PDF)
PAGES_TO_SCAN = [12, 15, 16, 17, 18, 21, 22, 23]
for pn in PAGES_TO_SCAN:
    page = doc[pn - 1]
    pix = page.get_pixmap(matrix=fitz.Matrix(1.0, 1.0), alpha=False)
    img = np.array(Image.frombytes("RGB", (pix.width, pix.height), pix.samples))
    print("=" * 60)
    print(f"PAGE {pn}")

    # We want to find rectangles of non-white content in the RIGHT half (x > 500)
    right = img[:, 500:, :]
    # A pixel is "content" if not near-white
    gray = right.mean(axis=2)
    mask = gray < 230  # not white

    # Find horizontal strips of content (rows with any non-white)
    row_has = mask.any(axis=1)
    col_has = mask.any(axis=0)

    print("Rows with content (right half y bands):")
    in_band = False
    start = 0
    bands = []
    for y, v in enumerate(row_has):
        if v and not in_band:
            start = y
            in_band = True
        elif not v and in_band:
            bands.append((start, y - 1))
            in_band = False
    if in_band:
        bands.append((start, len(row_has) - 1))
    for s, e in bands:
        if e - s > 5:
            print(f"  y={s:4d}-{e:4d}")

    print("Cols with content (right half x bands):")
    in_band = False
    start = 0
    bands = []
    for x, v in enumerate(col_has):
        if v and not in_band:
            start = x
            in_band = True
        elif not v and in_band:
            bands.append((start, x - 1))
            in_band = False
    if in_band:
        bands.append((start, len(col_has) - 1))
    for s, e in bands:
        if e - s > 5:
            print(f"  x={s+500:4d}-{e+500:4d}  width={e-s}")
doc.close()
