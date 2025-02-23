from GestorMama import gestormama
from GestorNacimiento import gestornacimiento

if __name__ == "__main__":
    print("Menu de opciones:")
    mama = gestormama()
    nacimiento = gestornacimiento()
    a = int(input(
        " 1. Mostrar Informacion \n 2. Mostrar Datos \n 0. Para finalizar \n Su opcion: "))
    while a != 0:
        if a == 1:
            dnimama = int(input("Ingrese dni de una mama: "))
            mama.Mostrar(dnimama, nacimiento)
        if a == 2:
            nacimiento.MostrarDatos(mama)
        a = int(input(
            " 1. Mostrar Informacion \n 2. Mostrar Datos \n 0. Para finalizar \n Su opcion: "))
