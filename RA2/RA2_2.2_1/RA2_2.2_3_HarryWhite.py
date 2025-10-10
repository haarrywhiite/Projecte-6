# Autor: Harry White
# Data: 8-10-25

# Descripció del programa o enunciat de l'exercici:
# Programa que mostra la taula de multiplicar d'un nombre introduït per l'usuari.

# Especificacions d'entrada
# Un nombre enter introduït per l'usuari
# Especificacions de sortida
# Missatge amb la taula de multiplicar del nombre introduït

num = int(input("Introdueix un número enter: "))
i = 1
while i <= 10:
    print(num, "x", i, "=", num*i)
    i += 1

