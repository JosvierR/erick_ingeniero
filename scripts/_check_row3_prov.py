# -*- coding: utf-8 -*-
"""Look at row3 of providers more carefully."""
from pathlib import Path
import fitz
from PIL import Image

NEW_PDF = Path(r"c:\Users\Josvier\Desktop\Copia de Propuesta diseño DLCI (1).pdf")
OUT = Path(r"c:\Users\Josvier\Desktop\erick_ingeniero\dlci-web\public\dlci\_reimport_staging\logos_v3")

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


img = render(12)
# Wide crop covering legrand/bticino/leviton
crop_box(img, 990, 660, 1410, 780).save(OUT / "row3_wide.png")
# Try slightly wider for legrand alone
crop_box(img, 1010, 680, 1210, 730).save(OUT / "legrand_wide.png")
crop_box(img, 1010, 730, 1210, 770).save(OUT / "bticino_wide.png")
# Try slightly later start for leviton
crop_box(img, 1210, 680, 1395, 775).save(OUT / "leviton_v2.png")
print("done")
