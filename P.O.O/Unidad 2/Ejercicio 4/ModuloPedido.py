class pedido:
    __patenteAsig = str
    __id = int
    __comidas = str
    __tiempoEst = int
    __tiempoReal = int
    __precio = float

    def __init__(self, patenteAsig, id, comidas, tiempoEst, tiempoReal, precio):
        self.__patenteAsig = patenteAsig
        self.__id = int(id)
        self.__comidas = comidas
        self.__tiempoEst = int(tiempoEst)
        self.__tiempoReal = int(tiempoReal)
        self.__precio = float(precio)

    def settiempoReal(self, tiempo):
        self.__tiempoReal = int(tiempo)

    def getpatente(self):
        return self.__patenteAsig

    def gettiempoReal(self):
        return self.__tiempoReal

    def getid(self):
        return self.__id

    def gettiempoEst(self):
        return self.__tiempoEst

    def gettiempoReal(self):
        return self.__tiempoReal

    def getprecio(self):
        return self.__precio
