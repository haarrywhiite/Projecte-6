# Autor: Harry White
# Data: 5-11-25

#Descripció del programa o enunciat de l'exercici:
#Escriu una funció estat_persona(edat) que:
#Retorni "Menor d'edat", "Adult" o "Jubilat" segons l'edat.
#Torni tant l'estat com una descripció (return estat, descripcio).

# Especificacions d'entrada
#Introdueix una edat (nombre enter)
# Especificacions de sortida
#L'estat de la persona (cadena de text)

edat = int(input("Introdueix una edat (nombre enter): "))
def estat_persona(edat):
    if edat < 18:
        estat = "Menor d'edat"
        descripcio = "La persona és menor d'edat."
    elif 18 <= edat < 65:
        estat = "Adult"
        descripcio = "La persona és adulta."
    else:
        estat = "Jubilat"
        descripcio = "La persona està jubilada."
    return estat, descripcio
estat, descripcio = estat_persona(edat)

print("Estat:", estat)
print("Descripció:", descripcio)


