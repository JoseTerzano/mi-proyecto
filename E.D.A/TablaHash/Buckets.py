import numpy as np

class buckets:
    __tabla: np.ndarray
    __overflow: int
    __cant_claves: np.ndarray
    __dimension: int

    def __init__(self, claves, buckets):
        self.__dimension = int((claves / buckets) + 20 % (claves / buckets))
        self.__tabla = np.empty((self.__dimension, buckets))
        self.__cant_claves = np.zeros(self.__dimension)
        self.__overflow = claves / buckets

    def metodo_division(self, clave, c, b):
        return int(clave % (c / b))

    def insertar(self, clave, c, b):
        pos = self.metodo_division(clave, c, b)
        if self.__cant_claves[pos] < b:
            self.__tabla[pos, int(self.__cant_claves[pos])] = clave
            self.__cant_claves[pos] += 1
        else:
            o = int(self.__overflow)
            while self.__cant_claves[o] == b and o != self.__dimension:
                o += 1
            if o == self.__dimension:
                print("No queda espacio en el área de overflow. No se puede insertar")
            else:
                self.__tabla[o, self.__cant_claves[o]] = clave
                self.__cant_claves[o] += 1

    def buscar(self, clave, c, b):
        pos = self.metodo_division(clave, c, b)
        fila = None
        columna = None
        j = 0
        while j < b and self.__tabla[pos, j] != clave:
            j += 1
        if j < b:
            fila = pos
            columna = j
        else:
            o = self.__overflow
            while o < self.__dimension:
                j = 0
                while j < b and self.__tabla[o, j] != clave:
                    j += 1
                if j == b:
                    o += 1
                else:
                    fila = o
                    columna = j
                    break
        return fila, columna

if __name__ == "__main__":
    tabla = buckets(100, 10)
    tabla.insertar(150, 100, 10)
    tabla.insertar(250, 100, 10)
    tabla.insertar(10, 100, 10)
    tabla.insertar(4, 100, 10)
    tabla.insertar(8, 100, 10)
    tabla.insertar(2, 100, 10)
    tabla.insertar(22, 100, 10)
    tabla.insertar(32, 100, 10)
    tabla.insertar(42, 100, 10)
    print("el número 8 está en la posición", tabla.buscar(8, 100, 10))
    print("el número 4 está en la posición", tabla.buscar(4, 100, 10))
    print("el número 2 está en la posición", tabla.buscar(2, 100, 10))
    print("el número 150 está en la posición", tabla.buscar(150, 100, 10))
    print("el número 250 está en la posición", tabla.buscar(250, 100, 10))
    print("el número 22 está en la posición", tabla.buscar(22, 100, 10))
    print("el número 32 está en la posición", tabla.buscar(32, 100, 10))
    print("el número 42 está en la posición", tabla.buscar(42, 100, 10))
