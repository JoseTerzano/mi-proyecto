const container = document.getElementById("container"); /* obtiene el elemento con id container */

const addElemento = document.getElementById("addElemento"); /* obtiene el elemento con id addElemento */
const removeElemento = document.getElementById("removeElemento"); /* obtiene el elemento con id removeElemento */

addElemento.addEventListener("click", function(){ /*Crea un evento click para el boton addElemento */
    const newParrafo = document.createElement("p"); /* crea un nuevo elemento p */

    newParrafo.textContent = "Este es un nuevo parrafo que acabamos de crear"; /* asigna el texto a la propiedad textContent del nuevo parrafo */

    newParrafo.className = 'NuevoParrafo'; /* asigna la clase NuevoParrafo al nuevo parrafo */

    container.appendChild(newParrafo); /* agrega el nuevo parrafo al elemento con id container */    
});

/*Ahora eliminamos el ultimo parrafo que acabamos de crear */
removeElemento.addEventListener("click", function(){
    if (container.lastElementChild){
        container.removeChild(container.lastElementChild);
    } else {
        alert("No hay elementos que eliminar");
        }
});