class movimiento:
    __nroCuenta = int
    __fecha = str
    __descripcion = str
    __tipoMov = str
    __importe = float

    def __init__(self, nroCuenta, fecha, descripcion, tipoMov, importe):
        self.__nroCuenta = int(nroCuenta)
        self.__fecha = fecha
        self.__descripcion = descripcion
        self.__tipoMov = tipoMov
        self.__importe = float(importe)

    def getNroCuenta(self):
        return self.__nroCuenta

    def gettipoMov(self):
        return self.__tipoMov

    def getimporte(self):
        return self.__importe

    def getfecha(self):
        return self.__fecha

    def getdescripcion(self):
        return self.__descripcion

    def __lt__(self, otro):
        return self.__nroCuenta < otro.getNroCuenta()
