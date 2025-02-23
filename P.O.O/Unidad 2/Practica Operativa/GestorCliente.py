import csv
from ModuloCliente import cliente


class gestorcliente:
    __gestorCliente = list

    def __init__(self):
        self.__gestorCliente = []
        archivo = open("ClientesFarmaCiudad (1).csv")
        reader = csv.reader(archivo, delimiter=";")
        bandera = False
        for fila in reader:
            if bandera == False:
                bandera = True
            else:
                nombre = fila[0]
                apellido = fila[1]
                dni = int(fila[2])
                nroCuenta = int(fila[3])
                saldoAnt = float(fila[4])
                nuevocliente = cliente(
                    nombre, apellido, dni, nroCuenta, saldoAnt)
                self.__gestorCliente.append(nuevocliente)
        archivo.close()

    def BuscaCliente(self, dni):
        i = 0
        while ((i < len(self.__gestorCliente)) and (dni != self.__gestorCliente[i].getdni())):
            i += 1
        if i >= len(self.__gestorCliente):
            i = -1
            print("El dni no se encuentra")
        return i

    def ActualizaSaldo(self, gestormovimiento, dni):
        i = self.BuscaCliente(dni)
        print(f"El cliente {self.__gestorCliente[i].getapellido()} {
            self.__gestorCliente[i].getnombre()}     Nro Cuenta {self.__gestorCliente[i].getnroCuenta()}")
        print(f"Saldo Anterior {self.__gestorCliente[i].getsaldoAnt()}")
        nuevosaldo = self.__gestorCliente[i].getsaldoAnt(
        ) + gestormovimiento.suma(self.__gestorCliente, i) - gestormovimiento.resta(self.__gestorCliente, i)
        gestormovimiento.listarmovimientos(self.__gestorCliente, i)
        print(f"El nuevo saldo es {nuevosaldo}")

    def informar(self, gestormovimiento, dni):
        i = self.BuscaCliente(dni)
        band = gestormovimiento.existeMovimiento(self.__gestorCliente, i)
        if band == 1:
            print("La persona realizo movimientos")
        else:
            print("la persona", self.__gestorCliente[i].getnombre(
            ), "no realizo movimientos")
