# -*- coding: utf-8 -*-
"""More precise diagnostic - separately detect TEXT rows and PHOTO rows."""
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


def classify_rows(img: Image.Image, x0: int, x1: int, label=""):
    """For each row, classify as: empty (mostly white), text (sparse dark), or photo (consistent content)."""
    arr = np.array(img).astype(np.float32)
    right = arr[:, int(x0 * DPI):int(x1 * DPI), :]
    h = right.shape[0]
    w = right.shape[1]
    gray = right.mean(axis=2)

    rows_info = []
    for y in range(h):
        row = gray[y]
        nonwhite_pct = (row < 230).sum() / w
        row_color = right[y].std()
        if nonwhite_pct < 0.02:
            kind = "empty"
        elif nonwhite_pct < 0.3 and row_color < 60:
            kind = "text"
        else:
            kind = "photo"
        rows_info.append((kind, nonwhite_pct, row_color))

    print(f"\n[{label}] Page rows classification (showing only transitions):")
    last_kind = None
    last_start = 0
    for y in range(h):
        kind = rows_info[y][0]
        if kind != last_kind:
            if last_kind is not None:
                length_pts = (y - last_start) / DPI
                if length_pts > 5:
                    print(f"  y={last_start/DPI:6.1f} to y={y/DPI:6.1f}  ({length_pts:5.1f}pt)  {last_kind}")
            last_kind = kind
            last_start = y
    if last_kind is not None:
        length_pts = (h - last_start) / DPI
        if length_pts > 5:
            print(f"  y={last_start/DPI:6.1f} to y={h/DPI:6.1f}  ({length_pts:5.1f}pt)  {last_kind}")


for page_no in [21, 22, 23]:
    img = render(page_no)
    classify_rows(img, 800, 1290, label=f"p{page_no} right-col x=800..1290")
