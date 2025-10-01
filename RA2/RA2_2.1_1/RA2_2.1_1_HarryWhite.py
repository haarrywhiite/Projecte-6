# Autor: Harry White
# Data: 1-10-25

# Descripció del programa o enunciat de l'exercici:
#Programa que diu si un número és més gran, més petit o igual que 0
# Especificacions d'entrada
#Introduir un número
# Especificacions de sortida
#Missatge dient si és més gran, més petit o igual que 0

num1=int(input())

if num1 > 0:
    print("Es mes gran")
if num1 == 0:
    print("Es igual")
if num1 < 0:
    print("Es mes petit")