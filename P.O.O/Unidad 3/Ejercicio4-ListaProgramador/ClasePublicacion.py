class Publicacion:
    __titulo: str
    __categoria: str
    __precioB: float

    def __init__(self, titulo, categoria, precioB):
        self.__titulo = titulo
        self.__categoria = categoria
        self.__precioB = precioB

    def gettitulo(self):
        return self.__titulo

    def getcategoria(self):
        return self.__categoria

    def getprecioB(self):
        return self.__precioB

    def getimporteventa(self):
        pass
