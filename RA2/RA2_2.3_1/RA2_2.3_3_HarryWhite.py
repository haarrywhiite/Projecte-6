# Autor: Harry White
# Data: 17-10-25

#Descripció del programa o enunciat de l'exercici:
#Utilitzant el range() escriu un programa que mostri la taula de multiplicar d'un número introduït per l'usuari.
#Pista: Utilitza range(1, 11) per generar els multiplicadors del 1 al 10.​
#Excepció: Gestiona l'error si l'usuari introdueix un valor que no és un nombre enter.

# Especificacions d'entrada
# Demana a l'usuari que introdueixi un nombre enter
# Especificacions de sortida
# Imprimeix la taula de multiplicar del nombre introduït

try:
    num = int(input("Introdueix un numero enter: "))
    for i in range(1, 11):
      print (f"{num}x{i}={num*i}")
except ValueError:
    print("Error: Si us plau, introdueix un nombre enter vàlid.")