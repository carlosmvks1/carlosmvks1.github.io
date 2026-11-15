# Sistema visual de El cuaderno

Guía detallada de la identidad «Revista nocturna» tal como está implementada.
Las reglas breves y obligatorias están en [`AGENTS.md`](../AGENTS.md). Este
documento explica el porqué y el cómo. Si algo aquí contradice el código, manda
el código: corregí este documento en el mismo cambio.

Estado: vigente desde noviembre de 2026. Las secciones marcadas **Pendiente**
o **Idea futura** no están aprobadas y no deben tratarse como reglas.

---

## 1. Dirección

- **Collage editorial como protagonista.** Cada entrada importante abre con
  una composición hecha a partir de fotografías, láminas o grabados. No se
  trata de ilustraciones decorativas.
- **Atmósfera nocturna, íntima, curiosa y expresiva.** Las superficies son de
  carbón con matiz azul, el texto es marfil y los acentos tienen la luz de una
  ciudad de noche (ladrillo, interior encendido, zócalo deslavado).
- **Raíces hondureñas, sin limitarse a Tegucigalpa.** La identidad sale de una
  mirada personal sobre lugares reales de Honduras: calles, plazas, iglesias,
  ríos, laderas, materiales. Tegucigalpa está presente, pero también otros
  lugares del país. No hace falta que Honduras aparezca literalmente en cada
  página: puede estar en la paleta, los materiales y algunos fragmentos.
- **Sin clichés.** No se usan banderas, mapas, las cinco estrellas, souvenirs
  ni acumulaciones de símbolos nacionales. Tampoco patrones indígenas como
  decoración genérica, ni imágenes que reduzcan el país a deterioro o
  nostalgia. Una imagen de una ciudad genérica, o una generada, nunca se
  presenta como si documentara un lugar hondureño.
- **Qué evitar en la atmósfera:** una biblioteca europea antigua, el lujo con
  dorados y la interfaz tecnológica con neón.

## 2. Carácter

Riqueza visual, presencia editorial y personalidad. **No simplificar hacia el
minimalismo** por preferencia del agente: no quitar collages, texturas,
etiquetas, color por tema ni contrastes de escala para que el sitio «se vea
más limpio». La lectura se protege de otra manera: el cuerpo de texto va sobre
una superficie estable y sin textura, con buen contraste, y la riqueza visual
se concentra en aperturas, portadas y la home.

---

## 3. Sistema de collage (reglas vigentes)

Implementado en [`_collage/componer.py`](../_collage/componer.py). Las mismas
funciones sirven para todos los collages; no dupliques lógica.

### 3.1 Tratamiento fotográfico

| Tipo de imagen | Tratamiento | Función |
|---|---|---|
| Fotografía de lugar, de día | Duotono tinta `#181c24` → cal `#e9e1cf` (o cal tibia `#f0d6a8`), contraste 1.15–1.35 | `duotone()` |
| Fotografía nocturna | Conserva su color, calentada (rojo ×1.05–1.15, azul ×0.92, contraste ×1.1) | `night()` |
| Láminas, grabados de archivo | Tinta sobre papel de cal | `ink()` |
| Detalle ampliado (lupa, espejo, foco) | Duotono dentro de un círculo, con aro de color opcional | `circle_window()` + `disc()` |

### 3.2 Paleta de los collages

Valores RGB exactos del diccionario `C` en `componer.py`:

| Nombre | RGB | Hex | Uso |
|---|---|---|---|
| noche | 19, 23, 30 | `#13171e` | Fondo de todo collage |
| tinta | 24, 28, 36 | `#181c24` | Sombras del duotono, texto de etiquetas |
| cal | 233, 225, 207 | `#e9e1cf` | Luces del duotono, papel de etiquetas |
| cal_tibia | 240, 214, 168 | `#f0d6a8` | Variante cálida del duotono |
| terracota | 196, 98, 62 | `#c4623e` | Color plano |
| ambar | 226, 163, 59 | `#e2a33b` | Color plano |
| azul | 122, 151, 173 | `#7a97ad` | Color plano |
| rosa | 214, 139, 138 | `#d68b8a` | Color plano |

Los colores planos de los collages son algo más profundos que los tokens CSS
del mismo nombre (sección 5), porque van impresos sobre papel y foto, no como
texto.

### 3.3 Reglas de composición

1. Fondo de noche con grano (`background()`, grano 14).
2. **Máximo dos colores planos por pieza.** Se usan para tapar, sustituir,
   unir o señalar algo del argumento, no para decorar.
3. **Cortes rectos; como mucho un borde rasgado por pieza** (`piece(torn=…)`).
4. **Sombra corta y dura:** desplazamiento de 5 × 7 px, desenfoque de 3 px y
   60 % de opacidad (`paste()`).
5. **Rotaciones de 3 grados o menos.**
6. **Como mucho una palabra o frase del texto**, recortada en papel cal con
   Fraunces cursiva (`label()`). En algunas piezas son dos rótulos que se
   responden («mi versión» / «la tuya», «lo que podrías ser» / «eso sos»).
