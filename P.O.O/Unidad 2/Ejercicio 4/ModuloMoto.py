
class moto:
    __patente = str
    __marca = str
    __nombre = str
    __apellido = str
    __kilometro = int

    def __init__(self, patente, marca, nombre, apellido, kilometro):
        self.__patente = patente
        self.__marca = marca
        self.__nombre = nombre
        self.__apellido = apellido
        self.__kilometro = kilometro

    def getpatente(self):
        return self.__patente

    def getnombre(self):
        return self.__nombre

    def getapellido(self):
        return self.__apellido

    def getmarca(self):
        return self.__marca

    def getkilometro(self):
        return self.__kilometro
