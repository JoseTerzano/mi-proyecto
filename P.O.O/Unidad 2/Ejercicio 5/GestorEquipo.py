import csv
from ModuloEquipo import Equipo
from GestorFecha import gestorfecha


class gestorequipo:
    __gestorEquipo = list

    def __init__(self):
        self.__gestorEquipo = []
        archivo = open("equipos2024.csv")
        reader = csv.reader(archivo, delimiter=";")
        bandera = False
        for fila in reader:
            if bandera == False:
                bandera = True
            else:
                id = int(fila[0])
                nombre = fila[1]
                golesFav = int(fila[2])
                golesCont = int(fila[3])
                diferencia = float(fila[4])
                puntos = int(fila[5])
                nuevoequipo = Equipo(
                    id, nombre, golesFav, golesCont, diferencia, puntos)
                self.__gestorEquipo.append(nuevoequipo)
        archivo.close()

    def BuscaEquipo(self, equipo):
        i = 0
        while ((i < len(self.__gestorEquipo)) and (equipo != self.__gestorEquipo[i].getnombre())):
            i += 1
        if i >= len(self.__gestorEquipo):
            return -1
        else:
            return i

    def Obtenerid(self, i):
        p = self.__gestorEquipo[i].getid()
        return p

    def Nombre(self, i):
        return self.__gestorEquipo[i].getnombre()

    def Actualiza(self, gestorfecha):
        for i in range(len(gestorfecha)):
            for j in range(len(self.__gestorEquipo)):
                if self.__gestorEquipo[j].getid() == gestorfecha[i].getidLocal():
                    if gestorfecha[i].getgolesLocal() == gestorfecha[i].getgolesVisit():
                        d = 1
                    elif gestorfecha[i].getgolesLocal() > gestorfecha[i].getgolesVisit():
                        d = 3
                    elif gestorfecha[i].getgolesLocal() < gestorfecha[i].getgolesVisit():
                        d = 0
                    self.__gestorEquipo[j].setpuntos(d)

                elif self.__gestorEquipo[j].getid() == gestorfecha[i].getidVisit():
                    if gestorfecha[i].getgolesLocal() == gestorfecha[i].getgolesVisit():
                        d = 1
                    elif gestorfecha[i].getgolesLocal() > gestorfecha[i].getgolesVisit():
                        d = 0
                    elif gestorfecha[i].getgolesLocal() < gestorfecha[i].getgolesVisit():
                        d = 3
                    self.__gestorEquipo[j].setpuntos(d)
        if i >= len(gestorfecha):
            return 1

    def Ordenar(self):
        self.__gestorEquipo.sort()
        print("Se ordeno")

    def ListaEquipos(self):
        lista = []
        for fila in self.__gestorEquipo:
            lista.append(fila.getnombre())
        return lista

    def guardarCSV(self):
        posiciones = self.ListaEquipos()
        posiciones = [[pos] for pos in posiciones]
        with open('tposiciones.csv', 'w', newline='') as archivo:
            writer = csv.writer(archivo)
            writer.writerows(posiciones)
        print("Se guardaron los datos exitosamente!")
