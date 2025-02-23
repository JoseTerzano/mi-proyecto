
from GestorCliente import gestorcliente
from GestorMovimiento import gestormovimiento


if __name__ == "__main__":
    print("Menu de opciones:")
    movimientos = gestormovimiento()
    clientes = gestorcliente()
    a = int(input(" 1. Actualizar Saldo (Primero Ordene Movimientos) \n 2. Informar Movimientos \n 3. Ordenar Movimientos \n 0. Para finalizar \n Su opcion: "))
    while a != 0:
        if a == 1:
            dni = int(input("Ingrese dni para actualizar saldo: "))
            clientes.ActualizaSaldo(movimientos, dni)
        if a == 2:
            dni = int(input("Ingrese dni: "))
            clientes.informar(movimientos, dni)
        if a == 3:
            movimientos.ordenarMovimientos()

        a = int(input(" 1. Actualizar Saldo (Primero Ordene Movimientos) \n 2. Informar Movimientos \n 3. Ordenar Movimientos \n 0. Para finalizar \n Su opcion: "))
