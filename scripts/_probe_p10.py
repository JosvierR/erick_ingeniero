# -*- coding: utf-8 -*-
"""Lista todas las imágenes de page 10 con tamaño e índice."""
import fitz
from pathlib import Path

pdf = Path(r"c:\Users\Josvier\Desktop\Copia de Propuesta diseño DLCI.pdf")
doc = fitz.open(pdf)
page = doc[9]
for j, im in enumerate(page.get_images(full=True)):
    b = doc.extract_image(im[0])
    rects = page.get_image_rects(im[0])
    for rect in rects:
        print(f"#{j} {b['width']}x{b['height']} {b['ext']} rect=({rect.x0:.0f},{rect.y0:.0f},{rect.x1:.0f},{rect.y1:.0f})")
doc.close()
