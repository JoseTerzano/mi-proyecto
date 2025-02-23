import numpy as np

class Hash:
    __tabla: np.ndarray
    __M: int
    def __init__(self, M):
        self.__M = int(M/0.7)
        self.__tabla = np.empty(self.__M, dtype= object)
    
    def metodoDivision(self, clave):
        return clave % self.__M
    
    def metodoExtraccion(self, clave):
        primeras_dos_cifras = str(clave)[:2]
        return int(primeras_dos_cifras)
    """
    def metodoPlegado(self, clave):
        primeraparte = str(clave)[:2]
        segundaparte = str(clave)[2:]
        return int(primeraparte + segundaparte)
    """

    def insertar(self, clave):
        numero = self.metodoDivision(clave)
        while self.__tabla[numero] is not None:
            numero = (numero + 2) % self.__M
        self.__tabla[numero] = clave

    def buscar(self, clave):
        posicion = self.metodoDivision(clave)
        while self.__tabla[posicion] != clave and self.__tabla[posicion] is not None:
            posicion = (posicion+2) % self.__M
        if self.__tabla[posicion] == clave:
                return posicion
        else:
            print("No existe la clave")
        
if __name__ == "__main__":
    tabla = Hash(100)
    tabla.insertar(150)
    tabla.insertar(250)
    tabla.insertar(10)
    tabla.insertar(4)
    tabla.insertar(8)
    tabla.insertar(2)
    print("el numero 5 esta en la posicion", tabla.buscar(5))
    print("el numero 8 esta en la posicion", tabla.buscar(8))
    print("el numero 4 esta en la posicion", tabla.buscar(4))
    print("el numero 2 esta en la posicion", tabla.buscar(2))
    print("el numero 150 esta en la posicion", tabla.buscar(150))
    print("el numero 250 esta en la posicion", tabla.buscar(250))

