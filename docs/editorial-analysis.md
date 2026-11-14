# Análisis editorial de El cuaderno

**Estado: propuesta pendiente de revisión por Carlos.** Este documento
describe cómo están escritas las entradas publicadas. Las interpretaciones y
recomendaciones son del análisis, no decisiones aprobadas. La guía práctica que
se desprende de aquí está en [`editorial-system.md`](editorial-system.md).
Las decisiones que Carlos ya tomó sobre este análisis están registradas en la
sección 7 de esa guía.

Describir un rasgo no lo vuelve obligatorio. Los recursos frecuentes
(antítesis, frases cortas, analogías clínicas, preguntas) están disponibles, no
son una receta para imitar a Carlos.

Convenciones:

- **Observación:** lo que el texto hace, verificable en la ruta citada.
- **Interpretación:** el efecto probable en quien lee. No se atribuyen
  intenciones ni estados de ánimo al autor.
- **Recomendación:** qué convendría conservar o mejorar.
- Los ejemplos «después» son **propuestas** de redacción. No se aplicaron a
  ningún artículo.

---

## 1. Corpus y versión analizada

- **Versión:** rama `claude/cuaderno-editorial-system-890bxu`, creada desde
  `main` en el commit `92cfbef` (14 de noviembre de 2026).
- **Alcance:** las 13 entradas de `_posts/`, leídas completas (unas 40 000
  palabras). También `about.md`, para contrastar con lo que Carlos dice de su
  propia escritura.
- **Ediciones previas de agentes.** Antes de este análisis, otras sesiones
  tocaron las entradas (commits `1e59c8e` en adelante):
  - normalizaron los niveles de los títulos y corrigieron tildes sueltas;
  - cambiaron fechas y nombres de archivo;
  - **escribieron todas las `description`**, el `subtitle` y la `cita` de
    «La mentira que no se siente como mentira»;
  - convirtieron sus dos referencias en notas al pie y crearon su única
    anotación al margen (`{: .anotacion}`).

  Por eso las descripciones, las notas al pie y la anotación **no se usan aquí
  como evidencia de la voz de Carlos**. Los títulos, la prosa y la estructura sí
  son suyos.

### 1.1 Inventario

| Ruta (`_posts/…`) | Título | Categoría | Palabras aprox. | Formato (sección 3) |
| --- | --- | --- | --- | --- |
| `2025-05-05-TDAH.md` | Explorando el TDAH desde dentro | medicina | 8100 | Divulgación clínica |
| `2025-05-10-anamnesis.md` | Anamnesis: guía para estudiantes de medicina | medicina | 3500 | Guía práctica |
| `2025-09-16-narcicismo.md` | Narcisismo y Trastorno Narcisista de la Personalidad: una mirada desde dentro | medicina | 4700 | Divulgación clínica |
| `2025-10-12-Amor.md` | ¿Y si el amor no fuera un sentimiento? | filosofía | 1350 | Ensayo reflexivo |
| `2025-10-12-SN.md` | El fundamento o el abismo: por qué negar un ser necesario también es una fe | filosofía (serie, 1) | 1300 | Ensayo argumentativo |
| `2025-11-20-Romanos.md` | La lección que Romanos 1–3 imprime en el alma | fe | 4000 | Lectura comentada (bíblica) |
| `2025-11-23-IIEAN.md` | Lo que repetís, eso sos: Aristóteles y carácter | filosofía | 1250 | Lectura comentada (filosófica) |
| `2025-11-25-Elecciones.md` | Lo que Honduras decide en 2025: no personas, sino futuros posibles | filosofía | 4600 | Análisis comparativo de actualidad |
| `2025-11-26-Fuego.md` | Fuego que no debe tocar nada | proyectos | 850 | Prosa breve |
| `2025-12-05-Trinidad.md` | La Ontología del Ser Necesario: Simplicidad, Perfección y Alteridad Interna | filosofía (serie, 2) | 2000 | Ensayo argumentativo |
| `2025-12-11-Juan.md` | Si Dios permanece, el amor aparece | fe | 3100 | Lectura comentada (bíblica) |
| `2026-05-26-Amarlaherida.md` | Amar la herida | filosofía | 1500 | Ensayo reflexivo con andamio filosófico |
| `2026-06-20-Mentirnos.md` | La mentira que no se siente como mentira | filosofía | 2500 | Ensayo reflexivo con evidencia |

En adelante, cada entrada se cita por la parte final de su ruta (por ejemplo,
`Mentirnos.md:218` es la línea 218 de `_posts/2026-06-20-Mentirnos.md`).

---

## 2. Rasgos de voz compartidos

Solo se incluyen rasgos que aparecen en tres entradas o más. Los recursos de
una o dos entradas están en la sección 2.9.

### 2.1 Frase corta que remata un desarrollo

**Observación.** Después de un párrafo largo, una línea breve, a menudo de una
o dos palabras, cierra la idea:

- «Siempre.» (`SN.md:19`); «Esto no es poco.» (`SN.md:151`)
- «Porque eso sos.» (`IIEAN.md:165`); «**Se talla.** / A golpes. / A diario.»
  (`IIEAN.md:178-180`)
- «Da vértigo.» (`Romanos.md:581`)
- «La creemos.» (`Mentirnos.md:244`)
- «Elegir la calma. / Elegir la espera. / Elegir la cordura.» (`Fuego.md:73-75`)

**Interpretación.** Marca el ritmo y fija la idea. Funciona mejor cuando lo que
remata ya está argumentado.

