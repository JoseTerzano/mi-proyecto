
function testVar() {
    var x = 1;
    if (true) {
        var x = 2; // Misma variable, se sobrescribe
        console.log("Dentro del bloque, var x:", x); // Imprime 2
    }
    console.log("Fuera del bloque, var x:", x); // También imprime 2
}

function testLet() {
    let y = 1;
    if (y == 1) {
        let y = 2; // Nueva variable, solo existe en este bloque
        console.log("Dentro del bloque, let y:", y); // Imprime 2
    }
    console.log("Fuera del bloque, let y:", y); // Imprime 1
}

function testConst() {
    const z = 3;
    if (z == 3) {
        const z = 4; // Nueva variable, solo existe en este bloque
        console.log("Dentro del bloque, const z:", z); // Imprime 4
    }
    console.log("Fuera del bloque, const z:", z); // Imprime 3
}

// Ejemplo de Hoisting
console.log(miVar); // Imprime "undefined"
var miVar = 5;
console.log(miVar); // Imprime 5

// Ejemplo de Hoisting 
console.log(miLet); // ReferenceError: Cannot access 'miLet' before initialization // Em vez de imprimit undefined imrime el error
let miLet = 10;

//Ejemplo Arreglo

const arreglo = [1, 2, 3, 4, 5, 6, 11, 23, 1, 989, 0, 1, 111, 645, 50, 45];

// 1. Retornar el menor elemento del arreglo
const menor = arreglo.reduce((min, actual) => (actual < min ? actual : min), arr[0]);
console.log(menor); // 0

// 2. Retornar la suma de todos los elementos del arreglo
const suma = arreglo.reduce((total, actual) => total + actual, 0);
console.log(suma); // 1897

// 3. Retornar un arreglo donde cada elemento es el doble que en el arreglo original
const doble = arreglo.map(num => num * 2);
console.log(doble); // [2, 4, 6, 8, 10, 12, 22, 46, 2, 1978, 0, 2, 222, 1290, 100, 90]

// 4. Retornar un arreglo con los elementos que sean mayores o iguales a 10
const mayores10 = arreglo.filter(num => num >= 10);
console.log(mayores10); // [11, 23, 989, 111, 645, 50, 45]

// 5. Retornar el índice del primer elemento mayor a 10
const indiceMayor10 = arreglo.findIndex(num => num > 10);
console.log(indiceMayor10); // 6

//Definir e Instanciar un objeto

class Automovil {
    constructor(ruedas, puertas, color, velocidad = 0) {
        this.ruedas = ruedas;
        this.puertas = puertas;
        this.color = color;
        this.velocidad = velocidad;
    }

    // Método para aumentar la velocidad
    aumentar(cantidad) {
        this.velocidad += cantidad;
        console.log(`La velocidad actual es de ${this.velocidad} km/h`);
    }
}

const miAuto = new Automovil(4, 4, 'rojo', 60);

console.log(miAuto); // Automovil { ruedas: 4, puertas: 4, color: 'rojo', velocidad: 60 }

miAuto.aumentar(20); // Imprime: "La velocidad actual es de 80 km/h"


