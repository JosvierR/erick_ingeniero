# -*- coding: utf-8 -*-
import fitz
from pathlib import Path

PDF = Path(r"c:\Users\Josvier\Desktop\Copia de Propuesta diseño DLCI.pdf")
doc = fitz.open(PDF)
for pn in (5, 6):
    print(f"=== p{pn} ===")
    page = doc[pn - 1]
    for j, im in enumerate(page.get_images(full=True)):
        b = doc.extract_image(im[0])
        rects = page.get_image_rects(im[0])
        for rect in rects:
            w = b["width"]
            h = b["height"]
            ext = b["ext"]
            print(f"#{j:2d}  {w:4d}x{h:4d}  {ext:5s}  rect=({rect.x0:.0f},{rect.y0:.0f},{rect.x1:.0f},{rect.y1:.0f})")
doc.close()
