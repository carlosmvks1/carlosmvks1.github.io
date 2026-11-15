# Verificación de las correcciones (15 de noviembre de 2026)

- **Rama:** `claude/auditoria-accesibilidad`. Parte de `78a7512`, el commit
  auditado en
  [`2026-11-15-accesibilidad-claridad-tokens.md`](2026-11-15-accesibilidad-claridad-tokens.md).
- **Build:** Jekyll 3.10.0 (`github-pages` 233), sin errores.
- **Cómo se probó:** el build local se sirvió por HTTP y se probó con
  Playwright 1.63 (Chromium) y axe-core 4.10.3. La versión anterior (`78a7512`)
  se sirvió en paralelo para comparar.

> **Sin lector de pantalla.** Los nombres, roles y estados que se citan abajo
> son los observados en el DOM y en el árbol de accesibilidad de Chromium. No
> se comprobó cómo los anuncia NVDA, JAWS, VoiceOver ni TalkBack.
>
> **Sin declaración de conformidad.** Estas pruebas no permiten afirmar que el
> sitio cumple WCAG 2.2 AA en su totalidad. Lo pendiente está al final.

## 1. Resultado por hallazgo

| # | Clasificación previa | Resultado | Evidencia tras la corrección |
|---|---|---|---|
| A1 | Problema funcional; posible 1.3.2 y 4.1.2 | Corregido | Ver 1.1 |
| A2 | Incumplimiento 2.4.11 | Corregido | Ver 1.2 |
| A3 | Incumplimiento 4.1.2 y 2.4.4 | Corregido | Ver 1.3 |
| A4 | Problema funcional | Corregido | Ver 1.4 |
| B1 | Problema funcional | Corregido | Ver 1.5 |
| B2 | Posible 2.1.1 | Corregido en Chromium; falta probar otros navegadores | Ver 1.6 |
| B3 | Recomendación 1.1.1 | Corregido | `collage_alt` de «Amar la herida» y del TDAH completados (1.7) |
| B4a | Incumplimiento 1.3.1 | Corregido | `<h2 class="fuentes-titulo" id="fuentes">Fuentes</h2>` en el HTML; rol `doc-endnote`: 0 |
| B4b | Recomendación | Corregido en niveles; pendiente en párrafos en negrita | Ver 1.8 |
| B4c | Recomendación | Corregido | Ver 1.8 |
| C1 | Incumplimiento 1.4.1 | Corregido | Ver 1.9 |
| C2 | Recomendación | Corregido | Nombre en el árbol: «Medicina 3 entradas» (texto `.solo-lectores`) |
| C3 | Recomendación | Corregido | `aside.lectura-indice` pasa a ser `div`; las notas del margen tienen `aria-hidden` y la desplegable es `div role="note"` con nombre |
| C4 | Cumplía por excepción | Mejorado | Ver 1.10 |
| C5 | Informativo | Corregido | A 320 px con el espaciado de 1.4.12: `scrollWidth` 320 en home, archivo, Mentirnos, Narcisismo y SN |

### 1.1 A1: notas

Página: `/filosofia/2026/06/20/Mentirnos.html`.

**Escritorio (1440 px):**

- Se ve el enlace del número y el botón está oculto.
- Enter sobre el número lleva a `#fn:mezulis`.
- Enter sobre «↩» vuelve a `#fnref:mezulis`, y la llamada queda dentro de la
  ventana. El siguiente Tab cae en el número.
- Las dos notas al margen se ven, tienen `aria-hidden="true"` y sus enlaces
  tienen `tabindex="-1"`.
- En el árbol de accesibilidad de `.prose` no aparece ningún *complementary* ni
  nota duplicada. «Fuentes» aparece como `heading level=2`.

**Móvil (390 px):**

- El enlace está oculto y el botón «Fuente 1» se ve.
- Enter abre la nota: `aria-expanded="true"`, visible y justo después del
  párrafo. Enter otra vez la cierra.
- Desde «Fuentes», «↩» vuelve a `#fnref:mezulis`, y el siguiente Tab cae en el
  botón de la nota.

**Sin JavaScript:** `#fnref:mezulis` y `#fnref:pronin` existen, y los números
son enlaces visibles.

**Nombres:** el regreso se llama «Volver al pasaje de la fuente N» con JS y
«Volver al pasaje» sin JS.

### 1.2 A2: menú móvil

Prueba a 390 px, en la home:

