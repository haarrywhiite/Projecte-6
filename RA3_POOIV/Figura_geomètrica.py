# Autor: Harry White
# Data: 28-01-26
# Descripció del programa o enunciat de l'exercici
#Exercici 4: Figura geomètrica Crea una classe Figura amb un mètode area() que només imprimeixi "Àrea no definida". Crea dues subclasses: Quadrat amb atribut costat i mètode area() que calculi l'àrea. Cercle amb atribut radi i mètode area() que calculi l’àrea (usa math.pi).

class Figura:
    def area(self):
        print("Àrea no definida")

class Quadrat(Figura):
    def __init__(self, costat):
        self.costat = costat

    def area(self):
        return self.costat ** 2

class Cercle(Figura):
    def __init__(self, radi):
        self.radi = radi

    def area(self):
        import math
        return math.pi * (self.radi ** 2)
    
    