# Autor: Harry White
# Data:8-10-25

# Descripció del programa o enunciat de l'exercici:
#Demana a l'usuari una cadena de text i mostra-la invertida.

# Especificacions d'entrada
# Una cadena de text introduïda per l'usuari
# Especificacions de sortida
# La cadena de text invertida

text = input("Introdueix una frase: ")
result = ""
i = len(text) - 1
while i >= 0:
    result += text[i]
    i -= 1

print("Frase invertida:", result)


