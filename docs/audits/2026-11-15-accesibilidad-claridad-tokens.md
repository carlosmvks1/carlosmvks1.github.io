# Auditoría: accesibilidad, claridad de elección y design tokens

- **Fecha:** 15 de noviembre de 2026
- **Commit evaluado:** `78a7512b29bb82cb96e6fb89d6129722bc063cbb`. Es el último commit de `main`
  en esa fecha: «Sistema editorial: análisis del corpus y guía de escritura (#4)».
  La rama evaluada fue `claude/vibrant-allen-2fbvpb`, idéntica a `main`.
- **Sitio publicado:** https://carlosmvks1.github.io. Corresponde al mismo commit. Las únicas
  diferencias con el build local son la versión del plugin SEO y la minificación del CSS.
- **Build:** `jekyll build` con Jekyll 3.10.0 (gema `github-pages` 233), sin errores ni avisos.
- **Referencia:** WCAG 2.2, Recomendación del W3C del 12 de diciembre de 2024
  (<https://www.w3.org/TR/WCAG22/>). En 2.2, el criterio 4.1.1 (Parsing) es obsoleto y no se
  evalúa.
- **Estado:** este documento recoge lo que se encontró **antes** de corregir. El resultado de
  las correcciones está en la sección 6.

> **Precisión sobre el lector de pantalla.** Ninguna de las pruebas usó un lector de pantalla:
> el entorno no tenía NVDA, JAWS, VoiceOver ni TalkBack. Cuando este informe habla de nombres,
> roles o estados, describe lo observado en el DOM y en el árbol de accesibilidad de Chromium
> (`ariaSnapshot` de Playwright). **No afirma cómo lo anuncia un lector concreto.** Esa
> comprobación queda pendiente (sección 5).

## 1. Método

### 1.1 Pruebas automáticas

- Herramienta: axe-core 4.10.3, con las etiquetas `wcag2a`, `wcag2aa`, `wcag21a`, `wcag21aa`,
  `wcag22aa` y `best-practice`.
- Alcance: 22 páginas (la home, `/archivo/`, las 4 categorías, `/sobre-mi/`, `/cuaderno/`,
  `/creditos/` y las 13 entradas).
- Anchos: 1440 px y 390 px.
- Navegador: Chromium, con Playwright 1.63.

### 1.2 Pruebas manuales con Playwright y Chromium

- Recorrido completo con Tab en la home, en una entrada, en el archivo y en el menú móvil. En
  cada parada se comprobó que el contorno se viera, que el elemento quedara en la ventana y que
  no lo tapara otro (`elementFromPoint`). Esta prueba se repitió con `reducedMotion: reduce`,
  porque el desplazamiento suave daba falsos «fuera de vista».
- Operación con teclado de:
  - el menú móvil (Enter y Escape);
  - los filtros;
  - el índice;
  - las notas (Enter sobre el botón).
- Las mismas páginas sin JavaScript.
- Redistribución:
  - a 320 × 640 px;
  - a 640 × 400 px, equivalente a un zoom de 200 % sobre 1280 px.
- Espaciado de texto con los valores de 1.4.12: interlineado 1.5, párrafos 2, letras 0.12 y
  palabras 0.16.
- Objetivos: medición de todos los elementos enfocables visibles menores de 24 px.
- `prefers-reduced-motion: reduce`.
- Árbol de accesibilidad con `locator('main').ariaSnapshot()`.

### 1.3 Otras comprobaciones

- **Contraste:** se calculó con la fórmula de luminancia relativa de WCAG para todos los pares
  de tokens.
- **Código:** se leyeron `assets/main.scss`, `_layouts/*`, `_includes/*`,
  `assets/cuaderno.js`, `_collage/componer.py` y el front matter de las entradas. Todo se
  contrastó con `docs/visual-system.md`.

Una puntuación automática no prueba conformidad. Varios hallazgos importantes (A1, A2, A4) solo
aparecieron en la revisión manual.

## 2. Clasificación

- **Incumplimiento comprobado:** se observó en el sitio o en el DOM, y contradice un criterio
  AA o A de WCAG 2.2.
- **Posible incumplimiento:** depende del navegador, del lector o de una interpretación que no
  se pudo confirmar aquí.
- **Problema funcional:** algo no funciona como se espera o como dice la guía, aunque no sea
  un criterio WCAG concreto.
- **Recomendación:** una mejora de buena práctica o de mantenimiento.

## 3. Accesibilidad: hallazgos

| # | Hallazgo | Clasificación | Criterio |
|---|---|---|---|
| A1 | Notas: el regreso al pasaje está roto con JS, el estado del botón es falso en escritorio y la nota está antes del párrafo en el DOM | Problema funcional; posible incumplimiento | 1.3.2, 4.1.2 |
| A2 | Menú móvil: el foco avanza a enlaces tapados por el panel abierto | Incumplimiento comprobado | 2.4.11 |
| A3 | Enlaces de imagen sin nombre accesible | Incumplimiento comprobado | 4.1.2, 2.4.4 |
| A4 | Índice invisible sin JS en escritorio y al ensanchar la ventana | Problema funcional | — |
| B1 | Filtros del archivo: el conteo no cambia, no se anuncian resultados y, sin JS, se ven controles inertes | Problema funcional; recomendación | 4.1.3 (ver nota) |
| B2 | Tablas con desplazamiento horizontal sin elemento enfocable | Posible incumplimiento | 2.1.1 |
| B3 | Dos `collage_alt` omiten las palabras del collage | Recomendación (equivalencia) | 1.1.1 |
| B4a | «Fuentes» se ve como título, pero en el DOM no es un encabezado | Incumplimiento comprobado | 1.3.1 |
| B4b | Saltos de nivel en tres entradas y párrafos en negrita usados como títulos | Recomendación; posible incumplimiento | 1.3.1, 2.4.6 |
| B4c | Home: «Más entradas» sin encabezado y la región «Del archivo» nombrada por el título de la entrada | Recomendación | 1.3.1 |
| C1 | La página y la sección actuales se marcan solo con color (menú móvil e índice) | Incumplimiento comprobado | 1.4.1 |
| C2 | Cifras de «Entrar por tema» sin rótulo | Recomendación | 2.4.4 |
| C3 | `aside` sin nombre (índice y notas) | Recomendación | — |
| C4 | Objetivos menores de 24 px (notas, «↩», tema en la meta) | Cumple por excepciones | 2.5.8 |
| C5 | Desbordamiento con espaciado de texto aumentado a 320 px | Informativo | Más allá del mínimo |

### A1. Notas (`/filosofia/2026/06/20/Mentirnos.html`)

Evidencia en el DOM con JavaScript:

- `cuaderno.js` reemplaza cada `<sup id="fnref:…">` por `<button class="nota-ref">` sin `id`.
- `.footnotes a.reversefootnote` apunta a `#fnref:mezulis` y `#fnref:pronin`, pero
  `document.getElementById` devuelve `null` para ambos. Sin JS, los dos destinos existen.
- Desde el pasaje no queda ningún enlace a la lista de fuentes: el `<a href="#fn:…">`
  desaparece con el reemplazo.
- A 1440 px, el botón tiene `pointer-events: none` pero sigue en el orden de Tab. Al pulsar
  Enter, `aria-expanded` pasa a `true`, aunque la nota estaba visible antes y nada cambia.
- A 1440 px, `aside.nota-margen` se inserta **antes** del bloque que contiene la llamada. El
  orden del DOM pone la referencia antes del pasaje que la cita. A 390 px la inserta después.

### A2. Menú móvil (todas las páginas por debajo de 960 px)

Evidencia a 390 px, en la home:

- Se abrió el menú con Enter sobre `summary` y se avanzó con Tab por los 6 enlaces.
- El siguiente Tab llevó a «Sobre mí» de la portadilla, cuyo rectángulo va de y = 301 a
  y = 320. El panel `nav`, en posición absoluta, ocupa de y = 68 a y = 423, así que el enlace
  enfocado queda tapado por completo. El menú seguía abierto.
- Escape no cierra el `details`.

### A3. Enlaces de imagen sin nombre

- Elemento: `a.entrada-imagen[tabindex="-1"]`. Contiene un `<img alt="">` o una portada
  automática con `aria-hidden`.
- Dónde aparece:
  - la home, en «Más entradas» (3 enlaces);
  - «Para seguir leyendo», en 11 de las 13 entradas.
- Evidencia: axe `link-name` (serio). En el árbol de accesibilidad aparecen como enlaces sin
  nombre. `tabindex="-1"` saca el enlace del orden de Tab, pero no del árbol.
- Inconsistencia relacionada: la protagonista, «Del archivo» y «Para seguir leyendo» ponen el
  `collage_alt` completo en la imagen enlazada. En el árbol de accesibilidad, ese enlace queda
  con un nombre largo y repite el destino del enlace del título.

### A4. Índice (entradas con 3 o más `h2`, a 1440 px)

- Sin JS:
  - `details.toc-movil` queda cerrado y `summary` tiene `display: none`;
  - los enlaces del índice dan `checkVisibility() === false`;
  - no hay manera de abrirlo.
- Con JS:
  - se cargó a 800 px y se ensanchó a 1300 px;
  - el índice quedó cerrado y sin `summary`, porque `toc.open` solo se fija al cargar.
- La sección activa se marca con la clase `.activo`, sin `aria-current`.

### B1. Filtros (`/archivo/`)

- Al pulsar «Medicina», quedan 3 de 13 filas y la entradilla sigue diciendo «13 entradas».
- No hay región `role="status"` ni `aria-live`.
- Nota sobre 4.1.3: no hay un mensaje de estado visible que deba exponerse, así que no se
  registra como incumplimiento de 4.1.3. Lo que falla es que el conteo visible queda
  desactualizado y el cambio de resultados no se comunica.
- Sin JS, `.filtros { display: flex }` anula el atributo `hidden`, y aparecen cinco botones que
  no hacen nada.

### B2. Tablas

- Páginas, a 390 px: `Elecciones` (1 tabla), `narcicismo` (2) y `anamnesis` (1).
- La tabla tiene `display: block; overflow-x: auto` y no contiene elementos enfocables. axe
  marca `scrollable-region-focusable`.
- Chromium reciente hace enfocables los contenedores con desplazamiento; otros navegadores no
  necesariamente. No se pudo probar en Safari ni en Firefox.
- `display: block` sobre `<table>` puede alterar la semántica de tabla en algunos navegadores.
  No se verificó aquí.

### B3. Palabras incorporadas a los collages

| Collage | Palabras en la imagen (`componer.py`) | ¿Están en `collage_alt`? |
|---|---|---|
| `mentira` | «mi versión», «la tuya» | Sí |
| `puente` | «lo que podrías ser», «eso sos» | Sí |
| `reflejo` | «el reflejo» | Sí |
| `brasa` | «brasas que alumbran» | Sí |
| `herida` | «la espera» | **No** |
| `tdah` | «¿cuál primero?» | **No** |

Los rótulos en inglés de la lámina anatómica de `mentira` son incidentales.

### B4. Encabezados y estructura

- **«Fuentes»** se genera con `.footnotes::before`. En el árbol de accesibilidad es texto, no
  encabezado.
- **Secuencias de niveles** (axe `heading-order`):
  - `anamnesis`: empieza con `h3` antes del primer `h2`, y hay `h2 → h4` (5 casos);
  - `Elecciones`: 9 saltos;
  - `SN`: `h2 → h4`.
- **Párrafos en negrita como títulos** en `anamnesis`: «Importancia de la anamnesis clínica»,
  «Descripción y elementos clave».
- **Home:**
  - la sección «Más entradas» tiene `aria-label` pero no encabezado, así que sus `h3` cuelgan
    en el esquema del `h2` de la banda «Del archivo»;
  - esa banda está nombrada (`aria-labelledby`) por el título de la entrada, no por «Del
    archivo».
- **Rol obsoleto:** kramdown marca cada nota con `role="doc-endnote"`, un rol que ARIA ya no
  recomienda. axe lo señala como «menor».

### C1. Estado actual indicado solo por color

- **Menú móvil:** `a[aria-current="page"]` solo pasa de `--marfil-2` a `--marfil`, una
  diferencia de 1.41:1 sin otra señal. En escritorio sí hay subrayado.
- **Índice:** la sección activa solo cambia de color.

### C2 a C5

- **C2:** los nombres en el árbol son «Medicina 3», «Filosofía 7», sin indicar qué se cuenta.
- **C3:**
  - `aside.lectura-indice` envuelve un `nav` con nombre;
  - cada `aside.nota-margen` crea un *complementary* anónimo dentro de `main`.
- **C4:** medidas a 390 px y excepción de 2.5.8 que cubre cada caso:

  | Objetivo | Medida | Excepción |
  |---|---|---|
  | Botón de nota | 21 × 19 px | En línea |
  | «↩» | 16 × 17 px | En línea |
  | Enlace de tema en la meta | 74 × 21 px | Espaciado: sus vecinos no son objetivos |
  | Filtros, menú y botones de tema | 40 px o más | — |

- **C5:** con el espaciado de 1.4.12 a 320 px, desbordan la portadilla (+23 px) y el título de
  `narcicismo` (+10 px). 1.4.12 no exige combinarlo con 320 px.

### Lo que se comprobó y está bien

- **Saltar al contenido:** es la primera parada, se ve al recibir el foco y lleva el foco a
  `<main>`.
- **Foco:** contorno ámbar de 2 px. Tiene 8.9:1 sobre `--noche` y 8.3:1 sobre `--noche-2`.
  En 136 paradas, el foco nunca quedó sin contorno ni tapado con el menú cerrado.
- **Orden y bloqueos:** el orden del foco sigue el visual y no hay trampas de teclado.
- **Contraste de texto:** todos los pares superan 4.5:1.

  | Token sobre `--noche` | Contraste |
  |---|---|
  | `--marfil` | 14.2 |
  | `--marfil-2` | 10.1 |
  | `--gris` | 6.5 |
  | `--terracota` | 5.7 |
  | `--azul` | 8.0 |
  | `--rosa` | 8.5 |
  | `--ambar` | 8.9 |

  El texto `--noche` sobre los colores de tema supera 5.7:1.
- **Estados de los controles:** el filtro activo tiene 14.2:1.
- **Bordes de los controles:** el borde `--linea` mide 1.44:1, pero los controles se
  identifican por su texto, así que 1.4.11 se cumple.
- **Redistribución:** a 320 px no hay desplazamiento horizontal (las tablas se desplazan dentro
  de su marco), y a 640 px tampoco.
- **Espaciado de texto:** a 1440 px no se pierde contenido.
- **Movimiento reducido:** la transición dura 0 s y el desplazamiento es `auto`.
- **Imágenes decorativas:** marcas de tema y portadas automáticas con `aria-hidden`.
- **Enlaces en el texto:** los de `.prose` se distinguen con subrayado.
- **Idioma y títulos:** `lang="es"` y un `<title>` único por página.

## 4. Claridad de elección (ley de Hick como heurística)

**O** = observado en la interfaz; **H** = hipótesis que requeriría pruebas con lectores.

### 4.1 Encontrar una primera lectura

- **O:** en escritorio hay 15 enlaces antes de la protagonista. Los temas, el archivo y
  «Sobre mí» aparecen en la cabecera y otra vez en la portadilla.
- **O:** la única propuesta es «Última entrada». Siete entradas tienen `featured: true`, pero
  ninguna plantilla lo usa.
- **H:** la entrada más reciente no tiene por qué ser la mejor primera lectura.

### 4.2 Explorar un tema

- **O:** hay cuatro accesos por tema en la home.
- **O:** el mismo concepto tiene tres nombres: «tema», «Entrar por tema» y «Cuatro líneas de
  trabajo».
- **H:** «Proyectos» puede no anticipar la prosa poética.

### 4.3 Buscar una entrada anterior

- **O:** el archivo está a un clic, agrupado por año y con filtros.
- **O:** no muestra descripciones, y el filtro no queda en la URL.

### 4.4 Seguir una serie

- **O:** en la parte 1 de «El ser necesario» compiten tres continuaciones:
  - la lista de la serie, que lleva a la parte 2;
  - «Para seguir leyendo», con la parte 2 en tercer lugar;
  - «Siguiente», que sigue el orden cronológico y lleva a otra entrada.
- **O:** el aviso «Parte 1 de la serie» no es un enlace.

### 4.5 Consultar una fuente y regresar al pasaje

- **O:** las notas al margen en escritorio y desplegables en móvil están bien pensadas, pero
  el regreso está roto (A1).
- **O:** solo 1 de las 13 entradas usa notas al pie.

## 5. Design tokens

### 5.1 Inventario

- **Hay tokens solo para:** color (13 de paleta más `--tema`), dos familias tipográficas y
  `--ancho`, `--gutter` y `--lectura`.
- **No hay tokens para:** espaciado, tamaños de letra, bordes, radios, sombras, capas,
  movimiento ni puntos de corte.

### 5.2 Hallazgos

1. **Tokens sin usar:** `--noche-3` y `--cal` aparecen documentados pero el CSS no los usa.
2. **Colores fuera del sistema:**
   - `#f6efe2` en `.prose strong`;
   - `rgba(244, 236, 220, .03/.08)`;
   - `rgba(0,0,0,.45)`.
3. **`--ambar` cumple cuatro funciones:**
   - color de Fe;
   - foco;
   - acento de marca;
   - borde de las anotaciones.

   Cambiar el color de Fe cambiaría el foco.
4. **El rótulo en versalitas está implementado siete veces**, con tamaños de 0.7 a 0.8rem y
   espaciado de 0.12 o 0.14em.
5. **39 tamaños de letra distintos.** Los `clamp()` de títulos son composición deliberada.
6. **Barras de tema de 2, 3 y 4 px**, sin regla.
7. **Dos radios orgánicos casi idénticos:** `50% 46% 52% 48%` y `50% 47% 52% 49%`.
8. **Dos sombras de papel distintas en CSS:** 5 × 7 y 4 × 6 px. Ninguna coincide con la de los
   collages (§3.3 de la guía).
9. **Hover inconsistente** entre componentes equivalentes.
10. **Los datos de los temas están repetidos en seis lugares:**
    - `cat-name.html`;
    - `cat-url.html`;
    - `nav-links.html`;
    - tres listas literales `"medicina,filosofia,fe,proyectos"`;
    - además, `.tema--x` y `.tema-fondo--x` repiten el mismo mapa de colores.
11. **Los puntos de corte están escritos a mano** en 18 `@media`.
12. **Capas y movimiento:** pocos valores; basta con documentarlos.

### 5.3 La guía frente al código

| Afirmación de `docs/visual-system.md` | Estado |
|---|---|
| `--noche-3` «superficies elevadas» | Falso: no se usa |
| Kicker «0.78rem, 0.14em» | Parcial: hay cinco variantes |
| Índice «con más de tres secciones» | Falso: aparece con 3 o más `h2` |
| «Sin JavaScript, el índice se abre a mano» | Falso en ≥ 1100 px |
| «Al final siguen las notas completas» | Cierto, pero el regreso está roto con JS |
| Contrastes de la tabla 5.1 | Correctos; falta `--marfil-2` (10.1:1) |

## 6. Limitaciones y pendientes de esta auditoría

- **Lector de pantalla:** sin probar. Pendientes: NVDA con Firefox, VoiceOver con Safari en
  macOS e iOS, y TalkBack con Chrome en Android.
- **Navegadores:** solo Chromium. Faltan Safari y Firefox.
- **Dispositivos y zoom:** sin dispositivos táctiles reales; el zoom se simuló por ancho de
  ventana.
- **Modos de color:** no se evaluaron alto contraste (`forced-colors`) ni modo claro.
- **Revisión manual de las entradas:** completa en 4 de las 13 (Mentirnos, SN, Trinidad y
  anamnesis). axe se corrió en las 13.
- **Fuera de alcance:** la comprensibilidad del lenguaje y las imágenes de texto (1.4.5): las
  palabras de los collages se consideraron parte de la obra.

## 7. Correcciones posteriores

El resultado de cada hallazgo después de corregirlo está en
[`2026-11-15-verificacion.md`](2026-11-15-verificacion.md).
