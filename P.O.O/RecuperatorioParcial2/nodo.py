from ClassMaquina import Maquina

class Nodo:
    __maquina: Maquina
    __sig: object
    
    def __init__(self, maquina):
        self.__maquina = maquina
        self.__sig = None

    def getMaquina(self):
        return self.__maquina

    def getSig(self):
        return self.__sig

    def setSig(self, sig):
        self.__sig = sig