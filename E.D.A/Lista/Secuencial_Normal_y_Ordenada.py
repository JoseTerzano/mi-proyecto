import numpy as np

class ListaSecuencial:
    def __init__(self, tamanio=5):
        self.__tamanio = tamanio
        self.__ultimo = -1
        self.__cantidad = 0
        self.__arreglo = np.empty(self.__tamanio, dtype=int)
        
    def vacia(self):
        return self.__cantidad == 0
    
    def lleno(self):
        return self.__cantidad == self.__tamanio
    
    def insertar(self, dato, posicion):
        if not self.lleno():
            if 0 <= posicion <= self.__ultimo + 1:
                i = self.__ultimo + 1
                while i > posicion:
                    self.__arreglo[i] = self.__arreglo[i - 1]
                    i -= 1
                self.__arreglo[posicion] = dato  # Mueve esta línea fuera del bucle while
                self.__ultimo += 1
                self.__cantidad += 1
            else:
                print("Posición fuera de rango")
        else:
            print("Lista llena")
    
    def insertarPorContenido(self, dato):
        if not self.lleno():
            if self.vacia():
                self.__ultimo += 1
                self.__arreglo[self.__ultimo] = dato
                self.__cantidad += 1
                print(f"Elemento insertado: {dato}")
            else:
                i = 0
                while i <= self.__ultimo and self.__arreglo[i] < dato: #busca la posicion
                    i += 1
                for j in range(self.__ultimo + 1, i, -1): #desplaza hacia la derecha los elementos para hacer espacio en la posicion i y poder insertar el elemento
                    self.__arreglo[j] = self.__arreglo[j - 1]
                self.__arreglo[i] = dato
                self.__ultimo += 1
                self.__cantidad += 1
                print(f"Elemento insertado: {dato}")
        else:
            print("Lista llena")
            
    def recorrer(self):
        if not self.vacia():
            for i in range(self.__ultimo + 1):
                print(self.__arreglo[i])
        else:
            print("Lista vacía")
                
    def suprimir(self, pos):
        if not self.vacia():
            if 0 <= pos <= self.__ultimo:
                eliminado = self.__arreglo[pos]
                for i in range(pos, self.__ultimo):
                    self.__arreglo[i] = self.__arreglo[i + 1]
                self.__cantidad -= 1
                self.__ultimo -= 1
                print(f"Elemento eliminado: {eliminado}")
            else:
                print("Posición fuera de rango")
        else:
            print("Lista vacía")
    
    def suprimirPorContenido(self, dato):
        if not self.vacia():
            i = 0
            while i <= self.__ultimo and self.__arreglo[i] != dato: 
                i += 1
            if i <= self.__ultimo:
                for j in range(i, self.__ultimo): #desplaza hacia la izquierda los elementos para eliminar el espacio vacio por el elemento eliminado
                    self.__arreglo[j] = self.__arreglo[j + 1]
                self.__ultimo -= 1
                self.__cantidad -= 1
                print(f"Elemento eliminado: {dato}")
            else:
                print(f"El elemento {dato} no se encuentra en la lista")
        else:
            print("Lista vacía")
            
    def buscar(self, dato):
        if not self.vacia():
            i = 0
            while i <= self.__ultimo and self.__arreglo[i] != dato:
                i += 1
            if i <= self.__ultimo:
                print(f"Elemento encontrado: {dato} en posicion {i}")
                return i
            else:
                print(f"El elemento {dato} no se encuentra en la lista")
                return -1
        else:
            print("Lista vacía")
            return -1
            
    def primerElemento(self):
        if not self.vacia():
            return self.__arreglo[0]
        
    def ultimoElemento(self):
        if not self.vacia():
            return self.__arreglo[self.__ultimo]
        
    def siguiente(self, pos):
        if not self.vacia():
            if pos == self.__ultimo:
                print("No hay más elementos")
            elif 0 <= pos < self.__ultimo:
                print(f"El elemento siguiente es {self.__arreglo[pos + 1]}")
            else:
                print("Posición fuera de rango")
                    
    def anterior(self, pos):
        if not self.vacia():
            if pos == 0:
                print("No hay más elementos anteriores")
            elif 0 < pos <= self.__ultimo:
                print(f"El elemento anterior es {self.__arreglo[pos - 1]}")
            else:
                print("Posición fuera de rango")

if __name__ == "__main__":
    lista = ListaSecuencial(5)
    lista.insertar(1, 0)
    lista.insertar(2, 1)
    lista.insertar(3, 0)
    lista.insertar(4, 1)
    lista.recorrer()
    lista.suprimir(0)
    lista.buscar(3)
    print(lista.primerElemento())
    print(lista.ultimoElemento())
    lista.siguiente(0)
    lista.anterior(1)