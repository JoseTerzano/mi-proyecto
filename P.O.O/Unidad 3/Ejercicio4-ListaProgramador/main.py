from ClaseLista import Lista
from ClaseMenu import MenuDeOpciones


def test():
    list = Lista()
    list.cargaPubli()
    c = MenuDeOpciones()
    c.Menu(list)


if __name__ == '__main__':
    test()
