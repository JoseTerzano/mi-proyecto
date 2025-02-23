from ClasePublicacion import Publicacion


class Nodo(Publicacion):
    __publi: Publicacion
    __sig: object

    def __init__(self, publi):
        self.__publi = publi
        self.__sig = None

    def setsig(self, sig):
        self.__sig = sig

    def getsig(self):
        return self.__sig

    def getpubli(self):
        return self.__publi
