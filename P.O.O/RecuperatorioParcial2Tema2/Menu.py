from Gestor import Lista

if __name__ == "__main__":
    l = Lista()
    l.inicializar()
    print("Menu de opciones")
    a = int(input("1. Mostrar Tipo\n2. Contar y Mostrar\n3. Mostrar Listado\n4. Mostrar\n Su Opcion: "))
    while a != 0:
        if a == 1:
            try:
                pos = int(input("Ingrese posicion: "))
                l.buscar(pos)
            except IndexError as e:
                print(e)
        if a == 2:
            nombre = input("Ingrese cobertura: ")
            l.Inciso2(nombre)
        a = int(input("1. Ingresar Plan\n2. Mostrar Listado\n3. Salir ingrese 0\n"))