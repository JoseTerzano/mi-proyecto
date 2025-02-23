from ClasePlan import Plan

class Nodo:
    __maquina: Plan
    __sig: object
    
    def __init__(self, plan):
        self.__maquina = plan
        self.__sig = None

    def getplan(self):
        return self.__maquina

    def getSig(self):
        return self.__sig

    def setSig(self, sig):
        self.__sig = sig