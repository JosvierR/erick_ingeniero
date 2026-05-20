# -*- coding: utf-8 -*-
import fitz
import os
import json
import glob

pdfs = glob.glob("*.pdf")
os.makedirs("extracted", exist_ok=True)
info = []
for pdf in pdfs:
    doc = fitz.open(pdf)
    for i in range(min(len(doc), 25)):
        page = doc[i]
        for j, img in enumerate(page.get_images(full=True)):
            xref = img[0]
            base = doc.extract_image(xref)
            ext = base["ext"]
            w, h = base["width"], base["height"]
            if w < 100 or h < 100:
                continue
            safe = pdf.replace(".pdf", "").replace(" ", "_")[:25]
            name = f"{safe}_p{i+1}_img{j}.{ext}"
            path = os.path.join("extracted", name)
            with open(path, "wb") as f:
                f.write(base["image"])
            info.append({"file": name, "w": w, "h": h, "page": i + 1, "pdf": pdf})
    doc.close()
print(json.dumps(info, indent=2))
print("total", len(info))
