# Autor: Harry White
# Data: 19-11-25

#Descripció del programa o enunciat de l'exercici:
#Gestionar errors d'escriptura: Escriu un programa que intenti escriure en un fitxer anomenat resultats.txt, però gestiona l'error que es pot produir si el fitxer és només de lectura o si el sistema impedeix escriure-hi (permisos denegats).
#Pista: captura PermissionError.


# Especificacions d'entrada

# Especificacions de sortida

try:
    fitxer = open("resultats.txt", "w")
    fitxer.write("Aquest es un text de prova per a la gestio d'errors.\n")
    fitxer.close()
    print("Escriptura al fitxer realitzada amb exit.")

except PermissionError:
    print("Error: Permisos denegats per escriure al fitxer resultats.txt.")
