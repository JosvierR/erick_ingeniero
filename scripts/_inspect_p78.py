# -*- coding: utf-8 -*-
import fitz
from pathlib import Path

pdf = Path(r"c:\Users\Josvier\Desktop\Copia de Propuesta diseño DLCI.pdf")
doc = fitz.open(pdf)
for p in [7, 8]:
    page = doc[p - 1]
    print(f"\n=== Page {p} ===")
    for j, im in enumerate(page.get_images(full=True)):
        xref = im[0]
        info = doc.extract_image(xref)
        for rect in page.get_image_rects(xref):
            w = rect.x1 - rect.x0
            h = rect.y1 - rect.y0
            aspect = w / max(h, 1)
            print(f"  #{j} {info['width']}x{info['height']} {info['ext']:5s} | rect=({rect.x0:.0f},{rect.y0:.0f},{rect.x1:.0f},{rect.y1:.0f}) | {w:.0f}x{h:.0f} aspect={aspect:.2f}")
doc.close()
