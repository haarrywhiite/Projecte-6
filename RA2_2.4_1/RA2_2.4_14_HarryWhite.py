# Autor: Harry White
# Data: 31-10-25

#Descripció del programa o enunciat de l'exercici:
#Demana 10 números i crea dues llistes: una amb els parells i una altra amb els senars.

# Especificacions d'entrada
# Demana a l'usuari que introdueixi 10 números
# Especificacions de sortida
# Imprimeix les dues llistes: una amb els números parells i una altra amb els números senars

parells = []
senars = []
for i in range(10):
    numero = int(input("Introdueix el número {}: ".format(i+1)))
    if numero % 2 == 0:
        parells.append(numero)
    else:
        senars.append(numero)
print("Llista de números parells:", parells)
print("Llista de números senars:", senars)
    
