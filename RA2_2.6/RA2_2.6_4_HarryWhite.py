# Autor: Harry White
# Data: 19-11-25

#Descripció del programa o enunciat de l'exercici:
#Comptar línies: Llegeix un fitxer i mostra quantes línies té.

# Especificacions d'entrada

# Especificacions de sortida

fitxer = open("missatge.txt", "r")

contador = 0
for linia in fitxer:
    contador += 1
print("El fitxer té", contador, "línies.")
fitxer.close()



