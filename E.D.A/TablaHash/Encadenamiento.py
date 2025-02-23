from claseNodo import Nodo

class hash_encadenamiento:
    __tabla:list
    __dimension:int
    __cant:int

    def __init__(self, dim):
        self.__dimension = dim
        self.__tabla = [None] * self.__dimension
        self.__cant = 0

    def metodo_division(self, clave):
        return clave % self.__dimension

    def insertar(self, valor):
        pos = self.metodo_division(valor)
        if self.__tabla[pos] is None:
            self.__cant += 1
            nuevo = Nodo(valor)
            self.__tabla[pos] = nuevo
        else:
            cabeza = self.__tabla[pos]
            while cabeza.getDato() != valor and cabeza.getSiguiente() is not None:
                cabeza = cabeza.getSiguiente()
            if cabeza.getSiguiente() is None:
                nuevo = Nodo(valor)
                cabeza.setSiguiente(nuevo)
                self.__cant += 1

    def buscar(self, valor):
        pos = self.metodo_division(valor)
        cabeza = self.__tabla[pos]
        while cabeza.getDato() != valor and cabeza.getSiguiente() is not None:
            cabeza = cabeza.getSiguiente()
        if cabeza.getDato() == valor:
            return pos
        else:
            print("Valor no encontrado")
        
if __name__ == "__main__":
    tabla = hash_encadenamiento(100)
    tabla.insertar(150)
    tabla.insertar(250)
    tabla.insertar(10)
    tabla.insertar(4)
    tabla.insertar(8)
    tabla.insertar(2)
    print("el numero 8 esta en la posicion", tabla.buscar(8))
    print("el numero 4 esta en la posicion", tabla.buscar(4))
    print("el numero 2 esta en la posicion", tabla.buscar(2))
    print("el numero 150 esta en la posicion", tabla.buscar(150))
    print("el numero 250 esta en la posicion", tabla.buscar(250))
