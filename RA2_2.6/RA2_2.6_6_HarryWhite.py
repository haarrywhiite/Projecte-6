# Autor: Harry White
# Data: 19-11-25

#Descripció del programa o enunciat de l'exercici:
#Comprovar si el fitxer existeix abans de llegir-lo: Fes un programa que intenti llegir un fitxer anomenat dades.txt, però abans comprovi si existeix. Si no existeix, mostra un missatge d’error amigable.
#Pista: utilitza os.path.exists() o captura l’error FileNotFoundError


# Especificacions d'entrada

# Especificacions de sortida

try:
    fitxer = open("dades.txt", "r")
    for linia in fitxer:
        print(linia.strip())
    fitxer.close()
except FileNotFoundError:
    print("Error: El fitxer dades.txt no existeix.")
