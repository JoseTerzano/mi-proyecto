document.addEventListener("DOMContentLoaded", function(){
    let boton = document.getElementById("boton");
    let cuenta;
    boton.addEventListener("mouseover",function(){
        boton.style.backgroundColor = "white";
        boton.style.color = "black";
    })
    boton.addEventListener("mouseout",function(){
        boton.style.backgroundColor = "black";
        boton.style.color = "white";
    })
    boton.addEventListener("click",function(){
        let peso = parseFloat(document.getElementById("peso").value);
        let altura = parseFloat(document.getElementById("altura").value);
        if (peso <= 0 || altura <= 0){
            document.getElementById("resultado").textContent = "Datos Sin Completar";
        }else if (Number.isInteger(altura)){
            cuenta = (peso / (altura*altura)) * 10000;
            console.log(cuenta);
            document.getElementById("resultado").innerText = "Tu IMC es: " + cuenta.toFixed(2);
        }else{
            console.log(cuenta);
            cuenta = (peso / (altura*altura));
            document.getElementById("resultado").innerText = "Tu IMC es: " + cuenta.toFixed(2);
        }
        if (cuenta < 18.5){
            document.getElementById("resultado2").innerText = "Bajo de peso";
            document.getElementById("resultado2").style.backgroundColor = "yellow";
        }else if (cuenta > 18.5 && cuenta < 24.9){
            document.getElementById("resultado2").innerText = "Normal";
            document.getElementById("resultado2").style.backgroundColor = "green";
        }else if (cuenta > 25 && cuenta > 29.9){
            document.getElementById("resultado2").innerText = "Sobrepeso";
            document.getElementById("resultado2").style.backgroundColor = "brown";
        }else if (cuenta > 30){
            document.getElementById("resultado2").innerText = "Obeso";
            document.getElementById("resultado2").style.backgroundColor = "red";
        }
    })
})