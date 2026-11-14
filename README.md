# El cuaderno

Blog personal de Carlos Reyes sobre medicina, filosofía, fe y ética. Publicado con Jekyll en GitHub Pages: https://carlosmvks1.github.io

## Escribir una entrada

Crea `_posts/AAAA-MM-DD-slug.md`. La fecha del nombre de archivo debe coincidir con `date:`.

```yaml
---
layout: post
title: "Título de la entrada"
date: AAAA-MM-DD
description: "Una o dos frases. Se usa en la portada, en las listas y al compartir el enlace."
subtitle: "Opcional: bajada que aparece bajo el título (si falta, se usa la descripción)."
categories: [medicina]   # medicina | filosofia | fe | proyectos
---
```

- Las secciones empiezan en `##` (el título de la entrada ya es el `#`).
- Para enlazar otra entrada: `{% post_url AAAA-MM-DD-slug %}`.

## Probar en local

```bash
bundle exec jekyll serve
```

## Campos opcionales del diseño

```yaml
collage: mentira          # usa assets/collage/mentira-{v,m,h}.webp
collage_alt: "…"          # descripción del collage para lectores de pantalla
cita: "…"                 # frase destacada en la portada si es la última entrada
apertura: guia            # para guías médicas: imagen más pequeña e índice al frente
serie: "El ser necesario" # agrupa entradas en una serie
serie_parte: 1
estado: "En desarrollo"   # solo si el texto realmente sigue abierto
```

Las referencias van como notas al pie de kramdown (`[^nombre]`); en escritorio
aparecen en el margen, junto al pasaje. Una anotación al margen es un párrafo
seguido de `{: .anotacion}`. Los collages se generan con `_collage/componer.py`
(ver `_collage/README.md`).
