from nodo import Nodo
from ClaseClienteNacional import ClienteNacional
from ClaseClienteLocal import ClienteLocal

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
            dato = self.__actual.getCliente()
            self.__actual = self.__actual.getSig()
            self.__indice += 1
            return dato
    
    def agregar(self, cliente):
        nodo = Nodo(cliente)
        if self.__comienzo is None:
            self.__comienzo = nodo
        else:
            actual = self.__comienzo
            while actual.getSig() is not None:
                actual = actual.getSig()
            actual.setSig(nodo)
        self.__tope += 1
        
    def inicializar(self, objeto):
        self.agregar(objeto)

    def mostrar(self):
        for dato in self:
            print(dato)

    def Inciso1(self):
        for dato in self:
            if isinstance(dato, ClienteNacional):
                print(dato.getnombre(), dato.getprovincia())
    
    def Inciso2(self, pos):
        aux = self.__comienzo
        self.__actual = 0
        while self.__actual != pos and self.__actual < self.__tope:
            aux = aux.getSig()
            self.__actual += 1
        if self.__actual == pos:
            if isinstance(aux.getCliente(), ClienteNacional):
                print("En dicha posicion el Cliente es Nacional")
            elif isinstance(aux.getCliente(), ClienteLocal):
                print("En dicha posicion el Cliente es Local")
        else:
            raise IndexError("Posicion invalida")