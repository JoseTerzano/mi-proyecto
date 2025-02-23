from datetime import datetime
from ClasePublicacion import Publicacion


class Libro(Publicacion):
    __nomA: str
    __fechaE: str
    __cantP: int

    def __init__(self, titulo, categoria, precioB, nomA, fechaE, cantP) -> None:
        super().__init__(titulo, categoria, precioB)
        self.__nomA = nomA
        self.__fechaE = fechaE
        self.__cantP = cantP

    def getnomA(self):
        return self.__nomA

    def getfechaE(self) -> str:
        return self.__fechaE

    def getcantP(self):
        return self.__cantP

    def getimporteventa(self):
        añoE = int(self.__fechaE.split('-')[0])
        añoA = datetime.now().year
        añoAn = (añoA - añoE)
        porc = 0.01 * añoAn
        imp = float(self.getprecioB()) - float(self.getprecioB()) * porc
        return imp
