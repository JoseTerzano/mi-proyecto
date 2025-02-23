import abc
from abc import ABC
class ClienteLocal(ABC):
    __nombre: str
    __apellido: str
    __email: str
    __contrasena: str
    __direccion: str
    __telefono: str

    def __init__(self, nombre, apellido, email, contrasena, direccion, telefono):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__email = email
        self.__contrasena = contrasena
        self.__direccion = direccion
        self.__telefono = telefono
        
    def __str__(self):
        return f"{self.__nombre} {self.__apellido}"
    
    def getnombre(self):
        return self.__nombre