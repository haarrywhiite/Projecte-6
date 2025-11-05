# Autor: Harry White
# Data: 31-10-25

#Descripció del programa o enunciat de l'exercici:
#Demana una paraula i verifica si és un palíndrom (ex: "anna", "civic", etc.).

# Especificacions d'entrada
# Demana a l'usuari que introdueixi una paraula
# Especificacions de sortida
# Indica si la paraula és un palíndrom o no

paraula = input("Introdueix una paraula: ")
if paraula == paraula[::-1]:
    print("La paraula és un palíndrom.")
else:
    print("La paraula no és un palíndrom.")

