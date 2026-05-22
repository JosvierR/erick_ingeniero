# -*- coding: utf-8 -*-
"""Test specific crops on p18 to find exact coords for the 4 project images."""
from pathlib import Path
import fitz
from PIL import Image, ImageDraw, ImageFont

PDF = Path(r"c:\Users\Josvier\Desktop\Copia de Propuesta diseño DLCI (1).pdf")
OUT = Path(r"c:\Users\Josvier\Desktop\erick_ingeniero\dlci-web\public\dlci\_reimport_staging\test_crops")
OUT.mkdir(parents=True, exist_ok=True)

dpi = 3.0
doc = fitz.open(PDF)
page = doc[17]  # p18
pix = page.get_pixmap(matrix=fitz.Matrix(dpi, dpi), alpha=False)
img = Image.frombytes("RGB", (pix.width, pix.height), pix.samples).copy()
print(f"page render: {pix.width}x{pix.height}")
doc.close()

# Save full p18 at 2x DPI for visual reference
img.save(OUT / "p18_full.png")

# Try several candidate crops for the 4 images
candidates = {
    "asturias_v1": (605, 175, 795, 435),
    "asturias_v2": (600, 180, 795, 440),
    "asturias_v3": (615, 190, 810, 440),
    "aitana_v1": (810, 175, 1010, 435),
    "aitana_v2": (820, 190, 1005, 440),
    "montpellier_v1": (590, 525, 795, 795),
    "montpellier_v2": (605, 535, 800, 790),
    "porto_v1": (805, 525, 1005, 795),
    "porto_v2": (820, 535, 1010, 790),
}
for name, (x0, y0, x1, y1) in candidates.items():
    crop = img.crop((int(x0 * dpi), int(y0 * dpi), int(x1 * dpi), int(y1 * dpi)))
    crop.save(OUT / f"crop_{name}.png")
    print(name, x0, y0, x1, y1, "->", crop.size)
