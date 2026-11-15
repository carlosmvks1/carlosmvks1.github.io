# Instrucciones para agentes: El cuaderno

Blog personal de Carlos Reyes (medicina, filosofía, fe, proyectos). Está hecho
en Jekyll y se publica en GitHub Pages desde `main`
(https://carlosmvks1.github.io).

**Guía detallada del sistema visual:** [`docs/visual-system.md`](docs/visual-system.md).
Leela antes de tocar el diseño, los collages o las imágenes. Estas son las
reglas esenciales. Si algo cambia en el código, actualizá esa guía en el
mismo cambio.

**Sistema editorial (integrado; solo es obligatorio lo marcado como [Vigente] o [Carlos]):**
[`docs/editorial-system.md`](docs/editorial-system.md), con su análisis en
[`docs/editorial-analysis.md`](docs/editorial-analysis.md). Leelo antes de
redactar o editar artículos.

## Identidad (vigente)

- Dirección «Revista nocturna»: **el collage editorial es el protagonista**,
  con atmósfera nocturna y **raíces hondureñas**, sin limitarse a
  Tegucigalpa. Nada de banderas, mapas, souvenirs ni patrones indígenas
  decorativos.
- **Riqueza visual, presencia editorial y personalidad.** No simplifiques
  hacia el minimalismo por preferencia propia: no quites collages, color por
  tema, texturas ni contrastes de escala. La lectura se protege con el cuerpo
  de texto sobre una superficie estable y legible.
- Paleta, tipografías (solo Fraunces y Public Sans) y tokens: los de
  `assets/main.scss`, documentados en la guía. No agregues familias ni
  colores nuevos sin decisión de Carlos.
- Los componentes usan los tokens de función (`--color-*`, `--tema`), no la
  paleta directamente. Los temas (nombre, URL y color) se definen solo en
  `_data/temas.yml`.

## Collages

- Hacelos con `_collage/componer.py`, que reúne las funciones comunes:
  - fondo de noche con grano;
  - foto de día en duotono tinta/cal, o foto nocturna en color calentado;
  - láminas en tinta sobre cal;
  - **como máximo dos colores planos** por pieza;
  - cortes rectos, con un solo borde rasgado como máximo;
  - sombra corta y dura;
  - rotación de 3° o menos;
  - como mucho una frase del texto, en papel.
- Los círculos, las etiquetas y los grabados son **opcionales**. No los pongas
  en todas las piezas.
- Cada collage se hace en tres formatos: `-v` 4:5, `-m` 1:1 (recompuesto, no
  recortado) y `-h` 3:2.
- Una entrada sin collage usa una portada automática. Puede fijar su
  fragmento con `fragmento:` cuando uno le corresponde de verdad.

## Fotografías propias

- Dales prioridad cuando aporten al texto. Se pueden combinar con recursos
  externos autorizados. **No fuerces asociaciones** ni sustituyas imágenes que
  ya funcionan.
- **Originales:** viven en la carpeta privada «fotos blog» de Drive. Nunca se
  borran, se modifican ni se suben al repositorio. En el repositorio solo van
  derivados recortados y **sin metadatos** (sin EXIF, GPS, XMP ni ICC),
  generados con `_collage/preparar_propias.py`.
- No atribuyas lugares sin evidencia visible en la imagen. No publiques
  personas reconocibles, capturas, documentos personales, ni imágenes
  clínicas o íntimas.

## Decisiones aprobadas por Carlos

- **Conservá el collage de «Amar la herida»** tal como está, con el busto y el
  disco rosa.
- **Excluí las fotos del bolsillo y del microscopio:** no van al sitio ni al
  repositorio.
- Las fotos de «fotos blog» se pueden publicar cuando encajen con el
  contenido y la composición.

Lo que no figure en esta lista no está aprobado. Los pendientes están en la
sección 11 de la guía.

## Licencias y créditos

- Fuentes externas: solo de dominio público o con licencia libre verificada.
  Registralas en `_collage/README.md` y en `creditos.md`.
- Las referencias de diseño (Javier Palma, 24 Grados, MUA, Estudio 1331)
  **no autorizan a reutilizar sus obras**. Ninguna imagen sale de ellas.
- Si quitás un recurso, quitá también su crédito.

## Contenido y escritura

- El sistema editorial enlazado arriba es una propuesta: solo lo marcado allí
  como **[Vigente]** o **[Carlos]** es obligatorio; lo marcado como
  **[Propuesta]** es sugerencia hasta que Carlos lo apruebe. Sus descripciones
  de formatos se basan en pocas entradas: orientan, no son normas.
- **Conservá los enlaces públicos** (nombres de archivo, `permalink`, rutas de
  categorías) y el sentido de los textos.
- **Conservá la voz de Carlos sin reproducir sus errores.** Las erratas,
  muletillas, mezclas de voseo y tuteo o afirmaciones sin respaldo no son
  rasgos de estilo (ver la sección 4 del análisis). Sus recursos frecuentes
  (antítesis, frases cortas, analogías clínicas, preguntas) están disponibles,
  no son una receta: no los agregues para que un texto «suene a Carlos».
- **La conclusión no puede aumentar el grado de certeza ni eliminar los
  matices** establecidos en el desarrollo.
- **Referencias:** en entradas nuevas, notas al pie. Cada cifra clínica, con
  una fuente que respalde la población, el resultado y el contexto
  mencionados. Las afirmaciones sobre personas o instituciones que puedan
  afectar su reputación necesitan respaldo; si no lo tienen, se reformulan o
  se retiran.
- **No inventes experiencias, creencias ni posiciones personales** de Carlos.
  Si un texto necesita un ejemplo propio, dejá `[EJEMPLO: …]` y preguntale.
- **No modifiques el sentido de un texto sin señalarlo** en el resumen del
  cambio, aunque sea para hacerlo más prudente.
- Verificá la fuente antes de cambiar una afirmación, cifra, cita o
  referencia. Si no podés verificarla, no la cambies: anotala como pendiente.
- **Respetá el sistema visual existente:** la guía editorial no lo redefine.

## Antes de entregar

1. Corré `bundle exec jekyll build` (o `jekyll build`) sin errores.
2. Revisá en escritorio (1440 px) y en móvil (390 px), sin desbordamiento
   horizontal: la home, el artículo tocado, `/archivo/` y `/creditos/`.
3. Comprobá que todas las imágenes cargan y que los enlaces internos dan 200.
4. Comprobá que el foco es visible y que el contraste es al menos 4.5:1.
5. Comprobá que no hay metadatos: el comando está en la sección 7.4 de la
   guía.
6. Revisá el diff: no deben quedar originales, pruebas temporales ni fotos
   excluidas.
7. Trabajá en una rama y no publiques en `main` sin autorización de Carlos.
