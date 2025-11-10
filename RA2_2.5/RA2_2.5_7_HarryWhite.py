# Autor: Harry White
# Data: 5-11-25

#Descripció del programa o enunciat de l'exercici:
#Escriu una funció maxim(a, b, c) que retorni el nombre més gran entre els tres.

# Especificacions d'entrada
#Introdueix tres nombres enters
# Especificacions de sortida
#El nombre més gran (enter)

a = int(input("Introdueix el primer nombre: "))
b = int(input("Introdueix el segon nombre: "))
c = int(input("Introdueix el tercer nombre: "))

def maxim(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c
print("El nombre més gran és:", maxim(a, b, c))
