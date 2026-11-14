#!/usr/bin/env python3
"""Compone los collages editoriales de El cuaderno.

Uso:  python3 _collage/componer.py            (todos)
      python3 _collage/componer.py mentira    (uno)

Cada collage se escribe en assets/collage/ en tres formatos:
  <nombre>-v.webp  4:5   portada y apertura en escritorio
  <nombre>-m.webp  1:1   recomposición para móvil (menos piezas, más grandes)
  <nombre>-h.webp  3:2   tarjetas y listas

Reglas comunes (ver _collage/README.md):
  1. Fondo de noche (carbón azulado) con grano.
  2. Fotografía de lugar en duotono tinta/cal. Solo las fotos nocturnas
     conservan su color, calentado.
  3. Láminas y grabados de archivo: tinta sobre papel de cal.
  4. Máximo dos colores planos por pieza (terracota, ámbar, azul, rosa),
     usados para tapar, sustituir o señalar.
  5. Cortes rectos; como mucho un borde rasgado por pieza.
  6. Sombra corta y dura. Rotaciones de 3 grados o menos.
  7. Una sola palabra o frase del texto, recortada en papel.
"""
import os
import random
import sys

from PIL import Image, ImageChops, ImageDraw, ImageEnhance, ImageFilter, ImageFont, ImageOps

BASE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(BASE, "fuentes")
OUT = os.path.join(BASE, "..", "assets", "collage")
FONT_ITALIC = os.path.join(BASE, "fonts", "FrauncesItalic.ttf")
FONT_SANS = os.path.join(BASE, "fonts", "PublicSansSemi.ttf")

C = {
    "noche": (19, 23, 30),
    "tinta": (24, 28, 36),
    "cal": (233, 225, 207),
    "cal_tibia": (240, 214, 168),
    "terracota": (196, 98, 62),
    "ambar": (226, 163, 59),
    "azul": (122, 151, 173),
    "rosa": (214, 139, 138),
}


def src(name):
    return Image.open(os.path.join(SRC, name)).convert("RGB")


def crop_frac(im, box):
    w, h = im.size
    return im.crop((int(box[0] * w), int(box[1] * h), int(box[2] * w), int(box[3] * h)))


def fit(im, size):
    return ImageOps.fit(im, size, Image.LANCZOS)


def duotone(im, dark=C["tinta"], light=C["cal"], contrast=1.2):
    g = ImageOps.grayscale(im)
    g = ImageOps.autocontrast(g, cutoff=1)
    g = ImageEnhance.Contrast(g).enhance(contrast)
    return ImageOps.colorize(g, dark, light)


def ink(im, paper=C["cal"], ink_c=C["tinta"]):
    g = ImageOps.autocontrast(ImageOps.grayscale(im), cutoff=2)
    return ImageOps.colorize(g, ink_c, paper)


def night(im, warmth=1.15):
    r, g, b = im.split()
    r = r.point(lambda v: min(255, int(v * warmth)))
    b = b.point(lambda v: int(v * 0.92))
    return ImageEnhance.Contrast(Image.merge("RGB", (r, g, b))).enhance(1.1)


def grain(im, amount=16):
    n = Image.effect_noise(im.size, amount).convert("L")
    n = Image.merge("RGB", (n, n, n))
    out = ImageChops.add(im.convert("RGB"), n, 1.0, -128)
    if im.mode == "RGBA":
        out.putalpha(im.getchannel("A"))
    return out


def rough_mask(size, torn="", amp=7, seed=1):
    """Máscara rectangular; los lados en `torn` (t,b,l,r) quedan rasgados."""
    rnd = random.Random(seed)
    w, h = size
    step = 9
    pts = []

    def jit(side):
        return rnd.uniform(0, amp) if side in torn else 0

    for x in range(0, w + 1, step):
        pts.append((x, jit("t")))
    for y in range(0, h + 1, step):
        pts.append((w - jit("r"), y))
    for x in range(w, -1, -step):
        pts.append((x, h - jit("b")))
    for y in range(h, -1, -step):
        pts.append((jit("l"), y))
    m = Image.new("L", size, 0)
    ImageDraw.Draw(m).polygon(pts, fill=255)
    return m


def piece(im, torn="", seed=1, rotate=0):
    p = im.convert("RGBA")
    p.putalpha(rough_mask(p.size, torn, seed=seed))
    if rotate:
        p = p.rotate(rotate, resample=Image.BICUBIC, expand=True)
    return p


