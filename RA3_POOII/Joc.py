# Autor: Harry White
# Data: 23-01-26

# Descripció del programa o enunciat de l'exercici:
#9. Gestor de puntuació Classe Joc amb atribut privat __puntuacio. Inicialitza a 0 Afegeix mètodes per sumar punts i reiniciar la puntuació El getter retorna la puntuació

class Joc:
    def __init__(self):
        self.__puntuacio = 0

    def sumar_punts(self, punts):
        if punts > 0:
            self.__puntuacio += punts

    def reiniciar_puntuacio(self):
        self.__puntuacio = 0

    def obtenir_puntuacio(self):
        return self.__puntuacio
