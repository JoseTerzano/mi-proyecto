const eventoBox = document.getElementById("eventoBox"); /* obtiene el elemento con id eventoBox */
const eventoButton = document.getElementById("eventoButton"); /* obtiene el elemento con id eventoButton */
const eventoKey = document.getElementById("eventoKey"); /* obtiene el elemento con id eventoKey */

/* Evento de poner el raton sobre el elemento eventoBox */
eventoBox.addEventListener("mouseover", function(){
    eventoBox.style.backgroundColor = "lightgreen";
    eventoBox.textContent = "¡Pusiste en Mouse en la Caja!";
    });

/* Evento de poner el raton fuera del elemento eventoBox */
eventoBox.addEventListener("mouseout", function(){
    eventoBox.style.backgroundColor = "lightgray";
    eventoBox.textContent = "Pasa el raton aqui";
    });

/* Evento de click en el elemento eventoBox */
eventoBox.addEventListener("click", function(){
    eventoBox.style.backgroundColor = "red";
    eventoBox.textContent = "¡AUCH! Hiciste 1 Click";
    });

/* Evento de doble click en el elemento eventoBox */
eventoBox.addEventListener("dblclick", function(){
    eventoBox.style.backgroundColor = "red";
    eventoBox.textContent = "¡AUCH! Hiciste 2 Doble Click";
    });

/* Evento de presionar una tecla */
document.addEventListener("keydown", function(event){
    eventoKey.textContent = "Presionaste la tecla: " + event.key;
    });

/* Evento de soltar una tecla */
document.addEventListener("keyup", function(event){
    eventoKey.textContent = "Soltaste la tecla: " + event.key;
    });
/* Evento de MouseUp y MouseDown en eventoButton */
eventoButton.addEventListener("mousedown", function(){
    eventoButton.style.border = " 1px solid red";
    eventoButton.textContent = "Boton Presionado";
    });
eventoButton.addEventListener("mouseup", function(){
    eventoButton.style.border = " 1px solid green";
    eventoButton.textContent = "Boton Soltado";
    });