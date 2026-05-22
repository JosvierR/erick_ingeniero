# -*- coding: utf-8 -*-
"""Recorta el fondo del hero para la tarjeta derecha (misma foto, sin bordes negros)."""
from pathlib import Path

try:
    from PIL import Image, ImageEnhance
except ImportError:
    raise SystemExit("pip install pillow") from None

ROOT = Path(__file__).resolve().parents[1]
DLCI = ROOT / "dlci-web" / "public" / "dlci"


def grade(img: Image.Image) -> Image.Image:
    """Misma sensación que el CSS del hero (saturación / brillo)."""
    img = ImageEnhance.Color(img).enhance(0.85)
    return ImageEnhance.Brightness(img).enhance(0.62)


def main() -> None:
    bg_path = DLCI / "hero-bg.jpg"
    if not bg_path.exists():
        print("missing", bg_path)
        return

    bg = Image.open(bg_path).convert("RGB")
    w, h = bg.size
    # Panel derecho del collage (obra / edificio) — encaja con el fondo
    crop = bg.crop((int(w * 0.38), 0, w, h))
    target = (1200, 900)
    crop = crop.resize(target, Image.Resampling.LANCZOS)
    graded = grade(crop)
    graded.save(DLCI / "hero-card.jpg", "JPEG", quality=92, optimize=True)
    graded.save(DLCI / "hero-project.jpg", "JPEG", quality=92, optimize=True)
    print("ok hero-card.jpg + hero-project.jpg")


if __name__ == "__main__":
    main()
