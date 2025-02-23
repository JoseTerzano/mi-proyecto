from ClasePlan import Plan
class Telefonia(Plan):
    __tipo: str
    __minutos: int

    def __init__(self, nombre, duracion, cobertura, preciobase, tipo, minutos):
        super().__init__(nombre, duracion, cobertura, preciobase)
        self.__tipo = tipo
        self.__minutos = minutos

    def __str__(self):
        return f"""Tipo: {self.__tipo}  Minutos: {self.__minutos}"""