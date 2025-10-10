# Autor: Harry White
# Data: 8-10-25

# Descripció del programa o enunciat de l'exercici:
#Mostra els primers 10 termes de la seqüència de Fibonacci.

# Especificacions de sortida
# Els primers 10 termes de la seqüència de Fibonacci, un per línia.

a, b = 0, 1
cont = 0
while cont < 10:
	print(a)
	temp = b
	prox = a + b
	a = temp
	b = prox
	cont += 1


