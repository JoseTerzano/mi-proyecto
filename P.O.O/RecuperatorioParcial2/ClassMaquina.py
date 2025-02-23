import abc
from abc import ABC
class Maquina(ABC):
    __marca = str
    __modelo = str
    __anio = int
    __combustible = str
    __potencia = int
    __capacidadcarga = int
    __alquilerdiario = int
    __diasalquiler = int

    def __init__(self, marca, modelo, anio, combustible, potencia, capacidadcarga, alquilerdiario, diasalquiler):
        self.__marca = marca
        self.__modelo = modelo
        self.__anio = anio
        self.__combustible = combustible
        self.__potencia = potencia
        self.__capacidadcarga = capacidadcarga
        self.__alquilerdiario = alquilerdiario
        self.__diasalquiler = diasalquiler

    def __str__(self):
        return f"{self.__marca} {self.__modelo} {self.__anio} {self.__combustible} {self.__potencia} {self.__capacidadcarga} {self.__alquilerdiario} {self.__diasalquiler}"
    
    def getMarca(self):
        return self.__marca
    
    def getanio(self):
        return self.__anio
    
    def getcapacidadCarga(self):
        return self.__capacidadcarga
    @abc.abstractmethod
    def tarifaAlquiler(self):
        pass

    def getalquierdiario(self):
        return self.__alquilerdiario
    
    def getdiasalquiler(self):
        return self.__diasalquiler