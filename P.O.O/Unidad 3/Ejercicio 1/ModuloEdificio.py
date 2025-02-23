

class Edificio:
    __id = int
    __nombre = str
    __direccion = str
    __empresa = str
    __cantpisos = int
    __cantdptos = int
    __departamentos = list

    def __init__(self, i, n, d, e, c, ca):
        self.__id = i
        self.__nombre = n
        self.__direccion = d
        self.__empresa = e
        self.__cantpisos = c
        self.__cantdptos = ca
        self.__departamentos = []

    def agregardepartamento(self, dpto):
        self.__departamentos.append(dpto)

    def ListaDptos(self):
        return self.__departamentos

    def getnombreEdi(self):
        return self.__nombre
