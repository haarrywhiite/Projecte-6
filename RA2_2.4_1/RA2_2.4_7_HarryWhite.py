# Autor: Harry White
# Data: 31-10-25

#Descripció del programa o enunciat de l'exercici:
#Demana una cadena i compta quantes vegades apareix una lletra concreta.

# Especificacions d'entrada
# Demana a l'usuari que introdueixi una cadena de text i una lletra concreta
# Especificacions de sortida
# Imprimeix el nombre de vegades que la lletra apareix en la cadena

cadena = input("Introdueix una cadena de text: ")
lletra = input("Introdueix una lletra concreta: ")
contador = cadena.count(lletra)
print(f"La lletra '{lletra}' apareix {contador} vegades en la cadena.")

