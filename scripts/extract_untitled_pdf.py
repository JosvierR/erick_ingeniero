# -*- coding: utf-8 -*-
"""Extract 6 composite project images from Untitled design.pdf (pp 1-2, col 'Nueva')."""
from pathlib import Path
import fitz
from PIL import Image

PDF = Path(r"c:\Users\Josvier\Desktop\Untitled design.pdf")
PROJ = Path(r"c:\Users\Josvier\Desktop\erick_ingeniero\dlci-web\public\dlci\projects")
PROBE = Path(r"c:\Users\Josvier\Desktop\erick_ingeniero\dlci-web\public\dlci\_untitled_probe")
PROBE.mkdir(parents=True, exist_ok=True)

DPI = 3.0

# Right column — solo el collage "Nueva" (sin etiquetas de texto).
RIGHT_X = (870, 1395)
PAGE1 = [
    ("torre-soria.jpg", 95, 262),
    ("torre-biventi-iii.jpg", 340, 505),
    ("residencial-sorrento.jpg", 580, 795),
]
PAGE2 = [
    ("torre-bonsai.jpg", 95, 262),
    ("torre-murcia.jpg", 340, 505),
    ("residencial-dj.jpg", 580, 795),
]


def render(pdf: Path, page_1based: int) -> tuple[Image.Image, float]:
    doc = fitz.open(pdf)
    page = doc[page_1based - 1]
    pix = page.get_pixmap(matrix=fitz.Matrix(DPI, DPI), alpha=False)
    img = Image.frombytes("RGB", (pix.width, pix.height), pix.samples).copy()
    doc.close()
    return img, DPI


def crop(img: Image.Image, dpi: float, x0: float, y0: float, x1: float, y1: float) -> Image.Image:
    return img.crop((int(x0 * dpi), int(y0 * dpi), int(x1 * dpi), int(y1 * dpi)))


def save_jpg(img: Image.Image, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if img.mode != "RGB":
        img = img.convert("RGB")
    img.save(path, "JPEG", quality=92, optimize=True)
    print("jpg", path.name, img.size)


def main() -> None:
    img1, dpi = render(PDF, 1)
    img2, dpi = render(PDF, 2)
    x0, x1 = RIGHT_X

    for name, y0, y1 in PAGE1:
        crop_img = crop(img1, dpi, x0, y0, x1, y1)
        save_jpg(crop_img, PROJ / name)
        crop_img.save(PROBE / f"p1_{name.replace('.jpg', '')}.jpg", "JPEG", quality=90)

    for name, y0, y1 in PAGE2:
        crop_img = crop(img2, dpi, x0, y0, x1, y1)
        save_jpg(crop_img, PROJ / name)
        crop_img.save(PROBE / f"p2_{name.replace('.jpg', '')}.jpg", "JPEG", quality=90)

    print("Listo")


if __name__ == "__main__":
    main()
