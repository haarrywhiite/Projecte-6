# Autor: Harry White
# Data: 1-10-25

# Descripció del programa o enunciat de l'exercici:
#Demana a l'usuari una frase i compta quantes vocals conté.

# Especificacions d'entrada
# Una frase introduïda per l'usuari
# Especificacions de sortida
# El nombre de vocals en la frase introduïda

text = input("Introdueix una frase: ")
vocals = "aeiouAEIOU"
count = 0
for char in text:
    if char in vocals:
        count += 1
print("Nombre de vocals:", count)



