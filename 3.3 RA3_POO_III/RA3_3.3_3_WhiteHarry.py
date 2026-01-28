# Autor: Harry White
# Data: 28-1-26

#Descripció del programa o enunciat de l'exercici:
#Refés el codi perquè la lògica de descompte no estigui codificada dins CarretCompra. Has de: Crear una classe Descompte20 amb un mètode aplicar(total). Fer que CarretCompra rebi l’estratègia de descompte al constructor.

class CarretCompra:
    def __init__(self, total):
        self.total = total

    def calcular_total_amb_descompte(self, descompte):
        return descompte.aplicar(self.total)

class Descompte20:
    def aplicar(self, total):
        descompte = total * 0.2
        return total - descompte

# Exemple d'ús
carret = CarretCompra(1000.0)
descompte_20 = Descompte20()
total_amb_descompte = carret.calcular_total_amb_descompte(descompte_20)
print(f"Total amb descompte: {total_amb_descompte}")
