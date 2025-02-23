import abc
from abc import ABC

class Plan(ABC):
    __nombre: str
    __duracion: int
    __cobertura: str
    __preciobase: int
    
    def __init__(self, nombre, duracion, cobertura, precio):
        self.__nombre = nombre
        self.__duracion = duracion
        self.__cobertura = cobertura
        self.__preciobase = precio

    def getcobertura(self):
        return self.__cobertura
    
    def __str__(self):
        return f"""Nombre: {self.__nombre}  Duracion: {self.__duracion}  Cobertura: {self.__cobertura}  Precio base: {self.__preciobase}"""