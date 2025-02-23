document.addEventListener("DOMContentLoaded", function(){
    let eventoBoton = document.getElementById("calculo");
eventoBoton.addEventListener("mouseover", function(){
    eventoBoton.style.backgroundColor = "white";
    eventoBoton.style.color="black";
});
eventoBoton.addEventListener("mouseout",function(){
    eventoBoton.style.backgroundColor = "black";
    eventoBoton.style.color= "white";
});

function Validar(){
    let a = parseFloat(document.getElementById("numero-peso").value);
    let b = parseFloat(document.getElementById("numero-altura").value);

    if (isNaN(a) || isNaN(b) || a <= 0 || b <= 0){
        alert("Por favor ingrese datos válidos");
        return false;
    }
    else{
        return true;
    }
}

function calcular(){
    if (!Validar()){
        return;
    }
    let a = parseFloat(document.getElementById("numero-peso").value);
    let b = parseFloat(document.getElementById("numero-altura").value);
    let imc;

    if (Number.isInteger(b)){
        imc = (a / (b*b)) * 10000;
    }else{
        imc = a / (b*b);
    }
    
    if (imc < 18.5){
        document.getElementById("Resultado").innerText = "Tu IMC es: " + imc.toFixed(2) + ". Estas Bajo de Peso";
        document.getElementById("Resultado").style.backgroundColor = "yellow";
        return;
    }
    if (imc >= 18.5 && imc <= 24.9){
        document.getElementById("Resultado").textContent = "Tu IMC es: " + imc.toFixed(2) + ". Estas Normal de Peso";
        document.getElementById("Resultado").style.backgroundColor = "green";
        return;
    }
    if (imc >= 25 && imc <= 29.9 ){
        document.getElementById("Resultado").textContent = "Tu IMC es: " + imc.toFixed(2) + ". Estas con Sobrepeso";
        document.getElementById("Resultado").style.backgroundColor = "brown";
        return;
    }
    if (imc >= 30) {
        document.getElementById("Resultado").textContent = "Tu IMC es: " + imc.toFixed(2) + ". Estas Obeso";
        document.getElementById("Resultado").style.backgroundColor = "red";
        return;
    }
}

eventoBoton.addEventListener("click", calcular);

})
