import random
# Autor: Harry White
# Data: 8-10-25

# Descripció del programa o enunciat de l'exercici:
#Joc d'endevinar un número entre l'1 i el 100

# Especificacions d'entrada
#Nombre enter introduït per l'usuari

# Especificacions de sortida
# Missatge indicant si el número a endevinar és més gran o més petit que el número introduït per l'usuari

num=random.randint(1,100)
n_usu=int(input("Introdueix un número entre l'1 i el 100: "))

while n_usu!=num:
    if num < n_usu:
        print("El número és més petit")
        n_usu=int(input("Introdueix un altre número: "))
    if num > n_usu:
        print("El número és més gran")
        n_usu=int(input("Introdueix un altre número: "))
print("Has encertat!")
        

