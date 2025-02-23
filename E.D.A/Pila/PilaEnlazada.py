
from claseNodo import Nodo
class PilaEncadenada:
    __tope:Nodo
    __cont:int

    def __init__(self):
        self.__tope=None
        self.__cont=0

    def vacia(self):
        return self.__cont==0

    def insertar(self,item):
        nuevoNodo=Nodo(item)
        nuevoNodo.setSiguiente(self.__tope)
        self.__tope=nuevoNodo
        self.__cont+=1

    def suprimir(self):
        elemento=None
        if self.vacia():
            print("Pila Vacia, no se pueden eliminar elementos")
        else:
            elemento=self.__tope.getDato()
            self.__tope=self.__tope.getSiguiente()
            self.__cont -= 1
        return elemento

    def recorrer(self):
        aux=self.__tope
        while aux is not None:
            print(aux.getDato())
            aux=aux.getSiguiente()
    
if __name__=="__main__":
    p=PilaEncadenada()
    p.insertar(5)
    p.insertar(-7)
    p.insertar(6)
    p.recorrer()
    print("Se elimina el ",p.suprimir())
    p.recorrer()
    print("Se elimina el ",p.suprimir())
    p.recorrer()
    print("Se elimina el ",p.suprimir())