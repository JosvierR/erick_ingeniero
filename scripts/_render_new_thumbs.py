# -*- coding: utf-8 -*-
"""Render thumbnails of every page in the new PDF for visual inspection."""
from pathlib import Path
import fitz

PDF = Path(r"c:\Users\Josvier\Desktop\Copia de Propuesta diseño DLCI (1).pdf")
OUT = Path(r"c:\Users\Josvier\Desktop\erick_ingeniero\dlci-web\public\dlci\_reimport_staging\new_proposal")
OUT.mkdir(parents=True, exist_ok=True)

doc = fitz.open(PDF)
for i, page in enumerate(doc, start=1):
    pix = page.get_pixmap(matrix=fitz.Matrix(1.0, 1.0))
    pix.save(OUT / f"p{i:02d}.png")
    print(f"p{i:02d} {pix.width}x{pix.height}")
doc.close()
print("done")
