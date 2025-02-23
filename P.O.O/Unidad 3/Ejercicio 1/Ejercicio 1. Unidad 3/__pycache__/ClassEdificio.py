from ClassDpto import Departamento
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

    def getnombre(self):
        return self.__nombre
    
    def agregardpto(self, depto):
        d = Departamento(depto.getidd(), depto.getnom(), depto.getnumeropiso(), depto.getnumerodepto(), depto.getchab(), depto.getcbanos(), depto.getsup())
        self.__departamento.append(d)

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
    
    def __del__(self):
        print("Se ha eliminado el edificio")
        del self.__departamento