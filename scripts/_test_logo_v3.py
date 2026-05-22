# -*- coding: utf-8 -*-
"""Test extraction with corrected coordinates based on observed content."""
from pathlib import Path
import fitz
from PIL import Image

NEW_PDF = Path(r"c:\Users\Josvier\Desktop\Copia de Propuesta diseño DLCI (1).pdf")
OUT = Path(r"c:\Users\Josvier\Desktop\erick_ingeniero\dlci-web\public\dlci\_reimport_staging\logos_v3")
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


img = render(12)

LOGOS = [
    # CLIENTS row 1 (4 logos)
    ("colon-genao",      630, 160, 830, 290),
    ("infante-curiel",   840, 160, 1040, 290),
    ("jri-inversiones",  1045, 160, 1195, 290),
    ("infante-pichardo", 1195, 160, 1400, 290),

    # CLIENTS row 2 (3 logos)
    ("ortefil",          600, 285, 935, 385),
    ("colizma",          940, 285, 1140, 385),
    ("zonafranca",       1155, 285, 1410, 390),

    # CLIENTS row 3 (3 logos)
    ("murcia-group",     600, 395, 870, 480),
    ("pak-label",        870, 395, 1115, 480),
    ("plusval",          1115, 390, 1320, 480),

    # PROVIDERS row 1 (4 logos)
    ("ochoa-8a",         585, 500, 870, 600),
    ("maelec",           880, 500, 1015, 680),
    ("montan",           1020, 500, 1155, 680),
    ("master",           1165, 500, 1420, 605),

    # PROVIDERS row 2 (2 logos)
    ("bellon",           595, 600, 870, 680),
    ("abb",              1190, 590, 1380, 685),

    # PROVIDERS row 3 (5 logos: ilumeyco, daco, legrand/bticino stacked, leviton)
    ("ilumeyco",         600, 680, 855, 775),
    ("daco",             865, 690, 1015, 760),
    ("legrand",          1020, 680, 1190, 730),
    ("bticino",          1020, 730, 1190, 775),
    ("leviton",          1200, 680, 1390, 775),
]

for name, *rect in LOGOS:
    crop = crop_box(img, *rect)
    crop.save(OUT / f"{name}.png", "PNG")
print("Outputs:", OUT)
