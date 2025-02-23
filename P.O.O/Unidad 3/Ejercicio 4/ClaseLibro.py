from ClasePublicacion import Publicacion


class Libro(Publicacion):
    __autor = str
    __fecha = str
    __paginas = int

    def __init__(self, autor, fecha, paginas, titulo, cat, preciobase):
        super().__init__(titulo, cat, preciobase)
        self.__autor = autor
        self.__fecha = fecha
        self.__paginas = paginas

    def getfecha(self):
        return self.__fecha

    def CalcularImporte(self):
        fecha = self.getfecha().strip(' "')
        diferencia = 2024 - int(fecha)
        importe = int((diferencia/100)*self.getpreciobase())
        return importe

    def __str__(self):
        return f"autor del libro {self.__autor}, fecha {self.__fecha}, paginas {self.__paginas} {self.gettitulo()} {self.getcat()} {self.getpreciobase()}"
