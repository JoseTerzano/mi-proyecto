// Función para saludar al usuario
function saludar() {
    const saludoElemento = document.getElementById('saludo');
    saludoElemento.textContent = "¡Hola, usuario! Bienvenido al Práctico N° 3.";
}

// Cambiar el color del header y footer después de 5 segundos
setTimeout(() => {
    document.querySelector('header').style.backgroundColor = 'lightgreen';
    document.querySelector('footer').style.backgroundColor = 'lightgreen';
}, 5000);

// Obtener datos de la API al hacer clic en el botón GET DATA
document.getElementById("getDataBtn").addEventListener("click", getData);

function getData() {
    fetch('https://jsonplaceholder.typicode.com/posts')
        .then(response => response.json())
        .then(data => {
            // Mostrar solo los primeros 10 elementos
            const primerosDiez = data.slice(0, 10);

            // Verificar si el contenedor de la lista ya existe, si no, crearlo
            let lista = document.getElementById('dataList');
            if (!lista) {
                lista = document.createElement('ul'); // Crear una lista desordenada
                lista.id = 'dataList'; // Añadir un ID para futuras referencias
                document.body.appendChild(lista); // Insertar la lista en el body
            } else {
                lista.innerHTML = ''; // Limpiar la lista si ya existe
            }

            // Añadir los elementos a la lista
            primerosDiez.forEach(item => {
                const li = document.createElement('li');
                li.textContent = item.title;
                lista.appendChild(li);
            });
        })
        .catch(error => console.error('Error:', error));
}
