// El cuaderno: mejoras progresivas. Sin JavaScript todo sigue siendo legible:
// el índice está abierto, las llamadas de nota enlazan con «Fuentes» y vuelven
// con «↩», el archivo muestra todas las entradas y las tablas se desplazan solas.
(function () {
  var ancho = window.matchMedia("(min-width: 1100px)");
  var alCambiarAncho = function (fn) {
    if (ancho.addEventListener) ancho.addEventListener("change", fn);
    else if (ancho.addListener) ancho.addListener(fn);
  };

  // 1. Menú móvil (<details>): se cierra con Escape (y el foco vuelve a
  //    «Menú»), al salir el foco del menú y al tocar fuera. Así el foco nunca
  //    avanza detrás del panel abierto.
  var menu = document.querySelector(".mobile-menu");
  if (menu) {
    var resumen = menu.querySelector("summary");
    menu.addEventListener("keydown", function (ev) {
      if (ev.key === "Escape" && menu.open) {
        menu.open = false;
        resumen.focus();
      }
    });
    menu.addEventListener("focusout", function (ev) {
      if (menu.open && ev.relatedTarget && !menu.contains(ev.relatedTarget)) menu.open = false;
    });
    document.addEventListener("click", function (ev) {
      if (menu.open && !menu.contains(ev.target)) menu.open = false;
    });
  }

  // 2. Índice: abierto en escritorio, plegado en móvil, también al cambiar de
  //    ancho. Marca la sección actual con aria-current="location".
  var toc = document.querySelector(".toc-movil");
  if (toc) {
    var ajustarIndice = function () { toc.open = ancho.matches; };
    ajustarIndice();
    alCambiarAncho(ajustarIndice);
    var enlaces = toc.querySelectorAll("a");
    if ("IntersectionObserver" in window && enlaces.length) {
      var porId = {};
      enlaces.forEach(function (a) { porId[decodeURIComponent(a.hash.slice(1))] = a; });
      var obs = new IntersectionObserver(function (entradas) {
        entradas.forEach(function (e) {
          if (e.isIntersecting && porId[e.target.id]) {
            enlaces.forEach(function (a) { a.removeAttribute("aria-current"); });
            porId[e.target.id].setAttribute("aria-current", "location");
          }
        });
      }, { rootMargin: "0px 0px -70% 0px" });
      Object.keys(porId).forEach(function (id) {
        var h = document.getElementById(id);
        if (h) obs.observe(h);
      });
    }
  }

  // 3. Notas. La llamada <sup id="fnref:…"><a href="#fn:…"> se conserva: es el
  //    destino de «↩» y, en escritorio, lleva a «Fuentes».
  //    - Escritorio: copia visual al margen, oculta para tecnologías de apoyo
  //      (la nota completa sigue en «Fuentes», sin lectura duplicada).
  //    - Móvil: un botón dentro del mismo <sup> despliega la nota bajo el párrafo.
  //    El CSS muestra el enlace o el botón según el ancho.
  var llamadas = document.querySelectorAll(".prose sup[id^='fnref']");
  llamadas.forEach(function (sup, i) {
    var link = sup.querySelector("a.footnote");
    if (!link) return;
    var nota = document.getElementById(decodeURIComponent(link.hash.slice(1)));
    var bloque = sup.closest("p, li, blockquote");
    if (!nota || !bloque || nota.contains(sup)) return;
    var n = i + 1;
    nota.querySelectorAll(".reversefootnote").forEach(function (r) {
      r.setAttribute("aria-label", "Volver al pasaje de la fuente " + n);
    });
    var contenido = function () {
      var copia = nota.cloneNode(true);
      copia.querySelectorAll(".reversefootnote").forEach(function (r) { r.remove(); });
      return '<span class="nota-num">' + n + "</span>" + copia.innerHTML.replace(/<\/?p>/g, " ");
    };

    var margen = document.createElement("div");
    margen.className = "nota-margen";
    margen.setAttribute("aria-hidden", "true");
    margen.innerHTML = contenido();
    margen.querySelectorAll("a").forEach(function (a) { a.setAttribute("tabindex", "-1"); });
    bloque.insertAdjacentElement("beforebegin", margen);

    var desplegable = document.createElement("div");
    desplegable.className = "nota-desplegable";
    desplegable.id = "nota-" + n;
    desplegable.setAttribute("role", "note");
    desplegable.setAttribute("aria-label", "Fuente " + n);
    desplegable.hidden = true;
    desplegable.innerHTML = contenido();
    bloque.insertAdjacentElement("afterend", desplegable);

    var btn = document.createElement("button");
    btn.type = "button";
    btn.className = "nota-ref";
    btn.textContent = n;
    btn.setAttribute("aria-expanded", "false");
    btn.setAttribute("aria-controls", desplegable.id);
    btn.setAttribute("aria-label", "Fuente " + n);
    btn.addEventListener("click", function () {
      var abrir = desplegable.hidden;
      desplegable.hidden = !abrir;
      btn.setAttribute("aria-expanded", String(abrir));
    });
    sup.appendChild(btn);
  });
  if (llamadas.length) document.querySelector(".prose").classList.add("con-notas");

  // 4. Archivo: filtro por tema, con el conteo visible actualizado y un
  //    mensaje de estado para lectores de pantalla.
  var filtros = document.querySelector(".filtros");
  if (filtros) {
    filtros.hidden = false;
    var cuenta = document.getElementById("archivo-cuenta");
    var estado = document.getElementById("archivo-estado");
    var total = cuenta ? cuenta.dataset.total : "";
    filtros.addEventListener("click", function (ev) {
      var b = ev.target.closest("button");
      if (!b) return;
      var t = b.dataset.filtro;
      filtros.querySelectorAll("button").forEach(function (x) { x.setAttribute("aria-pressed", String(x === b)); });
      document.querySelectorAll(".indice-fila").forEach(function (f) { f.hidden = t !== "todos" && f.dataset.tema !== t; });
      document.querySelectorAll(".anio").forEach(function (a) { a.hidden = !a.querySelector(".indice-fila:not([hidden])"); });
      var visibles = document.querySelectorAll(".indice-fila:not([hidden])").length;
      var palabra = visibles === 1 ? "entrada" : "entradas";
      var texto = t === "todos"
        ? total + " entradas, de la más reciente a la más antigua."
        : visibles + " de " + total + " entradas · " + b.dataset.nombre + ", de la más reciente a la más antigua.";
      if (cuenta) cuenta.textContent = texto;
      if (estado) estado.textContent = t === "todos"
        ? "Mostrando las " + total + " entradas."
        : "Mostrando " + visibles + " " + palabra + " de " + b.dataset.nombre + ".";
    });
  }

  // 5. Tablas anchas: el marco que se desplaza recibe el foco y un nombre
  //    solo cuando el contenido desborda.
  var tablas = document.querySelectorAll(".prose table");
  if (tablas.length) {
    var marcos = [];
    tablas.forEach(function (tabla, i) {
      var marco = document.createElement("div");
      marco.className = "tabla-marco";
      tabla.parentNode.insertBefore(marco, tabla);
      marco.appendChild(tabla);
      var previo = marco.previousElementSibling, titulo = "";
      while (previo && !titulo) {
        if (/^H[2-6]$/.test(previo.tagName)) titulo = previo.textContent.trim();
        previo = previo.previousElementSibling;
      }
      marco.dataset.nombre = "Tabla " + (i + 1) + (titulo ? ": " + titulo : "");
      marcos.push(marco);
    });
    var revisar = function () {
      marcos.forEach(function (m) {
        if (m.scrollWidth > m.clientWidth + 1) {
          m.setAttribute("tabindex", "0");
          m.setAttribute("role", "region");
          m.setAttribute("aria-label", m.dataset.nombre + " (se desplaza horizontalmente)");
        } else {
          m.removeAttribute("tabindex");
          m.removeAttribute("role");
          m.removeAttribute("aria-label");
        }
      });
    };
    revisar();
    window.addEventListener("resize", revisar);
  }
})();
