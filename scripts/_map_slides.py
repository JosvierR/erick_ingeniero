# -*- coding: utf-8 -*-
"""Mapea cada slide del PPTX con su título y las imágenes que usa."""
from __future__ import annotations

import re
import zipfile
import xml.etree.ElementTree as ET
from pathlib import Path

NS = {
    "a": "http://schemas.openxmlformats.org/drawingml/2006/main",
    "r": "http://schemas.openxmlformats.org/officeDocument/2006/relationships",
    "p": "http://schemas.openxmlformats.org/presentationml/2006/main",
}


def parse_pptx(path: Path) -> None:
    print("\n========", path.name)
    with zipfile.ZipFile(path) as z:
        slides = sorted(n for n in z.namelist() if re.match(r"ppt/slides/slide\d+\.xml$", n))
        for slide in slides:
            slide_num = re.search(r"slide(\d+)", slide).group(1)
            xml = ET.fromstring(z.read(slide))
            texts = [t.text for t in xml.iter("{%s}t" % NS["a"]) if t.text]
            title = " | ".join(s.strip() for s in texts if s.strip())[:140]
            rels_name = slide.replace("slides/slide", "slides/_rels/slide") + ".rels"
            images = []
            if rels_name in z.namelist():
                rels = ET.fromstring(z.read(rels_name))
                for rel in rels:
                    tgt = rel.attrib.get("Target", "")
                    if "media/" in tgt:
                        images.append(Path(tgt).name)
            print(f"  slide{slide_num}: {images}")
            print(f"           {title}")


for name in [
    "Información General DLCI Electricidad.pptx",
    "Copia de Propuesta diseño DLCI.pdf",
    "Copia de Propuesta diseño DLCI (3).pptx",
    "Diseño DLCI.pptx",
]:
    p = Path(r"c:\Users\Josvier\Desktop") / name
    if p.exists() and p.suffix == ".pptx":
        parse_pptx(p)
