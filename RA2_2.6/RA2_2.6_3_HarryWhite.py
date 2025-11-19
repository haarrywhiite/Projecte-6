# Autor: Harry White
# Data: 19-11-25

#Descripció del programa o enunciat de l'exercici:
#Afegir continguts: Afegeix una línia nova a un fitxer existent (sortida.txt) sense esborrar el que ja hi ha.
# Especificacions d'entrada

# Especificacions de sortida

fitxer = open("sortida.txt", "a",)

fitxer.write("Aquesta es una linia afegida EX3.\n")

fitxer.close()
