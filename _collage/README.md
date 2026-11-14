# Collages de El cuaderno

Esta carpeta empieza con guion bajo, así que Jekyll no la publica. Aquí están
las imágenes de origen, las fuentes tipográficas y el script que compone los
collages que sí se publican en `assets/collage/`.

```bash
python3 _collage/componer.py            # todos
python3 _collage/componer.py mentira    # uno
```

Requiere Python 3 con Pillow (`pip install pillow`).

La guía completa del sistema visual está en
[`docs/visual-system.md`](../docs/visual-system.md). Esta página resume las
reglas y registra la procedencia.

Fotos propias: `python3 _collage/preparar_propias.py /ruta/a/copias` genera
los derivados recortados y sin metadatos de `fuentes/propias/`. Los originales
no se guardan aquí.

## Reglas del sistema

1. Fondo de noche (carbón azulado) con grano.
2. Fotografía de lugar en duotono tinta/cal. Solo las fotos nocturnas conservan
   su color, calentado. Las fotos propias tienen prioridad cuando aportan
   al texto.
3. Láminas y grabados de archivo: tinta sobre papel de cal.
4. Máximo dos colores planos por pieza (terracota, ámbar, azul, rosa), usados
   para tapar, sustituir o señalar algo del argumento.
5. Cortes rectos; como mucho un borde rasgado por pieza.
6. Sombra corta y dura. Rotaciones de 3 grados o menos.
7. Como mucho una palabra o frase del texto, recortada en papel.
8. Círculos, etiquetas y grabados son opcionales, no obligatorios.

Cada collage sale en tres formatos: `-v` (4:5, escritorio), `-m` (1:1, móvil,
recompuesto con menos piezas) y `-h` (3:2, listas).

Una entrada sin collage propio no necesita nada: el sitio arma una portada
automática con un fragmento de `assets/collage/fragmentos/`, el color y la
marca de su tema. Hay dos composiciones (disco a la derecha o banda recta a la
izquierda); la fecha decide cuál y qué fragmento, de modo que las entradas
cercanas no se repiten. Una entrada puede fijar su fragmento con
`fragmento: nombre`. Para sumar un fragmento: guardarlo en esa carpeta,
añadir su nombre a la lista de `_includes/cover.html` y correr
`python3 _collage/componer.py tamanos`.

Para usar un collage en una entrada:

```yaml
collage: mentira
collage_alt: "Una fachada partida en dos versiones; encima, una lámina del ojo con el punto ciego tapado por un disco de terracota."
```

## Procedencia de las imágenes

### Fotografías propias

Fotografías de Carlos Reyes, de su carpeta privada «fotos blog», publicadas
con su autorización (noviembre de 2026). No tienen licencia abierta
declarada. Los derivados están recortados, reducidos y sin metadatos (EXIF,
GPS, XMP, ICC). Solo se atribuye un lugar cuando la imagen lo prueba.

| Archivo (`fuentes/propias/`) | Qué muestra | Uso |
|---|---|---|
| `vado.jpg` | Vado de concreto sobre un río crecido | Collage `puente` (Lo que repetís, eso sos) |
| `busto-plaza.jpg` | Busto de una plaza, de noche, con el yeso saltado | Collage `reflejo` (Narcisismo) |
| `luna.jpg` | Luna entre ramas | Collage `brasa` (Fuego que no debe tocar nada) |
| `iglesia.jpg` | Iglesia iluminada de noche | Fragmento fijo de «Si Dios permanece…» |
| `crucifijo.jpg` | Crucifijo en relieve y santo en su nicho, en una fachada de La Campa (el letrero del cerro lo atestigua; no aparece en el recorte) | Fragmento fijo de «Romanos 1–3» |
| `curva.jpg` | Calle de noche con señal de curva | Fragmento fijo de «Lo que Honduras decide en 2025» |
| `isla.jpg` | Isla sola en el mar | Fragmento fijo de «El fundamento o el abismo» |
| `guerrero.jpg` | Estatua de un guerrero indígena y torre de reloj, de noche | Fragmento de la rotación general |

Excluidas por decisión de Carlos: las fotos del bolsillo y del microscopio.

### Fuentes externas

Ninguna es una obra de las referencias de diseño (Javier Palma, 24 Grados,
Mujeres en las Artes, Estudio 1331). Todas vienen de Wikimedia Commons y se
usan según su licencia, verificada el 14 de noviembre de 2026. Los collages derivados de obras CC BY-SA se publican
bajo CC BY-SA 4.0.

| Archivo | Obra original | Autor | Licencia | Uso |
|---|---|---|---|---|
| `casa.jpg` | [Old house in Tegucigalpa](https://commons.wikimedia.org/wiki/File:Old_house_in_Tegucigalpa.jpg) (2021) | Luis Alfredo Romero | CC BY-SA 4.0 | La mentira… |
| `escalinata.jpg` | [La Leona Tegucigalpa stairs](https://commons.wikimedia.org/wiki/File:La_Leona_Tegucigalpa_stairs.jpg) (2006) | chamo estudio | CC BY-SA 2.0 | TDAH, fragmento |
| `picacho.jpg` | [El Picacho at dusk](https://commons.wikimedia.org/wiki/File:El_Picacho_at_dusk.jpg) (2007) | Ian Mackenzie (madmack66), vía Flickr | CC BY 2.0 | Amar la herida |
| `calle.jpg` | [Tegucigalpa Honduras street](https://commons.wikimedia.org/wiki/File:Tegucigalpa_Honduras_street.jpg) (2006) | chamo estudio | CC BY-SA 2.0 | Fragmento |
| `grabado.jpg` | [Tegucigalpa late 19th century](https://commons.wikimedia.org/wiki/File:Tegucigalpa_late_19th_century.jpg) (1890) | Autor desconocido | Dominio público | Fragmento |
| `ojo.jpg` | [Gray869](https://commons.wikimedia.org/wiki/File:Gray869.png), *Gray's Anatomy* (1918) | Henry Vandyke Carter / Henry Gray | Dominio público | La mentira… |
| `platon.jpg` | [Plato Silanion Musei Capitolini MC1377](https://commons.wikimedia.org/wiki/File:Plato_Silanion_Musei_Capitolini_MC1377.jpg) | Marie-Lan Nguyen (Jastrow) | Fotografía CC BY 2.5 (escultura en dominio público) | Amar la herida |

Las fuentes tipográficas (Fraunces, Public Sans) están bajo SIL Open Font
License.
