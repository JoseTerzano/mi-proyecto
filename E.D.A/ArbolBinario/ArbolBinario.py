from claseNodo import Nodo

class Arbol:
    __raiz:Nodo
    def __init__(self):
        self.__raiz = None

    def getRaiz(self):
        return self.__raiz

    def insertar(self, nodo, x):
        if nodo is None:
            nuevonodo = Nodo(x)
            if self.__raiz is None:  # Si es la primera inserción, asignamos a la raíz del árbol
                self.__raiz = nuevonodo
                print(f"Insertando {x} en la raíz")
        else:
            if x == nodo.getDato():
                print("Ya existe el elemento")
            else:
                if x < nodo.getDato():
                    if nodo.getSiguienteIzq() is None:
                        nodo.setSiguienteIzq(Nodo(x))
                        print(f"Insertando {x} a la izquierda de {nodo.getDato()}")
                    else:
                        self.insertar(nodo.getSiguienteIzq(), x)
                else:
                    if nodo.getSiguienteDer() is None:
                        nodo.setSiguienteDer(Nodo(x))
                        print(f"Insertando {x} a la derecha de {nodo.getDato()}")
                    else:
                        self.insertar(nodo.getSiguienteDer(), x )

    def buscar(self, nodo, x):
        if nodo is None:
            print("No existe el elemento")
        else:
            if x == nodo.getDato():
                return nodo
            if x < nodo.getDato():
                return self.buscar(nodo.getSiguienteIzq(),x )
            else:
                return self.buscar(nodo.getSiguienteDer(),x )
        
    def gradoNodo(self,clave):
        nodo =  self.buscar(self.__raiz,clave) #Busco el nodo con la clave ingresada
        grado=None
        if nodo is not None: #Si existe... Voy a revisar cuantos hijos tiene(ese es el grado):
            if nodo.getSiguienteIzq() is not None and nodo.getSiguienteDer() is not None: #Si tiene en la izquierda y en la derecha, el grado es 2
                grado = 2
            elif (nodo.getSiguienteIzq() is not None and nodo.getSiguienteDer() is None) or (nodo.getSiguienteIzq() is None and nodo.getSiguienteDer() is not None): #Si solo tiene 1 en la izquierda o derecha, el grado es 1
                grado = 1
            else: #Si tiene None tanto en la izquierda como en la derecha... no tiene hijos, grado 0
                grado = 0
        return  grado
    
    def eshijo(self,padre,hijo):
        subarbol_padre= self.buscar(self.__raiz,padre)
        subarbol_hijo= self.buscar(self.__raiz,hijo)
        es_hijo= False
        if subarbol_hijo is not None and subarbol_padre is not None:
            if subarbol_padre.getSiguienteIzq() == subarbol_hijo or subarbol_padre.getSiguienteDer()==subarbol_hijo:
                es_hijo = True
        return es_hijo
    
    def espadre(self,padre,hijo):
        subarbol_padre= self.buscar(self.__raiz,padre)
        subarbol_hijo= self.buscar(self.__raiz,hijo)
        es_padre= False
        if subarbol_padre is not None and subarbol_hijo is not None:
            nodo= self.__raiz
            nivel= self.nivelNodo(hijo)
            nivel_actual= 1
            if hijo != nodo.getDato():
                while nivel_actual != nivel-1:
                    if hijo > nodo.getDato():
                        nodo= nodo.getSiguienteDer()
                    else:
                        nodo= nodo.getSiguienteIzq()
                    nivel_actual+=1
                es_padre = nodo==subarbol_padre
            else:
                print("Ingresaste la raiz. No tiene padre")
        return es_padre

    def nivelNodo(self,clave):
        nodo= self.buscar(self.__raiz,clave)
        nivel= None
        if nodo is not None:
            nivel=1
            subarbol= self.__raiz
            while subarbol.getDato() != clave:
                nivel+=1
                if clave > subarbol.getDato():
                    subarbol= subarbol.getSiguienteDer()
                else:
                    subarbol= subarbol.getSiguienteIzq()
        return nivel
    
    def ContarHojas(self, nodo):
        if nodo is not None:
            if self.hoja(nodo.getDato()):
                print(f"el nodo {nodo.getDato()} es hoja")
            else:
                self.ContarHojas(nodo.getSiguienteIzq())
                self.ContarHojas(nodo.getSiguienteDer())



    def getInfimo(self,subarbol):
        subarbol= subarbol.getSiguienteIzq()
        while self.gradoNodo(subarbol.getDato()) != 0:
            subarbol= subarbol.getSiguienteDer()
        return subarbol
    
    def getPadre(self,clave):
        nodo= self.__raiz
        nivel= self.nivelNodo(clave)
        nivel_actual= 1
        if clave != nodo.getDato():
            while nivel_actual != nivel-1:
                if clave > nodo.getDato():
                    nodo= nodo.getSiguienteDer()
                else:
                    nodo= nodo.getSiguienteIzq()
                nivel_actual+=1
        else:
            print("Ingresaste la raiz. No tiene padre")
        return nodo
    
    def suprimir(self,clave): #Es mas facil hacer el seguimiento viendo la imagen de la carpeta y ejecutandolo
        subarbol= self.buscar(self.__raiz,clave)
        padre= self.getPadre(clave)

        if subarbol is not None:
            grado= self.gradoNodo(clave)
            if grado == 0: #Si el grado es 0, es un nodo hoja. Ahora el padre va a apuntar a None en su rama derecha/izquierda en la que estaba el hijo suprimido
                if clave > padre.getDato():
                    padre.setSiguienteDer(None)
                else:
                    padre.setSiguienteIzq(None)
            if grado == 1: #Si el grado es 1, el nodo tenia un hijo. Ahora el padre deberá apuntar a ese hijo
                if subarbol.getSiguienteDer() is not None: #Busco el hijo (esta en la derecha O izquierda, ya que solo tiene 1)
                    hijo= subarbol.getSiguienteDer()
                else:
                    hijo= subarbol.getSiguienteIzq()
                subarbol.setDato(hijo.getDato()) #Ahora el nodo a suprimir será una copia de su hijo
                subarbol.setSiguienteDer(hijo.getSiguienteDer())
                subarbol.setSiguienteIzq(hijo.getSiguienteIzq())

                #if subarbol.getDerecha().getDato() == subarbol.getDato():
                #    subarbol.setSAD(None)
                #else:
                #    subarbol.setSAD(None)
            if grado== 2: #Si el grado es 2, hay que buscar el infimo o el supremo para reemplazarlo
                infimo=self.getInfimo(subarbol)
                padre_infimo= self.getPadre(infimo.getDato())
                subarbol.setDato(infimo.getDato())

                if infimo.getDato() > padre_infimo.getDato():
                    padre_infimo.setSiguienteDer(None)
                else:
                    padre_infimo.setSiguienteIzq(None)

    def hoja(self,clave):
        nodo= self.buscar(self.__raiz,clave)
        if nodo.getSiguienteIzq() is None and nodo.getSiguienteDer() is None:
            return True
        else:
            return False

    
    def altura(self,subarbol,maximo=1):
        if subarbol is not None:
            nivel = self.nivelNodo(subarbol.getDato())
            if nivel > maximo:
                maximo = nivel
            maximo = self.altura(subarbol.getSiguienteIzq(), maximo) #Voy a recorrer todos los de la izqueirda
            maximo = self.altura(subarbol.getSiguienteDer(), maximo) #Luego todos los de la derecha
        return maximo


    def camino(self,origen,destino):
        subarbol_origen= self.buscar(self.__raiz,origen)
        camino="° "
        if subarbol_origen is not None: #Reviso que el nodo origen exista
            subarbol_destino= self.buscar(subarbol_origen,destino) #Reviso que el nodo destino exista en los descendientes del arbol origen
            subarbol= subarbol_origen
            if subarbol_destino is not None: #Empezare a concatenar el contenido de los nodos como un camino en un string
                while subarbol.getDato() != destino:
                    if destino > subarbol.getDato():
                        camino+= str(subarbol.getDato())+ " -> "
                        subarbol= subarbol.getSiguienteDer()
                    else:
                        camino+= str(subarbol.getDato())+ " -> "
                        subarbol= subarbol.getSiguienteIzq()
                camino+= str(subarbol.getDato())+ " -|"
            else:
                print(f"ERROR. El nodo origen {subarbol.getDato()} no es antecesor de {destino}")
        return camino
    
    def hermanos(self, padre, hijo):
        hijo = self.buscar(self.__raiz, hijo)
        padre = self.buscar(self.__raiz, padre)
        hermano = None
        if hijo.getDato() < padre.getDato():
            hermano = padre.getSiguienteDer()
        else:
            hermano = padre.getSiguienteIzq()
        return hermano

    def InOrder(self,subarbol):
        if subarbol is not None:
            self.InOrder(subarbol.getSiguienteIzq())
            print(subarbol.getDato())
            self.InOrder(subarbol.getSiguienteDer())

    def PostOrden(self,subarbol):
        if subarbol is not None:
            self.InOrder(subarbol.getSiguienteIzq())
            self.InOrder(subarbol.getSiguienteDer())
            print(subarbol.getDato())

    def PreOrden(self,subarbol):
        if subarbol is not None:
            print(subarbol.getDato())
            self.InOrder(subarbol.getSiguienteIzq())
            self.InOrder(subarbol.getSiguienteDer())

    def contarDescendientes(self, clave):
        nodo = self.buscar(self.__raiz, clave)
        if nodo is None:
            print("El nodo no existe en el árbol.")
            return 0
        return self.__contarDescendientesRec(nodo) -1

    def __contarDescendientesRec(self, nodo):
        if nodo is None:
            return 0
        # Cuenta el nodo actual como 1 y suma los descendientes en los subárboles izquierdo y derecho
        return 1 + self.__contarDescendientesRec(nodo.getSiguienteIzq()) + self.__contarDescendientesRec(nodo.getSiguienteDer())

    
