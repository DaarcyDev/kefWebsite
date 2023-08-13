var generoSeleccionado = "";
var categoriaSeleccionada = "";
document.getElementById("btnMujer").addEventListener("click", function () {
  generoSeleccionado = "mujer";
  if (!categoriaSeleccionada) {
    mostrarRopa("mujer");
  } else {
    mostrarRopaCategoria(categoriaSeleccionada);
  }
  
});

document.getElementById("btnHombre").addEventListener("click", function () {
  generoSeleccionado = "hombre";
  if (!categoriaSeleccionada) {
    mostrarRopa("hombre");
  } else {
    mostrarRopaCategoria(categoriaSeleccionada);
  }
});

document.getElementById("btnNiño").addEventListener("click", function () {
  generoSeleccionado = "niño";
  if (!categoriaSeleccionada) {
    mostrarRopa("niño");
  } else {
    mostrarRopaCategoria(categoriaSeleccionada);
  }
});

document.getElementById("btnRopa").addEventListener("click", function() {
  categoriaSeleccionada = "Ropa"
  mostrarRopaCategoria("Ropa");
});

document.getElementById("btnAccesorios").addEventListener("click", function() {
  categoriaSeleccionada = "Accesorios"
  mostrarRopaCategoria("Accesorios");
});

document.getElementById("btnDeporte").addEventListener("click", function() {
  categoriaSeleccionada = "Deporte"
  mostrarRopaCategoria("Deporte");
});

document.getElementById("btnZapatos").addEventListener("click", function () {
  categoriaSeleccionada = "Zapatos"
  mostrarRopaCategoria("Zapatos");
});

document.getElementById("btnRopaInterior").addEventListener("click", function () {
  categoriaSeleccionada = "RopaInterior"
  mostrarRopaCategoria("RopaInterior");
});

document.getElementById("btnRopaBaño").addEventListener("click", function () {
  categoriaSeleccionada = "RopaBaño"
  mostrarRopaCategoria("RopaBaño");
});

document.getElementById("btnCamisa").addEventListener("click", function() {
  categoriaSeleccionada = "Camisa"
  mostrarRopaCategoria("Camisa");
});

document.getElementById("btnPantalones").addEventListener("click", function() {
  categoriaSeleccionada = "Pantalones"
  mostrarRopaCategoria("Pantalones");
});

document.getElementById("btnChaquetas").addEventListener("click", function() {
  categoriaSeleccionada = "Chaquetas"
  mostrarRopaCategoria("Chaquetas");
});

document.getElementById("btnZapatosVestir").addEventListener("click", function () {
  categoriaSeleccionada = "ZapatosVestir"
  mostrarRopaCategoria("ZapatosVestir");
});

document.getElementById("btnTrajes").addEventListener("click", function () {
  categoriaSeleccionada = "Trajes"
  mostrarRopaCategoria("Trajes");
});

document.getElementById("btnJeans").addEventListener("click", function () {
  categoriaSeleccionada = "Jeans"
  mostrarRopaCategoria("Jeans");
});

document.getElementById("btnPolos").addEventListener("click", function() {
  categoriaSeleccionada = "Polos"
  mostrarRopaCategoria("Polos");
});

document.getElementById("btnBolsos").addEventListener("click", function() {
  categoriaSeleccionada = "Bolsos"
  mostrarRopaCategoria("Bolsos");
});

document.getElementById("btnVestidos").addEventListener("click", function() {
  categoriaSeleccionada = "Vestidos"
  mostrarRopaCategoria("Vestidos");
});

document.getElementById("btnFaldas").addEventListener("click", function () {
  categoriaSeleccionada = "Faldas"
  mostrarRopaCategoria("Faldas");
});

document.getElementById("btnBlusas").addEventListener("click", function () {
  categoriaSeleccionada = "Blusas"
  mostrarRopaCategoria("Blusas");
});

document.getElementById("btnZapatosTacon").addEventListener("click", function () {
  categoriaSeleccionada = "ZapatosTacon"
  mostrarRopaCategoria("ZapatosTacon");
});

document.getElementById("btnPijamas").addEventListener("click", function() {
  categoriaSeleccionada = "Pijamas"
  mostrarRopaCategoria("Pijamas");
});

document.getElementById("btnPlayeras").addEventListener("click", function() {
  categoriaSeleccionada = "Playeras"
  mostrarRopaCategoria("Playeras");
});


function mostrarRopa(genero) {

  generoSeleccionado = genero
  // Ocultar todos los elementos de ropa
  var elementosRopa = document.getElementsByClassName("prendas");
  for (var i = 0; i < elementosRopa.length; i++) {
    elementosRopa[i].style.display = "none";
  }

  // Mostrar solo los elementos de ropa del género seleccionado
  var elementosFiltrados = document.getElementsByClassName(generoSeleccionado + " " + categoriaSeleccionada);
  for (var j = 0; j < elementosFiltrados.length; j++) {
    elementosFiltrados[j].style.display = "block";
  }
}

function mostrarRopaCategoria(genero) {

  categoriaSeleccionada = genero
  // Ocultar todos los elementos de ropa
  var elementosRopa = document.getElementsByClassName("ropa");
  for (var i = 0; i < elementosRopa.length; i++) {
    elementosRopa[i].style.display = "none";
  }

  // Mostrar solo los elementos de ropa del género seleccionado
  var elementosFiltrados = document.getElementsByClassName(generoSeleccionado + " " + categoriaSeleccionada);
  for (var j = 0; j < elementosFiltrados.length; j++) {
    elementosFiltrados[j].style.display = "block";
  }
}

