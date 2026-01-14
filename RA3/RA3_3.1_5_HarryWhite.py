# Autor: Harry White
# Data: 14-01-26

# Descripció del programa o enunciat de l'exercici:
#Crea una classe Estudiant mAtributs: nom, nota Mètode: dir si ha aprovat o no (nota ≥ 5)
#Crea una llista d’estudiants. Mostra només els que han aprovat.

from Estudiant import Estudiant

estudiants = [
    Estudiant("Anna", 7),
    Estudiant("Bernat", 4), 
    Estudiant("Carla", 9),
    Estudiant("David", 3)
]

print("Estudiants que han aprovat:")
for estudiant in estudiants:
    if estudiant.ha_aprovat():
        print(estudiant.nom)
    

