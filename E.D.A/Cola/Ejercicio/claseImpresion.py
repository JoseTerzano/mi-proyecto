class Impresion:
    __tiempoDemora:int

    def __init__(self, tiempoDemora):
        self.__tiempoDemora=tiempoDemora
    
    def gettiempoDemora(self):
        return self.__tiempoDemora
    
    def nuevademora(self,tiempoDemora):
        self.__tiempoDemora=tiempoDemora

    def __str__(self):
        return f"Tiempo de impresion: {self.__tiempoDemora}"