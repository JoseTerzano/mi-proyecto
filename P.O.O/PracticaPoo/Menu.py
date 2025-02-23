from ClaseColeccion import Lista
from ClaseClienteLocal import ClienteLocal
from ClaseClienteNacional import ClienteNacional

if __name__ == "__main__":
    lista = Lista()
    lista.inicializar(ClienteLocal("Juan", "Perez", "juanperez@gmail.com", "123456", "Av. Juan Perez 123", "123456789"))
    lista.inicializar(ClienteNacional("Pedro", "Perez", "pedroperez@gmail.com", "123456", "Av. Pedro Perez 123", "123456789", "San juan", "Rivadavia", 5400))
    lista.inicializar(ClienteLocal("Jose", "Terzano", "joseter@gmail.com", "654321", "Av. Libertad Sur", "44856697"))
    lista.inicializar(ClienteNacional("Lucas", "Ruiz", "luqita@gmail.com", "789456", "Av. San Juan 333", "789456123", "San Luis", "Rawson", 5200))
    print("Menu de Opciones:")
    a = int(input("1. Inciso 1\n2. Inciso 2\nSalir = 0\n"))
    while a != 0:
        if a == 1:
            lista.Inciso1()
        if a == 2:
            try:
                pos = int(input("Ingrese la posicion: "))
                lista.Inciso2(pos)
            except ValueError:
                print("Ingrese Valor Numerico Entero")
            except IndexError as e:
                print(e)
        a = int(input("1. Inciso 1\n2. Inciso 2\nSalir = 0\n"))