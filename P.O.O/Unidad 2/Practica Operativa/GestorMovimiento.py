import csv
import numpy as np
from ModuloMovimiento import movimiento
from GestorCliente import gestorcliente


class gestormovimiento:
    __gestor = np.ndarray
    __dimension: int
    __incremento: int
    __cantidad: int

    def AgregarMov(self, movimiento):
        if self.__cantidad == self.__dimension:
            self.__dimension += self.__incremento
            self.__gestor.resize(self.__dimension)
        self.__gestor[self.__cantidad] = movimiento
        self.__cantidad += 1

    def __init__(self):
        self.__cantidad = 0
        self.__dimension = 0
        self.__incremento = 1
        self.__gestor = np.empty(0, dtype=movimiento)
        archivo = open("MovimientosAbril2024 (1).csv")
        reader = csv.reader(archivo, delimiter=";")
        bandera = False
        for fila in reader:
            if bandera == False:
                bandera = True
            else:
                nroCuenta = int(fila[0])
                fecha = fila[1]
                descripcion = fila[2]
                tipoMov = fila[3]
                importe = float(fila[4])
                nuevomovimiento = movimiento(
                    nroCuenta, fecha, descripcion, tipoMov, importe)
                self.AgregarMov(nuevomovimiento)
        archivo.close()

    def suma(self, gestorcliente, i):
        j = 0
        total = 0
        while j < len(self.__gestor):
            if gestorcliente[i].getnroCuenta() == self.__gestor[j].getNroCuenta():
                if self.__gestor[j].gettipoMov() == "C":
                    total += self.__gestor[j].getimporte()
            j += 1
        return total

    def resta(self, gestorcliente, i):
        j = 0
        total = 0
        while j < len(self.__gestor):
            if gestorcliente[i].getnroCuenta() == self.__gestor[j].getNroCuenta():
                if self.__gestor[j].gettipoMov() == "P":
                    total += self.__gestor[j].getimporte()
            j += 1
        return total

    def listarmovimientos(self, gestorcliente, i):
        j = 0
        while j < len(self.__gestor):
            if gestorcliente[i].getnroCuenta() == self.__gestor[j].getNroCuenta():
                print(f"{self.__gestor[j].getfecha()}   {self.__gestor[j].getdescripcion()}  {
                    self.__gestor[j].getimporte()}    {self.__gestor[j].gettipoMov()}")
            j += 1

    def existeMovimiento(self, gestorcliente, i):
        j = 0
        while j < len(self.__gestor):
            if gestorcliente[i].getnroCuenta() == self.__gestor[j].getNroCuenta():
                if self.__gestor[i].gettipoMov() == "C" or "P":
                    bandera = 1
                else:
                    bandera = -1
            j += 1
        return bandera

    def ordenarMovimientos(self):
        self.__gestor.sort()
        print("La lista de movimientos fue ordenada")
