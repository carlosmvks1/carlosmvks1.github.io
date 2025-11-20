---
layout: category
title: Filosofía
permalink: /filosofia/
category: filosofia
description: Reflexiones, ideas y cuestionamientos sobre pensamiento crítico, filosofía y existencia.

---

{% for post in site.posts %}
  {% if post.categories contains "medicina" %}
  - [{{ post.title }}]({{ post.url }})
  {% endif %}
{% endfor %}
