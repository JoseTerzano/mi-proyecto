from CajaDeAhorro import CajaDeAhorro
from contenedor import contenedor


if __name__ == "__main__":
    prueba = CajaDeAhorro("", "", "", "", 0)
    lista = contenedor()
    for e in range(3):
        lista.agregar(prueba.crearCaja())
    lista.mostrar()
    cuilbuscar = input("Ingrese cuil a buscar: ")
    lista.buscaCuil(cuilbuscar)
