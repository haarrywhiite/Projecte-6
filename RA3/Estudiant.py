# Autor: Harry White
# Data: 14-01-26

# Descripció del programa o enunciat de l'exercici:
#Crea una classe Estudiant mAtributs: nom, nota Mètode: dir si ha aprovat o no (nota ≥ 5)

class Estudiant:
    def __init__(self,nom,nota):
        self.nom = nom
        self.nota = nota
    def ha_aprovat(self):
        if self.nota >= 5:
            return True
        else:
            return False