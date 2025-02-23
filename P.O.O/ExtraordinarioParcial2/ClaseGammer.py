class Gammer:
    __idjugador: int
    __dni: int
    __nombre: str
    __apellido: str
    __alias: str
    __plan: str
    __importebase: int
    __tiempolimite: int

    def __init__(self, idjugador, dni, nombre, apellido, alias, plan, importebase, tiempolimite):
        self.__idjugador = idjugador
        self.__dni = dni
        self.__nombre = nombre
        self.__apellido = apellido
        self.__alias = alias
        self.__plan = plan
        self.__importebase = importebase
        self.__tiempolimite = tiempolimite
    
    def getidjugador(self):
        return self.__idjugador
    
    def getdni(self):
        return self.__dni
    
    def getnombre(self):
        return self.__nombre
    
    def getapellido(self):
        return self.__apellido
    
    def getalias(self):
        return self.__alias
    
    def getplan(self):
        return self.__plan
    
    def getimportebase(self):
        return self.__importebase
    
    def gettiempolimite(self):
        return self.__tiempolimite