from ClasePublicacion import Publicacion


class CD(Publicacion):
    __tiempo = int
    __narrador = str

    def __init__(self, tiempo, nar, tit, cat, precio):
        super().__init__(tit, cat, precio)
        self.__tiempo = tiempo
        self.__narrador = nar

    def CalcularImporte(self):
        suma = (10*100)/self.getpreciobase()
        c = int(self.getpreciobase()+suma)
        return c

    def __str__(self):
        return f"narrador {self.__narrador}, tiempo {
            self.__tiempo} {self.gettitulo()} {self.getcat()} {self.getpreciobase()}"