7. Grano final de 7 sobre toda la composición (`save()`).
8. Aire alrededor del recorte: la composición no llena el lienzo de bordes a
   bordes.

### 3.4 Recursos opcionales

Los **círculos** (discos, lupas, espejos), las **etiquetas** y los
**grabados o láminas** son recursos disponibles, **no obligatorios**. No deben
aparecer en todas las piezas. Una pieza puede ser solo una foto en duotono con
tiras de color. Hoy: «Amar la herida» usa disco y etiqueta, «Lo que repetís»
usa tiras y dos etiquetas sin círculo, y en los fragmentos automáticos no hay
etiquetas.

### 3.5 Formatos

Cada collage se compone **tres veces**; el formato móvil es una recomposición,
no un recorte:

| Sufijo | Proporción | Tamaño | Uso | Anchos menores (srcset) |
|---|---|---|---|---|
| `-v` | 4:5 | 1200 × 1500 | Apertura y protagonista en escritorio (≥ 860 px) | 800 |
| `-m` | 1:1 | 1000 × 1000 | Apertura y protagonista en móvil (menos piezas, más grandes) | 800, 640 |
| `-h` | 3:2 | 1200 × 800 | Tarjetas y listas | 800, 480 |

Los fragmentos miden como máximo 900 px y tienen anchos de 640 y 480.

### 3.6 Collages actuales

| Collage | Entrada | Idea | Fuentes |
|---|---|---|---|
| `mentira` | La mentira que no se siente como mentira | Punto ciego: fachada partida en dos versiones; lámina del ojo con el punto ciego tapado por un disco de terracota | Wikimedia (casa, ojo) |
| `herida` | Amar la herida | Busto de Platón partido y unido con cintas de ámbar; **disco rosa**; ladera de El Picacho al anochecer | Wikimedia (platon, picacho) |
| `tdah` | Explorando el TDAH desde dentro | Atención en competencia: focos circulares sobre una escalinata; uno vacío en terracota | Wikimedia (escalinata) |
| `puente` | Lo que repetís, eso sos | «El hábito es el puente…»: vado sobre un río crecido en duotono; tiras ámbar repetidas sobre la losa | Foto propia (vado) |
| `reflejo` | Narcisismo y TNP | «Un reflejo que cambia…»: busto de plaza de noche (color); espejo con aro azul que muestra el rostro invertido | Foto propia (busto-plaza) |
| `brasa` | Fuego que no debe tocar nada | «Brasas que alumbran pero no queman»: luna entre ramas (color nocturno), hilo ámbar y disco terracota medio tapado | Foto propia (luna) |

---

## 4. Fotografías propias

- **Se priorizan cuando aportan al texto.** Si una foto de Carlos encaja con
  el contenido y la composición, va antes que un recurso externo.
- **Se pueden combinar** con láminas, grabados y fotografías externas de
  licencia verificada.
- **No forzar asociaciones.** Si la relación entre la foto y el texto necesita
  una explicación rebuscada, no se usa. Una entrada puede quedar con portada
  automática.
- **No sustituir imágenes que funcionan.** Los collages existentes no se
  rehacen solo para usar fotos propias.
- **No atribuir lugares sin evidencia.** Solo se nombra un lugar cuando la
  propia imagen lo prueba (un rótulo, por ejemplo). Hoy el único atribuido
  es La Campa, por el letrero pintado en el cerro, que el recorte del
  fragmento `crucifijo` no incluye.
- **Personas.** No se publican personas reconocibles sin decisión expresa de
  Carlos. Las tomas con personas al fondo se descartan o se recortan.
- **Excluidas:** capturas de pantalla, documentos personales, imágenes
  clínicas o íntimas, y obra de terceros (murales, marcas visibles).

### 4.1 Decisiones aprobadas por Carlos

- Conservar el collage de «Amar la herida» tal como está, **incluidos el busto
  y el disco rosa**.
- **Excluir las fotos del bolsillo y del microscopio.** No se incorporan al
  sitio ni al repositorio.
- Se pueden usar y publicar las fotografías de la carpeta «fotos blog» cuando
  encajen con el contenido y la composición. Esto incluye subir al
  repositorio los derivados que el blog necesite, sin metadatos privados.
- Los originales de Drive no se borran ni se modifican.

### 4.2 Uso actual de fotos propias

| Derivado (`_collage/fuentes/propias/`) | Dónde se usa | Tratamiento |
|---|---|---|
| `vado.jpg` | Collage `puente` | Duotono |
| `busto-plaza.jpg` | Collage `reflejo` | Nocturno; el rostro en duotono cal tibia dentro del espejo |
| `luna.jpg` | Collage `brasa` | Nocturno |
| `iglesia.jpg` | Fragmento fijo de «Si Dios permanece, el amor aparece» («Dios es luz») | Nocturno |
| `crucifijo.jpg` | Fragmento fijo de «La lección que Romanos 1–3…» | Duotono |
| `curva.jpg` | Fragmento fijo de «Lo que Honduras decide en 2025» («futuros posibles») | Nocturno |
| `isla.jpg` | Fragmento fijo de «El fundamento o el abismo» | Duotono |
| `guerrero.jpg` | Rotación general de portadas automáticas | Nocturno |

