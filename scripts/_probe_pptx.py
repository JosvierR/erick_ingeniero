# -*- coding: utf-8 -*-
import zipfile
from pathlib import Path

for name in [
    "Información General DLCI Electricidad.pptx",
    "Copia de Propuesta diseño DLCI (3).pptx",
    "Diseño DLCI.pptx",
]:
    p = Path(r"c:\Users\Josvier\Desktop") / name
    if not p.exists():
        print("missing", name)
        continue
    with zipfile.ZipFile(p) as z:
        media = sorted(n for n in z.namelist() if n.startswith("ppt/media/"))
    print(name, "->", len(media), "files")
    for m in media:
        data = z.read(m)
        print(" ", m, len(data))
