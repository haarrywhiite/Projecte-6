# Autor: Harry White
# Data: 19-11-25

#Descripció del programa o enunciat de l'exercici:
#Llegir i escriure: Obre un fitxer en mode lectura i escriptura (r+). Mostra el contingut per pantalla i afegeix una línia al final sense esborrar el contingut anterior.


# Especificacions d'entrada

# Especificacions de sortida

fitxer = open("sortida.txt", "r+")
for linia in fitxer:
    print(linia.strip())
fitxer.write("Aquesta es una linia afegida EX5.\n")
fitxer.close()
