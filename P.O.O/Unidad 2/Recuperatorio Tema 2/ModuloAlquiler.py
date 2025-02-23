class Alquiler:
    __nombrePersona = str
    __idCanchaAlquilada = str
    __hora = str
    __minutos = str
    __duracion = int

    def __init__(self, nombre, id, hora, minutos, duracion):
        self.__nombrePersona = nombre
        self.__idCanchaAlquilada = id
        self.__hora = hora
        self.__minutos = minutos
        self.__duracion = int(duracion)

    def getnombre(self):
        return self.__nombrePersona

    def getidcancha(self):
        return self.__idCanchaAlquilada

    def gethora(self):
        return self.__hora

    def getminutos(self):
        return self.__minutos

    def getduracion(self):
        return self.__duracion

    def __gt__(self, otro):
        if self.__hora == otro.gethora():
            return self.__minutos < otro.getminutos()
        else:
            return self.__hora < otro.gethora()
