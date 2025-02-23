import numpy as np
class PilaSecuencial:
    __tope:int
    __arreglo:np.ndarray

    def __init__(self):
        self.__tope = -1
        self.__arreglo = np.empty(10,dtype=object)

    def vacia(self):
        return self.__tope == -1

    def llena(self):
        return self.__tope==len(self.__arreglo)-1

    def insertar(self,item):
        if self.llena() is False:
            self.__tope+=1
            self.__arreglo[self.__tope]=item
        else:
            print(f"No es posible insertar el elemento {item}. Pila llena")

    def suprimir(self):
        elemento=None
        if self.vacia() is False:
            elemento = self.__arreglo[self.__tope]
            self.__tope -= 1
        else:
            print("No es posible eliminar elementos. La pila esta vacia")
        return elemento

    def recorrer(self):
        i = self.__tope
        if not self.vacia():
            while i >= 0:
                print(self.__arreglo[i])
                i -= 1

                
if __name__=="__main__":
    p=PilaSecuencial()
    try:
        decimal=int(input("Ingresa el numero decimal: "))
        aux=decimal
        while aux>=1:
            modulo=aux%2
            aux=aux//2
            p.insertar(modulo)
    except ValueError:
        print("Error. Se esperaba un entero")
        
    print("En binario es: ",end=" ")
    while p.vacia() is False:
        print(p.suprimir(),end="")