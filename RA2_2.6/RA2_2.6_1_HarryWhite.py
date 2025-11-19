# Autor: Harry White
# Data: 18-11-25

#Descripció del programa o enunciat de l'exercici:
#Llegir un fitxer: Crea un fitxer de text anomenat missatge.txt amb contingut a mà (o des del codi). Escriu un programa que llegeixi i mostri el contingut per pantalla.

# Especificacions d'entrada

# Especificacions de sortida

fitxer = open("missatge.txt", "r")

for linia in fitxer:
    print(linia.strip())
    
fitxer.close()