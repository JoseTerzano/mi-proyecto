class Cliente:
    __tiempo_espera:int
    __tiempo_en_caja:int

    def __init__(self, tiempo_en_caja):
        self.__tiempo_espera = 0
        self.__tiempo_en_caja = tiempo_en_caja

    def settiempo_espera(self,tiempo_espera):
        self.__tiempo_espera=tiempo_espera

    def gettiempo_espera(self):
        return self.__tiempo_espera
    
    def gettiempo_en_caja(self):
        return self.__tiempo_en_caja
    
    def settiempo_en_caja(self):
        self.__tiempo_en_caja -= 1

    def __str__(self):
        return f"Cliente"