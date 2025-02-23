class Departamento:
    __id : int
    __NyA : str
    __numPiso : int
    __numDepto : int
    __chab : int
    __cbanos : int
    __sup : float
    def __init__(self, id, NyA, numPiso, numDepto, chab, cbanos, sup):
        self.__id = id
        self.__NyA = NyA
        self.__numPiso = numPiso
        self.__numDepto = numDepto
        self.__chab = chab
        self.__cbanos = cbanos
        self.__sup = sup
    def getnom(self):
        return self.__NyA
    def getnumeropiso(self):
        return self.__numPiso
    def getnumerodepto(self):
        return self.__numDepto
    def getchab(self):
        return self.__chab
    def getcbanos(self):
        return self.__cbanos
    def getsup(self):
        return self.__sup
    def __str__(self):
        cadena = "Propietario: {}".format(self.__NyA)
        return cadena
    