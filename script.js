function enviar() {
  const mensaje = document.getElementById("mensaje").value;
  document.getElementById("respuesta").textContent = "Has dicho: " + mensaje;
}