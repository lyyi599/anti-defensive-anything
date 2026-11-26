#!/usr/bin/env python3
"""Generate the logo: a four-point star breaking through its shield.

    python3 assets/src/gen_logo.py            # writes assets/logo.svg, logo.png, icon.png

logo.svg needs only the standard library; the PNGs need Pillow.
Tune the design through the PARAMS dict below.
"""
import math
from pathlib import Path

ASSETS = Path(__file__).resolve().parent.parent
COLOR = "#E4573D"

PARAMS = dict(
    tilt=10,        # star lean to the right, degrees
    top=-2.1,       # long (leading) tip, in star units
    half=0.66,      # left/right tips
    low=0.78,       # bottom tip
    cy=0.1,         # star vertical offset inside the shield
    pinch=0.6,      # how concave the star sides are (0 = straight, 1 = through centre)
    star_w=0.074,   # star stroke max half-width (strokes taper to points)
    shield_w=0.034, # shield stroke half-width
    gap=0.3,        # half-width of the breach in the shield's top edge
    margin=40,      # padding inside the 512 viewBox
)


def lerp(a, b, t):
    return (a[0] + (b[0] - a[0]) * t, a[1] + (b[1] - a[1]) * t)


def rot(p, deg):
    a = math.radians(deg)
    return (p[0] * math.cos(a) - p[1] * math.sin(a), p[0] * math.sin(a) + p[1] * math.cos(a))


def bez(p0, p1, p2, p3, n=90):
    out = []
    for j in range(n + 1):
        t = j / n
        u = 1 - t
        out.append(tuple(u**3 * p0[i] + 3 * u * u * t * p1[i] + 3 * u * t * t * p2[i] + t**3 * p3[i] for i in (0, 1)))
    return out


def line(a, b, n=40):
    return [lerp(a, b, j / n) for j in range(n + 1)]


def ribbon(pts, width):
    """Variable-width stroke around a centreline, as a closed polygon. width(t) is the half-width."""
    left, right = [], []
    n = len(pts)
    for i, (x, y) in enumerate(pts):
        a, b = pts[max(i - 1, 0)], pts[min(i + 1, n - 1)]
        dx, dy = b[0] - a[0], b[1] - a[1]
        m = math.hypot(dx, dy) or 1
        nx, ny = -dy / m, dx / m
        w = width(i / (n - 1))
        left.append((x + nx * w, y + ny * w))
        right.append((x - nx * w, y - ny * w))
    return left + right[::-1]


def star(p):
    tips = [rot(t, p["tilt"]) for t in [(0, p["top"]), (p["half"], 0), (0, p["low"]), (-p["half"], 0)]]
    tips = [(x, y + p["cy"]) for x, y in tips]
    taper = lambda t: 0.006 + (p["star_w"] - 0.006) * math.sin(math.pi * t)
    polys = []
    for i in range(4):
        a, b = tips[i], tips[(i + 1) % 4]
        c1 = lerp(lerp(a, b, 1 / 3), (0, 0), p["pinch"])
        c2 = lerp(lerp(a, b, 2 / 3), (0, 0), p["pinch"])
        polys.append(ribbon(bez(a, c1, c2, b), taper))
    return tips, polys


def shield_loop(top=-0.8, half=1.0, r=0.16, mid=0.1, bottom=1.32):
    """Closed shield outline starting and ending at the top centre, clockwise."""
    right = (line((0, top), (half - r, top))
             + bez((half - r, top), (half - r * 0.45, top), (half, top + r * 0.45), (half, top + r), 30)[1:]
             + line((half, top + r), (half, mid))[1:]
             + bez((half, mid), (half, 0.72), (0.5, 1.08), (0, bottom))[1:])
    left = [(-x, y) for x, y in reversed(right)]
    return right + left[1:]


def shield(p, tips):
    loop = shield_loop()
    top = loop[0][1]
    # where the star's leading tip crosses the top edge (axis: tip -> star centre)
    (x0, y0) = tips[0]
    x1, y1 = (tips[1][0] + tips[3][0]) / 2, (tips[1][1] + tips[3][1]) / 2
    xc = x0 + (x1 - x0) * (top - y0) / (y1 - y0)
    on_top = [i for i, (x, y) in enumerate(loop) if abs(y - top) < 1e-9]
    start = next(i for i in on_top if loop[i][0] >= xc + p["gap"])
    end = max(i for i in on_top if loop[i][0] <= xc - p["gap"])
    path = loop[start:end + 1]
    ramp = 0.06  # the breach edges taper to points
    return ribbon(path, lambda t: p["shield_w"] * min(1.0, t / ramp, (1 - t) / ramp))


def fit(polys, size=512, margin=40):
    xs = [x for p in polys for x, _ in p]
    ys = [y for p in polys for _, y in p]
    sc = (size - 2 * margin) / max(max(xs) - min(xs), max(ys) - min(ys))
    cx, cy = (max(xs) + min(xs)) / 2, (max(ys) + min(ys)) / 2
    return [[((x - cx) * sc + size / 2, (y - cy) * sc + size / 2) for x, y in p] for p in polys]


def build(p=PARAMS):
    tips, polys = star(p)
    return fit(polys + [shield(p, tips)], margin=p["margin"])


def write_svg(polys, path):
    body = "\n".join('  <path d="M' + " L".join(f"{x:.1f} {y:.1f}" for x, y in p) + 'Z"/>' for p in polys)
    path.write_text(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512">\n<g fill="{COLOR}">\n{body}\n</g>\n</svg>\n')


def write_pngs(polys, logo_path, icon_path, size=1024, scale=4):
    from PIL import Image, ImageDraw

    s = size * scale
    mask = Image.new("L", (s, s), 0)
    draw = ImageDraw.Draw(mask)
    for p in polys:
        draw.polygon([(x * s / 512, y * s / 512) for x, y in p], fill=255)
    logo = Image.new("RGBA", (size, size), COLOR)
    logo.putalpha(mask.resize((size, size), Image.LANCZOS))
    logo.save(logo_path)
    icon = Image.new("RGBA", (size, size), "#FFFFFF")
    inner = size * 900 // 1024
    off = (size - inner) // 2
    icon.alpha_composite(logo.resize((inner, inner), Image.LANCZOS), (off, off))
    icon.convert("RGB").save(icon_path)


if __name__ == "__main__":
    polys = build()
    write_svg(polys, ASSETS / "logo.svg")
    try:
        write_pngs(polys, ASSETS / "logo.png", ASSETS / "icon.png")
    except ImportError:
        print("Pillow not installed: wrote logo.svg only")
    print("wrote", ", ".join(str(p.relative_to(ASSETS.parent)) for p in sorted(ASSETS.glob("*.*"))))
