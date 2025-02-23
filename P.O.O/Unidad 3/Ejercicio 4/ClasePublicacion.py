class Publicacion:
    __titulo = str
    __cat = str
    __precioBase = float

    def __init__(self, t, c, p):
        self.__titulo = t
        self.__cat = c
        self.__precioBase = p

    def gettitulo(self):
        return self.__titulo

    def getcat(self):
        return self.__cat

    def getpreciobase(self):
        return self.__precioBase

    def __str__(self):
        return f"titulo {self.__titulo} \n categoria {
            self.__cat} \n precio base {self.__precioBase}"

    def CalcularImporte(self):
        pass