def disc(d, color, seed=3):
    """Círculo de papel cortado a mano: borde levemente irregular."""
    rnd = random.Random(seed)
    s = 4
    big = Image.new("RGBA", (d * s, d * s), (0, 0, 0, 0))
    dr = ImageDraw.Draw(big)
    import math

    pts = []
    for i in range(90):
        a = 2 * math.pi * i / 90
        r = d * s / 2 - 2 - rnd.uniform(0, d * s * 0.012)
        pts.append((d * s / 2 + r * math.cos(a), d * s / 2 + r * math.sin(a)))
    dr.polygon(pts, fill=color + (255,))
    return grain(big.resize((d, d), Image.LANCZOS), 10)


def circle_window(im, d):
    """Recorte circular de una imagen (lupa, foco)."""
    p = fit(im, (d, d)).convert("RGBA")
    m = Image.new("L", (d * 4, d * 4), 0)
    ImageDraw.Draw(m).ellipse((0, 0, d * 4 - 1, d * 4 - 1), fill=255)
    p.putalpha(m.resize((d, d), Image.LANCZOS))
    return p


def silhouette(im, tol=46):
    """Separa la figura de un fondo liso (el color de las esquinas superiores)."""
    px = im.load()
    w, h = im.size
    bg = [sum(c) / 2 for c in zip(px[3, 3], px[w - 4, 3])]
    diff = ImageChops.difference(im, Image.new("RGB", im.size, tuple(int(v) for v in bg)))
    g = ImageOps.grayscale(diff).point(lambda v: 255 if v > tol / 3 else 0)
    g = g.filter(ImageFilter.MaxFilter(3)).filter(ImageFilter.MinFilter(7)).filter(ImageFilter.MaxFilter(3))
    return g.filter(ImageFilter.GaussianBlur(1.2))


def cut_piece(p, torn="", seed=1, rotate=0):
    """Como piece(), pero conserva el alfa de una figura ya recortada."""
    a = ImageChops.multiply(p.getchannel("A"), rough_mask(p.size, torn, seed=seed))
    p = p.copy()
    p.putalpha(a)
    return p.rotate(rotate, resample=Image.BICUBIC, expand=True) if rotate else p


def slab(size, color, torn="", seed=5):
    p = Image.new("RGB", size, color)
    return piece(grain(p, 12), torn, seed)


def label(text, size=46, paper=C["cal"], color=C["tinta"], rotate=0, font=FONT_ITALIC):
    f = ImageFont.truetype(font, size)
    l, t, r, b = f.getbbox(text)
    pad_x, pad_y = int(size * 0.45), int(size * 0.28)
    w, h = r - l + pad_x * 2, b - t + pad_y * 2
    p = Image.new("RGB", (w, h), paper)
    ImageDraw.Draw(p).text((pad_x - l, pad_y - t), text, font=f, fill=color)
    return piece(grain(p, 8), "lr", seed=len(text), rotate=rotate)


def paste(canvas, p, xy, shadow=True):
    x, y = int(xy[0]), int(xy[1])
    if shadow:
        a = p.getchannel("A")
        sh = Image.new("RGBA", p.size, (0, 0, 0, 0))
        sh.putalpha(a.point(lambda v: int(v * 0.6)))
        sh = sh.filter(ImageFilter.GaussianBlur(3))
        canvas.alpha_composite(sh, (x + 5, y + 7))
    canvas.alpha_composite(p, (x, y))


def background(size):
    bg = Image.new("RGB", size, C["noche"])
    return grain(bg, 14).convert("RGBA")


