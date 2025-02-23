

class contenedor:
    lista = []

    def __init__(self):
        self.lista = []

    def agregar(self, objeto):
        self.lista.append(objeto)

    def mostrar(self):
        for e in self.lista:
            e.mostrarDatos()

    def buscaCuil(self, cuil):
        i = 0
        encontrado = False
        while ((i < len(self.lista)) & (encontrado is False)):
            if self.lista[i].getCuil() == cuil:
                encontrado = True
            else:
                i += 1
        if encontrado is False:
            print("Cuil no valido")
        else:
            self.lista[i].mostrarDatos()
