from GestorAlquiler import gestoralquiler
from GestorCancha import gestorcancha

if __name__ == "__main__":
    print("Menu de opciones:")
    alquiler = gestoralquiler()
    cancha = gestorcancha()
    a = int(input(
        " 1. Emitir Listado \n 2. Mostrar Cantidad de minutos \n 0. Para finalizar \n Su opcion: "))
    while a != 0:
        if a == 1:
            alquiler.ordenado()
            alquiler.MostrarLista(cancha)
        if a == 2:
            id = input("Ingrese id de cancha: ")
            alquiler.MostrarMinutos(id)
        a = int(input(
            " 1. Emitir Listado \n 2. Mostrar Cantidad de minutos \n 0. Para finalizar \n Su opcion: "))
