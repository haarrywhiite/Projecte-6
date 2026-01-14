# Autor: Harry White
# Data: 14-01-26

# Descripció del programa o enunciat de l'exercici:
#Crea una classe Llibre Atributs: títol, autor, any Mètode mostrar_info() per imprimir les dades

class Llibre:
    def __init__(self, titol, autor, any):
        self.titol = titol
        self.autor = autor
        self.any = any

    def mostrar_info(self):
        print(f"Títol: {self.titol}, Autor: {self.autor}, Any: {self.any}")

        