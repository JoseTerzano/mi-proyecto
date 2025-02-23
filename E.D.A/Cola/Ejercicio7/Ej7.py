import numpy as np
from random import uniform, choice
from ClaseCliente import Cliente  
class ColaSecuencial:
    __ult:int
    __pri:int
    __cont:int
    __arregloDatos:np.ndarray

    def __init__(self):
        self.__pri=0
        self.__ult=0
        self.__cont=0
        self.__arregloDatos=np.empty(100,dtype=object)

    def vacia(self):
        return self.__cont==0

    def llena(self):
        return self.__cont==len(self.__arregloDatos)

    def insertar(self,item):
        cliente = Cliente(item)
        cliente.settiempo_espera(self.sumar_espera())
        if self.__cont<len(self.__arregloDatos):
            self.__arregloDatos[self.__ult]=cliente
            self.__ult=(self.__ult+1)%len(self.__arregloDatos)
            self.__cont+=1
        else:
            print(f"No es posible insertar el elemento {cliente}. Pila llena")


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
    
    def llega_cliente(self):
        random= uniform(0,1) 
        if random <= 1/2: 
            llego_cliente=True
        else:
            llego_cliente=False
        return llego_cliente
    
    
    def getcantidad(self):  
        return self.__cont
    
    def disminuir_tiempo(self):
        band = False
        if self.vacia() is False:
            if self.__arregloDatos[self.__pri].gettiempo_en_caja() > 1:
                 self.__arregloDatos[self.__pri].settiempo_en_caja()
            else:
                self.suprimir()
                band = True
        return band
    
    def sumar_espera(self):
        sum = 0
        if self.vacia() is False:
            for i in range(self.__cont):
                sum += self.__arregloDatos[i].gettiempo_en_caja()
            return sum
        
    def gettiempoultimo(self):
        return self.__arregloDatos[self.__ult-1].gettiempo_espera()  


if __name__=="__main__":
    c1 = ColaSecuencial()
    c2 = ColaSecuencial()
    c3 = ColaSecuencial()
    tiempo = 0
    acumulador_de_tiempo = 0
    clientestotales = 0
    max = 0
    c = 0
    sumador = 0
    while tiempo < 120:
        print(f"--- Tiempo: {tiempo} ---")
        if c1.llega_cliente():
            clientestotales += 1
            if c1.vacia() is True and c2.vacia() is True and c3.vacia() is True:
                aleatorio = choice([1,2,3])
                if aleatorio == 1:
                    c1.insertar(5)
                    print("LLego un cliente en la cola 1")
                elif aleatorio == 2:
                    print("LLego un cliente en la cola 2")
                    c2.insertar(3)
                elif aleatorio == 3:
                    print("LLego un cliente en la cola 3")
                    c3.insertar(4)
            elif c1.vacia() is True:
                print("LLego un cliente en la cola 1")
                c1.insertar(5)
            elif c2.vacia() is True:
                print("LLego un cliente en la cola 2")
                c2.insertar(3)
            elif c3.vacia() is True:
                print("LLego un cliente en la cola 3")
                c3.insertar(4)
            elif c1.vacia() is False and c2.vacia() is False and c3.vacia() is False:
                if c1.getcantidad()<=c2.getcantidad() and c1.getcantidad()<=c3.getcantidad():
                    print("LLego un cliente en la cola 1")
                    sumador = c1.sumar_espera()
                    c1.insertar(5)
                    if c1.gettiempoultimo() > max:
                        max = c1.gettiempoultimo()
                elif c2.getcantidad()<=c1.getcantidad() and c2.getcantidad()<=c3.getcantidad():
                    print("LLego un cliente en la cola 2")
                    sumador = c2.sumar_espera()
                    c2.insertar(3)
                    if c2.gettiempoultimo() > max:
                        max = c2.gettiempoultimo()
                elif c3.getcantidad()<=c1.getcantidad() and c3.getcantidad()<=c2.getcantidad():
                    print("LLego un cliente en la cola 3")
                    sumador = c3.sumar_espera()
                    c3.insertar(4)
                    if c3.gettiempoultimo() > max:
                        max = c3.gettiempoultimo()
        tiempo += 1
        if c1.disminuir_tiempo() is True:
            c +=1
            print("Se elimino un cliente de la cola 1")
        if c2.disminuir_tiempo() is True:
            c +=1
            print("Se elimino un cliente de la cola 2")
        if c3.disminuir_tiempo() is True:
            c +=1
            print("Se elimino un cliente de la cola 3")
    clientesatendidos = c
    print(f"Clientes atendidos: {c}")
    print(f"Tiempo de espera maximo: {max}")
    print(f"Clientes sin atender: {clientestotales-clientesatendidos}")
    print(f"Promedio de tiempo de espera de clientes atendidos: {sumador/clientesatendidos}")
    print(f"Promedio de tiempo de espera de clientes sin atender: {sumador/(clientestotales-clientesatendidos)}")
    print("C1")
    c1.recorrer() 
    print("C2")
    c2.recorrer() 
    print("C3")
    c3.recorrer() 



