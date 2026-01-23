# Autor: Harry White
# Data: 21-01-26

# Descripció del programa o enunciat de l'exercici:
# 5. Sensor amb valors limitats Classe Sensor amb atribut privat __valor. El setter: només permet valors entre 0 i 100  el getter retorna el valor actual

class Sensor:
    def __init__(self, valor_inicial):
        self.__valor = 0
        self.valor = valor_inicial  
        
    @property
    def valor(self):
        return self.__valor

    @valor.setter
    def valor(self, nou_valor):
        if 0 <= nou_valor <= 100:
            self.__valor = nou_valor