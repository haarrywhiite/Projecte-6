# Autor: Harry White
# Data: 30-01-26
# Descripció del programa o enunciat de l'exercici
#Exercici 2: Dibuixar figures Crea una classe Figura amb un mètode dibuixar(). Crea subclasses com Cercle, Quadrat i Triangle, cadascuna amb la seva pròpia implementació del mètode dibuixar(). Crea una llista de figures i recorre-la cridant dibuixar() a cada element.

class Figura:
    def dibuixar(self):
        print("Dibuixant una figura genèrica.")

class Cercle(Figura):
    def dibuixar(self):
        print("Dibuixant un cercle.")

class Quadrat(Figura):
    def dibuixar(self):
        print("Dibuixant un quadrat.")

class Triangle(Figura):
    def dibuixar(self):
        print("Dibuixant un triangle.")

