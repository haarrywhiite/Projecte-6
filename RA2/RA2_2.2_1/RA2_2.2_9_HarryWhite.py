# Autor: Harry White
# Data: 10-10-25

# Descripció del programa o enunciat de l'exercici:
#Trobar el número màxim d’una llista

# Especificacions d'entrada
# Una llista de nombres enters
# Especificacions de sortida
# Missatge amb el número màxim de la llista

numbers = [3, 5, 2, 8, 1, 4]
max_num = numbers[0]
for num in numbers:
    if num > max_num:
        max_num = num
print("El número màxim és:", max_num)



