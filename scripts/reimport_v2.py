# -*- coding: utf-8 -*-
"""Re-importación V2 de assets DLCI siguiendo cambios solicitados por el cliente.

Fuente A: 'Copia de Propuesta diseño DLCI.pdf' (pp 5-8) -> composites "papel roto"
Fuente B: 'Copia de Propuesta diseño DLCI (1).pdf' (pp 12, 21-23) -> nuevos logos y servicios
Fuente C: 'Información General DLCI Electricidad (1).pdf' -> medicion-energia (sin cambios)

Salida: dlci-web/public/dlci/projects, services, partners.
"""
from pathlib import Path
import shutil
import zipfile
import fitz
from PIL import Image

# Paths
DESKTOP = Path(r"c:\Users\Josvier\Desktop")
OLD_PDF = DESKTOP / "Copia de Propuesta diseño DLCI.pdf"
NEW_PDF = DESKTOP / "Copia de Propuesta diseño DLCI (1).pdf"
INFO_PDF = Path(r"c:\Users\Josvier\Desktop\erick_ingeniero\Información General DLCI Electricidad (1).pdf")
PPTX_MEDICION = DESKTOP / "Copia de Propuesta diseño DLCI (3).pptx"

DLCI = Path(r"c:\Users\Josvier\Desktop\erick_ingeniero\dlci-web\public\dlci")
PROJ = DLCI / "projects"
SERV = DLCI / "services"
CLIENTS = DLCI / "partners" / "clients"
PROVIDERS = DLCI / "partners" / "providers"

RENDER_DPI = 3.0  # ~216 DPI


def render_page(pdf: Path, page_idx_1: int, dpi: float = RENDER_DPI) -> tuple[Image.Image, float]:
    doc = fitz.open(pdf)
    page = doc[page_idx_1 - 1]
    pix = page.get_pixmap(matrix=fitz.Matrix(dpi, dpi), alpha=False)
    img = Image.frombytes("RGB", (pix.width, pix.height), pix.samples).copy()
    doc.close()
    return img, dpi


def crop_box(img: Image.Image, dpi: float, x0: float, y0: float, x1: float, y1: float) -> Image.Image:
    return img.crop((int(x0 * dpi), int(y0 * dpi), int(x1 * dpi), int(y1 * dpi)))


def save_jpg(img: Image.Image, path: Path, quality: int = 92) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if img.mode != "RGB":
        bg = Image.new("RGB", img.size, (255, 255, 255))
        if img.mode in ("RGBA", "LA"):
            bg.paste(img, mask=img.split()[-1])
        else:
            bg.paste(img.convert("RGBA"), mask=img.convert("RGBA").split()[-1])
        img = bg
    img.save(path, "JPEG", quality=quality, optimize=True)
    print("jpg", path.relative_to(DLCI))


