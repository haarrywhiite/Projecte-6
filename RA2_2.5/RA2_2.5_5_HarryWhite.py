# Autor: Harry White
# Data: 5-11-25

#Descripció del programa o enunciat de l'exercici:
#Escriu una funció saluda_nom(nom="amic") que imprimeixi "Hola, <nom>".
#Si no passes cap nom, ha de imprimir "Hola, amic".
# Especificacions d'entrada
#Introdueix un nom (cadena de caràcters)
# Especificacions de sortida
#Hola, <nom> (cadena de caràcters) o amic si no s'ha introduït cap nom


nom = input("Introdueix un nom: ")
def saluda_nom (nom):
    print ("Hola, " + nom)
if nom == "":
    saluda_nom ("amic")
else:
    saluda_nom (nom)