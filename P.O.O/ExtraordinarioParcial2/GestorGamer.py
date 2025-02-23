from ClaseGammer import Gammer
import csv

class GestorGammer:
    __gestorGamer = list

    def __init__(self):
        self.__gestorGamer = []
        archivo = open("gammers.csv")
        reader = csv.reader(archivo, delimiter=";")
        for fila in reader:
            nlista = Gammer(int(fila[0]), int(fila[1]), fila[2], fila[3], fila[4], fila[5], int(fila[6]), int(fila[7]))
            self.__gestorGamer.append(nlista)
        archivo.close()

    def BuscarDNI(self, dni):
        i = 0
        while i < len(self.__gestorGamer) and self.__gestorGamer[i].getdni() != dni:
            i += 1
        if self.__gestorGamer[i].getdni() == dni:
            return self.__gestorGamer[i]
        else:
            raise IndexError("DNI no encontrado")
        
    def Mostrar(self, conexion):
        i = 0
        while i < len(self.__gestorGamer) and self.__gestorGamer[i].getidjugador() != conexion.getid():
            i += 1
        if self.__gestorGamer[i].getidjugador() == conexion.getid():
            print(f"direccion: {conexion.getdirection()}  nombre y apellido: {self.__gestorGamer[i].getnombre()} {self.__gestorGamer[i].getapellido()}  alias: {self.__gestorGamer[i].getalias()}  plan: {self.__gestorGamer[i].getplan()} ")
        
    def BuscarPlan(self, idjugador):
        i = 0
        while i < len(self.__gestorGamer) and self.__gestorGamer[i].getidjugador() != idjugador:
            i += 1
        if self.__gestorGamer[i].getidjugador() == idjugador:
            return self.__gestorGamer[i].getplan()