# -*- coding: utf-8 -*-
"""Auto-detect logo bounding boxes on p12 of NEW PDF."""
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
arr = np.array(img).astype(np.float32)
print("Image size:", img.size)  # (4320, 2430) at DPI=3
print("Page size in points:", img.width / DPI, img.height / DPI)  # (1440, 810)

# Crop to right side where logos are (clients top half + providers bottom)
# Page is 1440 points wide. Logos start around x=400
H, W = arr.shape[:2]
gray = arr.mean(axis=2)
mask = gray < 240

# Find connected components in a downsampled way
# Sum per row and column to find non-empty regions
row_has = mask.sum(axis=1)
col_has = mask.sum(axis=0)

# Save annotated image with grid
ann = img.copy()
draw = ImageDraw.Draw(ann)
# Coordinate grid every 50 points
for x in range(0, 1440, 50):
    px = int(x * DPI)
    draw.line([(px, 0), (px, H)], fill=(255, 0, 0, 128), width=1)
    if x % 100 == 0:
        draw.text((px + 2, 2), str(x), fill=(255, 0, 0))
for y in range(0, 810, 50):
    py = int(y * DPI)
    draw.line([(0, py), (W, py)], fill=(0, 0, 255, 128), width=1)
    if y % 100 == 0:
        draw.text((2, py + 2), str(y), fill=(0, 0, 255))

ann.save(OUT / "p12_grid.png")
print("Saved annotated grid:", OUT / "p12_grid.png")

# Now find rows that have content in x>=400 area (right side)
right_start = int(400 * DPI)
right_arr = mask[:, right_start:]
row_has_right = right_arr.sum(axis=1)
threshold = int(50 * DPI)  # minimum content in a row

# Find vertical bands of content
in_band = False
start = 0
bands = []
for y in range(H):
    if row_has_right[y] > threshold:
        if not in_band:
            start = y
            in_band = True
    else:
        if in_band:
            if (y - start) > int(40 * DPI):  # at least 40 points tall
                bands.append((start, y))
            in_band = False
if in_band:
    bands.append((start, H))

print(f"\nVertical bands (in points) on right half:")
for y0, y1 in bands:
    print(f"  y={y0/DPI:6.1f} to y={y1/DPI:6.1f}  (h={(y1-y0)/DPI:.1f}pt)")

# For each vertical band, find columns
print("\nLogos per vertical band:")
for bi, (y0, y1) in enumerate(bands):
    band_mask = mask[y0:y1, right_start:]
    col_has = band_mask.sum(axis=0)
    col_threshold = int(20 * DPI)
    cols = []
    in_col = False
    cs = 0
    for x in range(band_mask.shape[1]):
        if col_has[x] > col_threshold:
            if not in_col:
                cs = x
                in_col = True
        else:
            if in_col:
                if (x - cs) > int(20 * DPI):
                    cols.append((cs + right_start, x + right_start))
                in_col = False
    if in_col:
        cols.append((cs + right_start, band_mask.shape[1] + right_start))
    print(f"  band y={y0/DPI:.0f}..{y1/DPI:.0f}  -> {len(cols)} logos:")
    for x0, x1 in cols:
        print(f"      x={x0/DPI:5.0f}..{x1/DPI:5.0f}  (w={(x1-x0)/DPI:.0f}pt)")
