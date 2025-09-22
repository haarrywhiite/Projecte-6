# Autor: Harry White
# Fecha: 2024-06-22

# Observa el codi següent i respon (posa les respostes dins del codi en forma de
# comentari):

import math

PI = 3.1416

def calcular_area(radi):
    return PI * radi ** 2

radi = float(input("Introdueix el radi: "))
area = calcular_area(radi)

print("L'àrea del cercle és: ", area)

# Constants: PI
# Variables: radi, area
# Funció: calcular_area(radi)
# Llegeix dades de l'usuari: radi = float(input("Introdueix el radi: "))
# Mostra el resultat: print(f"L'àrea del cercle és: ", area)
