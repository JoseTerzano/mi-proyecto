class Conexion:
    __id: int
    __direccion: str
    __juego: str
    __fecha: str
    __horainicio: int
    __horafinal: int    

    def __init__(self, id, direccion, juego, fecha, horainicio, horafinal):
        self.__id = id
        self.__direccion = direccion
        self.__juego = juego
        self.__fecha = fecha
        self.__horainicio = horainicio
        self.__horafinal = horafinal

    def getid(self):
        return self.__id
    
    def getdirection(self):
        return self.__direccion
    
    def getjuego(self):
        return self.__juego
    
    def getfecha(self):
        return self.__fecha
    
    def gethorainicio(self):
        return self.__horainicio
    
    def gethorafinal(self):
        return self.__horafinal
    
    def __str__(self):
        return f"""{self.__id}   {self.__direccion}   {self.__juego}   {self.__fecha}   {self.__horainicio}   {self.__horafinal}"""
    
    def __eq__(self, other):
        return (
            self.__id == other.getid() and self.__fecha == other.getfecha() and self.__horainicio == other.gethorainicio() and self.__direccion != other.getdirection())
    
    def __lt__(self, other):
        return (self.__id < other.getid() and self.__fecha < other.getfecha() and self.__horainicio < other.gethorainicio() and self.__direccion < other.getdirection())