**Recomendación.** Conservar. Usarla al cierre de una sección, no al final de
cada párrafo: en `IIEAN.md` y en la conclusión de `Romanos.md` se encadenan
tantas que pierden fuerza (ver 4.3).

### 2.2 Antítesis «no X, sino Y»

**Observación.** Es la figura más frecuente del corpus:

- «No es algo que se siente sino algo que se hace» (`Amor.md:25`)
- «No deseo porque amo; muchas veces amo porque algo me falta.»
  (`Amarlaherida.md:27`)
- «Los éxitos se convierten en identidad. Los fracasos se convierten en
  circunstancias.» (`Mentirnos.md:108`)
- «el ídolo peligroso, **no niega la vida, la imita**» (`Juan.md:156`)
- «Su paciencia no es permisividad: es misericordia en espera.»
  (`Romanos.md:272`)
- «Es más sacerdote anticorrupción que político tradicional.»
  (`Elecciones.md:56`)

**Interpretación.** Condensa una distinción en una línea memorable. Cuando se
repite muchas veces seguidas, el texto parece avanzar por fórmulas en lugar de
por razones, y la segunda mitad a veces dice más de lo que el párrafo
demostró.

**Recomendación.** Conservar como rasgo central. Revisar que cada antítesis
cierre un razonamiento y no lo sustituya, y espaciar las que aparecen en
párrafos contiguos.

### 2.3 Paralelismos y anáforas

**Observación.** Series de frases con el mismo arranque:

- «Tu naturaleza no te salva. / Tu inteligencia no te salva. / Tus intenciones
  no te salvan.» (`IIEAN.md:93-96`)
- «no puedo vivir pensando que el ser es un accidente. / No puedo abrazar…
  / No puedo convencerme…» (`SN.md:180-182`)
- «Él mismo carga la culpa. / Él mismo paga la deuda.» (`Romanos.md:415-417`)
- «No se puede tenerlo todo. / No en este país. / No al mismo tiempo.»
  (`Elecciones.md:647-649`)

**Interpretación.** Da cadencia oral, casi de predicación o de clase. En
textos argumentativos convence por acumulación más que por prueba.

**Recomendación.** Conservar en cierres y en pasajes de exhortación. En la
parte expositiva, una serie de tres basta.

### 2.4 Voseo y habla hondureña

**Observación.** La voz del autor usa el voseo («vos», «sos», «podés»,
«pensalo») en `IIEAN.md`, `Romanos.md`, `SN.md`, `TDAH.md`, `Fuego.md` y
`Mentirnos.md`. Hay expresiones coloquiales e imágenes locales: «otro rollo»
(`Mentirnos.md:100`), «Te cerrás porque sos full evitativo»
(`Mentirnos.md:289`), «Que no te cueste equivocarte mi sangre»
(`Mentirnos.md:348`), «la patrulla de tránsito en el anillo periférico»
(`TDAH.md:100`), «estudiar fisiología ahorita» (`TDAH.md:112`), las *Far Lands*
de Minecraft (`SN.md:35`).

**Interpretación.** Es la marca más clara de identidad. Sitúa los textos y los
acerca a quien lee sin restarles seriedad.

**Recomendación.** Conservar. El problema no es el voseo, sino mezclarlo con el
tuteo en el mismo texto (ver 4.5).

### 2.5 Analogías clínicas y cotidianas

**Observación.** Las comparaciones vienen a menudo de la medicina, el deporte o
la vida diaria:

- «Si las cartas de Pablo fueran laboratorios, Romanos sería ese panel
  completo…» (`Romanos.md:36`); «como un médico haciendo examén físico»
  (`Romanos.md:457`)
- «Honduras no es un cuerpo sano enfermo de un tumor. / Es un cuerpo entero
  que ha aprendido a funcionar enfermo.» (`Elecciones.md:102-103`)
- «**Physis** es tu genética. / **Ethos** es el entrenamiento.»
  (`IIEAN.md:43-44`)
- La autoestima como globo o como planta (`narcicismo.md:161`, `:178`); las
  redes cerebrales como agentes de tránsito (`TDAH.md:100-118`).

**Interpretación.** Traducen lo abstracto a algo que se puede imaginar. La
mirada clínica funciona como firma personal incluso fuera de la medicina.

**Recomendación.** Conservar. Una analogía por idea, y avisar cuando la
analogía no cubre todo («a modo de analogía», como en `IIEAN.md:42`).

### 2.6 Apertura desde un disparador concreto

**Observación.** Muchas entradas parten de una lectura, una conversación o una
circunstancia:

- un video (`Amor.md:14`);
- *Confesiones* de Agustín (`Juan.md:11`);
- la difusión de la salud mental en redes (`TDAH.md:12`);
- la experiencia de quinto año en la UNAH (`anamnesis.md:9`);
- «Como muchos jóvenes, estoy tratando de entender…» (`Elecciones.md:16`).

**Interpretación.** Explica por qué existe el texto y crea confianza. Cuando el
disparador se alarga, retrasa la pregunta (por ejemplo, `anamnesis.md:9-17`
tarda cuatro párrafos en llegar a la guía).

**Recomendación.** Conservar como opción, no como regla. Llegar a la pregunta
central en el primer o segundo párrafo.

### 2.7 Tesis o pregunta explícita

**Observación.** Varias entradas declaran qué van a sostener:

- «Lo esencial que quiero mostrar aquí es simple…» (`SN.md:29`)
- «Como tesis central voy a desarrollar lo siguiente…» (`Amarlaherida.md:13`)
- «Ahí apareció la tesis.» (`Juan.md:30`)
- «la pregunta central de este ensayo» (`Trinidad.md:53`)
- «**¿Cómo pueden dos personas sinceras estar tan convencidas de versiones
  incompatibles?**» (`Mentirnos.md:19`)

