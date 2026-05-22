# -*- coding: utf-8 -*-
import fitz
from pathlib import Path

pdf = Path(r"c:\Users\Josvier\Desktop\Copia de Propuesta diseño DLCI.pdf")
doc = fitz.open(pdf)
for p in range(3, 14):
    page = doc[p]
    imgs = []
    for j, im in enumerate(page.get_images(full=True)):
        b = doc.extract_image(im[0])
        area = b["width"] * b["height"]
        imgs.append((j, b["width"], b["height"], b["ext"], area))
    imgs.sort(key=lambda x: -x[4])
    top = ", ".join(f"#{x[0]} {x[1]}x{x[2]} {x[3]}" for x in imgs[:4])
    print(f"page {p + 1}: {top}")
doc.close()
