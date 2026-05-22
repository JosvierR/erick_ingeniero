# -*- coding: utf-8 -*-
import fitz
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
for label, pdf in [
    ("propuesta", Path(r"c:\Users\Josvier\Desktop\Copia de Propuesta diseño DLCI.pdf")),
    ("info", ROOT / "Información General DLCI Electricidad (1).pdf"),
]:
    if not pdf.exists():
        print("missing", label)
        continue
    doc = fitz.open(pdf)
    print(f"\n=== {label} ({len(doc)} pages) ===")
    for p in [3, 4, 5, 6, 7, 8, 9, 10, 11, 12]:
        if p >= len(doc):
            continue
        imgs = []
        for j, im in enumerate(doc[p].get_images(full=True)):
            b = doc.extract_image(im[0])
            imgs.append((j, b["width"], b["height"], b["ext"], len(b["image"])))
        imgs.sort(key=lambda x: -x[4])
        line = ", ".join(f"#{i} {w}x{h}{e} {sz//1024}k" for i, w, h, e, sz in imgs[:6])
        print(f"  p{p+1}: {line}")
    doc.close()
