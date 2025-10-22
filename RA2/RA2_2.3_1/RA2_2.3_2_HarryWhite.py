# Autor: Harry White
# Data: 17-10-25

#Descripció del programa o enunciat de l'exercici:
#Demana a l'usuari un nombre enter i calcula la suma de tots els nombres des de 1 fins a aquest nombre.
#Pista: Utilitza range(1, n+1) per generar la seqüència i la funció sum() per obtenir la suma.
#Excepció: Gestiona l'error si l'usuari introdueix un valor que no és un nombre enter positiu.

# Especificacions d'entrada
# Demana a l'usuari que introdueixi un nombre enter positiu
# Especificacions de sortida
# Imprimeix la suma de tots els nombres des de 1 fins al nombre introduït

try:

    num =int(input("Introdueix un nombre enter positiu: "))

    for i in range(1, num + 1):
        suma = sum(range(1, num + 1))
    print("La suma de tots els nombres des de 1 fins a", num, "és:", suma)

except ValueError:
    print("Error: Si us plau, introdueix un nombre enter vàlid.")
    
    