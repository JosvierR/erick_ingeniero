# -*- coding: utf-8 -*-
"""Renderiza páginas del PDF para inspección visual."""
import fitz
from pathlib import Path

pdf = Path(r"c:\Users\Josvier\Desktop\Copia de Propuesta diseño DLCI.pdf")
out = Path(r"c:\Users\Josvier\Desktop\erick_ingeniero\dlci-web\public\dlci\_reimport_staging\pages")
out.mkdir(parents=True, exist_ok=True)
doc = fitz.open(pdf)
for p in range(3, 14):
    page = doc[p]
    pix = page.get_pixmap(matrix=fitz.Matrix(1.5, 1.5))
    pix.save(out / f"page{p + 1}.png")
    print("page", p + 1, "->", out / f"page{p + 1}.png")
doc.close()
