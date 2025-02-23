import csv
import numpy as np
from ClaseConexion import Conexion


class GestorConexiones:
    __arregloConexiones = np.ndarray
    __cantidad = 0
    __dimension = 0
    __incremento = 1
    
    def __init__(self):
        self.__arregloConexiones = np.empty([0], dtype=Conexion)
        archivo = open("conexiones.csv")
        reader = csv.reader(archivo, delimiter=";")
        for fila in reader:
            c = Conexion(int(fila[0]), fila[1], fila[2], fila[3], int(fila[4]), int(fila[5]))
            self.agregar(c)
        archivo.close()
        
    def agregar(self, conexion):
        if self.__dimension == self.__cantidad:
            self.__dimension += self.__incremento
            self.__arregloConexiones.resize(self.__dimension)
        self.__arregloConexiones[self.__cantidad] = conexion
        self.__cantidad += 1
        

    def MostrarLista(self, gestorjuego, dni):
        persona = gestorjuego.BuscarDNI(dni)
        totalhoras = 0
        print(f"""DNI: {dni}       Nombre y apellido: {persona.getnombre()} {persona.getapellido()}      Alias: {persona.getalias()}      Plan: {persona.getplan()}  Importe base: {persona.getimportebase()} """)
        print("Ip de conexion   Juego    Fecha    Hora inicio    Hora final")
        for c in self.__arregloConexiones:
            if c.getid() == persona.getidjugador():
                totalhoras = c.gethorafinal() - c.gethorainicio()
                print(f"{c.getdirection()}   {c.getjuego()}   {c.getfecha()}   {c.gethorainicio()}   {c.gethorafinal()}")
        exceso = totalhoras - persona.gettiempolimite()
        print(f"""Total de horas: {totalhoras}""")
        if exceso > 0:
            print(f"""Exceso de horas: {exceso}""")
        if persona.getplan() == "Basico":
            c = persona.getimportebase() * 1.25
            print(f"""Importe base: {c}""")
        elif persona.getplan() == "Completo":
            c = persona.getimportebase() * 1.3
            print(f"""Importe base: {c}""")
        elif persona.getplan() == "Extendido":
            c = persona.getimportebase() * 1.4
            print(f"""Importe base: {c}""")

    def ordenar(self):
        self.__arregloConexiones.sort()

    def Inciso2(self, nombre, gestorgamer):
        i = 0
        while i < len(self.__arregloConexiones):
            if self.__arregloConexiones[i].getjuego().lower() == nombre.lower():
                gestorgamer.Mostrar(self.__arregloConexiones[i])
            i += 1
        if i > len(self.__arregloConexiones):
            raise IndexError("Juego no encontrado")
        
    def Inciso3(self, gestorgamer):
        for i in range(len(self.__arregloConexiones)):
            plan = gestorgamer.BuscarPlan(self.__arregloConexiones[i].getid())
            if plan == "Basico":
                for j in range(i+1, len(self.__arregloConexiones)):
                    if self.__arregloConexiones[i] == self.__arregloConexiones[j]:
                        print(f"id: {self.__arregloConexiones[i].getid()}  direccion: {self.__arregloConexiones[i].getdirection()} ")