def save(canvas, name, fmt):
    os.makedirs(OUT, exist_ok=True)
    im = grain(canvas.convert("RGB"), 7)
    path = os.path.join(OUT, f"{name}-{fmt}.webp")
    im.save(path, "WEBP", quality=78, method=6)
    print(path, im.size, os.path.getsize(path) // 1024, "KB")
    tamanos(path)


# Anchos menores para srcset. Se derivan del archivo grande ya con grano, para
# que todas las versiones sean la misma imagen.
ANCHOS = {"v": [800], "m": [800, 640], "h": [800, 480], "frag": [640, 480]}


def tamanos(path):
    base, ext = os.path.splitext(path)
    fmt = base.rsplit("-", 1)[-1] if "-" in os.path.basename(base) else "frag"
    im = Image.open(path).convert("RGB")
    for w in ANCHOS.get(fmt, []):
        h = round(im.height * w / im.width)
        out = f"{base}-{w}{ext}"
        im.resize((w, h), Image.LANCZOS).save(out, "WEBP", quality=74, method=6)
        print("  ", out, (w, h), os.path.getsize(out) // 1024, "KB")


# ---------------------------------------------------------------------------
# La mentira que no se siente como mentira
# Idea: el punto ciego. La misma fachada partida en dos versiones que no
# coinciden; dentro, una lámina del ojo cuyo punto ciego (la salida del
# nervio óptico) queda tapado por un disco de terracota.
# ---------------------------------------------------------------------------
def mentira():
    casa = src("casa.jpg")
    fachada = crop_frac(casa, (0.0, 0.17, 0.72, 1.0))
    ojo = src("ojo.jpg")

    def build(W, H, F, E, D, labels):
        cv = background((W, H))
        # zócalo azul detrás, como la franja pintada de las paredes
        paste(cv, slab((int(W * 0.5), int(H * 0.17)), C["azul"]), (F[0] - 40, F[1] + F[3] - H * 0.09), shadow=False)
        fw, fh = F[2], F[3]
        base = fit(fachada, (fw, fh))
        mi = duotone(base.crop((0, 0, fw // 2, fh)))
        tuya = duotone(base.crop((fw // 2, 0, fw, fh)), light=C["cal_tibia"])
        paste(cv, piece(mi, seed=2), (F[0], F[1]))
        paste(cv, piece(tuya, seed=3), (F[0] + fw // 2 + int(W * 0.015), F[1] + int(H * 0.04)))
        ew = E[2]
        eh = int(ew * ojo.height / ojo.width)
        eye = piece(ink(ojo.resize((ew, eh), Image.LANCZOS)), torn="t", seed=7, rotate=E[3])
        paste(cv, eye, (E[0], E[1]))
        # el nervio óptico está en (0.50, 0.93) de la lámina
        cx = E[0] + eye.width * 0.505
        cy = E[1] + eye.height * 0.915
        paste(cv, disc(D, C["terracota"]), (cx - D / 2, cy - D / 2))
        for text, xy, size, rot in labels:
            paste(cv, label(text, size=size, rotate=rot), xy)
        return cv

    save(build(1200, 1500, (110, 150, 980, 860), (300, 860, 680, -3), 104,
               [("mi versión", (70, 95), 44, 2), ("la tuya", (700, 150), 44, -2)]), "mentira", "v")
    save(build(1000, 1000, (40, 40, 920, 560), (230, 470, 560, -2), 86,
               [("mi versión", (24, 12), 38, 2), ("la tuya", (560, 40), 38, -2)]), "mentira", "m")
    save(build(1200, 800, (60, 60, 700, 680), (600, 250, 560, -3), 86,
               [("mi versión", (30, 30), 36, 2), ("la tuya", (420, 54), 36, -2)]), "mentira", "h")


# ---------------------------------------------------------------------------
# Amar la herida
# Idea: Platón como andamio. El busto partido a la altura de los ojos y
# vuelto a unir con cintas de ámbar (reparación, no ruptura). Detrás, la
# ladera de El Picacho al anochecer: la espera, las ventanas encendidas.
# ---------------------------------------------------------------------------
def herida():
    pic = night(src("picacho.jpg"))
    pla = src("platon.jpg")
    busto = crop_frac(pla, (0.04, 0.02, 0.96, 0.86))

    def build(W, H, P, B, cut, gap, R, lab):
        cv = background((W, H))
        paste(cv, piece(fit(pic, (P[2], P[3])), seed=11), (P[0], P[1]))
        paste(cv, disc(R[2], C["rosa"], seed=9), (R[0], R[1]))
        bw, bh = B[2], int(B[2] * busto.height / busto.width)
        rs = busto.resize((bw, bh), Image.LANCZOS)
        b = duotone(rs, light=C["cal"], contrast=1.35).convert("RGBA")
        b.putalpha(silhouette(rs))
        cy = int(bh * cut)
        top = cut_piece(b.crop((0, 0, bw, cy)), torn="b", seed=21, rotate=-1.5)
        bot = cut_piece(b.crop((0, cy, bw, bh)), torn="t", seed=22, rotate=1)
        paste(cv, top, (B[0], B[1]))
        paste(cv, bot, (B[0] + int(bw * 0.03), B[1] + cy + gap))
        tw = int(bw * 0.07)
        for i, (fx, ang) in enumerate(((0.3, 9), (0.5, -5), (0.68, 7))):
            t = slab((tw, gap + int(bw * 0.12)), C["ambar"], torn="tb", seed=30 + i)
            t = t.rotate(ang, resample=Image.BICUBIC, expand=True)
            paste(cv, t, (B[0] + bw * fx - tw / 2, B[1] + cy - bw * 0.05))
        paste(cv, label(lab[0], size=lab[2], rotate=2), lab[1])
        return cv

    save(build(1200, 1500, (0, 0, 1200, 820), (220, 260, 760), 0.44, 34, (760, 1000, 360), ("la espera", (80, 1360), 46)), "herida", "v")
    save(build(1000, 1000, (0, 0, 1000, 520), (240, 90, 520), 0.44, 28, (650, 600, 300), ("la espera", (40, 880), 40)), "herida", "m")
    save(build(1200, 800, (0, 0, 1200, 470), (420, 30, 400), 0.44, 24, (800, 420, 300), ("la espera", (60, 690), 38)), "herida", "h")


# ---------------------------------------------------------------------------
# Explorando el TDAH desde dentro
# Idea: atención en competencia. Una escalinata de La Leona (direcciones,
# cables, puertas) con varios focos circulares que amplían detalles
# distintos al mismo tiempo; uno queda vacío, en terracota.
# ---------------------------------------------------------------------------
def tdah():
    esc = src("escalinata.jpg")

    def build(W, H, E, focos, vacio, lab):
        cv = background((W, H))
        paste(cv, piece(duotone(fit(esc, (E[2], E[3]))), seed=41), (E[0], E[1]))
        for (fx, fy, z, x, y, d, col) in focos:
            src_box = (fx - z, fy - z, fx + z, fy + z)
            ring = disc(d + 18, C[col], seed=int(x))
            paste(cv, ring, (x - 9, y - 9))
            paste(cv, circle_window(duotone(crop_frac(esc, src_box), light=C["cal_tibia"]), d), (x, y), shadow=False)
        paste(cv, disc(vacio[2], C["terracota"], seed=77), (vacio[0], vacio[1]))
        paste(cv, label(lab[0], size=lab[2], rotate=-2), lab[1])
        return cv

    # (centro x, centro y, radio en fracción, x, y, diámetro, color del aro)
    save(build(1200, 1500, (80, 120, 1040, 1040),
               [(0.84, 0.30, 0.09, 700, 900, 360, "ambar"), (0.12, 0.45, 0.08, 90, 980, 300, "ambar"), (0.24, 0.07, 0.07, 140, 60, 220, "azul")],
               (470, 1220, 170), ("¿cuál primero?", (700, 1340), 44)), "tdah", "v")
    save(build(1000, 1000, (40, 40, 920, 700),
               [(0.84, 0.30, 0.09, 600, 560, 300, "ambar"), (0.12, 0.45, 0.08, 60, 640, 250, "ambar")],
               (380, 800, 140), ("¿cuál primero?", (560, 900), 36)), "tdah", "m")
    save(build(1200, 800, (40, 40, 760, 720),
               [(0.84, 0.30, 0.09, 760, 120, 320, "ambar"), (0.12, 0.45, 0.08, 860, 470, 240, "ambar"), (0.24, 0.07, 0.07, 640, 560, 170, "azul")],
               (1040, 330, 120), ("¿cuál primero?", (700, 700), 34)), "tdah", "h")


# ---------------------------------------------------------------------------
# Fragmentos para portadas automáticas: las entradas sin collage propio usan
# uno de estos recortes (duotono) + el color y la marca de su tema, en CSS.
# ---------------------------------------------------------------------------
def fragmentos():
    os.makedirs(os.path.join(OUT, "fragmentos"), exist_ok=True)
    for name, box in {
        "grabado": (0.0, 0.25, 1.0, 1.0),
        "calle": (0.0, 0.0, 1.0, 1.0),
        "casa": (0.05, 0.1, 0.95, 1.0),
        "escalinata": (0.0, 0.0, 1.0, 1.0),
    }.items():
        im = crop_frac(src(name + ".jpg"), box)
        im.thumbnail((900, 900), Image.LANCZOS)
        im = grain(duotone(im, contrast=1.15), 9)
        path = os.path.join(OUT, "fragmentos", name + ".webp")
        im.save(path, "WEBP", quality=72, method=6)
        print(path, im.size, os.path.getsize(path) // 1024, "KB")


COLLAGES = {"mentira": mentira, "herida": herida, "tdah": tdah, "fragmentos": fragmentos}

def todos_los_tamanos():
    """Regenera solo los anchos menores a partir de las imágenes existentes."""
    import glob, re
    for f in sorted(glob.glob(os.path.join(OUT, "**", "*.webp"), recursive=True)):
        if not re.search(r"-\d+\.webp$", f):
            tamanos(f)


if __name__ == "__main__":
    random.seed(1)
    if sys.argv[1:] == ["tamanos"]:
        todos_los_tamanos()
        sys.exit()
    for name in sys.argv[1:] or COLLAGES:
        COLLAGES[name]()
