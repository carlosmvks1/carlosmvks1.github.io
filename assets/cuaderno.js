// El cuaderno: mejoras progresivas. Sin JavaScript todo sigue siendo legible:
// el índice se abre a mano y las fuentes quedan al final del texto.
(function () {
  var ancho = window.matchMedia("(min-width: 1100px)");

  // 1. Índice: abierto en escritorio, plegado en móvil; marca la sección actual.
  var toc = document.querySelector(".toc-movil");
  if (toc) {
    toc.open = ancho.matches;
    var enlaces = toc.querySelectorAll("a");
    if ("IntersectionObserver" in window && enlaces.length) {
      var porId = {};
      enlaces.forEach(function (a) { porId[decodeURIComponent(a.hash.slice(1))] = a; });
      var obs = new IntersectionObserver(function (entradas) {
        entradas.forEach(function (e) {
          if (e.isIntersecting && porId[e.target.id]) {
            enlaces.forEach(function (a) { a.classList.remove("activo"); });
            porId[e.target.id].classList.add("activo");
          }
        });
      }, { rootMargin: "0px 0px -70% 0px" });
      Object.keys(porId).forEach(function (id) {
        var h = document.getElementById(id);
        if (h) obs.observe(h);
      });
    }
  }

  // 2. Fuentes junto al pasaje: copia cada nota al pie después de su párrafo.
  //    En escritorio flota en el margen; en móvil se abre con el número.
  document.querySelectorAll(".prose sup[id^='fnref']").forEach(function (sup, i) {
    var link = sup.querySelector("a");
    if (!link) return;
    var nota = document.getElementById(decodeURIComponent(link.hash.slice(1)));
    var bloque = sup.closest("p, li, blockquote");
    if (!nota || !bloque) return;
    var n = i + 1;
    var aside = document.createElement("aside");
    aside.className = "nota-margen";
    aside.id = "nota-margen-" + n;
    var contenido = nota.cloneNode(true);
    contenido.querySelectorAll(".reversefootnote").forEach(function (r) { r.remove(); });
    aside.innerHTML = '<span class="nota-num">' + n + "</span>" + contenido.innerHTML.replace(/<\/?p>/g, " ");
    // En escritorio va antes del párrafo (así flota a su altura en el margen);
    // en móvil, después, para abrirse bajo el pasaje.
    var colocar = function () { bloque.insertAdjacentElement(ancho.matches ? "beforebegin" : "afterend", aside); };
    colocar();
    if (ancho.addEventListener) ancho.addEventListener("change", colocar);

    var btn = document.createElement("button");
    btn.type = "button";
    btn.className = "nota-ref";
    btn.textContent = n;
    btn.setAttribute("aria-expanded", "false");
    btn.setAttribute("aria-controls", aside.id);
    btn.setAttribute("aria-label", "Fuente " + n);
    btn.addEventListener("click", function () {
      var abierta = aside.classList.toggle("abierta");
      btn.setAttribute("aria-expanded", String(abierta));
    });
    sup.replaceWith(btn);
  });

  // 3. Archivo: filtro por tema.
  var filtros = document.querySelector(".filtros");
  if (filtros) {
    filtros.hidden = false;
    filtros.addEventListener("click", function (ev) {
      var b = ev.target.closest("button");
      if (!b) return;
      var t = b.dataset.filtro;
      filtros.querySelectorAll("button").forEach(function (x) { x.setAttribute("aria-pressed", String(x === b)); });
      document.querySelectorAll(".indice-fila").forEach(function (f) { f.hidden = t !== "todos" && f.dataset.tema !== t; });
      document.querySelectorAll(".anio").forEach(function (a) { a.hidden = !a.querySelector(".indice-fila:not([hidden])"); });
    });
  }
})();
