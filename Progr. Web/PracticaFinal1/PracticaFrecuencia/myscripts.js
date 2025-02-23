document.addEventListener("DOMContentLoaded", function(){
    let boton = document.getElementById("boton");

    boton.addEventListener("mouseover", function(){
        boton.style.backgroundColor = "yellow";
        boton.style.color = "red";
    });
    boton.addEventListener("mouseout", function(){
        boton.style.backgroundColor = "black";
        boton.style.color = "white";
    })

    boton.addEventListener("click", function(){
        let edad = document.getElementById("edad").value;
        let FCA = document.getElementById("FCA").value;
        if (isNaN(edad) || isNaN(FCA) || edad === "" || FCA === ""){
            alert("Ingrese un valor valido en los campos");
        }
        else{
            document.getElementById("mostrar-frecuencia").innerText = "su FCM es: " + (220 - edad);
            let porcentaje = (document.getElementById("FCA").value * 100) / (220-edad);
            if (porcentaje >= 50 && porcentaje <=60){
                document.getElementById("mostrar-zona").innerText = "Se encuentra en la zona 1, su porcentaje es de: %" + porcentaje.toFixed(0);
                document.getElementById("mostrar-zona").style.backgroundColor = "blue";
            }else if (porcentaje > 60 && porcentaje < 70){
                document.getElementById("mostrar-zona").innerText = "Se encuentra en la zona 2, su porcentaje es de: %" + porcentaje.toFixed(0);
                document.getElementById("mostrar-zona").style.backgroundColor = "green";
            }else if (porcentaje > 70 && porcentaje < 80){
                document.getElementById("mostrar-zona").innerText = "Se encuentra en la zona 3, su porcentaje es de: %" + porcentaje.toFixed(0);
                document.getElementById("mostrar-zona").style.backgroundColor = "yellow";
            }else if (porcentaje > 80 && porcentaje < 90){
                document.getElementById("mostrar-zona").innerText = "Se encuentra en la zona 4, su porcentaje es de: %" + porcentaje.toFixed(0);
                document.getElementById("mostrar-zona").style.backgroundColor = "orange";
            }else if (porcentaje > 90 && porcentaje < 100){
                document.getElementById("mostrar-zona").innerText = "Se encuentra en la zona 5, su porcentaje es de: %" + porcentaje.toFixed(0);
                document.getElementById("mostrar-zona").style.backgroundColor = "red";
            }else if(porcentaje < 50 || porcentaje >100){
                document.getElementById("mostrar-zona").innerText = "No te encuentras en ninguna zona, su porcentaje es de: %" + porcentaje.toFixed(0);
                document.getElementById("mostrar-zona").style.backgroundColor = "black";
                document.getElementById("mostrar-zona").style.color = "white";
            }
        }
    })













})


