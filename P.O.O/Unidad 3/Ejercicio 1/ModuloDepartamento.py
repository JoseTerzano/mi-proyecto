class Departamento:
    __id = int
    __nomyape = str
    __piso = int
    __dpto = int
    __cantdor = int
    __cantban = int
    __superficie = float

    def __init__(self, a, b, c, d, e, f, g):
        self.__id = a
        self.__nomyape = b
        self.__piso = c
        self.__dpto = d
        self.__cantdor = e
        self.__cantban = f
        self.__superficie = g

    def getid(self):
        return self.__id

    def getnombre(self):
        return self.__nomyape

    def getpiso(self):
        return self.__piso

    def getdpto(self):
        return self.__dpto

    def getcantdor(self):
        return self.__cantdor

    def getcantban(self):
        return self.__cantban

    def getsuperficie(self):
        return float(self.__superficie)

    def __str__(self):
        cadena = "propietario: {}".format(self.__nomyape)
        return cadena
