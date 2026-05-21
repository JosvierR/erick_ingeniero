# -*- coding: utf-8 -*-
import os
import shutil

src = "extracted"
dst = "dlci-web/public/dlci"
os.makedirs(f"{dst}/projects", exist_ok=True)

def copy_if_exists(src_name, dest_name):
    s = os.path.join(src, src_name)
    if os.path.exists(s):
        shutil.copy2(s, os.path.join(dst, dest_name))
        return True
    return False

# Logo from info PDF page 1
copy_if_exists("Informaci\u00f3n_General_DLCI__p1_img0.png", "logo-original.png")

# Hero from portafolio
for name in [
    "Portafolio_DLCI_Electrici_p2_img1.jpeg",
    "Portafolio_DLCI_Electrici_p10_img1.jpeg",
    "Informaci\u00f3n_General_DLCI__p13_img0.jpeg",
]:
    if copy_if_exists(name, "hero-project.jpg"):
        break

# Project images from portafolio pages 4-9 (first large jpeg each page)
# Orden portafolio (páginas 4–9) según propuesta de diseño
project_sources = [
    ("Portafolio_DLCI_Electrici_p5_img0.jpeg", "torre-soria.jpg"),
    ("Portafolio_DLCI_Electrici_p4_img0.jpeg", "torre-biventi-iii.jpg"),
    ("Portafolio_DLCI_Electrici_p7_img0.jpeg", "residencial-sorrento.jpg"),
    ("Portafolio_DLCI_Electrici_p8_img0.jpeg", "torre-bonsai.jpg"),
    ("Portafolio_DLCI_Electrici_p9_img0.jpeg", "torre-murcia.jpg"),
    ("Portafolio_DLCI_Electrici_p6_img0.jpeg", "residencial-dj.jpg"),
]
for src_name, dest_name in project_sources:
    copy_if_exists(src_name, f"projects/{dest_name}")

# Logo transparente + versión clara para navbar oscuro
try:
    from PIL import Image
    src_logo = os.path.join(dst, "logo-original.png")
    if os.path.exists(src_logo):
        img = Image.open(src_logo).convert("RGBA")
        px = img.load()
        w, h = img.size
        for y in range(h):
            for x in range(w):
                r, g, b, a = px[x, y]
                if r < 45 and g < 45 and b < 55:
                    px[x, y] = (0, 0, 0, 0)
        img.save(os.path.join(dst, "logo-transparent.png"))
        light = img.copy()
        px2 = light.load()
        for y in range(h):
            for x in range(w):
                r, g, b, a = px2[x, y]
                if a > 0:
                    px2[x, y] = (255, 255, 255, a)
        light.save(os.path.join(dst, "logo-light.png"))
except ImportError:
    pass

print("Assets copied to", dst)
for root, _, files in os.walk(dst):
    for f in files:
        print(os.path.join(root, f))
