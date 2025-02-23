import csv
from ModuloEdificio import Edificio
from ModuloDepartamento import Departamento


class gestoredificio:
    __gestorEdificio = list

    def __init__(self):
        self.__gestorEdificio = []
        archivo = open("EdificioNorte (1).csv")
        reader = csv.reader(archivo, delimiter=";")
        for fila in reader:
            if len(fila) == 6:
                id = int(fila[0])
                nombre = fila[1]
                direccion = fila[2]
                empresa = fila[3]
                pisos = int(fila[4])
                dptos = int(fila[5])
                nuevoedificio = Edificio(
                    id, nombre, direccion, empresa, pisos, dptos)
                self.__gestorEdificio.append(nuevoedificio)
            elif len(fila) == 7:
                idd = int(fila[0])
                nom = fila[1]
                piso = int(fila[2])
                dpto = int(fila[3])
                cantdor = int(fila[4])
                cantban = int(fila[5])
                desc = fila[6]
                departamento = Departamento(
                    idd, nom, piso, dpto, cantdor, cantban, desc)
                nuevoedificio.agregardepartamento(departamento)
        archivo.close()

    def MostrarPropietarios(self, nombreedificio):
        i = 0
        while i < len(self.__gestorEdificio):
            if nombreedificio == self.__gestorEdificio[i].getnombreEdi():
                for edif in self.__gestorEdificio[i].ListaDptos():
                    print(edif)
            i += 1

    def SuperficieTotal(self, nombre):
        total1 = 0
        i = 0
        while i < len(self.__gestorEdificio):
            if (nombre == self.__gestorEdificio[i].getnombreEdi()):
                for depto in self.__gestorEdificio[i].ListaDptos():
                    total1 += depto.getsuperficie()
            i += 1
        return total1

    def MostrarSup(self, nombreEd, nombre, suptotal):
        total = 0
        i = 0
        while i < len(self.__gestorEdificio):
            if (nombreEd == self.__gestorEdificio[i].getnombreEdi()):
                for dpto in self.__gestorEdificio[i].ListaDptos():
                    if dpto.getnombre() == nombre:
                        total += dpto.getsuperficie()
            i += 1
        porcentaje = float((total*100)/suptotal)
        print(f"La superficie es: {total} \n El porcentaje es: {porcentaje}")

    def Mostrar(self, nombreEd, numeropiso):
        i = 0
        c = 0
        while i < len(self.__gestorEdificio):
            if (nombreEd == self.__gestorEdificio[i].getnombreEdi()):
                for dpto in self.__gestorEdificio[i].ListaDptos():
                    if dpto.getpiso() == numeropiso:
                        if ((dpto.getcantdor() == 3) and (dpto.getcantban() > 1)):
                            c += 1
            i += 1
        print(f'En el edificio {nombreEd} hay {c} departamentos que cumplen')
