from ClaseNodo import Nodo
from ClaseAudio import Audio
from ClaseLibro import Libro
import csv


class Lista:
    __comienzo: Nodo
    __actual: Nodo
    __indice: int
    __tope: int

    def __init__(self):
        self.__comienzo = None
        self.__actual = None
        self.__indice = 0
        self.__tope = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.__indice == self.__tope:
            self.__actual = self.__comienzo
            self.__indice = 0
            raise StopIteration
        else:
            self.__indice += 1
            publi = self.__actual.getpubli()
            self.__actual = self.__actual.getsig()
            return publi

    def gettope(self):
        return self.__tope

    def agregarPubli(self, publi):
        nodo = Nodo(publi)
        nodo.setsig(self.__comienzo)
        self.__comienzo = nodo
        self.__actual = nodo
        self.__tope += 1

    def cargaPubli(self):
        band1 = True
        archi1 = open('librosimpresos.csv')
        reader1 = csv.reader(archi1, delimiter=';')
        for linea in reader1:
            if band1:
                band1 = False
            else:
                self.agregarPubli(
                    Libro(linea[0], linea[1], linea[2], linea[3], linea[4], linea[5]))
        archi1.close()
        band2 = True
        archi2 = open('audiolibros.csv')
        reader2 = csv.reader(archi2, delimiter=';')
        for linea in reader2:
            if band2:
                band2 = False
            else:
                self.agregarPubli(
                    Audio(linea[0], linea[1], linea[2], linea[3], linea[4]))
        archi2.close()

    def mostrarTipoPublicacion(self, pos):
        ret = 0
        if pos < self.gettope():
            aux = self.__comienzo
            for i in range(pos):
                aux = aux.getsig()
            if isinstance(aux.getpubli(), Libro):
                ret = 1
            elif isinstance(aux.getpubli(), Audio):
                ret = 2
        else:
            print("Posicion fuera del rango")
        return ret

    def mostrarCant(self):
        cantL = 0
        cantA = 0
        aux = self.__comienzo
        while aux is not None:
            publi = aux.getpubli()
            if isinstance(publi, Libro):
                cantL += 1
            elif isinstance(publi, Audio):
                cantA += 1
            aux = aux.getsig()
        print(f"Cantidad de Libros: {cantL}")
        print(f"Cantidad de Audiolibros: {cantA}")

    def MuestraPub(self):
        for publi in self:
            print(f"Titulo: {publi.gettitulo()}")
            print(f"Categoria: {publi.getcategoria()}")
            print("Importe de Venta: {:.2f}\n".format(publi.getimporteventa()))
