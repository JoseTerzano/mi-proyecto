const tittle = document.getElementById("ejemplo_id"); /* obtiene el elemento con id ejemplo_id */
console.log("El titulo es: " + tittle);
tittle.style.color = "blue";

const parrafos = document.getElementsByClassName("ejemplo_class"); /* obtiene todos los elementos con clase ejemplo_class */
console.log("Los parrafos que tienen esa claseson: " + parrafos);

for (let i = 0; i < parrafos.length; i++){ /* itera sobre todos los elementos de  parrafos */
    parrafos[i].style.fontSize = "50px";
    }

const spans = document.getElementsByTagName("span"); /* obtiene todos los elementos con tag span */
console.log("Los spans son: " + spans);

for (let i = 0; i < spans.length; i++){ /* itera sobre todos los elementos de  spans */
    spans[i].style.backgroundColor = "yellow";
    }

const container = document.querySelector(".container"); /* accediendo a un solo elemento de la class container */
console.log("El elemento con class container es: " + container);
container.style.border = "1px solid black";

const todosParrafos = document.querySelectorAll(".ejemplo_class"); /* obtiene todos los elementos de la class ejemplo_class */
console.log("Los elementos con class ejemplo_class son: " + todosParrafos);
todosParrafos.forEach(parrafo => {parrafo.style.fontSize = "20px"}); /* itera sobre todos los elementos de todosParrafos */