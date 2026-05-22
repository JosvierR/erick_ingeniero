# -*- coding: utf-8 -*-
"""
Reimporta proyectos/servicios/logos renderizando las páginas del PDF y
recortando cada foto por su bbox real. Así obtenemos lo mismo que muestra
el PDF (con cielo y fondo natural), sin manipular pixeles.
"""
from __future__ import annotations

import io as io_module
import shutil
import zipfile
from io import BytesIO as io_BytesIO
from pathlib import Path

import fitz
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
DLCI = ROOT / "dlci-web" / "public" / "dlci"
DESKTOP = Path(r"c:\Users\Josvier\Desktop")

PROPOSAL_PDF = DESKTOP / "Copia de Propuesta diseño DLCI.pdf"
INFO_PDF = ROOT / "Información General DLCI Electricidad (1).pdf"
if not INFO_PDF.exists():
    INFO_PDF = DESKTOP / "Información General DLCI Electricidad (1).pdf"
PPTX_MEDICION = DESKTOP / "Copia de Propuesta diseño DLCI (3).pptx"

STAGING = DLCI / "_reimport_staging"
RENDER_DPI = 220


def render_page(doc: fitz.Document, page_no: int) -> tuple[Image.Image, float]:
    """Renderiza la página completa y devuelve la imagen + factor px/punto."""
    page = doc[page_no - 1]
    zoom = RENDER_DPI / 72.0
    pix = page.get_pixmap(matrix=fitz.Matrix(zoom, zoom), alpha=False)
    img = Image.frombytes("RGB", (pix.width, pix.height), pix.samples)
    return img, zoom


def get_image_rects(doc: fitz.Document, page_no: int, min_w: int = 80, min_h: int = 60) -> list[dict]:
    """Lista de imágenes con bbox real en puntos, filtradas por tamaño mínimo."""
    page = doc[page_no - 1]
    items = []
    for j, im in enumerate(page.get_images(full=True)):
        xref = im[0]
        info = doc.extract_image(xref)
        w, h = info["width"], info["height"]
        if w < min_w or h < min_h:
            continue
        rects = page.get_image_rects(xref)
        for rect in rects:
            items.append(
                {
                    "xref": xref,
                    "page_idx": j,
                    "rect": rect,
                    "w": w,
                    "h": h,
                }
            )
    return items


def crop_from_render(rendered: Image.Image, zoom: float, rect: fitz.Rect, padding_pt: float = 0) -> Image.Image:
    """Recorta del render usando el rect en puntos."""
    pad = padding_pt
    left = max(0, int((rect.x0 - pad) * zoom))
    top = max(0, int((rect.y0 - pad) * zoom))
    right = min(rendered.width, int((rect.x1 + pad) * zoom))
    bottom = min(rendered.height, int((rect.y1 + pad) * zoom))
    return rendered.crop((left, top, right, bottom))


def save_jpg(img: Image.Image, dest: Path, quality: int = 92) -> None:
    dest.parent.mkdir(parents=True, exist_ok=True)
    if img.mode != "RGB":
        img = img.convert("RGB")
    img.save(dest, "JPEG", quality=quality, optimize=True)


def save_png(img: Image.Image, dest: Path) -> None:
    dest.parent.mkdir(parents=True, exist_ok=True)
    img.save(dest, "PNG", optimize=True)


def crop_rect(doc: fitz.Document, page_no: int, rect: tuple[float, float, float, float], dest: Path) -> None:
    rendered, zoom = render_page(doc, page_no)
    img = crop_from_render(rendered, zoom, fitz.Rect(*rect))
    save_jpg(img, dest)
    print("crop", dest.name, rect)


def export_projects(doc: fitz.Document) -> None:
    """Layout verificado visualmente con bboxes exactos del PDF."""
    # Página 4: 6 fotos en grilla 3x2 (heurística automática)
    page = 4
    rendered, zoom = render_page(doc, page)
    items = get_image_rects(doc, page, min_w=400, min_h=300)
    items.sort(key=lambda x: (round(x["rect"].y0 / 20), x["rect"].x0))
    layout_p4 = [
        "residencial-sorrento",
        "torre-biventi-iii",
        "torre-soria",
        "residencial-dj",
        "torre-murcia",
        "torre-bonsai",
    ]
    for slug, item in zip(layout_p4, items[: len(layout_p4)]):
        img = crop_from_render(rendered, zoom, item["rect"])
        save_jpg(img, DLCI / "projects" / f"{slug}.jpg")
        print("project", slug, item["rect"])

    # Página 6: Aston (izq) / Ethan (der) — foto edificio completa bajo papel roto
    crop_rect(doc, 6, (44.5, 435.0, 363.5, 614.5), DLCI / "projects/torre-aston.jpg")
    crop_rect(doc, 6, (744.9, 435.0, 1064.5, 615.0), DLCI / "projects/residencial-ethan.jpg")

    # Página 7: Asturias bottom-left (vista aérea), Aitana bottom-right (vista aérea)
    crop_rect(doc, 7, (54.0, 577.0, 268.0, 776.0), DLCI / "projects/asturias-residences.jpg")
    crop_rect(doc, 7, (749.0, 598.0, 1021.0, 751.0), DLCI / "projects/residencial-aitana.jpg")

    # Página 8: Montpellier mid clean (169x191), Porto Bello mid clean (288x191)
    crop_rect(doc, 8, (53.0, 433.0, 222.0, 624.0), DLCI / "projects/torre-montpellier.jpg")
    crop_rect(doc, 8, (749.0, 433.0, 1037.0, 624.0), DLCI / "projects/porto-bello-tower.jpg")


