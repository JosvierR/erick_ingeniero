# -*- coding: utf-8 -*-
"""Logos y fotos de servicios: fondo blanco, sin deformar."""
from pathlib import Path

try:
    from PIL import Image
except ImportError:
    raise SystemExit("pip install pillow") from None

ROOT = Path(__file__).resolve().parents[1]
INFO = ROOT / "dlci-web" / "public" / "dlci" / "info-extract"
PARTNERS = ROOT / "dlci-web" / "public" / "dlci" / "partners"
SERVICES = ROOT / "dlci-web" / "public" / "dlci" / "services"
PROPOSAL = ROOT / "dlci-web" / "public" / "dlci" / "proposal-extract"


def is_background(r: int, g: int, b: int, a: int, threshold: int = 32) -> bool:
    if a < 10:
        return True
    return r <= threshold and g <= threshold and b <= threshold


def strip_to_rgba(src: Image.Image, threshold: int = 32) -> Image.Image:
    img = src.convert("RGBA")
    px = img.load()
    for y in range(img.height):
        for x in range(img.width):
            r, g, b, a = px[x, y]
            if is_background(r, g, b, a, threshold):
                px[x, y] = (255, 255, 255, 0)
            else:
                px[x, y] = (r, g, b, 255)
    bbox = img.getbbox()
    return img.crop(bbox) if bbox else img


def fit_on_canvas(
    src: Image.Image,
    canvas_size: tuple[int, int],
    padding: int = 12,
    threshold: int = 32,
) -> Image.Image:
    cut = strip_to_rgba(src, threshold=threshold)
    cw, ch = canvas_size
    inner_w = cw - padding * 2
    inner_h = ch - padding * 2
    if cut.width < 1 or cut.height < 1:
        return Image.new("RGB", canvas_size, (255, 255, 255))

    scale = min(inner_w / cut.width, inner_h / cut.height, 1.0)
    nw = max(1, int(cut.width * scale))
    nh = max(1, int(cut.height * scale))
    resized = cut.resize((nw, nh), Image.Resampling.LANCZOS)

    canvas = Image.new("RGBA", canvas_size, (255, 255, 255, 255))
    x = (cw - nw) // 2
    y = (ch - nh) // 2
    canvas.paste(resized, (x, y), resized)
    return canvas.convert("RGB")


def save_logo(src: Path, dest: Path, crop: tuple[int, int, int, int] | None = None) -> None:
    dest.parent.mkdir(parents=True, exist_ok=True)
    img = Image.open(src)
    if crop:
        img = img.crop(crop)
    # Logos oscuros (Colizma, Ortefil): solo quitar negro puro
    name = dest.name.lower()
    th = 22 if "colizma" in name or "ortefil" in name else 32
    out = fit_on_canvas(img, (280, 112), padding=10, threshold=th)
    out.save(dest, "PNG", optimize=True)


def save_service_jpg(src: Path, dest: Path) -> None:
    dest.parent.mkdir(parents=True, exist_ok=True)
    out = fit_on_canvas(Image.open(src), (800, 500), padding=24, threshold=38)
    out.save(dest, "JPEG", quality=92, optimize=True)


def main() -> None:
    combined = INFO / "p1_1_384x135.png"
    if not combined.exists():
        print("missing info-extract; run PDF extract first")
        return

    w, h = Image.open(combined).size
    mid = w // 2

    logos = [
        ("clients/colon-genao.png", INFO / "p1_0_355x200.png", None),
        ("clients/infante-curiel.png", combined, (0, 0, mid - 4, h)),
        ("clients/jri-inversiones.png", combined, (mid + 4, 0, w, h)),
        ("clients/ortefil.png", INFO / "p1_2_303x114.png", None),
        ("clients/infante-pichardo.png", INFO / "p1_3_355x217.png", None),
        ("clients/colizma.png", INFO / "p1_4_366x221.png", None),
        ("clients/zona-franca.png", INFO / "p1_5_400x126.png", None),
        ("providers/ferreteria-8a.png", INFO / "p1_7_510x112.png", None),
        ("providers/ferreteria-bellon.png", INFO / "p1_8_909x254.png", None),
        ("providers/ilumeyco.png", INFO / "p1_9_199x79.png", None),
        ("providers/montan.png", INFO / "p1_10_300x300.png", None),
    ]

    for rel, src, crop in logos:
        if not src.exists():
            print("skip", rel)
            continue
        save_logo(src, PARTNERS / rel, crop)
        print("logo", rel)

    service_map = [
        ("diseno.jpg", "p10_4.png"),
        ("gestion.jpg", "p10_5.png"),
        ("baja.jpg", "p10_6.png"),
        ("media.jpg", "p10_7.png"),
        ("supervision.jpg", "p10_8.png"),
        ("suministro.jpg", "p10_9.png"),
    ]
    for dest_name, src_name in service_map:
        src = PROPOSAL / src_name
        if not src.exists():
            print("skip service", dest_name)
            continue
        save_service_jpg(src, SERVICES / dest_name)
        print("service", dest_name)


if __name__ == "__main__":
    main()
