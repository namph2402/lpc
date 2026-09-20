"""Sinh ảnh OG (1200x630) cho từng trang + sitemap.xml + robots.txt từ scripts/pages.json.

Chạy:  python3 scripts/build_seo_assets.py
Cần:   Pillow, font Noto Sans (hỗ trợ tiếng Việt).
"""
import json
from datetime import date
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter, ImageFont

ROOT = Path(__file__).resolve().parent.parent
DATA = json.loads((ROOT / "scripts/pages.json").read_text(encoding="utf-8"))
OUT = ROOT / "assets/og"
OUT.mkdir(parents=True, exist_ok=True)

FONT_DIR = Path("/usr/share/fonts/truetype/noto")
BOLD = str(FONT_DIR / "NotoSans-Bold.ttf")
REG = str(FONT_DIR / "NotoSans-Regular.ttf")
BOLD_IT = str(FONT_DIR / "NotoSans-BoldItalic.ttf")

W, H = 1200, 630
NAVY = (11, 31, 68)
NAVY_2 = (26, 52, 112)
RED = (227, 30, 36)
BLUE = (30, 91, 216)
BLUE_LIGHT = (111, 162, 255)
WHITE = (255, 255, 255)


def bezier(p0, p1, p2, p3, steps=40):
    pts = []
    for i in range(steps + 1):
        t = i / steps
        x = (1 - t) ** 3 * p0[0] + 3 * (1 - t) ** 2 * t * p1[0] + 3 * (1 - t) * t**2 * p2[0] + t**3 * p3[0]
        y = (1 - t) ** 3 * p0[1] + 3 * (1 - t) ** 2 * t * p1[1] + 3 * (1 - t) * t**2 * p2[1] + t**3 * p3[1]
        pts.append((x, y))
    return pts


def draw_logo(d, x, y, s=1.6):
    """Biểu tượng tháp LPC (giống SVG trong js/layout.js), gốc (x, y), tỷ lệ s."""
    def P(px, py):
        return (x + px * s, y + py * s)

    strokes = [
        (RED, 4, [(4, 50), (16, 40), (22, 24), (25, 2)], [(25, 2), (28, 24), (34, 40), (46, 50)]),
        (BLUE_LIGHT, 3, [(13, 50), (21, 42), (24, 30), (25, 16)], [(25, 16), (26, 30), (29, 42), (37, 50)]),
        (WHITE, 2.4, [(20, 50), (24, 44), (25, 38), (25, 30)], [(25, 30), (25, 38), (26, 44), (30, 50)]),
    ]
    for color, width, a, b in strokes:
        for seg in (a, b):
            d.line(bezier(*[P(*p) for p in seg]), fill=color, width=int(width * s), joint="curve")
    d.text(P(54, 6), "LPC", font=ImageFont.truetype(BOLD_IT, int(30 * s)), fill=WHITE)
    d.text(P(55, 41), "Responsive to change", font=ImageFont.truetype(REG, int(9 * s)), fill=(200, 210, 228))


def wrap(d, text, font, max_w):
    words, lines, cur = text.split(), [], ""
    for w in words:
        test = f"{cur} {w}".strip()
        if d.textlength(test, font=font) <= max_w:
            cur = test
        else:
            lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def background():
    img = Image.new("RGB", (W, H), NAVY)
    grad = Image.linear_gradient("L").rotate(90).resize((W, H))
    img = Image.composite(Image.new("RGB", (W, H), NAVY_2), img, grad.point(lambda v: int(v * 0.85)))
    d = ImageDraw.Draw(img, "RGBA")
    # Lưới blueprint
    for gx in range(0, W, 32):
        d.line([(gx, 0), (gx, H)], fill=(111, 162, 255, 18))
    for gy in range(0, H, 32):
        d.line([(0, gy), (W, gy)], fill=(111, 162, 255, 18))
    # Skyline mờ bên phải
    sky = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    sd = ImageDraw.Draw(sky)
    buildings = [(640, 380), (690, 300), (730, 420), (770, 230), (830, 330), (870, 180), (930, 280),
                 (975, 360), (1010, 210), (1070, 300), (1110, 390), (1150, 260)]
    for i, (bx, top) in enumerate(buildings):
        bw = 44 if i % 2 else 36
        sd.rectangle([bx, top, bx + bw, H], fill=(255, 255, 255, 26))
        for wy in range(top + 14, H - 10, 18):
            for wx in range(bx + 6, bx + bw - 6, 10):
                sd.rectangle([wx, wy, wx + 4, wy + 7], fill=(160, 200, 255, 30))
    sd.polygon([(870, 180), (891, 120), (914, 180)], fill=(255, 255, 255, 26))
    img.paste(sky.filter(ImageFilter.GaussianBlur(0.6)), (0, 0), sky)
    # Làm tối vùng chữ bên trái
    shade = Image.linear_gradient("L").rotate(90).resize((W, H)).point(lambda v: int((255 - v) * 0.55))
    img = Image.composite(Image.new("RGB", (W, H), NAVY), img, shade)
    return img


