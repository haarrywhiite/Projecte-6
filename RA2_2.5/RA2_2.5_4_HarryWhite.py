# Autor: Harry White
# Data: 5-11-25

#Descripció del programa o enunciat de l'exercici:
#Escriu una funció es_parell(numero) que retorni True si numero és parell i False si no

# Especificacions d'entrada
# Especificacions de sortida

def es_parell(numero):
    return numero % 2 == 0
num = 4
if es_parell(num):
    print(num, "és un número parell.")
