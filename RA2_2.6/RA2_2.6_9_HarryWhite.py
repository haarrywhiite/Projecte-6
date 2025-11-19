# Autor: Harry White
# Data: 19-11-25

#Descripció del programa o enunciat de l'exercici:
#Crear el fitxer si no existeix: Intenta obrir un fitxer en mode lectura. Si no existeix, crea’l automàticament i escriu-hi una línia per defecte: "Fitxer creat automàticament".
#Pista: utilitza try-except amb open(...) en mode "r", i si falla, obre'l en mode "w".


# Especificacions d'entrada

# Especificacions de sortida

try:
    fitxer = open("dades.txt", "r")
    for linia in fitxer:
        print(linia.strip())
    fitxer.close()
except FileNotFoundError:
    fitxer = open("dades.txt", "w")
    fitxer.write("Fitxer creat automàticament.\n")
    fitxer.close()
    print("El fitxer dades.txt no existia i ha estat creat automàticament.")
    



