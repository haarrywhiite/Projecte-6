# Autor: Harry White
# Data: 06-02-26
# Descripció del programa o enunciat de l'exercici
#Exercici 3: Empleats i sous Crea una classe Empleat amb un mètode calcular_sou(). Crea subclasses com Fixe i Autonom, cadascuna amb una fórmula diferent per calcular el sou. Escriu una funció mostrar_sous(llista_empleats) que imprimeixi el sou de cadascun.


class Empleat:
    def calcular_sou(self):
        pass

class Fixe(Empleat):
    def __init__(self, salari_base):
        self.salari_base = salari_base

    def calcular_sou(self):
        return self.salari_base


