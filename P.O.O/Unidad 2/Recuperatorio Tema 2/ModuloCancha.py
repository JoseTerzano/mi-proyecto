class Cancha:
    __id = str
    __tipo = str
    __importe = float

    def __init__(self, id, tipo, importe):
        self.__id = id
        self.__tipo = tipo
        self.__importe = float(importe)

    def getid(self):
        return self.__id

    def gettipo(self):
        return self.__tipo

    def getimporte(self):
        return self.__importe
