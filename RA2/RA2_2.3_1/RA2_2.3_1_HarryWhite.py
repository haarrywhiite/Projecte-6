# Autor: Harry White
# Data: 17-10-25

# Descripció del programa o enunciat de l'exercici:
#Utilitzant el range(),  escriu un programa que generi una seqüència de nombres des de 0 fins a un nombre introduït per l'usuari. 
#Excepció: Gestiona l'error si l'usuari introdueix un valor que no és un nombre enter

# Especificacions d'entrada
# Demana a l'usuari que introdueixi un nombre enter
# Especificacions de sortida
# Imprimeix la seqüència de nombres des de 0 fins al nombre introduït

try:
    num = int(input("Introdueix un nombre enter: "))
    
    for i in range(num + 1):
        print(i)
except ValueError:
    print("Error: Si us plau, introdueix un nombre enter vàlid.")



