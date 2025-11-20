---
layout: page
title: Medicina
permalink: /medicina/
---

Aquí encontrarás mis artículos relacionados con medicin.

{% for post in site.posts %}
  {% if post.categories contains "Medicina" %}
  - [{{ post.title }}]({{ post.url }})
  {% endif %}
{% endfor %}
