# Autor: Harry White
# Data: 5-11-25

#Descripció del programa o enunciat de l'exercici:
#Escriu una funció multiplica_tot(*nombres) que rebi qualsevol quantitat de nombres i retorni la seva multiplicació.

# Especificacions d'entrada
#Introdueix nombres separats per espais
# Especificacions de sortida
#La multiplicació és: (enter)

nombres = input("Introdueix nombres separats per espais: ")
def multiplica_tot(*nombres):
    resultat = 1
    for nombre in nombres:
        resultat *= nombre
    return resultat
nombres_list = [int(x) for x in nombres.split()]
print("La multiplicació és:", multiplica_tot(*nombres_list))


