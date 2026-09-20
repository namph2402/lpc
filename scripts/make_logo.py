"""Tạo bộ logo LPC từ file gốc (PNG nền trong suốt).

Chạy:  python3 scripts/make_logo.py <file-logo-goc.png>
Xuất:  assets/img/logo-lpc.png        — bản chuẩn (nền sáng)
       assets/img/logo-lpc-white.png  — bản chữ trắng (nền tối: footer, hero)
       assets/img/logo-mark.png       — riêng biểu tượng tháp (favicon, OG, app icon)
       assets/apple-touch-icon.png    — biểu tượng tháp trên nền navy, bo góc
       assets/favicon.svg             — favicon nhúng biểu tượng tháp
"""
import base64
import sys
from pathlib import Path

from PIL import Image, ImageDraw

ROOT = Path(__file__).resolve().parent.parent
IMG = ROOT / "assets/img"
IMG.mkdir(parents=True, exist_ok=True)
NAVY = (11, 31, 68, 255)


def trim(im):
    """Cắt sát viền theo kênh alpha."""
    return im.crop(im.getchannel("A").getbbox())


def to_white(im):
    """Đổi phần chữ/nét xanh sang trắng, giữ nguyên màu đỏ — dùng trên nền tối."""
    px = im.load()
    w, h = im.size
    for y in range(h):
        for x in range(w):
            r, g, b, a = px[x, y]
            if a and b > r:  # thiên xanh
                px[x, y] = (255, 255, 255, a)
    return im


def split_mark(im):
    """Tách riêng biểu tượng tháp: cắt tại hàng trống rộng nhất phía trên chữ LPC."""
    alpha = im.getchannel("A")
    w, h = im.size
    rows = [sum(alpha.crop((0, y, w, y + 1)).getdata()) for y in range(h)]
    # Biểu tượng nằm ở nửa trên; tìm hàng ít mực nhất trong khoảng 45–80% chiều cao
    lo, hi = int(h * 0.45), int(h * 0.80)
    cut = min(range(lo, hi), key=lambda y: rows[y])
    return trim(im.crop((0, 0, w, cut)))


def horizontal(mark, word, gap_ratio=0.12, word_ratio=0.62):
    """Ghép logo nằm ngang: biểu tượng bên trái, chữ LPC + tagline bên phải."""
    h = mark.height
    wh = int(h * word_ratio)
    w2 = word.resize((round(word.width * wh / word.height), wh), Image.LANCZOS)
    gap = int(h * gap_ratio)
    out = Image.new("RGBA", (mark.width + gap + w2.width, h), (0, 0, 0, 0))
    out.paste(mark, (0, 0), mark)
    out.paste(w2, (mark.width + gap, (h - wh) // 2), w2)
    return out


def rounded_icon(mark, size=180, pad_ratio=0.16, radius_ratio=0.22):
    icon = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    mask = Image.new("L", (size, size), 0)
    ImageDraw.Draw(mask).rounded_rectangle([0, 0, size - 1, size - 1], radius=int(size * radius_ratio), fill=255)
    icon.paste(Image.new("RGBA", (size, size), NAVY), (0, 0), mask)
    inner = size - int(size * pad_ratio) * 2
    m = mark.copy()
    m.thumbnail((inner, inner), Image.LANCZOS)
    icon.paste(m, ((size - m.width) // 2, (size - m.height) // 2), m)
    return icon


def main(src):
    base = trim(Image.open(src).convert("RGBA"))
    base.save(IMG / "logo-lpc.png")
    to_white(base.copy()).save(IMG / "logo-lpc-white.png")

    mark = split_mark(base)
    mark.save(IMG / "logo-mark.png")

    # Phần chữ (LPC + tagline) = phần còn lại phía dưới
    word = trim(base.crop((0, mark.height + base.height // 40, base.width, base.height)))
    word.save(IMG / "logo-word.png")

    # Bản nằm ngang dùng cho header
    horizontal(mark, word).save(IMG / "logo-lpc-h.png")
    horizontal(to_white(mark.copy()), to_white(word.copy())).save(IMG / "logo-lpc-h-white.png")

    icon = rounded_icon(to_white(mark.copy()))
    icon.save(ROOT / "assets/apple-touch-icon.png")

    small = icon.resize((64, 64), Image.LANCZOS)
    buf = ROOT / "assets/favicon.svg"
    from io import BytesIO

    b = BytesIO()
    small.save(b, "PNG", optimize=True)
    data = base64.b64encode(b.getvalue()).decode()
    buf.write_text(
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64">'
        f'<image width="64" height="64" href="data:image/png;base64,{data}"/></svg>',
        encoding="utf-8",
    )
    print("logo:", base.size, "· mark:", mark.size)


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else ROOT / "assets/img/logo-source.png")
