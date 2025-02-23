import csv
import numpy as np
from ModuloCancha import Cancha


class gestorcancha:
    __gestorCancha = np.ndarray
    __dimension: int
    __incremento: int
    __cantidad: int

    def Agregar(self, cancha):
        if self.__cantidad == self.__dimension:
            self.__dimension += self.__incremento
            self.__gestorCancha.resize(self.__dimension)
        self.__gestorCancha[self.__cantidad] = cancha
        self.__cantidad += 1

    def __init__(self):
        self.__cantidad = 0
        self.__dimension = 0
        self.__incremento = 6
        self.__gestorCancha = np.empty(0, dtype=Cancha)
        archivo = open("Canchas.csv")
        reader = csv.reader(archivo, delimiter=";")
        bandera = False
        for fila in reader:
            if bandera == False:
                bandera = True
            else:
                id = fila[0]
                tipo = fila[1]
                importe = float(fila[2])
                cancha = Cancha(
                    id, tipo, importe)
                self.Agregar(cancha)
        archivo.close()

    def importehora(self, id):
        i = 0
        while i < len(self.__gestorCancha):
            if id == self.__gestorCancha[i].getid():
                return self.__gestorCancha[i].getimporte()
            i += 1

    def MostrarDatos(self, gestoralquiler):
        total = 0
        for i in range(len(gestoralquiler)):
            duracionalquiler = gestoralquiler[i].getduracion() / 60
            importehora = self.importehora(gestoralquiler[i].getidcancha())
            importealquiler = importehora * duracionalquiler
            total += importealquiler
            print(f"""{gestoralquiler[i].gethora()}        {
                  gestoralquiler[i].getidcancha()}                 {duracionalquiler}              {importehora}               {importealquiler}""")
        print(
            f"""-------------------------------------------------------------------------------\nTotal Recaudado                                                   {total}""")
