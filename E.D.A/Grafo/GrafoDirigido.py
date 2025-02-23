import numpy as np

class Grafo:
    __num_vertices:int
    __matriz_adjacencia:np.ndarray
    
    def __init__(self, vertices):
        self.__num_vertices = vertices
        # Inicializamos la matriz de adyacencia con ceros
        #self.matriz_adjacencia = [[] * num_vertices for _ in range(num_vertices)]
        self.__matriz_adjacencia = np.zeros((vertices,vertices),dtype=int)

    def agregar_arista(self, origen, destino, peso=1):
        # Aseguramos que los vértices estén dentro de los límites
        if origen >= self.__num_vertices or destino >= self.__num_vertices:
            raise ValueError("Los vértices deben estar dentro del rango de la matriz")
        # Agregamos la arista (dirigida) con su peso
        self.__matriz_adjacencia[origen][destino] = peso

    def mostrar_matriz(self):
        for fila in self.__matriz_adjacencia:
            print(fila)
            
   # def nodos_adyacentes(self, nodo):
   #     if nodo >= self.__num_vertices:
   #         raise ValueError("El nodo debe estar dentro del rango de la matriz")
   #     else:
   #         print("Los nodos adyacentes de ", nodo,"son :",np.nonzero(self.__matriz_adjacencia[nodo]) )
    def nodos_adyacentes(self, nodo):
        if nodo >= self.__num_vertices:
            raise ValueError("El nodo debe estar dentro del rango de la matriz")
        else:
            adyacentes=[]
            rango=self.__num_vertices
            for i in range(rango):
               if self.__matriz_adjacencia[nodo][i] !=0 or self.__matriz_adjacencia[i][nodo] != 0:
                   adyacentes.append(i)
            print("Los nodos adyacentes de ", nodo,"son : ", end="" )
            for j in range(len(adyacentes)):
                print(f"{adyacentes[j]} - ",end="")  
            print()    
              
    def grado_Nodo(self, nodo):
        if nodo >= self.__num_vertices:
           raise ValueError("El nodo debe estar dentro del rango de la matriz")
        else:
            print("El grado del nodo", nodo," es ",np.sum(self.__matriz_adjacencia[nodo]))

    def gradoSalida(self, nodo): #cantidad de aristas que salen de un nodo
        if nodo >= self.__num_vertices:
            raise ValueError("nodo fuera de rango")
        else:
            grado = 0
            for i in range(self.__num_vertices):
                if self.__matriz_adjacencia[nodo][i]==1:
                    grado += 1
            print(f"el grado de salida del nodo {nodo} es {grado}")
            return grado
        
    def gradoEntrada(self, nodo): #cantidad de aristas que entran en un nodo
        if nodo >= self.__num_vertices:
            raise ValueError("nodo fuera de rango")
        else:
            grado = 0
            for i in range(self.__num_vertices):
                if self.__matriz_adjacencia[i][nodo]==1:
                    grado += 1
            print(f"el grado de entrada del nodo {nodo} es {grado}")
            return grado
            
    def nodoFuente(self, nodo): #no tiene aristas entrantes
        if self.gradoEntrada(nodo) == 0 and self.gradoSalida(nodo) > 0:
            print(f"nodo {nodo} es fuente")
            return True
        else:
            print(f"nodo {nodo} no es fuente")
            return False

    def nodoSumidero(self, nodo): #no tiene aristas salientes
        if self.gradoSalida(nodo) == 0 and self.gradoEntrada(nodo) > 0:
            print(f"nodo {nodo} es sumidero")
            return True
        else:
            print(f"nodo {nodo} no es sumidero")
            return False
        
    def ContarFuentes(self):
        c = 0
        for i in range(self.__num_vertices):
            if self.nodoFuente(i):
                c+=1
        return c
    
    def camino(self, inicio, fin):
        visitados = [False] * self.__num_vertices
        print("Visitados", visitados)
        pila = [(inicio, [inicio])]  # Pila que contiene tuplas (nodo_actual, camino_actual)
    
        while pila:
            nodo_actual, camino = pila.pop()
            print("nodo actual y camino",nodo_actual, camino ) 
            if nodo_actual == fin:
                return camino
            
            if  visitados[nodo_actual] is False:
                visitados[nodo_actual] = True
                print("visitados actualizado: ", visitados)
                
                for i in range(self.__num_vertices):
                    print("i: ", i)
                    if self.__matriz_adjacencia[nodo_actual][i] == 1 and visitados[i] is False:
                        pila.append((i, camino + [i]))
        
        return None  # No se encontró camino
    
    def es_conexo(self):
       num_vertices = len(self.__matriz_adjacencia)
       visitados = [False] * num_vertices
       print("visitados: ", visitados)
       pila = [0]

       while pila:
        vertice = pila.pop()
        if visitados[vertice] is False:
            visitados[vertice] = True
            for i in range(num_vertices):
                if self.__matriz_adjacencia[vertice][i] == 1 and visitados[i] is False:
                    pila.append(i)  
       
       return all(visitados) 
       ''' El método all() de Python es una función incorporada que devuelve VERDADERO
        si todos los elementos de un iterable proporcionado (Lista, Diccionario, Tupla, Conjunto, etc.)
        son Verdaderos, de lo contrario, devuelve FALSO".'''

    def aciclico(self):
        visitados = [False] * self.__num_vertices
        pila =[(0,-1)]
            
        while pila:
            vertice, padre = pila.pop()
            print("padre: ", padre)
            print("vertice: ", vertice)
            if not visitados[vertice]:
                visitados[vertice]=True
                for i in range(self.__num_vertices):
                    if self.__matriz_adjacencia[vertice][i] ==1 and not visitados[vertice]:
                        pila.append(i, vertice)
                    elif self.__matriz_adjacencia[vertice][i]== 1 and i != padre:
                        return False
        return True     
    
    def BEP(self, nodo):
        visitados=[False]*self.__num_vertices
        pila=[nodo]
        while pila:
            vertice=pila.pop()
            if not visitados[vertice]:
                visitados[vertice]=True
                for i in range(self.__num_vertices):
                    if self.__matriz_adjacencia[vertice][i]==1 and not visitados[i]:
                        pila.append(i)

        return all(visitados)
    
    def BEA(self, nodo):
        visitados=[False]*self.__num_vertices
        pila=[nodo]
        while pila:
            vertice=pila.pop(0)
            if not visitados[vertice]:
                visitados[vertice]=True
                for i in range(self.__num_vertices):
                    
                    if self.__matriz_adjacencia[vertice][i]==1 and not visitados[i]:
                        pila.append(i)

        return all(visitados)

 

    
# Ejemplo de uso
if __name__ == "__main__":
    grafo = Grafo(5)  # Crea un grafo con 5 vértices
    # Agregar aristas
    grafo.agregar_arista(1, 2)
    grafo.agregar_arista(1, 3)
    #grafo.agregar_arista(1, 4)
    grafo.agregar_arista(2, 3)
    grafo.agregar_arista(3, 4)
    grafo.agregar_arista(0, 4)
    print(grafo.ContarFuentes())

    # Mostrar la matriz de adyacencia
    print("Matriz de adyacencia:")
    
    grafo.mostrar_matriz()
    grafo.nodos_adyacentes(1)
    grafo.grado_Nodo(1)
    print("camino", grafo.camino(1,4))
    if grafo.es_conexo():
        print("El grafo es Conexo" )
    else:
        print('El grafo NO es Conexo')

    if grafo.aciclico():
        print("El grafo es aciclico")
    else:
        print("El grafo NO es aciclico")