from nodo import Nodo
from ClaseTelefonia import Telefonia
from ClaseTelevision import Television
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
        self.__actual = self.__comienzo
        self.__indice = 0
        return self
    
    def __next__(self):
        if self.__actual is None:
            raise StopIteration
        if self.__indice == self.__tope:
            self.__actual = self.__comienzo
            self.__indice = 0
            raise StopIteration
        else:
            dato = self.__actual.getplan()
            self.__actual = self.__actual.getSig()
            self.__indice += 1
            return dato
    
    def agregar(self, plan):
        nodo = Nodo(plan)
        nodo.setSig(self.__comienzo)
        self.__comienzo = nodo
        self.__tope += 1
        
    def inicializar(self):
        archivo = open("planes[1].csv")
        reader = csv.reader(archivo, delimiter=";")
        for fila in reader:
            if fila[0] == "M":
               telefono = Telefonia(fila[1], int(fila[2]), fila[3], int(fila[4]), fila[5], int(fila[6]))
               self.agregar(telefono)
            elif fila[0] == "T":
                herramienta1 = Television(fila[1],int(fila[2]), fila[3], int(fila[4]), int(fila[5]), int(fila[6]))
                self.agregar(herramienta1)
    

    def buscar(self, pos):
        aux = self.__comienzo
        actual = 0
        while (actual < self.__tope) and (actual != pos):
            aux = aux.getSig()
            actual += 1
        if actual == pos:
            if isinstance(aux.getplan(), Telefonia):
                print("es un telefono")
            elif isinstance(aux.getplan(), Television):
                print("es una television")
        else:
            raise IndexError("Posicion invalida")

    def Inciso2(self, nombre):
        aux = self.__comienzo
        c = 0
        for dato in self:
            if dato.getcobertura().lower() == nombre.lower():
                c += 1
        print(f"Cantidad de telefonias con cobertura {nombre}: {c}")