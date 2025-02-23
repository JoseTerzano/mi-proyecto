document.addEventListener("DOMContentLoaded",function(){
    let boton = document.getElementById("boton");
    let costo;
    let contenedor = document.getElementById("colocar-parrafo");
    boton.addEventListener("click", function(){
        let destino = document.getElementById("destino").value;
        let dias = document.getElementById("dias").value;
        let presupuesto = document.getElementById("presupuesto").value;
        let opciones = document.getElementById("opciones").value;
        if (destino === "" || dias <= 0 || presupuesto <= 0 || opciones === ""){
            let nuevoparrafo = document.createElement("p");
            nuevoparrafo.textContent = "Error en la Validacion de Datos";
            contenedor.appendChild(nuevoparrafo);
            nuevoparrafo.style.fontWeight = "bold";
            nuevoparrafo.style.fontSize = "25px";
            nuevoparrafo.style.textAlign = "center";
        }else if (opciones == "Economico"){
            costo = (30*dias);
        }else if (opciones == "Estandar"){
            costo = (50*dias);
        }else if (opciones == "Lujoso"){
            costo = (100*dias);
        }
        if (costo > presupuesto){
            document.getElementById("respuesta").textContent = "Dinero Insuficiente";
            document.getElementById("respuesta").style.fontWeight = "bold";
            document.getElementById("respuesta").style.fontSize = "25px";
            document.getElementById("respuesta").style.textAlign = "center";
            document.getElementById("respuesta").style.backgroundColor = "red";
        }else if (costo <= presupuesto){
            document.getElementById("respuesta").textContent = "Dinero Suficiente";
            document.getElementById("respuesta").style.fontWeight = "bold";
            document.getElementById("respuesta").style.fontSize = "25px";
            document.getElementById("respuesta").style.textAlign = "center";
            document.getElementById("respuesta").style.backgroundColor = "green";
        }
    })    

})