---

## 5. Diseño implementado

Todo el CSS está en [`assets/main.scss`](../assets/main.scss), en este orden:
tokens, base, cabecera, portada, inicio, artículo, archivo, pie, utilidades y
movimiento. El JavaScript está en [`assets/cuaderno.js`](../assets/cuaderno.js)
y solo hace mejora progresiva: sin él, todo se puede leer y usar (sección 6).

### 5.1 Tokens (`:root`)

Hay dos capas de color, pequeñas a propósito:

1. **Paleta**: los colores de identidad, con nombres de material. Solo se usan
   dentro de `:root`, para definir funciones y temas.
2. **Funciones**: lo que usan los componentes. Varias comparten valor
   (`--color-foco`, `--color-acento` y `--tema-fe` son ámbar), pero se pueden
   cambiar por separado: cambiar el color de Fe no cambia el foco.

**Paleta**

| Token | Valor | Contraste sobre `--noche` |
|---|---|---|
| `--noche` | `#13171e` | — |
| `--noche-2` | `#191e27` | — |
| `--linea` | `#2d3442` | 1.44:1 (solo filetes) |
| `--linea-suave` | `#232a36` | 1.25:1 (solo filetes) |
| `--marfil` | `#ece4d4` | 14.2:1 |
| `--marfil-2` | `#c9c1b1` | 10.1:1 |
| `--marfil-claro` | `#f6efe2` | 15.7:1 |
| `--gris` | `#a29b8d` | 6.5:1 |
| `--terracota` | `#d9774f` | 5.7:1 |
| `--ambar` | `#e6ad4a` | 8.9:1 |
| `--azul` | `#93b1c7` | 8.0:1 |
| `--rosa` | `#e2a3a0` | 8.5:1 |

Sobre `--noche-2`, todos los colores de texto siguen por encima de 5.3:1. El
texto `--noche` sobre cualquier color de tema supera 5.7:1. `--cal` (papel) y
los colores planos de los collages viven en `componer.py` (sección 3.2), no en
el CSS.

**Funciones**

| Token | Valor actual | Uso |
|---|---|---|
| `--color-fondo` | `--noche` | Fondo general, banda bajo títulos montados |
| `--color-superficie` | `--noche-2` | Bandas, menú móvil, notas, pie, portadas automáticas |
| `--color-filete` / `--color-filete-suave` | `--linea` / `--linea-suave` | Filetes y bordes de controles |
| `--color-texto` | `--marfil` | Texto principal |
| `--color-texto-2` | `--marfil-2` | Texto secundario, entradillas |
| `--color-texto-3` | `--gris` | Metadatos, rótulos neutros |
| `--color-texto-fuerte` | `--marfil-claro` | `<strong>` en el cuerpo |
| `--color-sobre-acento` | `--noche` | Texto sobre fondos de color o marfil |
| `--color-control-activo` | `--marfil` | Filtro activo, menú abierto |
| `--color-foco` | `--ambar` | Contorno de foco, «Saltar al contenido» |
| `--color-acento` | `--ambar` | Marca: «El», cursivas de la portadilla, años del archivo, subrayado de página actual |
| `--color-anotacion` | `--ambar` | Filete y énfasis de las anotaciones del autor |
| `--color-seleccion` | `--terracota` | Selección de texto |
| `--velo` / `--velo-hover` | marfil al 3 % / 8 % | Fondo de los botones de «Entrar por tema» |
| `--tema-{clave}` | Desde `_data/temas.yml` | Color de cada tema |
| `--tema` | `--tema-{clave}` o `--color-acento` | Acento del contexto actual |

**Otras familias**

| Grupo | Tokens |
|---|---|
| Tipografía | `--fuente-display` (Fraunces), `--fuente-texto` (Public Sans), `--t-rotulo` 0.78rem, `--t-rotulo-chico` 0.72rem, `--rotulo-espaciado` 0.14em, `--t-dato` 0.8rem, `--t-ui` 0.92rem, `--t-apoyo` 0.98rem |
| Medidas | `--ancho` 1240px, `--gutter` 16px (32px desde 760 px), `--lectura` 40rem |
| Ritmo de secciones | `--seccion-corta` 3.5rem, `--seccion` 4rem, `--seccion-larga` 5rem |
| Bordes | `--filete` y `--filete-suave` (1px sólido), `--barra` 4px (bloques y cabeceras de tema, serie), `--barra-media` 3px (subrayado del título protagonista al pasar), `--barra-fina` 2px (citas, cita de portada, anotaciones, notas, subrayado actual) |
| Radios | `--radio-pastilla` 99px, `--radio-disco` (disco recortado a mano) |
| Sombras | `--sombra-papel` 5×7 px, `--sombra-papel-corta` 4×6 px (forma de la portada automática), ambas sin desenfoque al 45 % |
| Capas | `--capa-montaje` 2 (título sobre collage), `--capa-cabecera` 5, `--capa-salto` 10 |
| Puntos de corte (Sass) | `$bp-columnas` 700, `$bp-margen` 760, `$bp-diseno` 860, `$bp-nav` 960, `$bp-lectura` 1100 |

