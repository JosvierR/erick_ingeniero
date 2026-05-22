# -*- coding: utf-8 -*-
"""List embedded images on p12 of NEW PDF to find logo bboxes."""
from pathlib import Path
import fitz

NEW_PDF = Path(r"c:\Users\Josvier\Desktop\Copia de Propuesta diseño DLCI (1).pdf")

doc = fitz.open(NEW_PDF)
page = doc[11]
print(f"Page size: {page.rect}")
print(f"Image list: {len(page.get_images(full=True))}")

# Method 1: get image rects
for img_info in page.get_images(full=True):
    xref = img_info[0]
    rects = page.get_image_rects(xref)
    for rect in rects:
        w = rect.x1 - rect.x0
        h = rect.y1 - rect.y0
        print(f"  xref={xref}  rect=({rect.x0:.0f},{rect.y0:.0f},{rect.x1:.0f},{rect.y1:.0f})  size={w:.0f}x{h:.0f}")

# Method 2: get all drawings/images via blocks
print("\n--- get_text dict blocks ---")
blocks = page.get_text("dict")["blocks"]
for b in blocks:
    if b["type"] == 1:  # image block
        bbox = b["bbox"]
        print(f"  image bbox=({bbox[0]:.0f},{bbox[1]:.0f},{bbox[2]:.0f},{bbox[3]:.0f})  size={bbox[2]-bbox[0]:.0f}x{bbox[3]-bbox[1]:.0f}")
doc.close()