**Interpretación.** Es uno de los mayores aciertos del corpus: quien lee sabe
qué se juega. Los textos que mejor sostienen su eje (`Mentirnos.md`,
`Juan.md`) vuelven a la pregunta al final.

**Recomendación.** Conservar y extender. Se puede quitar el andamiaje («Como
tesis central voy a desarrollar…») y dejar la tesis.

### 2.8 Matiz, objeción y límite

**Observación.** Los textos introducen contrapesos, aunque no siempre:

- «¿Y si el sesgo también nos mantiene en pie?» y «esto no demuestra que la
  disminución del sesgo cause depresión» (`Mentirnos.md:142-150`)
- «Ahora bien, amar no significa negar el mal… Juan no utiliza el lenguaje
  moderno de "límites", pero sí establece el criterio.» (`Juan.md:128`)
- «No hay demostraciones finales.» (`SN.md:162`)
- «yo mismo los estoy aprendiendo sobre la marcha» (`Trinidad.md:13`)
- Los «Mitos comunes» de `narcicismo.md:57-63`.

**Interpretación.** Cuando aparece, este gesto hace más creíble el texto y es
coherente con lo que dice `about.md` («La reflexión que no se pone a prueba se
vuelve dogma»). En otras entradas falta y hay afirmaciones absolutas (ver 4.1).

**Recomendación.** Conservarlo y hacerlo sistemático en ensayos y lecturas:
una objeción seria por texto, como mínimo.

### 2.9 Recursos ocasionales (una o dos entradas)

No conviene generalizarlos:

- **Escenas con personajes inventados:** Luis y Ana (`narcicismo.md:44-51`).
- **Diálogos breves en cita** para mostrar un sesgo (`Mentirnos.md:114-128`).
- **Secuencia numerada** que resume un proceso (`Mentirnos.md:256-270`).
- **Tabla de síntesis del argumento** (`Trinidad.md:254-263`) o comparativa
  (`Elecciones.md:602-619`, `narcicismo.md:113-123`).
- **Epígrafe literario** (`Fuego.md:10-24`) o bíblico (`Amor.md:11`).
- **Glosario previo** de conceptos (`Trinidad.md:10-51`).
- **Errores propios como lección** (`anamnesis.md:191-203`).
- **Prácticas o preguntas para el lector** tras la conclusión
  (`Romanos.md:632-662`).
- **Agradecimiento a una fuente** (`Romanos.md:630`).
- **Invitación a escribir al autor** (`Elecciones.md:664`).

### 2.10 Vocabulario recurrente

Palabras que vuelven en varios formatos: *alma*, *sostener*, *permanecer*,
*herida*, *vacío*, *frágil*, *espejo/reflejo*, *fundamento/suelo*, *cargar*,
*misterio*, *identidad*. Forman un campo coherente (qué sostiene a una
persona cuando algo falla). El riesgo es que se vuelvan muletillas:
«sostener» y sus formas aparecen en 12 de las 13 entradas, 15 veces en
`Romanos.md`, a veces más de una por párrafo (`Romanos.md:577-621`).

---

## 3. Formatos encontrados

No hay una estructura única. La primera versión de este análisis decía «seis
formatos», pero enumeraba siete; el recuento correcto es **siete**. Solo cuatro
tienen evidencia suficiente (dos entradas o más). Los otros tres se basan en
una sola entrada y son **categorías provisionales**: describen esa entrada, no
un patrón.

| Formato | Entradas | Evidencia |
| --- | --- | --- |
| 3.1 Divulgación clínica | `TDAH.md`, `narcicismo.md` | Suficiente (2) |
| 3.2 Guía práctica | `anamnesis.md` | Provisional (1) |
| 3.3 Ensayo argumentativo | `SN.md`, `Trinidad.md` | Suficiente (2, de una misma serie) |
| 3.4 Lectura comentada | `IIEAN.md`, `Romanos.md`, `Juan.md` | Suficiente (3). La variante filosófica tiene una sola entrada. |
| 3.5 Ensayo reflexivo | `Amor.md`, `Amarlaherida.md`, `Mentirnos.md` | Suficiente (3) |
| 3.6 Análisis de actualidad | `Elecciones.md` | Provisional (1) |
| 3.7 Prosa breve | `Fuego.md` | Provisional (1) |

Incluso los formatos con evidencia suficiente tienen dos o tres entradas: sus
descripciones son orientativas.

### 3.1 Divulgación clínica (`TDAH.md`, `narcicismo.md`)

- **Qué hace.** Abre con una escena en segunda persona («Imaginá que tenés que
  estudiar», `TDAH.md:23`; «Imagina estar frente al espejo»,
  `narcicismo.md:13`), desmonta un cliché y luego recorre definición, criterios
  DSM/CIE, bases biológicas, manifestaciones psicológicas, impacto,
  epidemiología, diagnóstico y tratamiento. Cierra con una pregunta ética o
  existencial (`TDAH.md:326`, `narcicismo.md:244`).
- **Qué cambia frente a otros formatos.** Registro más técnico, párrafos largos
  (mediana de 46 a 58 palabras), bibliografía numerada, poco voseo. Es el
  formato más largo: 4700 y 8100 palabras.
- **Lo mejor.** La escena inicial y las analogías hacen comprensible lo técnico
  («superávit de atención mal regulada», `TDAH.md:32`). La distinción entre
  rasgo y trastorno (`narcicismo.md:20-22`).
