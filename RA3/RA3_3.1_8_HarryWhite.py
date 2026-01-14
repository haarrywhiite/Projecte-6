# Autor: Harry White
# Data: 14-01-26

# Descripció del programa o enunciat de l'exercici:
#Crea una classe Animal Atributs: nom, espècie Mètode fer_soroll() que mostri un text genèric (“fa un soroll”)
#Crea una classe Gos que hereti d’Animal i sobreescrigui fer_soroll() per dir “Bup bup!”.

from Animal import Animal

class Gos(Animal):
    def fer_soroll(self):
        print(f"{self.nom} diu: Bup bup!")

gos = Gos("Sonny", "gos")
gos.fer_soroll()