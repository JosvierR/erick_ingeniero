# -*- coding: utf-8 -*-
"""Extract 6 clean building photos from the user-provided 3x2 grid image.

Source grid layout (1024x500 approx):
  Row 1: SORRENTO | BIVENTI 3 | SORIA   (title ~y=30; photo ~y=50-260)
  Row 2: DJ       | MURCIA    | BONSAI  (title ~y=290; photo ~y=305-490)
"""
from pathlib import Path
from PIL import Image

SRC = Path(
    r"C:\Users\Josvier\.cursor\projects\c-Users-Josvier-Desktop-erick-ingeniero"
    r"\assets\c__Users_Josvier_AppData_Roaming_Cursor_User_workspaceStorage"
    r"_338d46ad3c2de0267e03af1ce237e982_images_image-40e07840-08fa-4f62-a586-9e06e890cc53.png"
)
OUT = Path(r"c:\Users\Josvier\Desktop\erick_ingeniero\dlci-web\public\dlci\projects")

img = Image.open(SRC).convert("RGB")
W, H = img.size
print(f"source size: {W}x{H}")

# Fractional coordinates (independent of source resolution).
# Row Y bands (photo only, no title): row1=(0.10, 0.515), row2=(0.585, 0.98).
# Column X bands: col1=(0.005, 0.328), col2=(0.337, 0.66), col3=(0.668, 0.99).
ROW = [(0.14, 0.515), (0.62, 0.985)]
COL = [(0.005, 0.328), (0.337, 0.660), (0.668, 0.985)]

slots = [
    ("residencial-sorrento", 0, 0),
    ("torre-biventi-iii", 0, 1),
    ("torre-soria", 0, 2),
    ("residencial-dj", 1, 0),
    ("torre-murcia", 1, 1),
    ("torre-bonsai", 1, 2),
]


def save(crop: Image.Image, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    crop.save(path, "JPEG", quality=92, optimize=True)
    print("jpg", path.name, crop.size)


for name, r, c in slots:
    y0, y1 = ROW[r]
    x0, x1 = COL[c]
    box = (int(x0 * W), int(y0 * H), int(x1 * W), int(y1 * H))
    crop = img.crop(box)
    save(crop, OUT / f"{name}.jpg")
print("Listo")
