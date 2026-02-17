# Autor: Harry White
# Data: 28-1-26
#Descripció del programa o enunciat de l'exercici
#Exercici 1: Animals Crea una classe Animal amb un mètode parlar(). Després, crea dues subclasses: Gos → imprimeix "Bup bup!" Gat → imprimeix "Miau!" Crida el mètode parlar() per a cada tipus d’animal.

class Animal:
    def parlar(self):
        print ("L'animal fa un so.")

class Gos(Animal):
    def parlar(self):
        print("Bup bup!")

class Gat(Animal):
    def parlar(self):
        print("Miau!")

