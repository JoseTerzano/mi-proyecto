from ClaseClienteLocal import ClienteLocal
class ClienteNacional(ClienteLocal):
    __provincia: str
    __localidad: str
    __codigopostal: int

    def __init__(self, nombre, apellido, email, contrasena, direccion, telefono, provincia, localidad, codigopostal):
        super().__init__(nombre, apellido, email, contrasena, direccion, telefono)
        self.__provincia = provincia
        self.__localidad = localidad
        self.__codigopostal = codigopostal
    
    def __str__(self):
        return f"{super().__str__()}, {self.__provincia}, {self.__localidad}, {self.__codigopostal}"
    
    def getprovincia(self):
        return self.__provincia