# -*- coding: utf-8 -*-
"""Render multiple pages of the NEW PDF as thumbnails to locate the clean photo grid."""
from pathlib import Path
import fitz
from PIL import Image

NEW_PDF = Path(r"c:\Users\Josvier\Desktop\Copia de Propuesta diseño DLCI (1).pdf")
OUT = Path(r"c:\Users\Josvier\Desktop\erick_ingeniero\dlci-web\public\dlci\_p13_probe")
OUT.mkdir(parents=True, exist_ok=True)

doc = fitz.open(NEW_PDF)
print(f"Pages: {doc.page_count}")
for p in range(doc.page_count):
    page = doc[p]
    pix = page.get_pixmap(matrix=fitz.Matrix(1.2, 1.2), alpha=False)
    img = Image.frombytes("RGB", (pix.width, pix.height), pix.samples)
    img.save(OUT / f"thumb_p{p + 1:02d}.png")
print("done")
doc.close()
