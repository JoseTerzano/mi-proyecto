class cliente:
    __nombre = str
    __apellido = str
    __dni = int
    __nroCuenta = int
    __saldoAnt = float

    def __init__(self, nombre, apellido, dni, nroCuenta, saldoAnt):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__dni = int(dni)
        self.__nroCuenta = int(nroCuenta)
        self.__saldoAnt = float(saldoAnt)

    def getdni(self):
        return self.__dni

    def getsaldoAnt(self):
        return self.__saldoAnt

    def getnroCuenta(self):
        return self.__nroCuenta

    def setsaldo(self, saldo):
        self.__saldoAnt = saldo

    def getnombre(self):
        return self.__nombre

    def getapellido(self):
        return self.__apellido
