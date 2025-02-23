
class Edificio:
    __id : int
    __nombre : str
    __direc : str
    __empresa : str
    __cpisos : int
    __cdeptos : int
    __departamento : list
    def __init__(self, id, nombre, direc, empresa, cpisos, cdeptos):
        self.__id = id
        self.__nombre = nombre
        self.__direc = direc
        self.__empresa = empresa
        self.__cpisos = cpisos
        self.__cdeptos = cdeptos
        self.__departamento = []

    def agregardpto(self, depto):
        self.__departamento.append(depto)

    def getnombre(self):
        return self.__nombre
    
    def listardptos(self):
        for dpto in self.__departamento:
            print(dpto)

    def superficietotal(self):
        sum = 0
        for i in range(len(self.__departamento)):
            sum += self.__departamento[i].getsup()
        return sum 
    
    def getdepartamentos(self):
        return self.__departamento