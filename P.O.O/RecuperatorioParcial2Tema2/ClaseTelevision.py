from ClasePlan import Plan
class Television(Plan):
    __cantNacional: int
    __cantInternacional: int

    def __init__(self, nombre, duracion, cobertura, preciobase, cantNacional, cantInternacional):
        super().__init__(nombre, duracion, cobertura, preciobase)
        self.__cantNacional = cantNacional
        self.__cantInternacional = cantInternacional
    
    def __str__(self):
        return f""" Cant nacional: {self.__cantNacional}  Cant internacional: {self.__cantInternacional}"""
