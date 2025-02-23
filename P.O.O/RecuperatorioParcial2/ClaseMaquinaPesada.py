from ClassMaquina import Maquina

class MaquinaPesada(Maquina):
    __tipomaquina = str
    __peso = int

    def __init__(self, marca, modelo, anio, combustible, potencia, capacidadcarga, alquilerdiario, diasalquiler, tipomaquina, peso):
        super().__init__(marca, modelo, anio, combustible, potencia, capacidadcarga, alquilerdiario, diasalquiler)
        self.__tipomaquina = tipomaquina
        self.__peso = peso

    def __str__(self):
        return f"{super().__str__()} {self.__tipomaquina} {self.__peso} {self.tarifaAlquiler()}"
    
    def tarifaAlquiler(self):
        if self.__peso <= 10:
            c = super().getalquierdiario() * super().getdiasalquiler()
            return c
        else:
            c = super().getalquierdiario() * super().getdiasalquiler() * 1.2
            return c