from GestorEquipo import gestorequipo
from GestorFecha import gestorfecha

if __name__ == "__main__":
    print("Menu de Opciones: ")
    equipo = gestorequipo()
    fecha = gestorfecha()
    a = int(input(" 1. Almacenar Equipos \n 2. Almacenar Fechas \n 3. Listado \n 4. Actualizar Tabla \n 5. Ordenar Tabla \n 6. Almacenar tabla ordenada \n  Su opcion: "))
    while a != 0:
        if a == 1:
            print("Operacion Exitosa!")
        if a == 2:
            print("Operacion Exitosa!")
        if a == 3:
            nombreequipo = input(
                "Ingrese Nombre de Equipo para Listar Datos: ")
            fecha.MostrarLista(equipo, nombreequipo)
        if a == 4:
            fecha.Actualizar(equipo)
            print("Tabla Actualizada")
        if a == 5:
            equipo.Ordenar()
        if a == 6:
            equipo.guardarCSV()

        a = int(input(" 1. Almacenar Equipos \n 2. Almacenar Fechas \n 3. Listado \n 4. Actualizar Tabla \n 5. Ordenar Tabla \n 6. Almacenar tabla ordenada \n 0. Para Finalizar \n Su opcion: "))