- Enter abre el menú.
- Escape lo cierra, y el foco vuelve a «Menú».
- Con Tab hasta salir del menú, el foco llega a «Sobre mí» de la portadilla,
  con el menú ya cerrado. `elementFromPoint` confirma que el enlace no está
  tapado.
- Un clic fuera del menú lo cierra.

### 1.3 A3: enlaces de imagen

- En la home quedan 0 enlaces expuestos sin nombre.
- Los enlaces de imagen de tarjetas, protagonista y «Del archivo» tienen
  `aria-hidden="true"` y `tabindex="-1"`. El único enlace por entrada es el
  título.
- axe `link-name`: 0 en 44 combinaciones de página y ancho.

### 1.4 A4: índice

- Sin JS, los enlaces del índice se ven a 1440 px y a 390 px.
- Con JS:
  - cargado a 800 px, el índice está plegado;
  - al pasar a 1300 px, se ve;
  - al volver a 800 px, se pliega.
- La sección actual tiene `aria-current="location"` y subrayado.

### 1.5 B1: filtros del archivo

- Con «Medicina», quedan 3 filas.
- La entradilla visible pasa a «3 de 13 entradas · Medicina, de la más
  reciente a la más antigua.».
- La región `role="status"` contiene «Mostrando 3 entradas de Medicina.».
- Con «Todos», el texto vuelve a «13 entradas…».
- Sin JS, los filtros no se ven.

### 1.6 B2: tablas

- A 390 px, `Elecciones` (1) y `narcicismo` (2) tienen marcos que desbordan,
  con `tabindex="0"`, `role="region"` y un nombre, por ejemplo «Tabla 1:
  COMPARATIVA GLOBAL (se desplaza horizontalmente)».
- `anamnesis` no desborda, así que su marco no recibe foco.
- Con el foco en el marco, la flecha derecha desplaza 74 px y el contorno de
  foco se ve.
- A 1440 px no hay marcos enfocables.
- La tabla queda con `display: table`.

### 1.7 B3: textos alternativos

| Entrada | Se añadió |
|---|---|
| «Amar la herida» | «…; a su lado, un disco rosa y, abajo, un papel rotulado «la espera».» |
| «Explorando el TDAH desde dentro» | «… Abajo, un papel pregunta «¿cuál primero?».» |

Los collages no se tocaron.

### 1.8 B4b y B4c: encabezados y estructura

**Saltos de nivel** (secuencia observada en el DOM): 0 en la home, Mentirnos,
anamnesis, SN y Elecciones.

**Cambios de nivel**, sin cambiar palabras:

- **anamnesis:**
  - «Reglas de oro» pasa de `###` a `##`;
  - 16 `####` pasan a `###`.
- **SN:** «La honestidad filosófica» y «Reflexión personal y cierre» pasan de
  `####` a `###`.
- **Elecciones:**
  - desde «¿Qué propone cada candidato?», `####` pasa a `###` y `#####` pasa a
    `####`;
  - los `####` de «El estilo Asfura» siguen en `####`, porque cuelgan de un
    `###`.

**Home:** las regiones se llaman «También en el cuaderno», «Del archivo»,
«Más entradas» y «Los cuatro temas».

**Pendiente:** los párrafos en negrita que hacen de título en `anamnesis` no
se convirtieron (decisión de Carlos).

### 1.9 C1: estado actual sin depender del color

- **Menú móvil:** «Archivo» lleva `aria-current="page"` y un subrayado de 2 px
  en `rgb(230, 173, 74)`.
- **Índice:** la sección actual lleva subrayado y `aria-current="location"`.

### 1.10 C4: objetivos táctiles

- El botón de nota en móvil conserva su tamaño visual (17 × 16 px).
- Su área táctil, extendida con un pseudoelemento, mide 24 × 24 px. Las
  pruebas de impacto se hicieron con `elementFromPoint`: el botón responde
  de −12 a +11 px desde el centro en ambos ejes.

## 2. Pruebas generales

### 2.1 axe-core

- Etiquetas: `wcag2a`, `wcag2aa`, `wcag21a`, `wcag21aa`, `wcag22aa` y
  `best-practice`.
- Alcance: las 22 páginas a 1440 px y a 390 px.
- Resultado: 0 violaciones. Antes había `link-name`,
  `landmark-complementary-is-top-level`, `heading-order`,
  `scrollable-region-focusable` y `aria-deprecated-role`.

### 2.2 Teclado

