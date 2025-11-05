# Autor: Harry White
# Data: 31-10-25

#Descripció del programa o enunciat de l'exercici:
#Substitueix totes les lletres "a" per "@" en una frase donada.

# Especificacions d'entrada
# Demana a l'usuari que introdueixi una frase
# Especificacions de sortida
# Imprimeix la frase amb les substitucions realitzades

frase = input("Introdueix una frase: ")
lletra = "a"
substitucio = "@"
frase_modificada = frase.replace(lletra, substitucio)
print("Frase modificada:", frase_modificada)
