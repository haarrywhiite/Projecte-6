# Autor: Harry White
# Data: 30-01-26
# Descripció del programa o enunciat de l'exercici
#Crea una classe Animal amb un mètode fer_soroll(). Crea dues subclasses: Gat i Vaca, i sobreescriu el mètode per retornar "Miau" i "Muuu", respectivament. Després, crea una funció reproduir_soroll(animal) que cridi fer_soroll().

class Animal:
    def parlar(self):
        print("L'animal fa un soroll.")

class Gat(Animal):
    def parlar(self):
        print("Miau Miau!")

class Vaca(Animal):
    def parlar(self):
        print("Muuu!")

def reproduir_soroll(animal):
    animal.parlar()
