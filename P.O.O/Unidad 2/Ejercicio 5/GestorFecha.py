import csv
import numpy as np
from ModuloFecha import Fecha


class gestorfecha:
    __gestorFecha = np.ndarray
    __dimension: int
    __incremento: int
    __cantidad: int

    def AgregarMov(self, movimiento):
        if self.__cantidad == self.__dimension:
            self.__dimension += self.__incremento
            self.__gestorFecha.resize(self.__dimension)
        self.__gestorFecha[self.__cantidad] = movimiento
        self.__cantidad += 1

    def __init__(self):
        self.__cantidad = 0
        self.__dimension = 0
        self.__incremento = 3
        self.__gestorFecha = np.empty(0, dtype=Fecha)
        archivo = open("fechasFutbol.csv")
        reader = csv.reader(archivo, delimiter=";")
        bandera = False
        for fila in reader:
            if bandera == False:
                bandera = True
            else:
                fecha = fila[0]
                idEquipoLocal = int(fila[1])
                idEquipoVisit = int(fila[2])
                golesLocal = int(fila[3])
                golesVisit = int(fila[4])
                nuevafecha = Fecha(fecha, idEquipoLocal,
                                   idEquipoVisit, golesLocal, golesVisit)
                self.AgregarMov(nuevafecha)
        archivo.close()

    def MostrarLista(self, gestorequipo, nombreequipo):
        j = gestorequipo.BuscaEquipo(nombreequipo)
        nombre = gestorequipo.Nombre(j)
        id = gestorequipo.Obtenerid(j)
        i = 0
        gtf = 0
        gtc = 0
        dt = 0
        pt = 0
        if j == -1:
            print("No se encuentra el equipo")
        else:
            print(f"""Equipo: {
                  nombre}\nFecha      Goles a Favor      Goles en Contra    Diferencia     Puntos""")
            while i < len(self.__gestorFecha):
                if (id == self.__gestorFecha[i].getidLocal()):
                    diferencia = self.__gestorFecha[i].getgolesLocal(
                    ) - self.__gestorFecha[i].getgolesVisit()
                    if self.__gestorFecha[i].getgolesLocal() == self.__gestorFecha[i].getgolesVisit():
                        puntos = 1
                    elif self.__gestorFecha[i].getgolesLocal() > self.__gestorFecha[i].getgolesVisit():
                        puntos = 3
                    elif self.__gestorFecha[i].getgolesLocal() < self.__gestorFecha[i].getgolesVisit():
                        puntos = 0
                    print(f"""{self.__gestorFecha[i].getfecha()}       {self.__gestorFecha[i].getgolesLocal()}                 {
                          self.__gestorFecha[i].getgolesVisit()}                 {diferencia}            {puntos}""")
                    gtf += self.__gestorFecha[i].getgolesLocal()
                    gtc += self.__gestorFecha[i].getgolesVisit()
                    dt += diferencia
                    pt += puntos
                elif (id == self.__gestorFecha[i].getidVisit()):
                    diferencia = self.__gestorFecha[i].getgolesVisit(
                    ) - self.__gestorFecha[i].getgolesLocal()
                    if self.__gestorFecha[i].getgolesLocal() == self.__gestorFecha[i].getgolesVisit():
                        puntos2 = 1
                    elif self.__gestorFecha[i].getgolesLocal() > self.__gestorFecha[i].getgolesVisit():
                        puntos2 = 0
                    elif self.__gestorFecha[i].getgolesLocal() < self.__gestorFecha[i].getgolesVisit():
                        puntos2 = 3
                    print(f"""{self.__gestorFecha[i].getfecha()}       {self.__gestorFecha[i].getgolesVisit()}                 {
                          self.__gestorFecha[i].getgolesLocal()}                {diferencia}            {puntos2}""")
                    gtf += self.__gestorFecha[i].getgolesVisit()
                    gtc += self.__gestorFecha[i].getgolesLocal()
                    dt += diferencia
                    pt += puntos2
                i += 1
            print(f"""--------------------------------------------------------------------------\n                 {
                  gtf}                 {gtc}                 {dt}            {pt}""")

    def Actualizar(self, gestorequipo):
        gestorequipo.Actualiza(self.__gestorFecha)
