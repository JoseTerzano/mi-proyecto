import csv
from ModuloMoto import moto
from GestorPedido import gestorpedido


class gestormoto:
    __gestorMoto = list

    def __init__(self):
        self.__gestorMoto = []
        archivo = open("DatosMotos.csv")
        reader = csv.reader(archivo, delimiter=",")
        bandera = False
        for fila in reader:
            if bandera == False:
                bandera = True
            else:
                patente = fila[0]
                marca = fila[1]
                nombre = fila[2]
                apellido = fila[3]
                kilometro = int(fila[4])
                nuevomoto = moto(
                    patente, marca, nombre, apellido, kilometro)
                self.__gestorMoto.append(nuevomoto)
        archivo.close()

    def BuscaPatente(self, patente2):
        j = 0
        while (j < len(self.__gestorMoto)):
            if patente2.upper() == self.__gestorMoto[j].getpatente():
                bandera = j
            else:
                bandera = -1
            j += 1
        return bandera

    def MostrarDatos(self, gestorpedido, patente):
        i = self.BuscaPatente(patente)
        promedio = float(gestorpedido.Promedio(patente))
        print(f"Conductor: {self.__gestorMoto[i].getnombre()} {
              self.__gestorMoto[i].getapellido()}    Tiempo Pomedio: {promedio}")

    def MostrarDatosCompletos(self, gestorpedido):
        i = 0
        while i < len(self.__gestorMoto):
            print(f"Patente de Moto: {self.__gestorMoto[i].getpatente()}     Conductor: {
                self.__gestorMoto[i].getnombre()} {self.__gestorMoto[i].getapellido()}")
            gestorpedido.Mostrar(self.__gestorMoto[i].getpatente())
            i += 1
