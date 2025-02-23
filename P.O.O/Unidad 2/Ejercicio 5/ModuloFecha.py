
class Fecha:
    __fecha = str
    __idEquipoLocal = int
    __idEquipoVisit = int
    __golesLocal = int
    __golesVisit = int

    def __init__(self, fecha, idEquipoLocal, idEquipoVisit, golesLocal, golesVisit):
        self.__fecha = fecha
        self.__idEquipoLocal = int(idEquipoLocal)
        self.__idEquipoVisit = int(idEquipoVisit)
        self.__golesLocal = int(golesLocal)
        self.__golesVisit = int(golesVisit)

    def getfecha(self):
        return self.__fecha

    def getidLocal(self):
        return self.__idEquipoLocal

    def getidVisit(self):
        return self.__idEquipoVisit

    def getgolesLocal(self):
        return self.__golesLocal

    def getgolesVisit(self):
        return self.__golesVisit
