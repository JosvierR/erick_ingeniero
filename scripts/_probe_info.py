# -*- coding: utf-8 -*-
import fitz
from pathlib import Path

for pdf in [
    Path(r"c:\Users\Josvier\Desktop\erick_ingeniero\Información General DLCI Electricidad (1).pdf"),
    Path(r"c:\Users\Josvier\Desktop\Información General DLCI Electricidad (1).pdf"),
]:
    if not pdf.exists():
        continue
    doc = fitz.open(pdf)
    page = doc[0]
    for j, im in enumerate(page.get_images(full=True)):
        b = doc.extract_image(im[0])
        print(j, b["width"], b["height"], b["ext"], len(b["image"]))
    doc.close()
