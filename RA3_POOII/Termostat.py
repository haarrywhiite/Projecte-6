# Autor: Harry White
# Data: 21-01-26

# Descripció del programa o enunciat de l'exercici:
# 3. Termòstat Crea una classe Termostat amb un atribut privat __temperatura. Afegeix: un getter i setter amb @property el setter només accepta valors entre 10 i 30 °C

class Termostat:
    def __init__(self, temperatura_inicial):
        self.__temperatura = None
        self.temperatura = temperatura_inicial  # Utilitza el setter per validar

    @property
    def temperatura(self):
        return self.__temperatura

    @temperatura.setter
    def temperatura(self, nova_temperatura):
        if 10 <= nova_temperatura <= 30:
            self.__temperatura = nova_temperatura
        else:
            print("Error: La temperatura ha de ser entre 10 i 30 °C.")