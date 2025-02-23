class fontaneroDiligente:
    __arreglo = []
    def __init__(self, arreglo):
        self.__arreglo = arreglo

    def ordenarOptimo(self):
        tiemposOrdenados = sorted(self.__arreglo)  # Ordenar los tiempos de reparación en orden ascendente
        self.__arreglo = tiemposOrdenados

    def ordenarMenosOptimo(self):
        tiemposOrdenados = sorted(self.__arreglo, reverse=True)  # Ordenar los tiempos de reparación en orden descendente
        self.__arreglo = tiemposOrdenados

    def tiempoTotalEspera(self):
        tiempoTotalEspera = 0
        tiempoAcumulado = 0
        for tiempo in self.__arreglo:
            tiempoTotalEspera += tiempoAcumulado
            tiempoAcumulado += tiempo
        return tiempoTotalEspera
    
if __name__ == "__main__":
    arreglo = [5,4,8,3,1]
    fontanero = fontaneroDiligente(arreglo)
    fontanero2 = fontaneroDiligente(arreglo)
    fontanero3 = fontaneroDiligente(arreglo)

    fontanero.ordenarOptimo()
    fontanero3.ordenarMenosOptimo()

    c = fontanero.tiempoTotalEspera()
    p = fontanero2.tiempoTotalEspera()
    l = fontanero3.tiempoTotalEspera()

    print("Tiempo espera ordenado promedio: ", c/len(arreglo), " minutos")
    print("Tiempo espera sin ordenar promedio: ", p/len(arreglo), " minutos")
    print("Tiempo espera ordenado inverso promedio: ", l/len(arreglo), " minutos")
