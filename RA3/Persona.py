# Autor: Harry White
# Data: 14-01-26

# Descripció del programa o enunciat de l'exercici:
#Crea una classe Persona Atributs: nom, edat Mètode presentar_se() que imprimeixi “Hola, soc X i tinc Y anys”

class Persona:
    def __init__(self,nom, edat):
        self.nom = nom
        self.edat = edat

    def presentar_se(self):
        print(f"Hola, soc {self.nom} i tinc {self.edat} anys")

        