def render(page):
    img = background()
    d = ImageDraw.Draw(img, "RGBA")
    pad = 72

    draw_logo(d, pad, 52)

    # Eyebrow
    ey_font = ImageFont.truetype(BOLD, 22)
    d.rectangle([pad, 206, pad + 36, 209], fill=RED)
    d.text((pad + 50, 193), page["eyebrow"].upper(), font=ey_font, fill=WHITE)

    # Tiêu đề
    size = 60
    title = page["title"].upper()
    while True:
        tf = ImageFont.truetype(BOLD, size)
        lines = wrap(d, title, tf, 760)
        if len(lines) <= 2 or size <= 46:
            break
        size -= 2
    ty = 240
    for line in lines:
        d.text((pad, ty), line, font=tf, fill=WHITE)
        ty += int(size * 1.18)

    # Mô tả
    df = ImageFont.truetype(REG, 24)
    desc = wrap(d, page["description"], df, 700)
    if len(desc) > 2:
        desc = desc[:2]
        while d.textlength(desc[1] + " …", font=df) > 700:
            desc[1] = desc[1].rsplit(" ", 1)[0]
        desc[1] = desc[1].rstrip(",:;—–- ") + " …"
    ty += 26
    for line in desc:
        d.text((pad, ty), line, font=df, fill=(214, 222, 236))
        ty += 34

    # Từ khóa bên phải (giống hero)
    kf = ImageFont.truetype(BOLD, 20)
    kw = [k.upper() for k in page["keywords"]]
    kx = W - pad - max(d.textlength(k, font=kf) for k in kw)
    ky = H - 90 - len(kw) * 30
    d.rectangle([kx - 18, ky, kx - 15, ky + len(kw) * 30 - 6], fill=RED)
    for k in kw:
        d.text((kx, ky), k, font=kf, fill=WHITE)
        ky += 30

    # Chân: thanh đỏ + domain
    d.rectangle([0, H - 8, W, H], fill=RED)
    d.text((pad, H - 58), "lpc.vn  ·  Engineering · Technology · People", font=ImageFont.truetype(REG, 20), fill=(190, 202, 222))

    img.save(OUT / f"{page['slug']}.jpg", "JPEG", quality=88, optimize=True, progressive=True)


def sitemap():
    today = date.today().isoformat()
    urls = "\n".join(
        f"  <url>\n    <loc>{DATA['site']}/{'' if p['file'] == 'index.html' else p['file']}</loc>\n"
        f"    <lastmod>{today}</lastmod>\n    <priority>{p['priority']}</priority>\n  </url>"
        for p in DATA["pages"]
    )
    (ROOT / "sitemap.xml").write_text(
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + urls + "\n</urlset>\n",
        encoding="utf-8",
    )
    (ROOT / "robots.txt").write_text(f"User-agent: *\nAllow: /\n\nSitemap: {DATA['site']}/sitemap.xml\n", encoding="utf-8")


if __name__ == "__main__":
    for p in DATA["pages"]:
        render(p)
        print("og:", p["slug"])
    sitemap()
    print("sitemap.xml, robots.txt")
