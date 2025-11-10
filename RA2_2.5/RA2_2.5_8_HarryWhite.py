# Autor: Harry White
# Data: 5-11-25

#Descripció del programa o enunciat de l'exercici:
#Escriu una funció factorial(n) que calculi el factorial d'un nombre n de forma recursiva. (Pista: factorial de n és n * factorial(n-1), amb factorial(0) = 1.)

# Especificacions d'entrada
#Introdueix un nombre enter no negatiu
# Especificacions de sortida
#El factorial del nombre (enter)

n = int(input("Introdueix un nombre enter no negatiu: "))
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
print("El factorial de", n, "és:", factorial(n))


