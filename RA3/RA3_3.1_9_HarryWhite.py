# Autor: Harry White
# Data: 14-01-26

# Descripció del programa o enunciat de l'exercici:
#Crea una classe Llibre Atributs: títol, autor, any Mètode mostrar_info() per imprimir les dades
#Fes una classe Biblioteca que pugui afegir llibres (objectes Llibre) i mostrar-los tots.

from Llibre import Llibre

class Biblioteca:
    def __init__(self):
        self.llibretes = []

    def afegir_llibre(self, llibre):
        self.llibretes.append(llibre)

    def mostrar_llibres(self):
        for llibre in self.llibretes:
            llibre.mostrar_info()

biblioteca = Biblioteca()
llibre1 = Llibre("1984", "George Orwell", 1949)
llibre2 = Llibre("Brave New World", "Aldous Huxley", 1932)
biblioteca.afegir_llibre(llibre1)
biblioteca.afegir_llibre(llibre2)
biblioteca.mostrar_llibres()
