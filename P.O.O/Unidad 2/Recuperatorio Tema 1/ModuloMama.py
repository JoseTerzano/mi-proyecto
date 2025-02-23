class Mama:
    __dni = int
    __edad = int
    __apellidoynombre = str

    def __init__(self, dni, edad, apellidoynombre):
        self.__dni = int(dni)
        self.__edad = int(edad)
        self.__apellidoynombre = apellidoynombre

    def getdni(self):
        return self.__dni

    def getedad(self):
        return self.__edad

    def getapellido(self):
        return self.__apellidoynombre
