from ClassMaquina import Maquina

class MaquinaElectrica(Maquina):
    __alimentacion = str

    def __init__(self, marca, modelo, anio, combustible, potencia, capacidadcarga, alquilerdiario, diasalquiler, alimentacion):
        super().__init__(marca, modelo, anio, combustible, potencia, capacidadcarga, alquilerdiario, diasalquiler)
        self.__alimentacion = alimentacion
    
    def __str__(self):
        return f"{super().__str__()} {self.__alimentacion} {self.tarifaAlquiler()}"
    
    def tarifaAlquiler(self):
        if self.__alimentacion == "bateria":
            c = (super().getalquierdiario() * super().getdiasalquiler() )* 1.1
            return c
        else:
            c = super().getalquierdiario() * super().getdiasalquiler()
            return c
    
    