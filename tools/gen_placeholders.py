#!/usr/bin/env python3
"""Generate labeled placeholder assets for the docs.

Every image/animation referenced in docs/ gets a simple placeholder so the site
builds with `mkdocs build --strict`. Replace these with real screenshots and
screen recordings as they are produced. Re-running this script will NOT overwrite
an existing file, so real assets are safe.
"""
import os
import re
from PIL import Image, ImageDraw, ImageFont

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOCS = os.path.join(ROOT, "docs")

TEAL = (0, 121, 107)
ORANGE = (255, 112, 67)
BG = (236, 239, 241)
FG = (38, 50, 56)


def _font(size):
    for path in (
        "/System/Library/Fonts/Supplemental/Arial.ttf",
        "/System/Library/Fonts/Helvetica.ttc",
    ):
        if os.path.exists(path):
            try:
                return ImageFont.truetype(path, size)
            except Exception:
                pass
    return ImageFont.load_default()


def _frame(w, h, label, accent, tag):
    img = Image.new("RGB", (w, h), BG)
    d = ImageDraw.Draw(img)
    d.rectangle([0, 0, w - 1, h - 1], outline=accent, width=4)
    d.rectangle([0, 0, w - 1, 40], fill=accent)
    d.text((16, 10), f"PLACEHOLDER — {tag}", fill=(255, 255, 255), font=_font(20))
    d.text((16, h // 2 - 10), label, fill=FG, font=_font(22))
    d.text((16, h - 34), "replace with real asset", fill=TEAL, font=_font(16))
    return img


def find_assets():
    pat = re.compile(r"assets/(screenshots|animations|diagrams)/([A-Za-z0-9._-]+\.(png|gif|jpg|svg))")
    found = {}
    for base, _, files in os.walk(DOCS):
        for f in files:
            if not f.endswith(".md"):
                continue
            with open(os.path.join(base, f), encoding="utf-8") as fh:
                for m in pat.finditer(fh.read()):
                    found[m.group(0)] = m.group(3)
    return found


def main():
    assets = find_assets()
    created = 0
    for rel, ext in sorted(assets.items()):
        out = os.path.join(DOCS, rel)
        os.makedirs(os.path.dirname(out), exist_ok=True)
        if os.path.exists(out):
            continue
        name = os.path.basename(rel)
        if ext == "gif":
            frames = [_frame(640, 400, name, ORANGE, f"ANIMATION {i + 1}/3") for i in range(3)]
            frames[0].save(out, save_all=True, append_images=frames[1:], duration=700, loop=0)
        elif ext == "png":
            _frame(640, 400, name, TEAL, "SCREENSHOT").save(out)
        else:
            continue
        created += 1
        print("created", rel)
    print(f"done: {created} created, {len(assets) - created} already existed")


if __name__ == "__main__":
    main()
