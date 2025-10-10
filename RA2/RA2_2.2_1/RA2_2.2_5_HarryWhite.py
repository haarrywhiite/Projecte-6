# Autor: Harry White
# Data: 8-10-25

# Descripció del programa o enunciat de l'exercici:
#Demana a l'usuari un número enter positiu i determina si és un nombre primer o no

# Especificacions d'entrada
# Un número enter positiu introduït per l'usuari
# Especificacions de sortida
# Indica si el número és primer o no

num = int(input("Introdueix un número enter positiu: "))
if num < 2:
	print("No és primer")
else:
	i = 2
	es_compost = False
	while i * i <= num and not es_compost:
		if num % i == 0:
			es_compost = True
		i += 1
	print("No és primer" if es_compost else "És primer")


