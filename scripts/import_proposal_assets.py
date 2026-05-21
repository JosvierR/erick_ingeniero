# -*- coding: utf-8 -*-
"""Copia imágenes de la propuesta PDF a public/dlci."""
from pathlib import Path

try:
    from PIL import Image
except ImportError:
    raise SystemExit("pip install pillow") from None

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "dlci-web" / "public" / "dlci" / "proposal-extract"
DST = ROOT / "dlci-web" / "public" / "dlci"


def save_jpg(src: Path, dest: Path, quality: int = 88) -> None:
    dest.parent.mkdir(parents=True, exist_ok=True)
    img = Image.open(src)
    if img.mode in ("RGBA", "P"):
        img = img.convert("RGB")
    img.save(dest, "JPEG", quality=quality, optimize=True)


def main() -> None:
    projects = [
        ("p4_0.png", "projects/torre-soria.jpg"),
        ("p4_4.png", "projects/torre-biventi-iii.jpg"),
        ("p4_3.png", "projects/residencial-sorrento.jpg"),
        ("p4_1.png", "projects/torre-bonsai.jpg"),
        ("p4_5.png", "projects/torre-murcia.jpg"),
        ("p4_2.png", "projects/residencial-dj.jpg"),
        ("p6_0.png", "projects/torre-aston.jpg"),
        ("p6_1.png", "projects/residencial-ethan.jpg"),
        ("p7_8.png", "projects/asturias-residences.jpg"),
        ("p7_2.png", "projects/residencial-aitana.jpg"),
        ("p8_0.png", "projects/torre-montpellier.jpg"),
        ("p8_7.png", "projects/porto-bello-tower.jpg"),
    ]
    services = [
        ("p10_4.png", "services/diseno.jpg"),
        ("p10_5.png", "services/gestion.jpg"),
        ("p10_6.png", "services/baja.jpg"),
        ("p10_7.png", "services/media.jpg"),
        ("p10_8.png", "services/supervision.jpg"),
        ("p10_9.png", "services/suministro.jpg"),
    ]

    for name, rel in projects + services:
        src = SRC / name
        if not src.exists():
            print("skip missing", name)
            continue
        save_jpg(src, DST / rel)
        print("ok", rel)


if __name__ == "__main__":
    main()
