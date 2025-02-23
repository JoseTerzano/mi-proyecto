
class Equipo:
    __id = int
    __nombre = str
    __golesFav = int
    __golesCont = int
    __diferencia = int
    __puntos = int

    def __init__(self, id, nombre, golesFav, golesCont, diferencia, puntos):
        self.__id = int(id)
        self.__nombre = nombre
        self.__golesFav = int(golesFav)
        self.__golesCont = int(golesCont)
        self.__diferencia = int(diferencia)
        self.__puntos = int(puntos)

    def getnombre(self):
        return self.__nombre

    def getid(self):
        return self.__id

    def getgolesFav(self):
        return self.__golesFav

    def getgolesCont(self):
        return self.__golesCont

    def getdiferencia(self):
        return self.__diferencia

    def getpuntos(self):
        return self.__puntos

    def setpuntos(self, puntos):
        self.__puntos += puntos

    def __gt__(self, otro):
        if self.__puntos == otro.getpuntos():
            if self.__diferencia > otro.getdiferencia():
                return self.__diferencia > otro.getdiferencia()
            if self.__diferencia < otro.getdiferencia():
                return self.__diferencia < otro.getdiferencia()
            if self.__diferencia == otro.getdiferencia():
                if self.__golesFav > otro.getgolesFav():
                    return self.__golesFav < otro.getgolesFav()
                else:
                    return self.__golesFav > otro.getgolesFav()
        else:
            return self.__puntos < otro.getpuntos()
