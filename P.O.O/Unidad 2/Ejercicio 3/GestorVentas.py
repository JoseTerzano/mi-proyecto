import numpy as np


class gestor():
    def __init__(self):
        self.matriz = np.zeros((5, 7))

    def CargaDatos(self):
        dia = input("Ingrese dia de la semana: ")
        numero_suc = int(input("Ingrese numero de sucursal: "))
        importe = float(input("Ingrese importe de factura: "))
        if dia == "lunes":
            self.matriz[numero_suc - 1][0] += importe
        elif dia == "martes":
            self.matriz[numero_suc - 1][1] += importe
        elif dia == "miercoles":
            self.matriz[numero_suc - 1][2] += importe
        elif dia == "jueves":
            self.matriz[numero_suc - 1][3] += importe
        elif dia == "viernes":
            self.matriz[numero_suc - 1][4] += importe
        elif dia == "sabado":
            self.matriz[numero_suc - 1][5] += importe
        elif dia == "domngo":
            self.matriz[numero_suc - 1][6] += importe

    def Total(self, sucursal):
        total = 0
        for i in range(7):
            total += self.matriz[sucursal - 1][i]
        return total

    def mayorfact(self, dia):
        max = 0
        for i in range(5):
            if max < self.matriz[i][dia - 1]:
                max = self.matriz[i][dia - 1]
        for i in range(5):
            if max == self.matriz[i][dia - 1]:
                return i+1

    def menorfac(self):
        min = 999999
        sum = 0
        for i in range(5):
            for j in range(7):
                sum += self.matriz[i][j]
        if min > sum:
            min = sum
            suc = i

        return suc+1

    def sumatorio(self):
        sum = 0
        for i in range(5):
            for j in range(7):
                sum += self.matriz[i][j]
        return sum


if __name__ == "__main__":
    print("Menu de opciones:")
    Gestor = gestor()
    a = int(input(" 1. Cargar Datos \n 2. Total de Facturacion de Sucursal \n 3. Mayor Facturacion diaria \n 4. Menos Facturacion Semanal \n 5. Total de Sucursales Semanal \n : "))
    while a != 0:
        if a == 1:
            Gestor.CargaDatos()
        elif a == 2:
            sucursal = int(input("Ingrese numero sucursal para calcular: "))
            print("El total es: ", Gestor.Total(sucursal))
        elif a == 3:
            dia = int(input("Ingrese dia de semana con numero: "))
            print("La sucursal que mas facturo ese dia es la sucursal: ",
                  Gestor.mayorfact(dia))
        elif a == 4:
            print("La sucursal que menos facturo fue: ", Gestor.menorfac())
        elif a == 5:
            print("La suma es: ", Gestor.sumatorio())
        else:
            print("Numero erroneo")
        a = int(input("Ingrese otra opcion: "))
