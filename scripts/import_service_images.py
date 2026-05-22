# -*- coding: utf-8 -*-
"""Copia imágenes originales de la propuesta (sin quitar fondos)."""
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "dlci-web" / "public" / "dlci" / "services" / "_src"
OUT = ROOT / "dlci-web" / "public" / "dlci" / "services"
DESKTOP = Path(r"c:\Users\Josvier\Desktop")

# Orden según tarjetas en propuesta (p.10) + medición (pptx 3)
MAPPING = [
    ("diseno", SRC / "Copia_de_Pro_p10_4_1162x775.png"),
    ("gestion", SRC / "Copia_de_Pro_p10_5_1162x775.png"),
    ("baja", SRC / "Copia_de_Pro_p10_6_1161x775.png"),
    ("media", SRC / "Copia_de_Pro_p10_8_775x517.png"),
    ("supervision", SRC / "Copia_de_Pro_p10_9_775x517.png"),
    ("suministro", SRC / "Copia_de_Pro_p10_10_1162x775.png"),
]

MEDICION_SRC = SRC / "Copia_de_Pro_image2.jpeg"
PPTX_MEDICION = DESKTOP / "Copia de Propuesta diseño DLCI (3).pptx"


def extract_pptx_image(pptx: Path, index: int, dest: Path) -> bool:
    import io
    import zipfile

    with zipfile.ZipFile(pptx) as z:
        media = sorted(n for n in z.namelist() if n.startswith("ppt/media/image"))
        if index >= len(media):
            return False
        dest.write_bytes(z.read(media[index]))
        return True


def copy_file(src: Path, dest_stem: Path) -> Path:
    """Copia el archivo tal cual (sin quitar fondos ni recortar)."""
    dest_stem.parent.mkdir(parents=True, exist_ok=True)
    if not src.exists():
        raise FileNotFoundError(src)
    ext = src.suffix.lower()
    if ext in {".jpg", ".jpeg"}:
        out = dest_stem.with_suffix(".jpg")
    elif ext == ".png":
        out = dest_stem.with_suffix(".png")
    else:
        out = dest_stem.with_suffix(ext or ".bin")
    shutil.copy2(src, out)
    return out


def main() -> None:
    med_src = MEDICION_SRC
    if not med_src.exists() and PPTX_MEDICION.exists():
        tmp = OUT / "_tmp_medicion.jpeg"
        if extract_pptx_image(PPTX_MEDICION, 1, tmp):
            med_src = tmp

    all_items = list(MAPPING) + [("medicion-energia", med_src)]
    for slug, src in all_items:
        out = copy_file(src, OUT / slug)
        print("ok", out.name, "<-", src.name)


if __name__ == "__main__":
    main()
