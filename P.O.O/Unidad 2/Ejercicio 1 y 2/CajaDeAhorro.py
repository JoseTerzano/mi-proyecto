class CajaDeAhorro():
    nroCuenta = str
    cuil = str
    apellido = str
    nombre = str
    saldo = float

    def __init__(self, nroCuenta, cuil, apellido, nombre, saldo):
        self.__nroCuenta = nroCuenta
        self.__cuil = cuil
        self.__apellido = apellido
        self.__nombre = nombre
        self.__saldo = float(saldo)

    def mostrarDatos(self):
        print(f"""
        Nro de cuenta: {self.__nroCuenta}
        Cuil: {self.__cuil}
        Apellido y nombre: {self.__apellido} {self.__nombre}
        El saldo es {self.__saldo}""")

    def extraer(self, importe):
        if self.__saldo >= importe:
            self.__saldo -= importe
            print("El nuevo saldo es:", self.__saldo)
        else:
            print("Saldo insuficiente")

    def depositar(self, importe):
        if importe > 0:
            self.__saldo += importe

    def test(self):
        for _ in range(2):
            nrocuenta = input("Ingrese numero de cuenta ")
            cuil = input("Ingrese Cuil ")
            apellido = input("Ingrese apellido ")
            nombre = input("Ingrese nombre ")
            saldo = float(input("Ingrese saldo "))
            persona = CajaDeAhorro(nrocuenta, cuil, apellido, nombre, saldo)
            importe = float(input("Ingrese importe de extraccion: "))
            persona.extraer(importe)
            importe2 = float(input("Ingrese importe de deposito: "))
            persona.depositar(importe2)
            persona.mostrarDatos()

    def crearCaja(self):
        for _ in range(3):
            nrocuenta = input("Ingrese numero de cuenta ")
            cuil = input("Ingrese Cuil ")
            apellido = input("Ingrese apellido ")
            nombre = input("Ingrese nombre ")
            saldo = float(input("Ingrese saldo "))
            objeto = CajaDeAhorro(nrocuenta, cuil, apellido, nombre, saldo)
            return objeto

    def getCuil(self):
        return self.__cuil
