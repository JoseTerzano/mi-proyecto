document.addEventListener("DOMContentLoaded",function(){
    let div = document.getElementById("espacio");
    let agregar = document.getElementById("Agregar");
    let eliminar = document.getElementById("Eliminar");

    agregar.addEventListener("click", function(){
        let nuevoparrafo = document.createElement("p");

        nuevoparrafo.textContent = "Es un nuevo parrafo";

        div.appendChild(nuevoparrafo);
    })

    eliminar.addEventListener("click", function(){
        if (div.lastElementChild){
            div.removeChild(div.lastElementChild);
        }else{
        document.getElementById("parrafo-nuevo").innerText = "No hay elementos a eliminar";
        }
    })
})