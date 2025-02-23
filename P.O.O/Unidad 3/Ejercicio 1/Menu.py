from GestorEdificio import gestoredificio

if __name__ == "__main__":
    print("Menu de Opciones: ")
    edificio = gestoredificio()
    a = int(input(" 1. Mostrar Nombres de los Propietarios \n 2. Mostrar Superficie Total \n 3. Mostrar Superficie de un Dpto \n 4. Mostrar Cantidad de Dptos con 3 dormitorios y 1 baño \n  Su opcion: "))
    while a != 0:
        if a == 1:
            nombreEdificio = input("Ingrese nombre de edificio: ")
            edificio.MostrarPropietarios(nombreEdificio)
        if a == 2:
            nombreEdificio = input("Ingrese nombre de edificio: ")
            c = edificio.SuperficieTotal(nombreEdificio)
            print(f"El total es: {c}")
        if a == 3:
            nombre = input("Ingrese Nombre de Propietario: ")
            nombreEdificio = input("Ingrese nombre de edificio: ")
            c = edificio.SuperficieTotal(nombreEdificio)
            edificio.MostrarSup(nombreEdificio, nombre, c)
        if a == 4:
            nombreEdificio = input("Ingrese nombre de edificio: ")
            numero = int(input("Ingrese numero de piso: "))
            edificio.Mostrar(nombreEdificio, numero)
        a = int(input(" 1. Mostrar Nombres de los Propietarios \n 2. Mostrar Superficie Total \n 3. Mostrar Superficie de un Dpto \n 4. Mostrar Cantidad de Dptos con 3 dormitorios y 1 baño \n  Su opcion: "))
