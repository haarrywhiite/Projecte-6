# Autor: Harry White
# Data: 1-10-25

# Descripció del programa o enunciat de l'exercici:
# Escriu un programa que demani tres números i digui quin és el més gran.
# Especificacions d'entrada
# Tres números enters
# Especificacions de sortida

num1 = int(input())
num2 = int(input())
num3 = int(input())

if num1 >= num2 and num1 >= num3:
    print("El número més gran és:", num1)
elif num2 >= num1 and num2 >= num3:
    print("El número més gran és:", num2)
else:
    print("El número més gran és:", num3)