- **Lo débil.** Longitud y repetición (ver 4.7). Matices que se pierden al
  resumir (ver 4.1). En `TDAH.md` la bibliografía no está enlazada a las
  afirmaciones: el cuerpo no tiene ninguna llamada [n].
- **Ambigüedad del «desde dentro».** Ambos títulos dicen «desde dentro» y
  `TDAH.md:29` dice «Así se siente, muchas veces, vivir con TDAH». El texto no
  aclara si es una experiencia propia o una reconstrucción. **Ningún agente
  debe inferir de esto un diagnóstico o una experiencia personal de Carlos.**

### 3.2 Guía práctica (`anamnesis.md`, entrada única)

- **Qué hace.** Presentación personal, reglas, tabla de apartados, ejemplos de
  redacción clínica (HEA, FOG), técnicas de entrevista, recursos y una sección
  final de errores propios.
- **Lo mejor.** Los ejemplos utilizables (`anamnesis.md:66-89`) y la sección
  «Errores que me enseñaron a escuchar mejor» (`:191-203`), la más viva del
  texto.
- **Lo débil.** Se dirige al lector de tres maneras: «hablas claro» (`:25`),
  «Deben saber hacer transiciones» (`:146`) y «usted puede resumir» (`:127`).
  Los recursos aparecen sin enlaces y sin decir para qué sirve cada uno.

### 3.3 Ensayo argumentativo (`SN.md`, `Trinidad.md`)

- **Qué hace.** Pregunta en negrita, tesis declarada, opciones numeradas,
  premisas en lista («1. Si algo está compuesto… 3. Lo que no es
  autosuficiente no es necesario», `Trinidad.md:99-101`), objeciones y
  conclusión. `SN.md` termina con una sección personal («Reflexión personal y
  cierre»).
- **Lo mejor.** La claridad lógica y la separación de planos: «El teísmo
  filosófico no tiene nada que ver con liturgias. Ese es otro terreno.»
  (`SN.md:133`). El cierre personal de `SN.md:170-194` deja claro qué es
  argumento y qué es convicción.
- **Lo débil.** Afirmaciones de exhaustividad sin argumento («Todo lo demás son
  decoraciones conceptuales», `SN.md:102`). Tensión entre las partes de la
  serie: `SN.md:162` admite que «No hay demostraciones finales», pero
  `Trinidad.md:59` arranca con «Una vez concluimos que, efectivamente, existe
  un ser necesario». Títulos con mayúsculas a la inglesa en `Trinidad.md`.

### 3.4 Lectura comentada (`IIEAN.md`, `Romanos.md`, `Juan.md`)

Un texto ajeno (Aristóteles, Romanos, 1 Juan) guía el recorrido y se aplica a
la vida de quien lee.

- **Variante bíblica** (`Romanos.md`, `Juan.md`): contexto histórico, avance
  por capítulos o versículos, términos griegos con transliteración
  («**μένω (ménō)**», `Juan.md:104`), y una aplicación final en segunda
  persona. `Juan.md` está organizada en torno a una pregunta («¿cómo actúa
  alguien que vive desde ese amor?», `:62`) y la contesta punto por punto al
  final (`:158-170`): es el mejor ejemplo de pregunta sostenida del corpus.
- **Variante filosófica** (`IIEAN.md`): resumen de la tesis del libro, conceptos
  en griego, analogía de gimnasio, exhortación en voseo («Dejá de creer que vas
  a mejorar sin repetir actos de mejora», `:128`).
- **Lo débil.** La frontera entre lo que dice el texto y lo que interpreta
  Carlos se borra a veces: «Toda la teología paulina puede resumirse así»
  (`Romanos.md:111`), «No existe nada comparable en ningún sistema filosófico
  o religioso» (`Romanos.md:511`). Citas de terceros sin fuente
  (`IIEAN.md:74`, `Romanos.md:172`, `Romanos.md:348`; ver 4.2 y 4.11). `Romanos.md`
  tiene un cierre muy extenso (ver 4.3).

### 3.5 Ensayo reflexivo (`Amor.md`, `Amarlaherida.md`, `Mentirnos.md`)

Una experiencia común (amar, desear, justificarse) se examina con ayuda de
conceptos ajenos.

- **`Amor.md`:** parte de un video, avanza por metáforas (olas y mar, danza,
  llamas) y citas, y cierra con aforismos. Casi sin fuentes.
- **`Amarlaherida.md`:** tesis declarada y un «Andamio filosófico» (Platón,
  Kierkegaard) mediado y nombrado («En la lectura de la Stanford Encyclopedia
  of Philosophy…», `:29`). Termina sin conclusión separada.
- **`Mentirnos.md`:** pregunta, tres conceptos de psicología, objeción
  («¿Y si el sesgo también nos mantiene en pie?»), estudio con cifras, síntesis
  en secuencia y un giro final contra el propio lector («La última trampa»,
  `:306`). Es el texto con mejor equilibrio entre evidencia, ejemplo y voz.
- **Qué cambia.** La primera persona del plural («nosotros») y el «uno»
  dominan; las fuentes sirven de andamio y no de tema.

### 3.6 Análisis comparativo de actualidad (`Elecciones.md`, entrada única)

- **Qué hace.** Aviso de método, retrato de cada candidato (trayectoria,
  sombras, estilo), comparación por áreas, tabla global y conclusión con la
  pregunta al votante.
- **Lo mejor.** La estructura paralela facilita comparar. La conclusión no pide
  el voto y nombra el costo de cada opción.
