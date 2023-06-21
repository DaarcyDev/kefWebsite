document.getElementById("btnMujer").addEventListener("click", function() {
    mostrarRopa("mujer");
  });
  
  document.getElementById("btnHombre").addEventListener("click", function() {
    mostrarRopa("hombre");
  });

  document.getElementById("btnNiño").addEventListener("click", function() {
    mostrarRopa("niño");
  });
  
  function mostrarRopa(genero) {
    // Ocultar todos los elementos de ropa
    var elementosRopa = document.getElementsByClassName("ropa");
    for (var i = 0; i < elementosRopa.length; i++) {
      elementosRopa[i].style.display = "none";
      
    }
    // Mostrar solo los elementos de ropa del género seleccionado
    var elementosFiltrados = document.getElementsByClassName(genero);
    for (var j = 0; j < elementosFiltrados.length; j++) {
      elementosFiltrados[j].style.display = "block";
    }
  }
  