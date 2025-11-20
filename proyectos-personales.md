---
layout: page
title: Proyectos personales
permalink: /proyectos-personales/
description: Aquí documento mis proyectos a largo plazo: blog, estudios, entrenamiento, escritura, cuaderno de observaciones, y más.

---

{% for post in site.posts %}
  {% if post.categories contains "Proyectos_personales" %}
  - [{{ post.title }}]({{ post.url }})
  {% endif %}
{% endfor %}
