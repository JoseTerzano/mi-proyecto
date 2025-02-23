function ActualizarReloj() {
    var objetoHora = new Date();
    var hora = padZero(objetoHora.getHours());
    var minutos = padZero(objetoHora.getMinutes());
    var segundos = padZero(objetoHora.getSeconds());

    var options = {weekday:"short", year:"numeric", month:"short", day:"numeric"};

    var fechaString = new Date().toLocaleDateString("es-ES", options);

    var tiempoString = hora + ":" + minutos + ":" + segundos;

    document.getElementById("tiempo").textContent = tiempoString;
    document.getElementById("fecha").textContent = fechaString;

    setTimeout(ActualizarReloj, 1000);
    }

function padZero(numero) {
    return numero < 10 ? "0" + numero : numero;
}

ActualizarReloj();