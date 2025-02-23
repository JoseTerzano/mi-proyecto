from claseNodo import Nodo


class Lista:
    def __init__(self, xmax):
        self.max = xmax # max de elementos que puede tener la lista
        self.cab = 0 # puntero a la cabeza de la lista
        self.cantidad = 0 # cantidad de elementos de la lista
        self.espacio = [Nodo() for _ in range(xmax)] # arreglo de nodos
        self.disponible = 0 # indice del primer elemento disponible

    def vacia(self):
        return self.cantidad == 0

    def get_disponible(self):
        for i in range(self.max):
            if self.espacio[i].get_siguiente() == -2: # si el elemento es disponible
                self.disponible = i # guardar el indice
                return True
        self.disponible = -2 
        return False

    def free_disponible(self, disp):
        if 0 <= disp < self.max: # si el indice es correcto
            self.espacio[disp].set_siguiente(-2) # poner el elemento como disponible
            return True
        return False

    def insertar_por_posicion(self, x, xp): #inserta un nuevo elemento x en la posicion xp
        if self.cantidad < self.max and 0 <= xp <= self.cantidad and self.get_disponible(): # si la lista no es llena , verifica xp sea valida y que el elemento este disponible
            self.espacio[self.disponible].set_dato(x) # establece el valor del nuevo nodo
            ant = self.cab # guarda el anterior nodo
            cabeza = self.cab # guarda el actual nodo
            i = 0

            while i < xp: #recorre hasta encontrar xp
                i += 1 
                ant = cabeza # actualiza el anterior nodo
                cabeza = self.espacio[cabeza].get_siguiente() #mueve la cabeza al siguiente nodo

            if cabeza == self.cab:  # Insertar al inicio
                if self.cantidad == 0: # si esta vacia
                    self.espacio[self.cab].set_siguiente(-1) # poner cabeza como -1 (final de lista)
                else:
                    self.espacio[self.disponible].set_siguiente(self.cab) #se establece el nuevo nodo como el nuevo primero (cabeza) 
                self.cab = self.disponible
            elif cabeza == -1:  # Insertar al final
                self.espacio[self.disponible].set_siguiente(-1)
                self.espacio[ant].set_siguiente(self.disponible) # actualiza el nodo ant para que apunte al nuevo nodo (self.disponible)
            else: # Insertar en medio
                self.espacio[self.disponible].set_siguiente(cabeza) #el nuevo nodo (self.disponible) apunta al nodo actual (cabeza)
                self.espacio[ant].set_siguiente(self.disponible) # ant apunta al nuevo nodo (self.disponible)

            self.cantidad += 1
            return True
        else:
            print("Espacio lleno o posición incorrecta.")
            return False

    def insertar_por_contenido(self, x): #inserta un nuevo elemento x en orden ascendente, manteniendo la lista ordenada
        if self.cantidad < self.max and self.get_disponible(): # si la lista no es llena , verifica que el elemento este disponible
            ant = self.cab 
            cabeza = self.cab
            i = 0
            self.espacio[self.disponible].set_dato(x) #guarda el valor de x en el nodo disponible

            while i < self.cantidad and cabeza != -1 and self.espacio[cabeza].get_dato() < x: # recorre la lista  para encontrar la posicion donde x debe insertarse para mantener el orden
                i += 1
                ant = cabeza
                cabeza = self.espacio[cabeza].get_siguiente()

            if cabeza == self.cab:  # Insertar al inicio
                if self.cantidad == 0:
                    self.espacio[self.cab].set_siguiente(-1)
                else:
                    self.espacio[self.disponible].set_siguiente(self.cab)
                self.cab = self.disponible
            elif cabeza == -1:  # Insertar al final
                self.espacio[self.disponible].set_siguiente(-1)
                self.espacio[ant].set_siguiente(self.disponible)
            else:
                self.espacio[self.disponible].set_siguiente(cabeza)
                self.espacio[ant].set_siguiente(self.disponible)

            self.cantidad += 1
            return True
        else:
            print("Espacio lleno.")
            return False

    def suprimir(self, xp):
        if self.cantidad != 0 and 0 <= xp < self.cantidad:
            ant = self.cab
            cabeza = self.cab
            i = 0

            while i < xp and cabeza != -1: # recorre la lista hasta encontrar la posicion xp
                i += 1
                ant = cabeza
                cabeza = self.espacio[cabeza].get_siguiente()

            if cabeza == self.cab: # elimina el primer elemento
                if self.cantidad == 1: # si hay un solo elemento
                    self.cab = 0 # poner cabeza como 0
                else:
                    self.cab = self.espacio[ant].get_siguiente() 
            else:
                self.espacio[ant].set_siguiente(self.espacio[cabeza].get_siguiente()) # actualiza el anterior nodo para que apunte al siguiente nodo del que se elimina

            x = self.espacio[cabeza].get_dato() # recupera el valor del elemento eliminado
            self.disponible = cabeza 
            self.free_disponible(self.disponible) # libera el elemento eliminado
            self.cantidad -= 1
            return x    
        else:
            print("Lista vacía o posición incorrecta.")
            return None

    def recuperar(self, xp): # devuelve el dato de un elemento en la posicion xp
        if self.cantidad != 0 and 0 <= xp < self.cantidad:
            cabeza = self.cab
            i = 0

            while cabeza != -1 and i < xp:
                i += 1
                cabeza = self.espacio[cabeza].get_siguiente()

            return self.espacio[cabeza].get_dato()
        else:
            print("Lista vacía o posición incorrecta.")
            return None

    def recorrer(self):
        if self.cantidad != 0:
            cabeza = self.cab
            print("Lista:", end=" ")
            while cabeza != -1:
                print(self.espacio[cabeza].get_dato(), end=" ")
                cabeza = self.espacio[cabeza].get_siguiente()
            print()
        else:
            print("Lista vacía.")