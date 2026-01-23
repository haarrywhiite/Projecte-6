# Autor: Harry White
# Data: 21-01-26

# Descripció del programa o enunciat de l'exercici:
#7. Temps en hores Classe Rellotge amb atribut __hores. El setter només accepta valors entre 0 i 23. Afegeix mètode per mostrar les hores en format “HH:00”


class Rellotge:
    def __init__(self, hores):
        self.__hores = 0
        self.hores = hores

    @property
    def hores(self):
        return self.__hores

    @hores.setter
    def hores(self, noves_hores):
        if 0 <= noves_hores <= 23:
            self.__hores = noves_hores
        else:
            print("Error: Les hores han de ser entre 0 i 23.")

    def mostrar_hores(self):
        return f"{self.__hores:02d}:00"