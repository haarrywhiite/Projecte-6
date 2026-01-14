# Autor: Harry White
# Data: 14-01-26

# Descripció del programa o enunciat de l'exercici:
#Crea una classe Punt Atributs: x, y Mètode: calcular la distància a un altre punt
#Crea dos punts i calcula la distància entre ells.

from Punt import Punt

punt1 = Punt(3, 4)
punt2 = Punt(7, 1)

distancia = punt1.distancia(punt2)
print(f"La distància entre els punts és: {distancia}")

