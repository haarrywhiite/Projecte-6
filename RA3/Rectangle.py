# Autor: Harry White
# Data: 14-01-26

# Descripció del programa o enunciat de l'exercici:
#Crea una classe Rectangle Atributs: amplada, alçadaMètodes: area() i perimetre()

class Rectangle:
    def __init__(self, amplada, alçada):
        self.amplada = amplada
        self.alçada = alçada

    def area(self):
        return self.amplada * self.alçada
    def perimetre(self):
        return 2 * (self.amplada + self.alçada)
    
    
