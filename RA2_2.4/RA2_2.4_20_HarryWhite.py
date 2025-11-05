# Autor: Harry White
# Data: 5-11-25

#Descripció del programa o enunciat de l'exercici:
#Demana una llista de paraules i crea una nova llista amb només les paraules que comencen per vocal.

# Especificacions d'entrada
# Demana a l'usuari que introdueixi una llista de paraules separades per espais
# Especificacions de sortida
# Imprimeix la llista de paraules que comencen per vocal

paraules = input("Introdueix una llista de paraules separades per espais: ").split()
vocals = 'aeiouAEIOU'
paraules_amb_vocal = [paraula for paraula in paraules if paraula[0] in vocals]
print("Paraules que comencen per vocal:", paraules_amb_vocal)

