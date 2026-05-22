# -*- coding: utf-8 -*-
"""Extract each detected group region as a separate image to identify logos."""
from pathlib import Path
import fitz
from PIL import Image

NEW_PDF = Path(r"c:\Users\Josvier\Desktop\Copia de Propuesta diseño DLCI (1).pdf")
OUT = Path(r"c:\Users\Josvier\Desktop\erick_ingeniero\dlci-web\public\dlci\_reimport_staging\groups")
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

# Test extracting groups detected:
# Clients row 1: y=160-290
GROUPS = [
    ("c_r1_g1", 250, 160, 480, 290),
    ("c_r1_g2", 640, 160, 820, 290),
    ("c_r1_g3", 870, 160, 990, 290),
    ("c_r1_g4", 1050, 160, 1295, 290),

    # Clients row 2: y=285-380
    ("c_r2_g1_left", 320, 285, 530, 380),  # small "Actual" region
    ("c_r2_g2_main", 610, 285, 800, 380),  # ORTEFIL?
    ("c_r2_g3", 800, 285, 1100, 380),       # COLIZMA
    ("c_r2_g4", 1170, 285, 1395, 380),      # ZONAFRANCA

    # Clients row 3: y=390-480
    ("c_r3_full", 0, 390, 1440, 480),

    # Providers row 1: y=500-600
    ("p_r1_g1", 590, 500, 870, 600),
    ("p_r1_g2", 895, 500, 1015, 600),
    ("p_r1_g3", 1025, 500, 1155, 600),
    ("p_r1_g4", 1170, 500, 1270, 600),
    ("p_r1_g5", 1290, 500, 1410, 600),

    # Providers row 2: y=590-680
    ("p_r2_full", 0, 590, 1440, 680),

    # Providers row 3: y=660-770
    ("p_r3_full", 0, 660, 1440, 770),
]

for name, *rect in GROUPS:
    crop = crop_box(img, *rect)
    crop.save(OUT / f"{name}.png", "PNG")
print("Outputs:", OUT)
