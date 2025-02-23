import numpy as np
from random import uniform
from claseImpresion import Impresion
class ColaSecuencial:
    __ult:int
    __pri:int
    __cont:int
    __arregloDatos:np.ndarray

    def __init__(self):
        self.__pri=0
        self.__ult=0
        self.__cont=0
        self.__arregloDatos=np.empty(5,dtype=object)

    def vacia(self):
        return self.__cont==0

    def llena(self):
        return self.__cont==len(self.__arregloDatos)

    def insertar(self,item):
        if self.__cont<len(self.__arregloDatos):
            self.__arregloDatos[self.__ult]=item
            self.__ult=(self.__ult+1)%len(self.__arregloDatos)
            self.__cont+=1
        else:
            print(f"No es posible insertar el elemento {item}. Pila llena")


    def suprimir(self):
        elemento=None
        if self.vacia() is False:
            elemento=self.__arregloDatos[self.__pri]
            self.__pri=(self.__pri+1) % len(self.__arregloDatos)
            self.__cont-=1
        else:
            print("No es posible eliminar elementos. La pila esta vacia")
        return elemento

    def recorrer(self):
        i = self.__pri
        if self.vacia() is False:
            for j in range(self.__cont):
                print(self.__arregloDatos[i])
                i = (i + 1) % len(self.__arregloDatos)

    def contar(self):
        cont=0
        i = self.__pri
        if self.vacia() is False:
            for j in range(self.__cont):
                cont += 1
                i = (i + 1) % len(self.__arregloDatos)
        return cont
    
    def llega_impresion(self):
        random= uniform(0,1) #Determina si llega impresion
        if random <= 1/5: #La formula es 1/Frecuencia ; Siendo en este caso 5.
            llego_impresion=True
        else:
            llego_impresion=False
        return llego_impresion

    def verificar_tiempo(self,trabajo,acumulador_de_tiempo):
        tiempo_impresion = trabajo.gettiempoDemora()
        acumulador_de_tiempo += tiempo_impresion
        if tiempo_impresion > 5:
            trabajo.nuevademora(tiempo_impresion-5)
            self.insertar(self.suprimir())
        elif tiempo_impresion <= 5:
            self.suprimir()
        return acumulador_de_tiempo

if __name__=="__main__":
    c=ColaSecuencial()
    cantidad_impresiones = 0
    tiempo = 60
    acumulador_de_tiempo = 0
    while acumulador_de_tiempo < tiempo:
        if c.llega_impresion() is True:
            tiempo_impresion = int(input("Ingresa el tiempo de la impresion: "))
            trabajo = Impresion(tiempo_impresion)
            cantidad_impresiones += 1
            c.insertar(trabajo)
            acumulador_de_tiempo=c.verificar_tiempo(trabajo, acumulador_de_tiempo)
            print(c.recorrer())
            print(acumulador_de_tiempo)
    if c.contar()>0:
        print("los trabajos que quedaron sin atender son: {cont}".format(cont=c.contar()))
    else:
        print("No hay trabajos pendientes")
    print(f"El tiempo de espera fue {acumulador_de_tiempo/cantidad_impresiones}")
    


