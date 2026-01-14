# Autor: Harry White
# Data: 14-01-26

# Descripció del programa o enunciat de l'exercici:
#Crea una classe Animal Atributs: nom, espècie Mètode fer_soroll() que mostri un text genèric (“fa un soroll”)

class Animal:
    def __init__(self, nom, especie):
        self.nom = nom
        self.especie = especie
        
        def fer_soroll(self):
            print(f"{self.nom} fa un soroll.")

