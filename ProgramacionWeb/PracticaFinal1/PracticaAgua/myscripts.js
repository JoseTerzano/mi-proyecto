document.addEventListener("DOMContentLoaded", function(){
    let calculo;
    let boton = document.getElementById("boton");
    boton.addEventListener("click", function(){
        let kg = document.getElementById("peso").value;
        let eleccion = document.getElementById("eleccion").value;
        if (kg < 0 || kg === "" || eleccion === ""){
            alert("Ingresaste un peso negativo o no completaste uno datos");
        }else{
            if(eleccion == "Sedentario"){
                calculo = (35 * kg);
                document.getElementById("consumo").innerText = "El consumo recomendado es: " + (35 * kg) + " mililitros";
            }else if(eleccion == "Moderado"){
                calculo = (40 * kg);
                document.getElementById("consumo").innerText = "El consumo recomendado es: " + (40 * kg) + " mililitros";
            }else if(eleccion == "Activo"){
                calculo = (45 * kg);
                document.getElementById("consumo").innerText = "El consumo recomendado es: " + (45 * kg) + " mililitros";
            }
            if (calculo < 2000){
                document.getElementById("consumo2").innerText = "Hidtratacion Baja";
                document.getElementById("consumo2").style.backgroundColor =  "red";
            }else if( calculo > 2000 && calculo < 3000){
                document.getElementById("consumo2").innerText = "Hidratacion Media";
                document.getElementById("consumo2").style.backgroundColor = "yellow";
            }
            else if (calculo > 3000){
                document.getElementById("consumo2").innerText = "Hidratacion optima";
                document.getElementById("consumo2").style.backgroundColor = "green";
            }
        }
    })
    
})