- **Lo débil.** Promete basarse «únicamente en propuestas verificables,
  documentos oficiales y evidencia pública» (`:10`), pero no cita ninguna
  fuente. Menciona señalamientos concretos contra personas reales («Caso
  Pandora», «más de 280 millones de lempiras», `:140-142`) sin referencia. Usa
  calificativos que pesan en un texto que se presenta «sin propaganda»
  («sacerdote anticorrupción», «el terremoto que desacomoda»). Tiene 223 pares
  de negritas.
- **Provisional:** con una sola entrada no se puede saber si este formato
  volverá.

### 3.7 Prosa breve (`Fuego.md`, entrada única)

- **Qué hace.** Epígrafe de Pizarnik, segunda persona en voseo, imágenes que se
  encadenan (fiebre, hilo, brasas, león) y un cierre en verso.
- **Qué cambia.** No argumenta ni cita. El párrafo es la unidad rítmica.
- **Recomendación.** Las reglas de argumentación de este análisis no se le
  aplican. Lo único revisable es la economía: la imagen del león
  (`:78-87`) llega cuando la de las brasas (`:62`) ya había cerrado la idea.

### 3.8 Lo que comparten todos los formatos

Voseo como voz propia, antítesis, frases de remate, analogías concretas,
interés por la identidad y por lo que sostiene a una persona, y un cierre que
se vuelve hacia quien lee. Lo que más varía es el lugar de las fuentes (desde
ninguna hasta bibliografía numerada) y el registro (de clínico a lírico).

---

## 4. Debilidades recurrentes

Ordenadas por prioridad. Ninguna de estas debilidades debe imitarse.

### 4.1 Afirmaciones que exceden la evidencia o el argumento (prioridad alta)

**Observación.**

- **Matiz que se pierde al resumir.** `TDAH.md:80` dice que una mayor densidad
  del transportador de dopamina «**podría** conllevar una recaptación
  excesiva»; el resumen de `:92` afirma «**Hay** una recaptación excesiva de
  dopamina».
- **Causalidad sin respaldo.** La curva en «U invertida» «explica la
  procrastinación» (`TDAH.md:84`).
- **Exhaustividad declarada.** «Porque no hay salida lógica distinta… Todo lo
  demás son decoraciones conceptuales.» (`SN.md:94-102`)
- **Superlativos sin comparación.** «No existe nada comparable en ningún sistema
  filosófico o religioso.» (`Romanos.md:511`)
- **Conclusión más fuerte que el cuerpo.** El cuerpo de `Amor.md:24` dice que el
  amor «no puede sostenerse **solo** en los sentimientos»; el cierre afirma «El
  amor al final no se siente, se practica.» (`Amor.md:129`)
- **Categóricos clínicos sin fuente.** «en psiquiatría hay trastornos o
  condiciones, no enfermedades» (`TDAH.md:20`).

**Interpretación.** Son los puntos donde un lector crítico puede descartar el
texto entero. En las entradas más recientes (`Mentirnos.md`, `Juan.md`) el
problema disminuye porque hay frases de límite explícitas.

**Propuesta (antes/después, sin aplicar):**

> Antes (`TDAH.md:92`): «Hay una recaptación excesiva de dopamina y una baja
> disponibilidad de noradrenalina en áreas cerebrales clave, lo que dificulta
> el enfoque y la autorregulación.»
>
> Después: «Varios estudios encontraron más transportadores de dopamina y
> cambios en la noradrenalina. Eso podría reducir la dopamina disponible y
> dificultar el enfoque; es una hipótesis con apoyo, no un mecanismo
> cerrado.»

> Antes (`SN.md:94-102`): «Porque no hay salida lógica distinta. […] Todo lo
> demás son decoraciones conceptuales.»
>
> Después: «No encuentro una cuarta salida: las alternativas que conozco
> terminan reduciéndose a una de estas tres. Si existe otra, tendría que
> explicar por qué hay algo sin apoyarse en un fundamento, en una cadena
> infinita ni en un hecho bruto.»

> Antes (`Amor.md:129`): «El amor al final no se siente, se practica.»
>
> Después: «Al final, el amor no depende de lo que se siente: se practica.»

### 4.2 Fuentes: atribuciones imprecisas y sistemas mezclados (prioridad alta)

**Observación.**

- Conviven cuatro sistemas: bibliografía numerada con llamadas [n]
  (`narcicismo.md`, `anamnesis.md`), bibliografía sin llamadas (`TDAH.md`),
  notas al pie (`Mentirnos.md`, convertidas por un agente) y nada
  (`Amor.md`, `Juan.md`, `Romanos.md`, `Elecciones.md`, `Amarlaherida.md`).
- Fuentes débiles para cifras clínicas: blogs de centros de tratamiento
  (`narcicismo.md:256`, `:260`) para porcentajes de comorbilidad.
- Paráfrasis en cursiva que parecen citas textuales («Graham Oppy lo formula
  así: *el universo no necesita fundamento y punto*», `SN.md:83`).
- `Amarlaherida.md` es el mejor ejemplo de mediación honesta: nombra la
  Stanford Encyclopedia of Philosophy como intermediaria («La SEP resume esta
  idea…», `:54`), aunque sin enlace.

**Afirmaciones pendientes.** Ninguna se cambió. La verificación será un
encargo separado (decisión de Carlos). La tabla está en la sección 4.11,
ordenada por impacto.

**Propuesta (antes/después, sin aplicar):**

> Antes (`Amor.md:89`): «Platón, en El Banquete, contaba el mito del
> andrógino…»
>
> Después: «En *El Banquete*, Platón pone en boca de Aristófanes el mito del
> andrógino…»

### 4.3 Cierres en cascada (prioridad media)

