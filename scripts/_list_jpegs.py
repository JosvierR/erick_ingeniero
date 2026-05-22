# -*- coding: utf-8 -*-
import fitz
from pathlib import Path

pdf = Path(r"c:\Users\Josvier\Desktop\Copia de Propuesta diseño DLCI.pdf")
doc = fitz.open(pdf)
items = []
for p in range(len(doc)):
    for j, im in enumerate(doc[p].get_images(full=True)):
        b = doc.extract_image(im[0])
        if b["ext"] in ("jpeg", "jpg"):
            items.append((p + 1, j, b["width"], b["height"], len(b["image"])))
items.sort(key=lambda x: -x[4])
for it in items:
    print(f"p{it[0]} #{it[1]} {it[2]}x{it[3]} {it[4]//1024}KB")
doc.close()
