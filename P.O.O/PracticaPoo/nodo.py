from ClaseClienteLocal import ClienteLocal

class Nodo:
    __cliente: ClienteLocal
    __sig: object
    
    def __init__(self, cliente):
        self.__cliente = cliente
        self.__sig = None

    def getCliente(self):
        return self.__cliente

    def getSig(self):
        return self.__sig

    def setSig(self, sig):
        self.__sig = sig