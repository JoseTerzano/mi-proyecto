from ClaseLista import Lista

if __name__ == "__main__":
    l = Lista()
    a = int(input("1. Agregar Publicacion \n 2. Mostrar \n 3. Mostrar Total \n 4. Recorrer \n 0. Para Finalizar \n Su Opcion: "))
    while a != 0:
        if a == 1:
            l.CargarCD()
            l.cargarLibro()
            l.Mostrar()
        if a == 2:
            l.CargarCD()
            l.cargarLibro()
            pos = int(input("Ingrese posicion: "))
            l.MostrarPos(pos)
        if a == 3:
            l.CargarCD()
            l.cargarLibro()
            l.MostrarTodo()
        if a == 4:
            l.CargarCD()
            l.cargarLibro()
            l.Recorrer()
        a = int(input("1. Agregar Publicacion \n 2. Mostrar \n 3. Mostrar Total \n 4. Recorrer \n 0. Para Finalizar \n Su Opcion: "))
