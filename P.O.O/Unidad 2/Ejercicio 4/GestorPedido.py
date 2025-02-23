import csv
from ModuloPedido import pedido


class gestorpedido:
    __gestorPedido = list

    def __init__(self):
        self.__gestorPedido = []
        archivo = open("DatosPedidos.csv")
        reader = csv.reader(archivo, delimiter=",")
        bandera = False
        for fila in reader:
            if bandera == False:
                bandera = True
            else:
                patenteAsig = fila[0]
                id = int(fila[1])
                comidas = fila[2]
                tiempoEst = int(fila[3])
                tiempoReal = int(fila[4])
                precio = float(fila[5])
                nuevopedido = pedido(
                    patenteAsig, id, comidas, tiempoEst, tiempoReal, precio)
                self.__gestorPedido.append(nuevopedido)
        archivo.close()

    def NuevoPedido(self, patente, gestormoto, id, comidas, tiempoEst, tiempoReal, precio):
        i = gestormoto.BuscaPatente(patente)
        if i == 1:
            print("La patente se encuentra")
        else:
            print("La patente no se encuentra")
        patenteAsigg = patente
        idd = int(id)
        comidass = comidas
        tiempoEstt = int(tiempoEst)
        tiempoReall = int(tiempoReal)
        precioo = float(precio)
        nuevopedido = pedido(patenteAsigg, idd, comidass,
                             tiempoEstt, tiempoReall, precioo)
        self.__gestorPedido.append(nuevopedido)

    def NuevoTiempo(self, patente, tiempo):
        i = 0
        while ((i < len(self.__gestorPedido)) and (patente.upper() != self.__gestorPedido[i].getpatente())):
            i += 1
        if i >= len(self.__gestorPedido):
            print("La patente no se encuentra")
        else:
            self.__gestorPedido[i].settiempoReal(tiempo)

    def Promedio(self, patente):
        j = 0
        sum = 0
        c = 0
        while j < len(self.__gestorPedido):
            if self.__gestorPedido[j].getpatente() == patente.upper():
                c += 1
                sum += self.__gestorPedido[j].gettiempoReal()
            j += 1
        total = sum/c
        return total

    def Mostrar(self, patente):
        i = 0
        total = 0
        comision = 0
        print("Id del producto:     Tiempo estimado:     Tiempo real:     Precio:")
        while i < len(self.__gestorPedido):
            if self.__gestorPedido[i].getpatente() == patente.upper():
                print(self.__gestorPedido[i].getid(),    self.__gestorPedido[i].gettiempoEst(
                ),    self.__gestorPedido[i].gettiempoReal(),    self.__gestorPedido[i].getprecio())
                total += self.__gestorPedido[i].getprecio()
            i += 1
            comision = total + (total * 0.2)
        print(f"El total es: {total} \nComision: {comision}")
