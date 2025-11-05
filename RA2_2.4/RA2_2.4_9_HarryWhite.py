# Autor: Harry White
# Data: 31-10-25

#Descripció del programa o enunciat de l'exercici:
#Crea un programa que divideixi una frase en paraules i les mostri una per una.

# Especificacions d'entrada
# Demana a l'usuari que introdueixi una cadena de text
# Especificacions de sortida
# Imprimeix la cadena sense espais

frase = input("Introdueix una frase: ")
paraules = frase.split()
for paraula in paraules:
    print(paraula)

