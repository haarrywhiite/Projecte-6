# Autor: Harry White
# Data: 5-11-25

#Descripció del programa o enunciat de l'exercici:
#Fes un programa que elimini els duplicats d'una llista.

# Especificacions d'entrada
# Demana a l'usuari que introdueixi una llista de nombres separats per espais
# Especificacions de sortida
# Imprimeix la llista sense duplicats

llista = input("Introdueix una llista de nombres separats per espais: ").split()
llista_sense_duplicats = list(set(llista))
print("Llista sense duplicats:", llista_sense_duplicats)


