# Autor: Harry White
# Data: 14-01-26

# Descripció del programa o enunciat de l'exercici:
#Crea una classe Punt Atributs: x, y Mètode: calcular la distància a un altre punt

class Punt:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distancia(self, altre_punt):
        return ((self.x - altre_punt.x) ** 2 + (self.y - altre_punt.y) ** 2) ** 0.5
    
    