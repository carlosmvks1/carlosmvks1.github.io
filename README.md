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