**Observación.** Varias entradas tienen más de un cierre:

- `SN.md`: separador, «Conclusión», «La honestidad filosófica» y «Reflexión
  personal y cierre».
- `Romanos.md`: «¿qué queda para el alma?» (unas 50 líneas), un
  agradecimiento, «Prácticas para el alma» (sin encabezado) y una frase final.
- `narcicismo.md`: seis párrafos de conclusión que repiten la idea del espejo.
- `Amor.md:113-130`: ocho aforismos seguidos.
- `Elecciones.md`: tres subtítulos de conclusión.

**Interpretación.** Cada cierre repite el anterior con otras palabras y diluye
la frase final. En cambio, `Juan.md` y `Mentirnos.md` cierran una vez,
volviendo a su pregunta.

**Recomendación.** Una sola conclusión. Si hay prácticas o preguntas para el
lector, que sean una sección con encabezado propio, antes o después, pero no
otra conclusión. Carlos agregó una regla: la conclusión no puede aumentar el
grado de certeza ni eliminar los matices establecidos en el desarrollo
(`editorial-system.md`, 2.8).

### 4.4 Transiciones de andamio (prioridad media)

**Observación.** Frases que anuncian en vez de avanzar: «Bien, entonces,»
(`TDAH.md:33`), «Lo explico ahora:» (`TDAH.md:97`), «Esta parte es bastante
interesante e importante» (`TDAH.md:225`), «Entonces bueno.»
(`Mentirnos.md:206`), «Esto nos ocurre a todos. Exploremos la idea:»
(`Mentirnos.md:15`), «A continuación enlistaré» (`anamnesis.md:172`), «Ahora,
veamos un paneo limpio» (`Elecciones.md:311`). Además, dos entradas se llaman a
sí mismas «este blog» (`SN.md:31`, `Romanos.md:71`).

**Propuesta (antes/después, sin aplicar):**

> Antes (`Mentirnos.md:15-17`): «Esto nos ocurre a todos. Exploremos la idea:
> / Dos personas discuten.»
>
> Después: «Dos personas discuten.»

> Antes (`Mentirnos.md:206`): «Entonces bueno. La dificultad no consiste,
> entonces, en desconocer que los sesgos existen.»
>
> Después: «La dificultad, entonces, no está en desconocer que los sesgos
> existen.»

### 4.5 Cambios de registro dentro de un texto (prioridad media)

**Observación.**

- Voseo y tuteo mezclados: «Pensalo… ¿cuántas veces reconocés…?» y en la
  línea siguiente «si crees que no racionalizas» (`Mentirnos.md:192`);
  «Aprendes conceptos» (`:281`), «Mira el estudio» (`:299`) y «no perdás»
  (`:301`). «Imaginá que tenés» (`TDAH.md:23`) frente a «Imagina que tu
  cerebro» (`TDAH.md:100`).
- Saltos de tono no señalados: «INCORRECTO.» en mayúsculas
  (`Mentirnos.md:218`) dentro de un pasaje sereno.

**Interpretación.** El voseo es voz; la mezcla parece descuido. Los
coloquialismos («full», «otro rollo», «mi sangre») no son un problema en sí.
Carlos ya fijó el criterio para usarlos y para las mayúsculas enfáticas: ver
`editorial-system.md`, 1.3 y 7.

**Propuesta (antes/después, sin aplicar):**

> Antes (`Mentirnos.md:192`): «Ese último será el caso si crees que no
> racionalizas.»
>
> Después: «Y si creés que vos no racionalizás, probablemente estés en ese
> último caso.»

### 4.6 Abstracción sin anclaje (prioridad media)

**Observación.** Hay pasajes donde se encadenan sustantivos abstractos sin
ejemplo: «Es casi un organismo espiritual independiente, el espacio donde dos
libertades se inclinan sin quebrarse» (`Amor.md:94`); «se vuelve un principio
activo que reordena la vida» (`Juan.md:160`); «La descripción clínica del alma
desconectada de la Fuente» (`Romanos.md:241`). En contraste, los mejores
pasajes son concretos: los diálogos de `Mentirnos.md:114-128`, el muchacho con
apendicitis de `anamnesis.md:197` o las frases imaginadas de
`Amarlaherida.md:70`.

**Recomendación.** Cada afirmación abstracta importante debería tener un
ejemplo cerca. Muchas veces el ejemplo ya está en el mismo texto, en otro
lugar: `Amor.md:37` («callar cuando se quiere herir, escuchar cuando se quiere
huir, perdonar cuando se quiere ganar») podría anclar la idea del «vínculo
vivo» de `Amor.md:94`. **Un agente no debe inventar experiencias de Carlos
para crear ese anclaje:** puede proponer un ejemplo genérico, marcado como tal,
o pedírselo.

### 4.7 Extensión y redundancia en la divulgación clínica (prioridad media)

**Observación.** `TDAH.md` repite datos (la persistencia del 50–60 % en la
adultez aparece en `:34` y en `:228`) y usa «En suma», «En síntesis» o «En
resumen» siete veces. `narcicismo.md:109` y `:111` repiten la misma
frase. Hay subsecciones cuyo contenido ya se había dado (la definición de
`narcicismo.md` vuelve en tres lugares).

**Recomendación.** Decidir qué preguntas responde el texto y cortar lo que no
contribuye a ellas. Un «En suma» por sección, como máximo.

### 4.8 Énfasis inflado (prioridad baja)

**Observación.** Negritas en exceso: 223 pares en `Elecciones.md`, 70 en
`Juan.md` (incluidos cuatro párrafos enteros, `:134-140`), 53 en
`anamnesis.md`. En `Mentirnos.md` la cita en bloque (`>`) se usa para tres
cosas distintas: diálogos, preguntas y tesis del propio autor.

