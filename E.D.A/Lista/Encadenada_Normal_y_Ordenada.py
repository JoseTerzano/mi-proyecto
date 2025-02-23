from claseNodo import Nodo

class ListaEncadenada:
    def __init__(self):
        self.__cabeza = None
        self.__cont = 0

    def vacia(self):
        return self.__cont == 0

    def insertar(self, dato, posicion):
        nuevoNodo = Nodo(dato)
        if posicion >= 0 and posicion <= self.__cont:
            if posicion == 0:
                nuevoNodo.setSiguiente(self.__cabeza)
                self.__cabeza = nuevoNodo
            else:
                actual = self.__cabeza
                for _ in range(posicion - 1):
                    actual = actual.getSiguiente()
                
                nuevoNodo.setSiguiente(actual.getSiguiente())
                actual.setSiguiente(nuevoNodo)
                
            self.__cont += 1
        else:
            print("Índice fuera de rango")

    def suprimir(self, posicion):
        if self.vacia():
            print("La lista se encuentra vacía")
            return None
        elif posicion < 0 or posicion >= self.__cont:
            print("Índice fuera de rango")
            return None

        if posicion == 0:
            elemento = self.__cabeza.getDato()
            self.__cabeza = self.__cabeza.getSiguiente()
        else:
            anterior = self.__cabeza
            actual = anterior.getSiguiente()
            for _ in range(1, posicion):
                anterior = actual
                actual = actual.getSiguiente()

            elemento = actual.getDato()
            anterior.setSiguiente(actual.getSiguiente())

        self.__cont -= 1
        return elemento
    
    def insertarPorContenido(self, dato):
        nuevoNodo = Nodo(dato)
        if self.vacia():
            # Si la lista está vacía, simplemente se agrega como cabeza
            self.__cabeza = nuevoNodo
        else:
            # Caso cuando hay que insertar en la posición correcta
            actual = self.__cabeza
            anterior = None
            # Recorrer hasta encontrar la posición correcta para insertar
            while actual is not None and actual.getDato() < dato:
                anterior = actual
                actual = actual.getSiguiente()
            
            if anterior is None:
                # Insertar al principio si es el menor elemento
                nuevoNodo.setSiguiente(self.__cabeza)
                self.__cabeza = nuevoNodo
            else:
                # Insertar en la posición encontrada
                nuevoNodo.setSiguiente(actual)
                anterior.setSiguiente(nuevoNodo)
        
        self.__cont += 1
        print(f"Elemento insertado: {dato}")

    def suprimirPorContenido(self, dato):
        if self.vacia():
            print("Lista vacía")
            return False
        
        actual = self.__cabeza
        anterior = None
        
        # Buscar el nodo con el dato
        while actual is not None and actual.getDato() != dato:
            anterior = actual
            actual = actual.getSiguiente()
        
        # Si el nodo fue encontrado
        if actual is not None:
            if anterior is None:
                # Si el nodo a eliminar es el primero
                self.__cabeza = actual.getSiguiente()
            else:
                # Si el nodo a eliminar no es el primero
                anterior.setSiguiente(actual.getSiguiente())
            
            self.__cont -= 1
            print(f"Elemento eliminado: {dato}")
            return True
        else:
            print(f"El elemento {dato} no se encuentra en la lista")
            return False
    
    def mostrar(self):
        actual = self.__cabeza
        while actual is not None:
            print(f"{actual.getDato()}", end="->")
            actual = actual.getSiguiente()
        print("None")

    def buscar(self, dato):
        aux = self.__cabeza
        pos = 0
        while aux is not None and aux.getDato() != dato:
            aux = aux.getSiguiente()
            pos += 1
        if aux.getDato() == dato:
            return pos
        else:
            print(f"El elemento {dato} no se encuentra en la lista")

    def primerElemento(self):
        if self.__cabeza is not None:
            return self.__cabeza.getDato()
        else:
            print("La lista está vacía")
            return None

    def ultimoElemento(self):
        aux = self.__cabeza
        if aux is None:
            print("La lista está vacía")
            return None
        
        while aux.getSiguiente() is not None:
            aux = aux.getSiguiente()
        return aux.getDato()
    
    def anterior(self, pos):
        if pos <= 0 or pos >= self.__cont:
            print("El índice ingresado no es válido o es el primero (no tiene anterior).")
            return None
        
        aux = self.__cabeza
        for _ in range(pos - 1):
            aux = aux.getSiguiente()
        
        return aux.getDato()
    
    def siguiente(self, pos):
        if pos < 0 or pos >= self.__cont - 1:
            print("El índice ingresado no es válido o es el último (no tiene siguiente).")
            return None
        
        aux = self.__cabeza
        for _ in range(pos + 1):
            aux = aux.getSiguiente()
        
        return aux.getDato()

    def recuperar(self, pos):
        if pos < 0 or pos >= self.__cont:
            print("Índice fuera de rango")
            return None

        aux = self.__cabeza
        for _ in range(pos):
            aux = aux.getSiguiente()
        
        return aux.getDato()


if __name__ == "__main__":
    lista = ListaEncadenada()
    lista.insertarPorContenido(10)
    lista.insertarPorContenido(5)
    lista.insertarPorContenido(15)
    lista.insertarPorContenido(7)
    lista.mostrar()
    lista.insertar(10, 0)
    lista.insertar(5, 1)
    lista.insertar(15, 2)
    lista.insertar(7, 3)
    lista.mostrar()
    lista.insertar(15, 0)
    lista.insertar(7, 1)
    lista.mostrar()
    print(f"El primer elemento es: {lista.primerElemento()}")
    print(f"El último elemento es: {lista.ultimoElemento()}")
    print(f"Se elimina el {lista.suprimir(0)}")
    lista.mostrar()
    print(f"El elemento 10 está en la posición {lista.buscar(10)}")
    print(f"En la posición 2 se encuentra el elemento {lista.recuperar(2)}")
    print(f"El elemento siguiente a la posición 2 es el {lista.siguiente(2)}")
    print(f"El elemento anterior a la posición 1 es el {lista.anterior(1)}")