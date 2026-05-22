# -*- coding: utf-8 -*-
"""Find precise photo bounds by detecting strong (non-light) regions in narrow strips."""
from pathlib import Path
import fitz
from PIL import Image
import numpy as np

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


def find_color_bands(img: Image.Image, x0: int, x1: int, label=""):
    """A photo is a region where pixel saturation/intensity varies a lot.
    Text regions are mostly bright with isolated dark spots; photos have ranges of colors.
    Use per-row std-dev: text rows have low std, photos have high std."""
    arr = np.array(img).astype(np.float32)
    right = arr[:, int(x0 * DPI):int(x1 * DPI), :]
    # Per-row standard deviation across width and channels
    row_std = right.reshape(right.shape[0], -1).std(axis=1)
    # Threshold for "photo-like" row
    photo_thresh = 30.0
    h = right.shape[0]
    print(f"\n[{label}] row std stats: min={row_std.min():.1f} max={row_std.max():.1f} median={np.median(row_std):.1f}")
    bands = []
    in_band = False
    start = 0
    for y in range(h):
        if row_std[y] > photo_thresh:
            if not in_band:
                start = y
                in_band = True
        else:
            if in_band:
                end = y
                if end - start > 40 * DPI:  # at least 40 points tall
                    bands.append((start / DPI, end / DPI))
                in_band = False
    if in_band:
        bands.append((start / DPI, h / DPI))
    print(f"[{label}] photo bands (y0,y1) in points:")
    for y0, y1 in bands:
        print(f"    y={y0:.0f} to y={y1:.0f}  (height={y1-y0:.0f})")
    return bands


for page_no in [21, 22, 23]:
    img = render(page_no)
    find_color_bands(img, 800, 1290, label=f"p{page_no} right-col x=800..1290")
