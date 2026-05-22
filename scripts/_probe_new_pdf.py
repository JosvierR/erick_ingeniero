# -*- coding: utf-8 -*-
"""Compare new proposal PDF vs current one (page count, images per page)."""
from pathlib import Path
import fitz

NEW = Path(r"c:\Users\Josvier\Desktop\Copia de Propuesta diseño DLCI (1).pdf")
OLD = Path(r"c:\Users\Josvier\Desktop\Copia de Propuesta diseño DLCI.pdf")

for label, path in [("NEW", NEW), ("OLD", OLD)]:
    print("=" * 70)
    print(label, path.name, f"{path.stat().st_size/1024/1024:.1f} MB")
    doc = fitz.open(path)
    print(f"  pages: {len(doc)}")
    for i, page in enumerate(doc, start=1):
        imgs = page.get_images(full=True)
        text = page.get_text("text").strip().replace("\n", " | ")[:120]
        print(f"  p{i:2d}  imgs={len(imgs):2d}  text: {text}")
    doc.close()
