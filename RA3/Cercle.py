# Autor: Harry White
# Data: 14-01-26

# Descripció del programa o enunciat de l'exercici:
#Crea una classe Cercle Atribut: radi Mètodes: calcular àrea i perímetre

class Cercle:
    def __init__(self, radi):
        self.radi = radi

    def calcular_area(self):
        return 3.1416 * (self.radi ** 2)
    
    def calcular_perimetre(self):
        return 2 * 3.1416 * self.radi
    