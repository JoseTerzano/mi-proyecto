from ClaseLibro import Libro
from ClaseAudio import Audio

class MenuDeOpciones:
    __opcion: str
    def __init__(self):
        self.__opcion = None
    def Menu(self, list):
        while self.__opcion != '0':
            print('''
            ---MENU DE OPCIONES---
            1.  Agregar publicaciones a la colección  
            2.  Mostrar qué tipo de publicación se encuentra almacenada endicha posición. 
            3.  Mostrar la cantidad de publicaciones de cada tipo.  
            4.  Recorrer la colección y mostrar para todas las publicaciones.''')
            self.__opcion = input(">>> ")

            if self.__opcion == '1':
                titulo = input("Ingrese el Titulo: ") 
                categoria = input("Ingrese la Categoria: ")
                precioBase = float(input("Ingrese el Precio: "))
                tipo = input("Ingrese Tipo de publicacion (1-Libro  2-Audio): ")
                if tipo == '1':
                    autor = input("Ingrese el Autor: ")
                    fechaE = input("Ingrese Fecha de edicion: ")
                    cantPaginas = int(input("Ingrese Cant de paginas: "))
                    publi = Libro(titulo, categoria, precioBase, autor, fechaE, cantPaginas)
                elif tipo == '2':
                    tiempoR = int(input("Ingrese Tiempo de reproduccion: "))
                    narrador = input("Ingrese el Narrador: ")
                    publi = Audio(titulo, categoria, precioBase, tiempoR, narrador)
                list.agregarPubli(publi)

            elif self.__opcion == '2':
                pos = int(input("Ingrese una posición en la lista: "))
                posx = list.mostrarTipoPublicacion(pos)
                if posx == 1:
                    print("Es un libro")
                elif posx == 2:
                    print("Es un audiolibro")

            elif self.__opcion == '3':
                list.mostrarCant()

            elif self.__opcion == '4':
                list.MuestraPub()

            elif self.__opcion == '0':
                print("Gracias por utilizar el programa")
                return
            else: print("OPCION INVALIDA")