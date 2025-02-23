from ClassEdificio import Edificio
from ClassDpto import Departamento
import csv

class gestoredificio:
    __gestorEdificio = list

    def __init__(self):
        self.__gestorEdificio = []
        archivo = open("EdificioNorte (2).csv")
        reader = csv.reader(archivo, delimiter=";")
        for fila in reader:
            if len(fila) == 6:
                id = int(fila[0])
                nombre = fila[1]
                direccion = fila[2]
                empresa = fila[3]
                pisos = int(fila[4])
                dptos = int(fila[5])
                nuevoedificio = Edificio(id, nombre, direccion, empresa, pisos, dptos)
                self.__gestorEdificio.append(nuevoedificio)
            elif len(fila) == 8:
                idd = int(fila[1])
                nom = fila[2]
                piso = int(fila[3])
                dpto = int(fila[4])
                cantdor = int(fila[5])
                cantban = int(fila[6])
                sup = float(fila[7])
                departamento = Departamento(idd, nom, piso, dpto, cantdor, cantban, sup)
                nuevoedificio.agregardpto(departamento)
        archivo.close()
    
    def mostrarnombres(self, edi):
        i = 0
        while i < len(self.__gestorEdificio):
            if self.__gestorEdificio[i].getnombre().upper() == edi.upper():
                self.__gestorEdificio[i].listardptos()
            i += 1

    def mostrarsup(self, edi):
        i = 0
        while i < len(self.__gestorEdificio):
            if self.__gestorEdificio[i].getnombre().upper() == edi.upper():
                total = self.__gestorEdificio[i].superficietotal()
            i += 1
        print(f"El superficie total de {edi} es de {total} m2")

    def mostrarsuperficie(self, nombre):
        total = 0
        i = 0
        while i < len(self.__gestorEdificio):
            for dpto in self.__gestorEdificio[i].getdepartamentos():
                if dpto.getnom().upper() == nombre.upper():
                    total += dpto.getsup()
            i += 1
        print(f"La superficie de {nombre} es de {total} m2")

    def mostrar(self, numero):
        c = 0
        i = 0
        while i < len(self.__gestorEdificio):
            for dpto in self.__gestorEdificio[i].getdepartamentos():
                if dpto.getnumeropiso() == numero and dpto.getchab() == 3 and dpto.getcbanos() > 1:
                    c += 1
                    print(f"En el edificio {self.__gestorEdificio[i].getnombre()} el departamento del propietario {dpto.getnom()} tiene 3 habitaciones y 1 bano")
            i += 1