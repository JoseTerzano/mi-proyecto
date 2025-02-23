from ClasePublicacion import Publicacion
from ClaseCD import CD
from ClaseLibro import Libro
import csv


class Lista:
    __lista = list

    def __init__(self):
        self.__lista = []

    def CargarCD(self):
        archivo = open("cd.csv")
        reader = csv.reader(archivo, delimiter=";")
        for fila in reader:
            nlista = CD(int(fila[0]), fila[1], fila[2],
                        fila[3], float(fila[4]))
            self.__lista.append(nlista)
        archivo.close()

    def cargarLibro(self):
        archivo = open("libro.csv")
        reader = csv.reader(archivo, delimiter=";")
        for fila in reader:
            nilista = Libro(fila[0], fila[1], int(fila[2]),
                            fila[3], fila[4], float(fila[5]))
            self.__lista.append(nilista)
        archivo.close()

    def Mostrar(self):
        for p in self.__lista:
            print(p)

    def MostrarPos(self, pos):
        print(len(self.__lista))
        if pos >= len(self.__lista) or pos < 0:
            print("posicion fuera de rango")
        else:
            p = self.__lista[pos]
        if isinstance(p, CD):
            print("La publicacion es cd")
        elif isinstance(p, Libro):
            print("La publicacion es un libro")

    def MostrarTodo(self):
        cantcd = 0
        cantl = 0
        for i in range(len(self.__lista)):
            if isinstance(self.__lista[i], CD):
                cantcd += 1
            elif isinstance(self.__lista[i], Libro):
                cantl += 1
        print(f"La cantidad de libros es: {
              cantl}\nLa cantidad de cd es: {cantcd}")

    def Recorrer(self):
        for objeto in self.__lista:
            print(objeto.gettitulo())
            print(objeto.getcat())
            print(objeto.CalcularImporte())
