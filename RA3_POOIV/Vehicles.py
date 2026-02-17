# Autor: Harry White
# Data: 28-1-26
#Descripció del programa o enunciat de l'exercici
#Exercici 2: Vehicles Crea una classe Vehicle amb un atribut marca i un mètode arrencar(). Crea una subclasse Cotxe que afegeixi un mètode tocar_claxon() que imprimeixi "Pip pip!". Crea una instància de Cotxe i crida els dos mètodes.

class Vehicle:
    def __init__(self, marca):
        self.marca = marca

    def arrencar(self):
        print(f"El vehicle de marca {self.marca} està arrencant.")

class Cotxe(Vehicle):
    def tocar_claxon(self):
        print("Pip pip!")
