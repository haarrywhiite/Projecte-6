# Autor: Harry White
# Data: 14-01-26

# Descripció del programa o enunciat de l'exercici:
#Crea una classe Producte Atributs: nom, preu Mètode: aplicar un descompte (donat com a percentatge)

class Producte:
    def __init__(self, nom, preu):
        self.nom = nom
        self.preu = preu
    
    def aplicar_descompte(self, percentatge):
        descompte = self.preu * (percentatge / 100)
        self.preu -= descompte