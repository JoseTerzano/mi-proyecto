from ClasePublicacion import Publicacion

class Audio(Publicacion):
    __tieRep: int
    __nom: str
    def __init__(self, titulo, categoria, precioB, tieRep, nom):
        super().__init__(titulo, categoria, precioB)
        self.__tieRep = tieRep
        self.__nom = nom
    
    def gettieRep(self):
        return self.__tieRep
    def getnom(self):
        return self.__nom
    
    def getimporteventa(self):
        imp = float(self.getprecioB()) + float(self.getprecioB()) * 0.1
        return imp
    