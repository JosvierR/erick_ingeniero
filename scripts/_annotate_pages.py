# -*- coding: utf-8 -*-
"""Renderiza página con cuadrícula de coordenadas para identificar bboxes visualmente."""
import fitz
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

pdf = Path(r"c:\Users\Josvier\Desktop\Copia de Propuesta diseño DLCI.pdf")
out = Path(r"c:\Users\Josvier\Desktop\erick_ingeniero\dlci-web\public\dlci\_reimport_staging\annotated")
out.mkdir(parents=True, exist_ok=True)
doc = fitz.open(pdf)
zoom = 1.5
for p in [4, 7, 8, 10]:
    page = doc[p - 1]
    pix = page.get_pixmap(matrix=fitz.Matrix(zoom, zoom), alpha=False)
    img = Image.frombytes("RGB", (pix.width, pix.height), pix.samples).convert("RGBA")
    overlay = Image.new("RGBA", img.size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)

    # Cuadrícula cada 100 puntos
    for x in range(0, int(page.rect.width) + 1, 100):
        px = int(x * zoom)
        draw.line([(px, 0), (px, img.height)], fill=(255, 0, 0, 90), width=1)
        draw.text((px + 2, 4), str(x), fill=(255, 0, 0, 200))
    for y in range(0, int(page.rect.height) + 1, 100):
        py = int(y * zoom)
        draw.line([(0, py), (img.width, py)], fill=(0, 0, 255, 90), width=1)
        draw.text((4, py + 2), str(y), fill=(0, 0, 255, 200))
    img = Image.alpha_composite(img, overlay).convert("RGB")
    img.save(out / f"page{p}_grid.png")
    print("page", p, "->", out / f"page{p}_grid.png")
doc.close()