def save_png(img: Image.Image, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    img.save(path, "PNG", optimize=True)
    print("png", path.relative_to(DLCI))


def clear_dir(d: Path) -> None:
    if d.exists():
        for child in d.iterdir():
            if child.is_file():
                child.unlink()


def export_projects() -> None:
    """Composites 'papel roto' desde NEW PDF pp 15-18 (col 'Nueva').
    Coordenadas determinadas por auto-detección de regiones no-blancas."""
    print("== Proyectos ==")
    clear_dir(PROJ)

    # p15: Aston (top), Ethan (bottom)
    img15, dpi = render_page(NEW_PDF, 15)
    save_jpg(crop_box(img15, dpi, 955, 255, 1350, 465), PROJ / "torre-aston.jpg")
    save_jpg(crop_box(img15, dpi, 955, 495, 1350, 695), PROJ / "residencial-ethan.jpg")

    # p16: Soria, Biventi 3, Murcia (top → bottom)
    img16, dpi = render_page(NEW_PDF, 16)
    save_jpg(crop_box(img16, dpi, 951, 100, 1380, 280), PROJ / "torre-soria.jpg")
    save_jpg(crop_box(img16, dpi, 951, 340, 1380, 535), PROJ / "torre-biventi-iii.jpg")
    save_jpg(crop_box(img16, dpi, 951, 580, 1380, 800), PROJ / "torre-murcia.jpg")

    # p17: Sorrento, Bonsai, DJ (top → bottom)
    img17, dpi = render_page(NEW_PDF, 17)
    save_jpg(crop_box(img17, dpi, 951, 100, 1380, 340), PROJ / "residencial-sorrento.jpg")
    save_jpg(crop_box(img17, dpi, 951, 340, 1380, 555), PROJ / "torre-bonsai.jpg")
    save_jpg(crop_box(img17, dpi, 951, 580, 1380, 795), PROJ / "residencial-dj.jpg")

    # p18: 2x2 grid: Asturias | Aitana, Montpellier | Porto Bello
    img18, dpi = render_page(NEW_PDF, 18)
    save_jpg(crop_box(img18, dpi, 708, 205, 980, 470), PROJ / "asturias-residences.jpg")
    save_jpg(crop_box(img18, dpi, 1008, 205, 1281, 470), PROJ / "residencial-aitana.jpg")
    save_jpg(crop_box(img18, dpi, 708, 535, 980, 800), PROJ / "torre-montpellier.jpg")
    save_jpg(crop_box(img18, dpi, 1008, 535, 1281, 800), PROJ / "porto-bello-tower.jpg")


def export_services() -> None:
    """Nuevas imágenes de servicios desde NEW PDF pp 21-23 + medicion (PPTX/PDF)."""
    print("== Servicios ==")
    clear_dir(SERV)

    # p21: diseño electrico (top), gestión y aprobación (bottom)
    img21, dpi = render_page(NEW_PDF, 21)
    save_jpg(crop_box(img21, dpi, 840, 140, 1291, 470), SERV / "diseno.jpg")
    save_jpg(crop_box(img21, dpi, 840, 532, 1291, 775), SERV / "gestion.jpg")

    # p22: ejecución baja tensión (top), proyectos media tensión (bottom)
    img22, dpi = render_page(NEW_PDF, 22)
    save_jpg(crop_box(img22, dpi, 861, 145, 1276, 380), SERV / "baja.jpg")
    save_jpg(crop_box(img22, dpi, 861, 560, 1276, 770), SERV / "media.jpg")

    # p23: supervisión y dirección (top), suministro e instalación (bottom)
    img23, dpi = render_page(NEW_PDF, 23)
    save_jpg(crop_box(img23, dpi, 896, 145, 1258, 395), SERV / "supervision.jpg")
    save_jpg(crop_box(img23, dpi, 896, 540, 1258, 730), SERV / "suministro.jpg")

    # Medicion: panel eléctrico desde PPTX (3) (foto del analizador)
    if PPTX_MEDICION.exists():
        with zipfile.ZipFile(PPTX_MEDICION) as z:
            media = [n for n in z.namelist() if n.startswith("ppt/media/image") and n.lower().endswith((".jpg", ".jpeg"))]
            if media:
                best = max(media, key=lambda n: z.getinfo(n).file_size)
                data = z.read(best)
                dest = SERV / "medicion-energia.jpg"
                dest.write_bytes(data)
                print("jpg services/medicion-energia.jpg", dest.stat().st_size)


def export_logos() -> None:
    """Logos clientes y proveedores desde NEW PDF p12 (imágenes optimizadas)."""
    print("== Logos ==")
    clear_dir(CLIENTS)
    clear_dir(PROVIDERS)

    img12, dpi = render_page(NEW_PDF, 12)

    # Clientes (10) — coordenadas verificadas visualmente desde NEW_PDF p12
    clients_specs = [
        ("colon-genao.png",       630, 160,  830, 290),
        ("infante-curiel.png",    840, 160, 1030, 290),
        ("jri-inversiones.png",  1045, 160, 1195, 290),
        ("infante-pichardo.png", 1195, 160, 1400, 290),
        ("ortefil.png",           600, 285,  935, 385),
        ("colizma.png",           940, 285, 1140, 385),
        ("zonafranca.png",       1155, 285, 1410, 390),
        ("murcia-group.png",      600, 395,  870, 480),
        ("pak-label.png",         870, 395, 1115, 480),
        ("plusval.png",          1115, 390, 1320, 480),
    ]
    for name, *rect in clients_specs:
        save_png(crop_box(img12, dpi, *rect), CLIENTS / name)

    # Proveedores y Marcas Aliadas (11) — coordenadas verificadas
    providers_specs = [
        ("ochoa-8a.png",   585, 500,  870, 600),
        ("maelec.png",     880, 500, 1015, 675),
        ("montan.png",    1020, 500, 1155, 665),
        ("master.png",    1165, 495, 1420, 590),
        ("bellon.png",     595, 600,  870, 680),
        ("abb.png",       1190, 590, 1380, 685),
        ("ilumeyco.png",   600, 680,  855, 775),
        ("daco.png",       865, 690, 1015, 760),
        ("legrand.png",   1010, 680, 1210, 723),
        ("bticino.png",   1010, 735, 1210, 775),
        ("leviton.png",   1210, 680, 1395, 775),
    ]
    for name, *rect in providers_specs:
        save_png(crop_box(img12, dpi, *rect), PROVIDERS / name)


def main() -> None:
    export_projects()
    export_services()
    export_logos()
    print("Listo")


if __name__ == "__main__":
    main()