def _png_on_white(b: dict) -> Image.Image:
    raw = Image.open(io_BytesIO(b["image"]))
    if raw.mode in ("RGBA", "LA"):
        bg = Image.new("RGB", raw.size, (255, 255, 255))
        bg.paste(raw, mask=raw.split()[-1])
        return bg
    if raw.mode == "P" and "transparency" in raw.info:
        raw = raw.convert("RGBA")
        bg = Image.new("RGB", raw.size, (255, 255, 255))
        bg.paste(raw, mask=raw.split()[-1])
        return bg
    rgb = raw.convert("RGB")
    data = rgb.load()
    w, h = rgb.size
    for y in range(h):
        for x in range(w):
            r, g, bl = data[x, y]
            if r < 8 and g < 8 and bl < 8:
                data[x, y] = (255, 255, 255)
    return rgb


def export_services(doc: fitz.Document) -> None:
    """Página 10: extrae PNG raw o recorta render según corresponda."""
    page = doc[9]
    images = page.get_images(full=True)

    raw_map = {
        "diseno": 10,
        "baja": 12,
        "media": 4,
        "supervision": 5,
    }
    for slug, idx in raw_map.items():
        xref = images[idx][0]
        b = doc.extract_image(xref)
        out = _png_on_white(b)
        save_jpg(out, DLCI / "services" / f"{slug}.jpg")
        print("service", slug, "raw idx", idx, b["width"], "x", b["height"])

    rendered, zoom = render_page(doc, 10)
    # Gestión: 4 logos + MIVED diagrama
    img = crop_from_render(rendered, zoom, fitz.Rect(485, 130, 950, 400))
    save_jpg(img, DLCI / "services" / "gestion.jpg")
    print("service gestion (page crop)")
    # Suministro: cables + transformador + generador (composición sin título)
    img = crop_from_render(rendered, zoom, fitz.Rect(1000, 525, 1440, 820))
    save_jpg(img, DLCI / "services" / "suministro.jpg")
    print("service suministro (page crop)")


def export_medicion() -> None:
    """Servicio nuevo: foto del analizador en pptx (3)."""
    if not PPTX_MEDICION.exists():
        print("skip medicion (pptx falta)")
        return
    with zipfile.ZipFile(PPTX_MEDICION) as z:
        media = [n for n in z.namelist() if n.startswith("ppt/media/image") and n.lower().endswith((".jpg", ".jpeg"))]
        if not media:
            print("skip medicion (sin jpeg)")
            return
        best = max(media, key=lambda n: z.getinfo(n).file_size)
        data = z.read(best)
    dest = DLCI / "services/medicion-energia.jpg"
    dest.write_bytes(data)
    print("service medicion-energia", dest.stat().st_size)


def export_logos(info_doc: fitz.Document) -> None:
    """Página 1 PDF Información General: índices fijos por imagen embebida."""
    rendered, zoom = render_page(info_doc, 1)
    page = info_doc[0]
    xref_by_index: dict[int, int] = {}
    for j, im in enumerate(page.get_images(full=True)):
        xref_by_index[j] = im[0]

    def rect_of(idx: int):
        rects = page.get_image_rects(xref_by_index[idx])
        if not rects:
            raise ValueError(f"sin rect para imagen {idx}")
        return max(rects, key=lambda r: (r.x1 - r.x0) * (r.y1 - r.y0))

    def save_crop(idx: int, rel: str, *, split: str | None = None, split_ratio: float = 0.5) -> None:
        rect = rect_of(idx)
        if split is None:
            crop = crop_from_render(rendered, zoom, rect)
            save_png(crop, DLCI / "partners" / f"{rel}.png")
        else:
            mid_x = rect.x0 + (rect.x1 - rect.x0) * split_ratio
            if split == "left":
                rect2 = fitz.Rect(rect.x0, rect.y0, mid_x - 2, rect.y1)
            else:
                rect2 = fitz.Rect(mid_x + 2, rect.y0, rect.x1, rect.y1)
            crop = crop_from_render(rendered, zoom, rect2)
            save_png(crop, DLCI / "partners" / f"{rel}.png")
        print("logo", rel)

    save_crop(0, "clients/colon-genao")
    save_crop(1, "clients/infante-curiel", split="left", split_ratio=0.6)
    save_crop(1, "clients/jri-inversiones", split="right", split_ratio=0.55)
    save_crop(2, "clients/ortefil")
    save_crop(3, "clients/infante-pichardo")
    save_crop(4, "clients/colizma")
    save_crop(5, "clients/zona-franca")
    save_crop(7, "providers/ferreteria-8a")
    save_crop(8, "providers/ferreteria-bellon")
    save_crop(9, "providers/ilumeyco")
    save_crop(10, "providers/montan")


def main() -> None:
    if not PROPOSAL_PDF.exists():
        raise SystemExit(f"No se encuentra {PROPOSAL_PDF}")
    STAGING.mkdir(parents=True, exist_ok=True)

    print("Proyectos…")
    with fitz.open(PROPOSAL_PDF) as doc:
        export_projects(doc)
        print("Servicios…")
        export_services(doc)

    export_medicion()

    if INFO_PDF.exists():
        print("Logos…")
        with fitz.open(INFO_PDF) as doc:
            export_logos(doc)
    else:
        print("AVISO: falta PDF Información General para logos")

    print("\nListo.")


if __name__ == "__main__":
    main()
