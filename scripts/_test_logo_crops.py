# -*- coding: utf-8 -*-
"""Test crops for each logo with multiple x offsets to find correct positions."""
from pathlib import Path
import fitz
from PIL import Image, ImageDraw

NEW_PDF = Path(r"c:\Users\Josvier\Desktop\Copia de Propuesta diseño DLCI (1).pdf")
OUT = Path(r"c:\Users\Josvier\Desktop\erick_ingeniero\dlci-web\public\dlci\_reimport_staging\logo_crops")
OUT.mkdir(parents=True, exist_ok=True)

DPI = 2.5


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
print("Page size:", img.size)

# Save annotation showing proposed crop regions
ann = img.copy()
draw = ImageDraw.Draw(ann)

# Proposed coordinates (try first set)
LOGOS = [
    # (name, x0, y0, x1, y1, color)
    ("colon-genao",      590, 175, 730, 270, (255, 0, 0)),
    ("infante-curiel",   735, 175, 870, 280, (0, 200, 0)),
    ("jri-inversiones",  875, 195, 1000, 270, (0, 0, 255)),
    ("infante-pichardo", 1010, 165, 1180, 285, (200, 100, 0)),

    ("ortefil",          520, 290, 810, 380, (255, 0, 0)),
    ("colizma",          815, 295, 985, 380, (0, 200, 0)),
    ("zonafranca",       985, 280, 1190, 385, (0, 0, 255)),

    ("murcia-group",     575, 400, 770, 475, (255, 0, 0)),
    ("pak-label",        775, 405, 990, 475, (0, 200, 0)),
    ("plusval",          1000, 400, 1180, 480, (0, 0, 255)),

    ("ochoa-8a",         455, 510, 720, 595, (255, 0, 0)),
    ("maelec",           760, 510, 900, 680, (0, 200, 0)),
    ("montan",           900, 510, 1080, 680, (0, 0, 255)),
    ("master",           1090, 510, 1310, 595, (200, 100, 0)),

    ("bellon",           450, 600, 720, 675, (255, 0, 0)),
    ("abb",              1080, 595, 1320, 680, (200, 100, 0)),

    ("ilumeyco",         450, 685, 700, 770, (255, 0, 0)),
    ("daco",             740, 695, 940, 760, (0, 200, 0)),
    ("legrand",          760, 685, 920, 730, (0, 0, 255)),
    ("bticino",          760, 730, 920, 775, (200, 0, 200)),
    ("leviton",          1090, 685, 1320, 775, (200, 100, 0)),
]

for name, x0, y0, x1, y1, color in LOGOS:
    crop = crop_box(img, x0, y0, x1, y1)
    crop.save(OUT / f"{name}.png", "PNG")
    # Draw rectangle on annotation
    draw.rectangle(
        [int(x0 * DPI), int(y0 * DPI), int(x1 * DPI), int(y1 * DPI)],
        outline=color, width=3
    )
    draw.text((int(x0 * DPI) + 2, int(y0 * DPI) - 18), name, fill=color)

ann.save(OUT / "_annotated.png")
print("Outputs:", OUT)