**Criterio:** un valor se vuelve token cuando expresa un rol que se repite. Se
quedan escritos a mano, a propósito:

- los `clamp()` de títulos;
- el montaje del título sobre el collage;
- los porcentajes y la rotación de las portadas automáticas;
- la inclinación de 1.2° de la banda «Del archivo»;
- la miniatura de 7,5 rem de las recientes en móvil.

Son composición, no sistema. El movimiento (una transición de 0.4 s, solo con
`prefers-reduced-motion: no-preference`) tampoco necesita token.

**Temas.** La fuente única es [`_data/temas.yml`](../_data/temas.yml), con
`clave`, `nombre`, `url` y `color` (un token de la paleta). De ahí salen:

- la navegación (`nav-links.html`);
- `cat-name.html` y `cat-url.html`;
- los bloques de la home y los filtros del archivo;
- el CSS: `--tema-{clave}` y la regla `.tema--{clave}, .tema-fondo--{clave}`,
  que Liquid genera en `main.scss`.

La descripción de cada tema sigue en el front matter de su página
(`medicina.md`, etc.). Cada tema tiene además una **marca** SVG en
`_includes/category-mark.html`:

- medicina: pulso en círculo;
- filosofía: tres nodos;
- fe: cruz con arco;
- proyectos: dos bloques;
- el cuaderno, por defecto: una hoja.

**Rótulo editorial.** Las versalitas espaciadas en Public Sans se escriben
con el mixin `rotulo` de `main.scss`. Hay dos tamaños: el normal (eyebrows,
kickers, «Anterior por fecha», «Siguiente parte de la serie») y el chico
(«Entrar por tema», «En este texto», «Anotación»). El color es gris, salvo en
el kicker de tema, que usa `--tema`. El numeral de sección de los `h2`
(«01») no es un rótulo y se mantiene aparte.

### 5.2 Tipografía

- **Fraunces** (`--display`): títulos, entradillas en cursiva, anotaciones y
  etiquetas de los collages. Es variable, con eje óptico (opsz 9–144) y pesos
  de 400 a 700.
- **Public Sans** (`--texto`): texto, navegación y metadatos. Pesos de 400
  a 700.
- Se cargan desde Google Fonts con `display=swap`. Para los collages hay
  copias locales en `_collage/fonts/`. Las dos fuentes están bajo la SIL Open
  Font License.
- No se agregan otras familias.

Escala:

| Elemento | Tamaño |
|---|---|
| Título de artículo | `clamp(2.3rem, 8vw, 5.2rem)`, interlínea 0.98, `max-width: 14ch` |
| Título de la protagonista en la home | `clamp(2.2rem, 7.5vw, 5.4rem)` |
| Titular de la portadilla | `clamp(1.6rem, 4.2vw, 2.6rem)`, con la cursiva en ámbar |
| Entradilla (`.deck`) | Fraunces cursiva, `clamp(1.15rem, 2.4vw, 1.4rem)` en la apertura |
| Cuerpo (`.prose`) | 1.125rem (1.1875rem desde 760 px), interlínea 1.72, medida de 40rem |
| Rótulo (eyebrow, kicker) | `--t-rotulo` 0.78rem o `--t-rotulo-chico` 0.72rem, versalitas, peso 600, espaciado 0.14em |

### 5.3 Jerarquía de la home (`_layouts/home.html`)

La home alterna intensidades: **un solo foco fuerte** (la protagonista), un
grupo medio, un tramo tranquilo y un cierre medio. Ninguna sección compite en
escala con la protagonista. El análisis está en
`docs/audits/2026-11-15-portada.md`.

1. **Portadilla (baja):** quién escribe, con una frase y «Sobre mí».
   - Por debajo de 960 px, donde la cabecera pliega los temas en «Menú»,
     suma «Entrar por tema»: una línea de enlaces con su marca, sin cajas ni
     conteos, de 44 px de alto.
   - En escritorio no se muestra, porque la cabecera ya tiene esos enlaces.
2. **Protagonista (alta):** la entrada más reciente.
   - Lleva el título grande montado sobre el collage `-v`/`-m`, la
     entradilla y «Leer la entrada».
   - La `cita` opcional es una voz secundaria: filete lateral fino de
     `--barra-fina` y 1,12 rem en `--color-texto-2`.
3. **También en el cuaderno (media):** las tres entradas siguientes, en tres
   columnas iguales con imagen `-h`, alineadas y sin escalonar.
   - Por debajo de 700 px, la imagen pasa a miniatura de 7,5 rem junto al
     texto, y la meta muestra solo el tema y la fecha.
4. **Los cuatro temas (baja):** un bloque por tema con su marca, nombre,
   cuenta y descripción. Es la pausa entre composiciones y la bisagra para
   explorar un tema.
