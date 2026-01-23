# Autor: Harry White
# Data: 23-01-26

# Descripció del programa o enunciat de l'exercici:
#8. Alumne amb edat controlada Classe Alumne amb atribut privat __edat. El setter no accepta valors negatius El getter retorna l’edat

class Alumne:
    def __init__(self, edat_inicial):
        self.__edat = None
        self.edat = edat_inicial  
        
    @property
    def edat(self):
        return self.__edat

    @edat.setter
    def edat(self, nova_edat):
        if nova_edat >= 0:
            self.__edat = nova_edat
        else:
            print("Error: L'edat no pot ser negativa.")