#!/usr/bin/env python3
"""Prepara las fuentes de las fotografías propias de Carlos para los collages.

Uso:  python3 _collage/preparar_propias.py /ruta/a/copias/de/fotos-blog

Los originales NO se guardan en el repositorio. Viven en la carpeta privada
«fotos blog» de Google Drive de Carlos y nunca se modifican. Este script lee
una copia local (cada archivo nombrado con su ID de Drive + .jpg), endereza
según la orientación EXIF, recorta solo la zona que el collage necesita,
reduce el tamaño y guarda una imagen NUEVA sin EXIF, GPS, XMP ni perfil ICC
en _collage/fuentes/propias/. Después hay que correr componer.py.

Al sumar una foto: añadirla a FOTOS, correr este script, comprobar que no
tiene metadatos (ver docs/visual-system.md) y registrar su uso en
_collage/README.md y en creditos.md.
"""
import os
import sys

from PIL import Image, ImageOps

BASE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(BASE, "fuentes", "propias")

# nombre: (ID del archivo en Drive, recorte en fracciones x0,y0,x1,y1, lado largo máx.)
FOTOS = {
    # Collages
    "vado": ("1v3JVg51zGXO1IyWvrFZ7zM4rkNrzD2d4", (0.0, 0.30, 1.0, 0.80), 1400),
    "busto-plaza": ("1yxP3iMPNK6_9JWcq51uc41s4iDjqpuCY", (0.37, 0.03, 0.98, 0.78), 1800),
    "luna": ("1b1zXkU-3GLu4Qw04Il-ixByjx3LX4x4e", (0.08, 0.24, 0.92, 0.64), 1600),
    # Fragmentos de portadas automáticas
    "iglesia": ("1L-v6Bi7IjJPumyes53tB8zrLRceIC1mJ", (0.12, 0.04, 0.88, 0.96), 1200),
    "crucifijo": ("1ThrDb7IN8HGF8fMgUiXEQW8jAbhEnn59", (0.0, 0.0, 0.60, 0.96), 1200),
    "curva": ("1vbCu8IgjicFC2q0P8oKjlAz9Yt-tBHNc", (0.0, 0.14, 1.0, 0.74), 1200),
    "isla": ("1BaxaCfErzYWbpDYneCDdiU361CGlTU6D", (0.08, 0.22, 0.92, 0.86), 1200),
    "guerrero": ("1wNoEZgIpljDod8Kb7GXYqW1pA8zs0zH7", (0.0, 0.0, 1.0, 0.94), 1200),
}


def preparar(orig_dir):
    os.makedirs(OUT, exist_ok=True)
    for name, (fid, box, lado) in FOTOS.items():
        im = ImageOps.exif_transpose(Image.open(os.path.join(orig_dir, fid + ".jpg"))).convert("RGB")
        w, h = im.size
        im = im.crop((int(box[0] * w), int(box[1] * h), int(box[2] * w), int(box[3] * h)))
        im.thumbnail((lado, lado), Image.LANCZOS)
        limpia = Image.new("RGB", im.size)  # imagen nueva: no hereda info ni EXIF
        limpia.paste(im)
        path = os.path.join(OUT, name + ".jpg")
        limpia.save(path, "JPEG", quality=86, optimize=True)
        print(path, limpia.size, os.path.getsize(path) // 1024, "KB")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    preparar(sys.argv[1])