5. **Del archivo (media):** una banda de otra superficie, al final.
   - Muestra la entrada **más antigua** que tenga collage, sin contar la
     protagonista.
   - El título llega como máximo a 2,4 rem y el collage ocupa 5 de 12
     columnas, para que no parezca un segundo inicio.
   - La región se nombra con su kicker.

Las entradas que no entran en la home están en el archivo y en las páginas de
tema.

**Accesos a los temas.** Cada uno cumple una función distinta, y todos usan el
mismo término, «tema»:

- la cabecera es la navegación global de todas las páginas, y en móvil está
  plegada en «Menú»;
- «Entrar por tema» solo aparece en móvil, como puerta visible en la primera
  pantalla;
- «Los cuatro temas» explica cada tema con su descripción y su cuenta;
- el enlace de tema en la meta da contexto a cada entrada.

No se agregan conteos ni «última entrada» repetidos. Los títulos ya están
en la página.

**Imágenes de las tarjetas.** El enlace de la imagen tiene `tabindex="-1"` y
`aria-hidden="true"`, y la imagen tiene `alt=""`: con el ratón se puede hacer
clic en la imagen, y con teclado o tecnologías de apoyo hay un solo enlace
(el título). El `collage_alt` se reserva para la apertura del artículo, donde
el collage es contenido.

**Pendiente (decisión de Carlos):** siete entradas tienen `featured: true`,
pero ninguna plantilla lo usa. No está decidido si la home debe sugerir una
primera lectura ni cuál. La banda «Del archivo» sigue mostrando la entrada más
antigua con collage (sección 11).

### 5.4 Aperturas de artículos (`_layouts/post.html`)

| Tipo | Cuándo | Composición |
|---|---|---|
| `literaria` | Entradas con `collage` (por defecto) | Desde 860 px: rejilla de 12 columnas, texto en las columnas 1 a 7 e imagen en las 7 a 12. El título, sobre una banda de noche, se monta sobre el collage |
| `guia` | `apertura: guia` (textos médicos largos; hoy TDAH y Narcisismo) | Columnas 7fr/4fr, imagen más pequeña y título más contenido (`max-width: 18ch`) |
| `sencilla` | Entradas sin `collage` | Solo texto. La portada automática se usa en listas, no en la apertura |

En móvil, la apertura queda en una sola columna: primero el texto y debajo el
collage `-m`, a sangre.

### 5.5 Portadas automáticas

Las genera `_includes/cover.html` cuando una entrada no tiene `collage`:

- Fondo `--noche-2`, un fragmento de foto y una forma plana con el color del
  tema. Lleva la marca del tema en negro noche.
- Hay dos composiciones. La A pone el fragmento a la izquierda y un disco
  abajo a la derecha. La B pone el fragmento a la derecha y una banda recta e
  inclinada (−1.5°) abajo a la izquierda.
- La composición y el fragmento salen de la fecha (días desde 1970). Así, dos
  entradas cercanas no se repiten.
- Rotación general: `grabado, calle, casa, escalinata, guerrero`.
- Una entrada puede **fijar su fragmento** con `fragmento: nombre` cuando hay
  uno que de verdad le corresponde (sección 4.2).

### 5.6 Variantes móviles

- Cortes en 700, 760, 860, 960 y 1100 px. El cambio de diseño principal está
  en 860 px.
- El menú móvil es un `<details>`; el de escritorio, una navegación en línea.
- Las imágenes protagonistas usan `-m` (1:1) por debajo de 860 px y `-v`
  (4:5) por encima, con `<picture>` y `srcset`.
- Con 390 px de ancho no debe aparecer desbordamiento horizontal.

---

## 6. Lectura y navegación

Comportamiento comprobado en la auditoría del 15 de noviembre de 2026
([`docs/audits/`](audits/)).

- **Menú móvil:** es un `<details>`.
  - Se abre con Enter o Espacio sobre «Menú».
  - Se cierra con Escape, y el foco vuelve a «Menú».
  - También se cierra cuando el foco sale del menú y al tocar fuera. Así, el
    foco nunca avanza detrás del panel.
  - La página actual lleva `aria-current="page"` y un subrayado ámbar, igual
    que en escritorio.
- **Índice:** `_includes/toc.html` lo arma con los `h2` cuando hay **3 o más**.
  - El `<details>` sale abierto en el HTML, así que sin JavaScript se ve
    siempre.
  - `cuaderno.js` lo pliega por debajo de 1100 px y lo vuelve a abrir al pasar
    a escritorio. En escritorio, el `summary` se oculta solo cuando está
    abierto.
  - La sección actual lleva `aria-current="location"`, más color y subrayado.
- **Notas y referencias:** se escriben como notas al pie de Markdown
  (`[^id]`).
  - La llamada `<sup id="fnref:…">` se conserva siempre. Es el destino de «↩»
    («Volver al pasaje de la fuente N»).
  - **Escritorio (≥ 1100 px):** el número es un enlace a «Fuentes». Al margen
    aparece una copia visual de la nota, con `aria-hidden` y sus enlaces
    fuera del orden de Tab, para no duplicar la lectura.
  - **Móvil:** el número es un botón («Fuente N», con `aria-expanded`) que
    despliega la nota bajo el párrafo. Su área táctil mide 24 × 24 px sin
    cambiar el tamaño visual.
  - **Sin JavaScript:** el enlace y «↩» funcionan igual.
  - «Fuentes» es un `<h2>` real que agrega `post.html`. La misma plantilla
    quita el rol obsoleto `doc-endnote` y pasa `doc-noteref` del `<sup>` al
    enlace.
