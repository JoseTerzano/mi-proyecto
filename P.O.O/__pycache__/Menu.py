from GestorEdificio import gestoredificio

if __name__ == "__main__":
    print("Menu de Opciones: ")
    edificio = gestoredificio()
    a = int(input(" 1. Mostrar Nombres de los Propietarios \n 2. Mostrar Superficie Total \n 3. Mostrar Superficie de un Dpto \n 4. Mostrar Cantidad de Dptos con 3 dormitorios y 1 baño \n  Su opcion: "))
    while a != 0:
        if a == 1:
            nombre = input("Ingrese nombre de edificio: ")
            edificio.mostrarnombres(nombre)
        elif a == 2:
            nombre = input("Ingrese nombre de edificio: ")
            edificio.mostrarsup(nombre)
        elif a == 3:
            nombre = input("Ingrese nombre de propietario: ")
            edificio.mostrarsuperficie(nombre)
        a = 0