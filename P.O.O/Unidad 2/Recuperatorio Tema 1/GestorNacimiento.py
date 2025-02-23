import csv
from ModuloNacimiento import Nacimiento


class gestornacimiento:
    __gestorNacimiento = list

    def __init__(self):
        self.__gestorNacimiento = []
        archivo = open("Nacimientos.csv")
        reader = csv.reader(archivo, delimiter=";")
        bandera = False
        for fila in reader:
            if bandera == False:
                bandera = True
            else:
                dnimama = int(fila[0])
                tipo = fila[1]
                fecha = fila[2]
                hora = fila[3]
                peso = float(fila[4])
                altura = int(fila[5])
                nuevonacimiento = Nacimiento(
                    dnimama, tipo, fecha, hora, peso, altura)
                self.__gestorNacimiento.append(nuevonacimiento)
        archivo.close()

    def TipoParto(self, dni):
        i = 0
        while i < len(self.__gestorNacimiento):
            if dni == self.__gestorNacimiento[i].getdnimadre():
                return self.__gestorNacimiento[i].gettipoparto()
            i += 1

    def Bebes(self, dni):
        i = 0
        print("Peso  Altura")
        while i < len(self.__gestorNacimiento):
            if dni == self.__gestorNacimiento[i].getdnimadre():
                print(self.__gestorNacimiento[i].getpeso(
                ), self.__gestorNacimiento[i].getaltura())
            i += 1

    def MostrarDatos(self, gestormama):
        for i in range(len(self.__gestorNacimiento)):
            for j in range(len(self.__gestorNacimiento)):
                if self.__gestorNacimiento[i] == self.__gestorNacimiento[j]:
                    dni = self.__gestorNacimiento[j].getdnimadre()
                    nombre = gestormama.ObtenerNombre(dni)
                    edad = gestormama.ObtenerEdad(dni)
                    print(f"Nombre: {nombre}, edad: {edad}, dni: {dni}")
