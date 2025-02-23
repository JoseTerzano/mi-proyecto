import csv
from ModuloAlquiler import Alquiler


class gestoralquiler:
    __gestorAlquiler = list

    def __init__(self):
        self.__gestorAlquiler = []
        archivo = open("Alquiler.csv")
        reader = csv.reader(archivo, delimiter=";")
        bandera = False
        for fila in reader:
            if bandera == False:
                bandera = True
            else:
                nombre = fila[0]
                id = fila[1]
                hora = fila[2]
                minutos = fila[3]
                duracion = int(fila[4])
                nuevoalquiler = Alquiler(
                    nombre, id, hora, minutos, duracion)
                self.__gestorAlquiler.append(nuevoalquiler)
        archivo.close()

    def ordenado(self):
        self.__gestorAlquiler.sort()

    def MostrarLista(self, gestorequipo):
        print(
            "Hora   id de Cancha   Duracion Alquiler   Importe por Hora   Importe Aquiler")
        gestorequipo.MostrarDatos(self.__gestorAlquiler)

    def MostrarMinutos(self, id):
        total = 0
        for i in range(len(self.__gestorAlquiler)):
            if id.upper() == self.__gestorAlquiler[i].getidcancha():
                total += self.__gestorAlquiler[i].getduracion()
        print(f"La cantidad de minutos que estuco alquilada fue: {total}")