- **Tablas:**
  - Sin JavaScript, se desplazan dentro de su propio marco.
  - Con JavaScript, `cuaderno.js` las envuelve en `.tabla-marco`. Cuando
    desbordan, el marco recibe el foco (`tabindex="0"`), `role="region"` y un
    nombre («Tabla N: título de la sección»), y se desplaza con las flechas.
  - La tabla conserva `display: table`.
- **Anotaciones del autor:** un párrafo con `{: .anotacion}`, en cursiva y con
  un filete del color de anotación.
- **Archivo** (`/archivo/`): agrupado por año, con filtros de tema (botones
  con `aria-pressed`).
  - Al filtrar, la entradilla visible pasa a «3 de 13 entradas · Medicina…».
  - Una región `role="status"` anuncia el resultado.
  - Sin JavaScript, los filtros no se muestran.
- **Categorías:**
  - `/medicina/`, `/filosofia/`, `/fe_y_etica/` y `/proyectos/`, con la marca
    y la descripción de cada tema;
  - las entradas usan `categories: [medicina|filosofia|fe|proyectos]`
    (claves de `_data/temas.yml`).
- **Pie del artículo.** Tiene tres continuaciones distintas, en este orden:
  1. **Serie** (`serie` y `serie_parte`):
     - bloque con «Serie: nombre · parte N de M»;
     - si existe, «Siguiente parte de la serie» destacada;
     - la lista completa de partes.

     El aviso bajo la entradilla («Parte N de M de la serie…») enlaza a ese
     bloque.
  2. **Lecturas relacionadas · Tema:** hasta tres entradas del mismo tema,
     sin repetir las de la serie.
  3. **Entradas vecinas por fecha:** «Anterior por fecha» y «Siguiente por
     fecha».
- **Encabezados:** `h1` es el título. Las secciones son `h2` (numeradas y en
  el índice), y los niveles no se saltan. Los párrafos en negrita que hacen de
  título no se convierten sin decisión de Carlos.
- **Foco:** `:focus-visible` con un contorno de 2 px en `--color-foco`,
  desplazado 3 px. Hay un enlace para saltar al contenido.
- **Contraste:** todo el texto debe pasar 4.5:1 sobre su fondo (tabla 5.1). El
  desplazamiento suave solo se activa con
  `prefers-reduced-motion: no-preference`.
- **Texto alternativo:** cada `collage` lleva su `collage_alt`, que describe
  lo que se ve **e incluye las palabras recortadas en papel**. Las portadas
  automáticas son decorativas (`aria-hidden`).
- **Utilidad `.solo-lectores`:** texto disponible para lectores de pantalla y
  oculto en pantalla. Por ejemplo, «entradas» junto a las cifras de «Entrar
  por tema».

## 7. Producción de imágenes

### 7.1 Ubicación

| Ruta | Qué contiene | ¿Se publica? |
|---|---|---|
| `_collage/fuentes/*.jpg` | Fuentes externas (Wikimedia) | No: Jekyll ignora `_collage`, aunque el repositorio es público |
| `_collage/fuentes/propias/*.jpg` | Derivados recortados de fotos propias, sin metadatos | Igual que la fila anterior |
| `_collage/fonts/` | Fuentes tipográficas para las etiquetas | No |
| `assets/collage/*.webp` | Collages finales en tres formatos y sus anchos | Sí |
| `assets/collage/fragmentos/*.webp` | Fragmentos de las portadas automáticas | Sí |

**Los originales de las fotos propias nunca entran al repositorio.** Viven en
la carpeta privada «fotos blog» de Carlos en Google Drive.

### 7.2 Scripts

```bash
# 1. Derivados de fotos propias (solo cuando cambian las fotos o sus recortes).
#    Requiere una copia local de los originales, cada uno nombrado <ID de Drive>.jpg.
python3 _collage/preparar_propias.py /ruta/a/copias

# 2. Collages
python3 _collage/componer.py                 # todos
python3 _collage/componer.py puente          # uno
python3 _collage/componer.py fragmentos_propios
python3 _collage/componer.py tamanos         # solo rehace los anchos menores
```

Requisitos: Python 3 y Pillow.

Regenerar un collage existente vuelve a sortear el grano. Por eso, regenerá
solo los que cambiaste, para que el diff no se llene de binarios.

### 7.3 Formato y optimización

- Salida en WebP. Los collages van a calidad 78 y los anchos menores, a 74.
  Los fragmentos van a calidad 72. Siempre con `method=6`.
- Los derivados de fotos propias se guardan en JPEG de calidad 86, con un
  lado largo de 1200 a 1800 px.
