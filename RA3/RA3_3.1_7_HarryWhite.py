# Autor: Harry White
# Data: 14-01-26

# Descripció del programa o enunciat de l'exercici:
#Crea una classe Cercle Atribut: radi Mètodes: calcular àrea i perímetre
#Crea un llistat de cercles i mostra quins tenen àrea superior a 50

from Cercle import Cercle

cercles = [Cercle(4), Cercle(5), Cercle(6), Cercle(7), Cercle(8)]

for cercle in cercles:
    area = cercle.calcular_area()
    if area > 50:
        print(f"Cercle amb radi {cercle.radi} té àrea superior a 50: {area}")