**Interpretación.** Cuando todo se destaca, nada se destaca. Y si el bloque de
cita marca a veces palabras ajenas y a veces propias, quien lee no sabe de
quién es la frase.

**Recomendación.** Negrita para una frase clave por sección, como mucho. La
cita en bloque, para palabras ajenas o diálogos. La frase propia más
importante puede ir en `cita:` (portada) o quedarse sola en su párrafo.

### 4.9 Errores de superficie recurrentes (prioridad baja)

Para corregir solo cuando Carlos lo pida y sin tocar el sentido:

- «por que» en lugar de «porque» (`Amarlaherida.md:41`, `TDAH.md:159`,
  `:323`);
- concordancias («La primer gran revelación», `Juan.md:86`; «El autoestima»,
  `TDAH.md:149`);
- frases cortadas o con palabras de menos («Porque la mente además de
  interpretar lo ocurrido. Pone en marcha…», `Mentirnos.md:21`; «nuestra se
  siente como la realidad», `:25`; «Aprendes conceptos como proyección… no
  elimina nuestros sesgos», `:281`);
- tildes y erratas («examén», `Romanos.md:457`; «Eso llevo a tensiones»,
  `Romanos.md:21`); un «}» suelto (`TDAH.md:36`);
- comillas mezcladas (“ ”, " " y « ») en el mismo texto.

### 4.10 Jerarquía de encabezados (prioridad baja)

Saltos de nivel (`IIEAN.md` usa `###` para su conclusión; `SN.md`, `####`),
seudotítulos en cursiva o negrita que no entran en el índice
(`Amarlaherida.md:21`, `:53`, `:63`) y secciones sin encabezado
(`Romanos.md:632`). Como el índice automático se arma con los `h2`, estos
saltos cambian lo que ve quien lee.

### 4.11 Pendientes priorizados

Ninguna entrada se modificó. La verificación contra las fuentes será un
encargo separado.

**Estado:**

- **Confirmado:** se comprueba leyendo el propio repositorio (una
  contradicción entre dos pasajes, una fuente ausente, una cifra que cambia
  entre dos líneas).
- **Sospecha:** depende de una fuente externa que este análisis **no
  consultó**. Puede resultar correcta. No se presenta como error hasta
  verificarla.

#### Prioridad 1: errores factuales y atribuciones

Ordenados por impacto: primero lo que puede afectar a personas reales, luego
las cifras clínicas y al final las atribuciones de citas.

| # | Ruta | Afirmación | Estado | Qué hay que comprobar |
| --- | --- | --- | --- | --- |
| 1.1 | `Elecciones.md:140-142` y el resto de la entrada | Señalamientos contra candidatos («Caso Pandora», «más de 280 millones de lempiras», contratos dudosos) | **Confirmado:** no tienen fuente. **Sospecha:** su exactitud, que no se evaluó | Fuente de cada señalamiento. Si no la hay, reformular o retirar. |
| 1.2 | `Elecciones.md` | Propuestas y cifras de los programas (311 000 viviendas, 5000 km, etc.) | **Confirmado:** no tienen fuente | Plan de gobierno o declaración que respalde cada cifra. |
| 1.3 | `anamnesis.md:30` | Hampton et al. (1975): «el 66–80 % de los diagnósticos» | **Sospecha** | Si el artículo dice «66 de 80 pacientes» (≈ 82 %), no es un rango. |
| 1.4 | `narcicismo.md:182` | Comorbilidad del 57 % y del 40 %, respaldada en un artículo de revista profesional [6] y un blog de un centro de tratamiento [7] | **Confirmado:** las fuentes citadas son secundarias o comerciales. **Sospecha:** las cifras | Estudio original o revisión con la misma población y resultado. |
| 1.5 | `TDAH.md` (todo el cuerpo) | Cifras de prevalencia, heredabilidad, comorbilidad y pronóstico | **Confirmado:** la bibliografía no está enlazada a ninguna afirmación; no se sabe qué fuente respalda cada cifra | Asignar a cada cifra su fuente o marcarla. |
| 1.6 | `Mentirnos.md:130` | Mezulis: «El 89 % de las muestras» | **Sospecha** (ya en `visual-system.md`, 11) | Cifra en el artículo completo. |
| 1.7 | `TDAH.md:20` | «en psiquiatría hay trastornos o condiciones, no enfermedades» | **Confirmado:** sin fuente | Si es convención terminológica (DSM/CIE) o postura del autor. |
| 1.8 | `Amor.md:89` | «Platón, en El Banquete, contaba el mito del andrógino» | **Sospecha** | Si en el diálogo el mito lo cuenta Aristófanes. |
| 1.9 | `SN.md:83` | Parfit «lo llamó "brute fact"»; frase de Oppy en cursiva | **Sospecha** | Origen de la expresión; si la frase de Oppy es cita o paráfrasis. |
| 1.10 | `Romanos.md:172` | «Dios no nos pide lo que no nos da…» (Agustín) | **Sospecha** | Si es paráfrasis de «Da quod iubes et iube quod vis» (*Confesiones* X). |
| 1.11 | `Juan.md:104` | μένω aparece «23 veces» en 1 Juan | **Sospecha** | Recuento según el texto griego y las formas contadas. |
| 1.12 | `IIEAN.md:74` | Cita de Miyamoto Musashi | **Confirmado:** sin fuente. **Sospecha:** su autenticidad | Localizarla en *El libro de los cinco anillos*; si no aparece, retirarla o presentarla como «atribuida». |
| 1.13 | `Romanos.md:348` | Cita atribuida a Nietzsche | **Confirmado:** sin fuente. **Sospecha:** su autenticidad | Ídem. |
| 1.14 | `Amor.md:107-108` | Cita atribuida a «Coelho (inspirado en el Tao)» | **Confirmado:** sin fuente. **Sospecha:** su autenticidad | Ídem. |