- **Referencia de peso:** `-v` cerca de 350–500 KB, `-h-480` por debajo de
  25 KB y fragmentos por debajo de 200 KB.

### 7.4 Metadatos

`preparar_propias.py` copia los píxeles en una imagen nueva. Así no se
heredan EXIF (cámara, fecha), GPS, XMP ni perfil ICC, y la orientación queda
aplicada. Los WebP de `componer.py` también salen sin EXIF. Comprobación:

```bash
python3 -c "
from PIL import Image; import glob, sys
bad = [f for f in glob.glob('_collage/fuentes/propias/*') + glob.glob('assets/collage/**/*.webp', recursive=True)
       if dict(Image.open(f).getexif()) or {'exif', 'xmp', 'icc_profile'} & set(Image.open(f).info)]
print(bad or 'sin metadatos'); sys.exit(bool(bad))"
```

### 7.5 Procedencia y licencias

- Cada fuente se registra en la tabla de [`_collage/README.md`](../_collage/README.md)
  (archivo, obra, autor, licencia, uso) y en [`creditos.md`](../creditos.md),
  que se publica en `/creditos/`.
- **Fuentes externas:** solo dominio público o licencias libres verificadas
  en la página de origen, con la fecha de la verificación. Los collages que
  derivan de obras CC BY-SA se publican bajo CC BY-SA 4.0.
- **Fotos propias:** fotografías de Carlos Reyes, publicadas con su
  autorización. Hoy no tienen licencia abierta declarada (ver Pendientes).
- **Las referencias de diseño (sección 9) no autorizan a descargar ni
  reutilizar sus obras.** Ninguna imagen del sitio sale de ellas.
- Al dejar de usar un recurso, quitalo también de los créditos.

---

## 8. Mantenimiento

### 8.1 Añadir un artículo

La escritura, la estructura y las fuentes del texto se tratan en
[`editorial-system.md`](editorial-system.md) (en prueba). Esta
sección cubre solo la parte técnica.

1. Crea `_posts/AAAA-MM-DD-slug.md`, con la misma fecha en el nombre y en
   `date:`. Incluye `title`, `description` (una o dos frases) y `categories`.
   Los campos opcionales están en el [README](../README.md).
2. Las secciones empiezan en `##`, y los niveles no se saltan (`##` → `###` → `####`).
3. Las fuentes van como notas al pie.

### 8.2 ¿Collage propio o portada automática?

- **Collage propio** cuando hay una idea visual que sale del texto, idealmente
  de una frase concreta, y una fuente (foto propia o recurso con licencia)
  que la sostiene sin explicaciones rebuscadas.
- **Portada automática** en los demás casos. Es una salida digna, no un
  defecto.
- **`fragmento:` fijo** cuando un fragmento existente corresponde claramente
  al texto, pero no da para un collage completo.

Para un collage nuevo:

1. Si usa una foto propia, añádela a `FOTOS` en `preparar_propias.py` y corre
   el script.
2. Escribe la función en `componer.py`. Pon un comentario con la frase del
   texto y la idea, construye las tres composiciones (`-v`, `-m`, `-h`) y
   regístrala en `COLLAGES`.
3. Corre `python3 _collage/componer.py nombre`.
4. En el front matter, agrega `collage: nombre` y un `collage_alt` que
   describa lo que se ve, incluidas las palabras que lleve la imagen.
5. Registra la procedencia en `_collage/README.md` y en `creditos.md`.

Para un fragmento nuevo:

1. Agrégalo a `FRAG_PROPIOS` (o a `fragmentos()` si es externo) y corre el
   script.
2. Si debe entrar en la rotación general, súmalo a la lista de
   `_includes/cover.html`.

### 8.3 Comprobar el resultado

```bash
bundle exec jekyll build    # o: jekyll build
bundle exec jekyll serve    # http://localhost:4000
```

Revisá en escritorio (1440 px) y en móvil (390 px):

- la home;
- la entrada nueva;
- `/archivo/` y la categoría correspondiente;
- `/creditos/`.

Verificá además:

- que no haya desbordamiento horizontal: `document.documentElement.scrollWidth`
  debe ser igual al ancho de la ventana;
- que todas las imágenes carguen (ninguna con `naturalWidth` 0);
- que los enlaces internos respondan 200;
- que el foco con teclado sea visible;
- que el `collage_alt` exista e incluya las palabras de la imagen;
- con teclado: el menú móvil se cierra con Escape y no deja el foco detrás del
  panel; en una entrada con notas, el número lleva a «Fuentes» y «↩» vuelve al
  pasaje;
- sin JavaScript: el índice se ve y no aparecen controles que no funcionan;
- que no haya metadatos (sección 7.4).

---

## 9. Referencias visuales

Las referencias orientan el proyecto, **no son fuentes de imágenes** y no
autorizan a reutilizar sus obras. Revisadas en noviembre de 2026.

