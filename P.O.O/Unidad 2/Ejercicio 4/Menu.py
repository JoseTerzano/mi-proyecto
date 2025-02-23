from GestorMoto import gestormoto
from GestorPedido import gestorpedido

if __name__ == "__main__":
    print("Menu de opciones:")
    motos = gestormoto()
    pedidos = gestorpedido()
    a = int(input(" 1. Cargar Nuevos Pedidos \n 2. Modificar Tiempo Real \n 3. Mostrar Datos \n 4. Generar Listado Motos \n 0. Para finalizar \n Su opcion: "))
    while a != 0:
        if a == 1:
            patente = input("Ingrese patente: ")
            id = int(input("Ingrese id: "))
            comidas = input("Ingrese comidas: ")
            tiempoEst = int(input("Ingrese tiempo estimado de entrega: "))
            tiempoReal = int(input("Ingrese tiempo real de entrega: "))
            precio = float(input("Ingrese precio: "))
            pedidos.NuevoPedido(patente, motos, id, comidas,
                                tiempoEst, tiempoReal, precio)
        if a == 2:
            patente = input("Ingrese patente: ")
            id = int(input("Ingrese id: "))
            tiempoReal = int(input("Ingrese tiempo real de entrega: "))
            pedidos.NuevoTiempo(patente, tiempoReal)

        if a == 3:
            patente = input("Ingrese patente: ")
            motos.MostrarDatos(pedidos, patente)

        if a == 4:
            motos.MostrarDatosCompletos(pedidos)

        a = int(input(" 1. Cargar Nuevos Pedidos \n 2. Modificar Tiempo Real \n 3. Mostrar Datos \n 4. Generar Listado Motos \n 0. Para finalizar \n Su opcion: "))
