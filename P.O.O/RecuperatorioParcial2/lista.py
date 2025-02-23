from  nodo import Nodo
from ClassMaquina import Maquina
from ClaseMaquinaPesada import MaquinaPesada
from ClaseMaquinaElectrica import MaquinaElectrica
import csv

class Lista:
    __comienzo: Nodo
    __actual: Nodo
    __indice: int
    __tope: int
    
    def __init__(self):
        self.__comienzo = None
        self.__actual = None
        self.__indice = 0
        self.__tope = 0
        
    def __iter__(self):
        self.__actual = self.__comienzo
        self.__indice = 0
        return self
    
    def __next__(self):
        if self.__actual is None:
            raise StopIteration
        if self.__indice == self.__tope:
            self.__actual = self.__comienzo
            self.__indice = 0
            raise StopIteration
        else:
            dato = self.__actual.getMaquina()
            self.__actual = self.__actual.getSig()
            self.__indice += 1
            return dato
    
    def agregar(self, maquina):
        nodo = Nodo(maquina)
        nodo.setSig(self.__comienzo)
        self.__comienzo = nodo
        self.__tope += 1
        
    def inicializar(self):
        archivo = open("equipos[1].csv")
        reader = csv.reader(archivo, delimiter=";")
        for fila in reader:
            if fila[0] == "M":
               
               self.agregar(MaquinaPesada(fila[1], fila[2], int(fila[3]), fila[4], fila[5], int(fila[6]), float(fila[7]), int(fila[8]), fila[9], int(fila[10])))
            elif fila[0] == "E":
                herramienta1 = MaquinaElectrica(fila[1], fila[2], int(fila[3]), fila[4], fila[5], (fila[6]), float(fila[7]), int(fila[8]), fila[9])
                self.agregar(herramienta1)
                
    def mostrar(self):
        aux = self.__comienzo
        while aux != None:
            print(aux.getMaquina())
            aux = aux.getSig()

    def excepcion(self, pos):
        if pos >= self.__tope:
            raise IndexError("Posicion invalida")
        else:
            maq = self.buscarPos(pos)
            if isinstance(maq, MaquinaPesada):
                print("es una maquina pesada")
            elif isinstance(maq, MaquinaElectrica):
                print("es una maquina electrica")
            
    def buscarPos(self, pos):
        aux = self.__comienzo
        self.__actual = 0
        while self.__actual != pos and self.__actual < self.__tope:
            aux = aux.getSig()
            self.__actual += 1
        return aux.getMaquina()

    def mostrarcantidad(self, anio):
        aux = self.__comienzo
        c = 0
        for dato in self:
            if isinstance(dato, MaquinaElectrica):
                if dato.getanio() == anio:
                    c += 1
        print(f"Cantidad de maquinas electricas de {anio}: {c}")


    def mostrarcapacidad(self, capacidad):
        aux = self.__comienzo
        c = 0
        for dato in self:
            if isinstance(dato, MaquinaPesada) and dato.getcapacidadCarga() <= capacidad:
                c += 1
        print(f"Cantidad de maquinas con capacidad de carga <= {capacidad}: {c}")