if __name__ == "__main__":
    arbol = Arbol()
    arbol.insertar(arbol.getRaiz(),60)#
    arbol.insertar(arbol.getRaiz(),50)#
    arbol.insertar(arbol.getRaiz(),70)#
    arbol.insertar(arbol.getRaiz(),43)#
    arbol.insertar(arbol.getRaiz(),52)#
    arbol.insertar(arbol.getRaiz(),48)#
    arbol.insertar(arbol.getRaiz(),51)#
    arbol.insertar(arbol.getRaiz(),55)#
    arbol.insertar(arbol.getRaiz(),93)#
    arbol.insertar(arbol.getRaiz(),95)
    arbol.InOrder(arbol.getRaiz())
    print("---------")
    arbol.PostOrden(arbol.getRaiz())
    print("---------")
    arbol.PreOrden(arbol.getRaiz())

    arbol.ContarHojas(arbol.getRaiz())

    print("Contar descendientes de un nodo: 50: ", arbol.contarDescendientes(50))
    print("Contar descendientes de un nodo: 60: ", arbol.contarDescendientes(60))
    print("INICIANDO PRUEBAS DE SUPRESION (ver imagen de la carpeta)")
    print("--------------Primera supresion (nodo hoja 48)---------------------")
    print("Grado del nodo clave 43 antes de la supresion:", arbol.gradoNodo(43))
    print("Suprimir 48",arbol.suprimir(48))
    print("Grado del nodo clave 43 despues de la supresion:", arbol.gradoNodo(43))
    arbol.InOrder(arbol.getRaiz())
    print("--------------Segunda supresion (nodo 70 con un hijo)---------------------")
    print("Nivel  del nodo 93 antes de suprimir el 70:", arbol.nivelNodo(93))
    print("Suprimir 70",arbol.suprimir(70))
    print("Nivel  del nodo 93 despues de suprimir el 70:", arbol.nivelNodo(93))
    arbol.InOrder(arbol.getRaiz())
    print("--------------Tercera supresion (nodo 52 con 2 hijos)---------------------")
    print("Grado del nodo 51 antes de suprimir el 52: ",arbol.gradoNodo(51))
    print("Suprimir 52",arbol.suprimir(52))
    print("Grado del nodo 51 despues de suprimir el 52: ",arbol.gradoNodo(51))
    arbol.InOrder(arbol.getRaiz())
    print("REVISANDO GRADOS")
    print("Grado del nodo clave 60:", arbol.gradoNodo(60))
    print("Grado del nodo clave 50:", arbol.gradoNodo(50))
    print("Grado del nodo clave 93:", arbol.gradoNodo(93))
    print("Grado del nodo clave 43:", arbol.gradoNodo(43))
    print("Grado del nodo clave 51:", arbol.gradoNodo(51))
    print("Grado del nodo clave 55:", arbol.gradoNodo(55))
    print("Grado del nodo clave 95:", arbol.gradoNodo(95))
    print("----Suprimir la raiz 60---")
    arbol.suprimir(60)
    print("La nueva raiz es: ", arbol.getRaiz().getDato())
    print("Grado del nodo clave 50:", arbol.gradoNodo(50))
    print("Grado del nodo clave 93:", arbol.gradoNodo(93))
    print("Grado del nodo clave 43:", arbol.gradoNodo(43))
    print("Grado del nodo clave 51:", arbol.gradoNodo(51))
    print("Grado del nodo clave 55:", arbol.gradoNodo(55))
    print("Grado del nodo clave 95:", arbol.gradoNodo(95))
    print("------TESTEANDO OTRAS FUNCIONES----------")
    print("El 93 es hijo del 55?: ",arbol.eshijo(55,93))
    print("El 55 es padre del 43?: ",arbol.espadre(55,43))
    print("La altura del arbol es ", arbol.altura(arbol.getRaiz()))
    print("Camino desde el nodo 55 hasta el 51:", arbol.camino(55,51))