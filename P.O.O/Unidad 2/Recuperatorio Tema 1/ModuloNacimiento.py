class Nacimiento:
    __dnimadre = int
    __tipoparto = str
    __fecha = str
    __hora = str
    __peso = float
    __altura = int

    def __init__(self, dnimadre, tipoparto, fecha, hora, peso, altura):
        self.__dnimadre = int(dnimadre)
        self.__tipoparto = tipoparto
        self.__fecha = fecha
        self.__hora = hora
        self.__peso = float(peso)
        self.__altura = int(altura)

    def getdnimadre(self):
        return self.__dnimadre

    def gettipoparto(self):
        return self.__tipoparto

    def getfecha(self):
        return self.__fecha

    def gethora(self):
        return self.__hora

    def getpeso(self):
        return self.__peso

    def getaltura(self):
        return self.__altura

    def __eq__(self, otro):
        return self.__dnimadre == otro.getdnimadre() and self.__fecha == otro.getfecha()
