# Autor: Harry White
# Data: 14-01-26

# Descripció del programa o enunciat de l'exercici:
#Crea una classe CotxeAtributs: marca, model, any Mètode per mostrar la informació del cotxe
#Crea dos cotxes amb la classe Cotxe i imprimeix-ne la informació.

from Cotxe import Cotxe

cotxe1 = Cotxe("Ford", "Mustang", 2020)
cotxe2 = Cotxe("Ford", "Focus", 2018)

cotxe1.mostrar_info()
cotxe2.mostrar_info()