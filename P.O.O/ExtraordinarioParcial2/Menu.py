from GestorConexion import GestorConexiones
from GestorGamer import GestorGammer

if __name__ == "__main__":
    gg = GestorGammer()
    gc = GestorConexiones()
    gc.ordenar()
    print("Menu de opciones")
    a = int(input("1. Mostrar Listado \n 2. Ingresar Juego \n 3. Emitir Listado de Servicio Basico \n 0. Para Finalizar \n Su Opcion: "))
    while a != 0:
        if a == 1:
            try:
                dni = int(input("Ingrese DNI: "))
                gc.MostrarLista(gg, dni)
            except ValueError:
                print("ingrese un numero entero")
            except IndexError as e:
                print(e)
        if a == 2:
            try:
                nombre = input("Ingrese nombre del juego: ")
                gc.Inciso2(nombre, gg)
            except IndexError as e:
                print(e)
        if a == 3:
            gc.Inciso3(gg)
        a = int(input("1. Mostrar Listado \n 2. Ingresar Juego \n 3. Emitir Listado de Servicio Basico \n 0. Para Finalizar \n Su Opcion: "))