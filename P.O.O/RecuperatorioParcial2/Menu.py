from lista import Lista

if __name__ == "__main__":
    l = Lista()
    l.inicializar()
    print("Menu de opciones")
    a = int(input("1. Ingresar Posicion\n2. Ingresar Anio\n3. Mostrar Cantidad\n4. Mostrar\n6. Salir ingrese 0\n"))
    while a != 0:
        if a == 1:
            try:
                pos = int(input("Escribe la posicion: "))
                l.excepcion(pos)
            except ValueError:
                print("ingrese un numero valido")
            except IndexError as e:
                print(e)
        if a == 2:
            numero = int(input("Ingrese el anio: "))
            l.mostrarcantidad(numero)
        if a == 3:
            numero = int(input("Ingrese capacidad de carga: "))
            l.mostrarcapacidad(numero) 
        if a == 4:
            l.mostrar()
        a = int(input("1. Ingresar Posicion\n2. Ingresar Anio\n3. Mostrar Cantidad\n4. Mostrar\n6. Salir ingrese 0\n"))