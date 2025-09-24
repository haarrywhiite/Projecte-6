# Autor: Harry White
# Data: 24-09-25


# Constant
PI = 3.1416

# Funció
def calcular_perimetre(radi):
	return 2 * PI * radi

# Entrada de l'usuari
radi = float(input("Introdueix el radi del cercle: "))

# Sortida per pantalla
perimetre = calcular_perimetre(radi)
print(f"El perímetre del cercle és: {perimetre}")

