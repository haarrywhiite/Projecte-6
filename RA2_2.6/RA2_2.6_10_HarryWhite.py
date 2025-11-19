# Autor: Harry White
# Data: 19-11-25

#Descripció del programa o enunciat de l'exercici:
#Assegurar el tancament del fitxer (amb error): Simula una operació amb fitxers on pot haver-hi un error durant la lectura. Assegura’t que el fitxer es tanqui sempre, fins i tot si es produeix un error en llegir-lo.
#Pista: utilitza try-finally o millor encara: comprova què passa si no utilitzes with i ho fas tot manualment amb .open() i .close().

# Especificacions d'entrada

# Especificacions de sortida

try:
    fitxer = open("dades.txt", "r")
    for linia in fitxer:
        print(linia.strip())
        if linia.strip() == "3":
            raise ValueError("Simulem un error durant la lectura.")
except Exception as e:
    print("S'ha produït un error durant la lectura del fitxer:", e)

finally:
    fitxer.close()
    print("El fitxer ha estat tancat correctament.")
    