| Referencia | Qué se observó | Qué se tomó (principio) |
|---|---|---|
| [Javier Palma, collage](https://www.revuecolle.com/artists/palma) | Retratos en blanco y negro cortados en franjas y desplazados, con formas planas de color que tapan ojos o bocas, mucho espacio liso y dos o tres colores por pieza | El corte recto con desplazamiento, la forma plana que oculta o sustituye, el límite de colores por pieza y el aire alrededor del recorte |
| [24 Grados, arquitectura (ArchDaily)](https://www.archdaily.com/es/1029367/intervenciones-contextuales-y-una-mirada-al-patrimonio-explorando-la-arquitectura-de-24-grados-en-honduras) | Cal, ladrillo, teja, zócalos de color, gradas en pendiente y un croquis con anotaciones a mano | La paleta material (ladrillo, cal, zócalo deslavado), la franja de zócalo como pieza gráfica, la diagonal de la escalinata y la anotación sobre el dibujo, que dio origen a las anotaciones al margen |
| [MUA, «Con lo que sueño» de Julia Galeano](https://muahn.com/mua-inaugura-la-muestra-con-lo-que-sueno-de-julia-galeano/) | Una sola foto de sala, con luz rosada de interior. La página no muestra grabados de La Grafo | La luz cálida de interior y el rosa como color de intimidad |
| [Estudio 1331](https://estudio1331.com/) | Retratos de línea tipo grabado y sellos tipográficos | La etiqueta tipográfica como pieza física (las palabras recortadas en papel). Se dejaron fuera la estructura de tienda y lo souvenir |

**Decisiones propias del proyecto, que no vienen de las referencias:**

- la atmósfera nocturna y su paleta exacta;
- el duotono tinta/cal y la regla de las fotos nocturnas;
- el color y la marca por tema;
- el par Fraunces y Public Sans;
- las tres composiciones por collage;
- las portadas automáticas;
- el uso de fotos propias;
- cualquier textura de grabado: es idea propia, no algo visto en La Grafo.

---

## 10. Protección del contenido

- **Conservar los enlaces públicos.** No cambiar nombres de archivo de
  entradas, `permalink` ni rutas de categorías. Si un cambio es inevitable,
  dejar la URL antigua funcionando. Por ejemplo, «Amar la herida» mantiene su
  `permalink` histórico.
- **Conservar la voz y el sentido** de los textos de Carlos: el voseo, el
  registro y las cursivas propias. Las correcciones se limitan a ortografía,
  formato y errores evidentes.
- **Verificar las fuentes** antes de modificar una afirmación, cifra, cita o
  referencia. Si no se puede verificar, no se cambia; se deja anotado como
  pendiente.
- **Lo que no se publica:** documentos personales, capturas, imágenes clínicas
  o íntimas y personas reconocibles sin decisión expresa. Tampoco ubicaciones
  sin evidencia.

---

## 11. Pendientes e ideas futuras (no aprobados)

**Pendientes reales:**

- **Licencia de las fotos propias.** Se publican con autorización de Carlos,
  pero sin licencia abierta. Si quiere una (por ejemplo, CC BY-NC), hay que
  declararla en los créditos.
- **Foto del kiosco** para «¿Y si el amor no fuera un sentimiento?»: no está
  decidida, porque tiene una persona de espaldas y el nombre del negocio
  visible. Hoy no se usa.
- **Archivos sin abrir de «fotos blog»:** una foto de 16 MB (supera el límite
  de descarga del conector de Drive) y dos videos.
- **«La mentira que no se siente como mentira»:**
  - las propuestas de frases destacadas siguen sin decidir;
  - la cifra «89 % de las muestras» atribuida a Mezulis et al. (2004) no está
    verificada contra el artículo completo.

- **Primera lectura en la home:** siete entradas tienen `featured: true`, pero
  ninguna plantilla lo usa. Hay que decidir si la home sugiere una primera
  lectura, cuál, y si `featured` es el mecanismo (sección 5.3).
- **Párrafos en negrita usados como títulos** (por ejemplo, en «Anamnesis»:
  «Importancia de la anamnesis clínica», «Descripción y elementos clave»). Se
  podrían convertir en encabezados sin cambiar las palabras, pero no está
  decidido.
- **Fragmento repetido en la home:** la portada automática de «La Ontología
  del Ser Necesario» usa `escalinata`, la misma foto que el collage del TDAH,
  y las dos se ven en la home. Opciones: aceptarlo, fijar otro `fragmento:` a
  esa entrada o cambiar la regla de «Del archivo».
- **Nombre de «Proyectos»:** la página se titula «Proyectos personales» y el
  resto del sitio dice «Proyectos». Hay que decidir si se unifican.
- **Comprobaciones de accesibilidad que el entorno de agentes no permite:**
  lector de pantalla, Safari y Firefox, dispositivos reales y alto contraste
  (ver `docs/audits/`).

**Ideas futuras (sin aprobar), a partir de fotos candidatas que no se usan
todavía:**

- fachada barroca con columnas salomónicas;
- espadaña con cruces de hierro;
- ciudad de noche con laderas encendidas (habría que recortar un letrero
  comercial);
- reja forjada;
- sol entre ramas sobre teja;
- piso de mosaico de una plaza.

Podrían servir como fragmentos si aparece una entrada que les corresponda.