#### Prioridad 2: contradicciones y saltos argumentales

Todos están **confirmados**: se comprueban leyendo las entradas.

| # | Ruta | Problema |
| --- | --- | --- |
| 2.1 | `Trinidad.md:59` frente a `SN.md:162` | La parte 2 da por demostrada la existencia del ser necesario («Una vez concluimos que, efectivamente, existe»); la parte 1 dice «No hay demostraciones finales» y defiende solo que es la postura «más estable». |
| 2.2 | `TDAH.md:80` frente a `:92` | Un «podría conllevar» se convierte en «Hay una recaptación excesiva». |
| 2.3 | `Amor.md:24` frente a `:129` | El cuerpo dice «no solo en los sentimientos»; el cierre, «no se siente». |
| 2.4 | `SN.md:94-102` | «No hay salida lógica distinta» se afirma sin argumento. |
| 2.5 | `TDAH.md:84` | La curva en «U invertida» «explica la procrastinación», sin respaldo. |
| 2.6 | `Romanos.md:511` | «No existe nada comparable en ningún sistema filosófico o religioso», sin comparación. |
| 2.7 | `Elecciones.md:10` | Promete basarse «únicamente en propuestas verificables, documentos oficiales y evidencia pública», pero no cita ninguna. |

#### Prioridad 3: claridad y estilo

Están descritos en las secciones 4.3 a 4.10. Los más visibles son estos
(todos **confirmados**):

- frases cortadas o incompletas: `Mentirnos.md:21`, `:25` y `:281`;
- una frase repetida: `narcicismo.md:109` y `:111`;
- cierres sucesivos: `SN.md`, `Romanos.md`, `narcicismo.md` y `Amor.md`;
- voseo y tuteo mezclados: `Mentirnos.md` y `TDAH.md`.

---

## 5. Lo que conviene conservar (síntesis)

1. La pregunta o tesis explícita al principio (2.7).
2. El matiz y la objeción cuando aparecen (2.8).
3. El voseo y el habla hondureña como voz del autor (2.4).
4. Las analogías concretas, en especial las clínicas (2.5).
5. La antítesis y la frase de remate, dosificadas (2.1, 2.2).
6. Los ejemplos y diálogos breves (`Mentirnos.md`, `anamnesis.md`).
7. La separación de planos entre argumento y convicción (`SN.md:133`,
   `SN.md:170-194`).
8. La mediación declarada de las fuentes (`Amarlaherida.md`).

## 6. Mejoras prioritarias

1. Ajustar cada afirmación a su respaldo, sobre todo en resúmenes y
   conclusiones (4.1).
2. Notas al pie para las entradas nuevas y verificar los pendientes, en el
   orden de 4.11 (4.2).
3. Una sola conclusión por texto (4.3).
4. Un solo registro de tratamiento por texto (4.5).
5. Un ejemplo cerca de cada abstracción importante (4.6).

## 7. Decisiones de Carlos sobre este análisis

Carlos respondió las preguntas de la primera versión. Las decisiones están
registradas, con su alcance, en la sección 7 de
[`editorial-system.md`](editorial-system.md). En resumen:

1. **Registro:** el voseo es la norma cuando se le habla al lector, también en
   divulgación médica, pero la explicación impersonal es válida. Las
   expresiones hondureñas, solo si salen naturalmente; nada de mayúsculas
   enfáticas habituales.
2. **Fuentes:** notas al pie como sistema principal en entradas nuevas. Cada
   cifra clínica debe tener una fuente que respalde su población, su resultado
   y su contexto.
3. **Actualidad:** sin categoría nueva por ahora. Hechos, interpretación y
   opinión, separados; las afirmaciones que afecten a personas o instituciones
   llevan respaldo o se retiran.
4. **Cierres:** la pregunta al lector es opcional. La conclusión no puede
   aumentar la certeza ni eliminar los matices del desarrollo.
5. **Pendientes:** se verificarán en un encargo separado, en el orden de la
   sección 4.11.

## 8. Limitaciones del análisis

- **Corpus pequeño:** 13 entradas. Tres de los siete formatos (3.2, 3.6 y
  3.7) tienen una sola muestra y son provisionales; los demás, dos o tres.
- **Fechas no fiables para hablar de evolución:** un agente cambió fechas y
  nombres de archivo en `1e59c8e`. Se describen diferencias entre entradas, no
  una evolución en el tiempo.
- **Ediciones ajenas:** las descripciones, los niveles de encabezado y algunas
  notas fueron tocados por agentes (sección 1). Lo que podría venir de esas
  ediciones no se usó como evidencia de voz.
- **Recuentos aproximados:** las cifras de palabras, negritas y longitud de
  párrafos salen de un conteo automático sobre el Markdown. Sirven para
  comparar, no como medidas exactas.
- **Verificación de fuentes:** este análisis no consultó las fuentes externas.
  En la tabla 4.11, «confirmado» se refiere solo a lo que se comprueba dentro
  del repositorio; todo lo que depende de una fuente externa es una sospecha.
- **Sin intención del autor:** no se preguntó a Carlos por qué escribió cada
  texto como lo hizo. Las interpretaciones describen efectos probables en
  quien lee.
