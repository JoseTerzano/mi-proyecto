
class Nodo:
    __dato:object
    __siguienteizq:object
    __siguienteder:object

    def __init__(self,dato):
        self.__dato=dato
        self.__siguienteizq=None
        self.__siguienteder=None

    def setSiguienteIzq(self,siguiente):
        self.__siguienteizq=siguiente

    def setSiguienteDer(self,siguienteder):
        self.__siguienteder=siguienteder

    def getDato(self):
        return self.__dato
    
    def getSiguienteIzq(self):
        return self.__siguienteizq
    
    def getSiguienteDer(self):
        return self.__siguienteder
    
    def setDato(self,dato):
        self.__dato=dato