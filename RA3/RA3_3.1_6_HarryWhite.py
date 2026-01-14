# Autor: Harry White
# Data: 14-01-26

# Descripció del programa o enunciat de l'exercici:
#Crea una classe CompteBancari Atributs: saldo Mètodes: ingressar, retirar, veure saldo
#Crea un compte bancari i simula 3 operacions: ingrés, retirada vàlida i retirada superior al saldo.

from CompteBancari import compteBancari

compte = compteBancari(1000)

compte.ingressar(500)
compte.veure_saldo()

compte.retirar(300)
compte.veure_saldo()

compte.retirar(1500)
compte.veure_saldo()

