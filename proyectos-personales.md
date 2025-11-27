---
layout: category
title: Proyectos persolanes
permalink: /proyectos/
category: proyectos
description: Aquí reúno las piezas que no pertenecen a ninguna otra casa: prosa, análisis, ensayos, intuiciones, ejercicios de pensamiento.
Es el cuarto intermedio donde mi mente dialoga consigo misma, sin la obligación de ajustarse a una disciplina específica.

---

{% for post in site.posts %}
  {% if post.categories contains "pyoyectos" %}
  - [{{ post.title }}]({{ post.url }})
  {% endif %}
{% endfor %}
