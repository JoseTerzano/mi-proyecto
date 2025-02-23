import csv
from ModuloMama import Mama
import numpy as np


class gestormama:
    __gestorMama = np.ndarray
    __dimension: int
    __incremento: int
    __cantidad: int

    def Agregar(self, mama):
        if self.__cantidad == self.__dimension:
            self.__dimension += self.__incremento
            self.__gestorMama.resize(self.__dimension)
        self.__gestorMama[self.__cantidad] = mama
        self.__cantidad += 1

    def __init__(self):
        self.__cantidad = 0
        self.__dimension = 0
        self.__incremento = 3
        self.__gestorMama = np.empty(0, dtype=Mama)
        archivo = open("Mamas.csv")
        reader = csv.reader(archivo, delimiter=";")
        bandera = False
        for fila in reader:
            if bandera == False:
                bandera = True
            else:
                dni = int(fila[0])
                edad = int(fila[1])
                apellidoynombre = fila[2]
                mama = Mama(
                    dni, edad, apellidoynombre)
                self.Agregar(mama)
        archivo.close()

    def Mostrar(self, dnimadre, gestornacimiento):
        i = 0
        for i in range(len(self.__gestorMama)):
            if dnimadre == self.__gestorMama[i].getdni():
                print(f"Apellido y nombre: {
                      self.__gestorMama[i].getapellido()}")
                print(f"Edad: {self.__gestorMama[i].getedad()}")
                tipodeparto = gestornacimiento.TipoParto(dnimadre)
                print(f"Tipo de Parto: {tipodeparto}")
                print("bebe/s:")
                gestornacimiento.Bebes(dnimadre)

    def ObtenerEdad(self, dni):
        i = 0
        while i < len(self.__gestorMama):
            if self.__gestorMama[i].getdni() == dni:
                return self.__gestorMama[i].getedad()
            i += 1

    def ObtenerNombre(self, dni):
        i = 0
        while i < len(self.__gestorMama):
            if self.__gestorMama[i].getdni() == dni:
                return self.__gestorMama[i].getapellido()
            i += 1
