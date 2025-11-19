# Autor: Harry White
# Data: 19-11-25

#Descripció del programa o enunciat de l'exercici:
# Crea un programa que escrigui les següents 3 línies en un fitxer nou anomenat sortida.txt. El contingut anterior (si n'hi ha) ha de desaparèixer.

# Especificacions d'entrada

# Especificacions de sortida

fitxer = open("sortida.txt", "w",)
fitxer.write("Aquesta és la primera línia EX2.\n")
fitxer.write("Aquesta és la segona línia EX2.\n")
fitxer.write("Aquesta és la tercera línia EX2.\n")
fitxer.close()