Se recorrió cada página con Tab, comprobando contorno, que el elemento quedara
en la ventana y que no lo tapara otro:

| Página | Ancho | Paradas | Problemas |
|---|---|---|---|
| Mentirnos | 1440 px | 37 | 0 |
| Mentirnos | 390 px | 26 | 0 |
| SN | 1440 px | 32 | 0 |
| Archivo | 390 px | 27 | 0 |
| Home | 390 px | 37 | 0 |

### 2.3 Redistribución y espaciado

`scrollWidth` es 320 en las 5 páginas probadas, a 320 px y también a 320 px
con el espaciado de 1.4.12.

### 2.4 Enlaces e imágenes

- Los 24 enlaces internos únicos responden 200.
- No hay anclas sin destino.
- No hay imágenes rotas.

### 2.5 Metadatos

El comando de la sección 7.4 de la guía visual da «sin metadatos».

### 2.6 Regresión visual

Se compararon capturas de página completa de las 22 páginas a 1440 y 390 px,
antes y después, con pixelmatch (umbral 0.1).

**Sin cambios (0.00 %):**

- `/archivo/` a 1440 px;
- las cuatro categorías, `/creditos/`, `/cuaderno/` y `/sobre-mi/` a 1440 px.

A 390 px, esas mismas páginas dan entre 0.02 y 0.06 %: son píxeles sueltos de
suavizado de letras, sin cambios de posición.

**Cambios previstos:**

- **Encabezados de anamnesis, SN y Elecciones:** son los que más cambian, con
  hasta +376 px de alto, porque los `h3` son más grandes que los `h4`.
- **Pie de las series:** la siguiente parte aparece destacada.
- **Rótulos:** el peso de «Entrar por tema», el tamaño de «En este texto» y de
  «Anotación», y los textos «Lecturas relacionadas · Tema», «Anterior/Siguiente
  por fecha» y «Los cuatro temas».
- **Subrayado del estado actual** en el menú móvil y en el índice.

**Ruido descartado:**

- La home a 1440 px marca 2.4 %, pero comparar la línea base consigo misma da
  el mismo valor: es la carga diferida del collage de «Del archivo».
- IIEAN, Elecciones, Mentirnos y Narcisismo muestran el mismo ruido de carga
  diferida en las tarjetas relacionadas.

**Comparaciones antes y después** en [`capturas/`](capturas/):

- `serie-pie`
- `serie-aviso`
- `nota-movil`
- `fuentes`
- `menu-movil`
- `archivo-filtro`
- `indice-actual`
- `anamnesis-encabezados`
- `elecciones-encabezados`
- `home-temas`
- `home-cuatro-temas`

**Regresión encontrada y corregida durante la verificación:** un primer botón
de nota de 24 px visibles empujaba el punto final a la línea siguiente. Se
cambió por un área táctil invisible de 24 px que conserva el tamaño original.

## 3. Pendiente (el entorno no lo permite)

- **Lector de pantalla:**
  - NVDA con Firefox y JAWS con Chrome en Windows: notas, menú, filtros
    (anuncio de `role="status"`) y tablas;
  - VoiceOver con Safari en macOS e iOS: además, la semántica de tabla dentro
    de `.tabla-marco`;
  - TalkBack con Chrome en Android: botón de nota y menú.
- **Navegadores:** Safari y Firefox. En particular, el foco de `.tabla-marco`
  y `details`/`summary` con Escape.
- **Dispositivos reales:** área táctil del botón de nota y menú móvil.
- **Zoom real** del navegador al 200 % y al 400 %; aquí se simuló con el ancho
  de la ventana.
- **Alto contraste** (`forced-colors`): el subrayado del estado actual y los
  bordes de los botones.

## 4. Decisiones pendientes de Carlos

1. **Primera lectura en la home:** hay que decidir si se sugiere una, cuál y
   si `featured: true` (hoy en siete entradas, sin uso) es el mecanismo.
2. **Párrafos en negrita que hacen de título** en «Anamnesis» («Importancia de
   la anamnesis clínica», «Descripción y elementos clave», «Ejemplo»):
   convertirlos en encabezados o dejarlos.
3. **«Proyectos personales» (título de la página) frente a «Proyectos»** (resto
   del sitio).
4. **Opcional:**
   - guardar el filtro del archivo en la URL;
   - mostrar descripciones en el archivo;
   - unificar los *hover* de los enlaces de título.
