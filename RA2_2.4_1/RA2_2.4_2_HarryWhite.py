# Autor: Harry White
# Data: 31-10-25

#Descripció del programa o enunciat de l'exercici:
#Demana una frase i compta quantes vocals conté.

# Especificacions d'entrada
# Demana a l'usuari que introdueixi una frase
# Especificacions de sortida
# Imprimeix el nombre de vocals a la frase introduïda

frase = input("Introdueix una frase: ")
vocals = "aeiouAEIOU"
contador = 0
for char in frase:
    if char in vocals:
        contador += 1
print("El nombre de vocals a la frase és:", contador)




        
        
