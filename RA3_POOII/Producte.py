# Autor: Harry White
# Data: 21-01-26

# Descripció del programa o enunciat de l'exercici:
#6. Producte amb preu controlat Classe Producte amb atributs: nom (públic) __preu (privat) Mètodes per obtenir i modificar el preu (només si > 0)

class Producte:
    def __init__(self, nom, preu):
        self.nom = nom
        self.__preu = 0
        self.modificar_preu(preu)  

    def obtenir_preu(self):
        return self.__preu

    def modificar_preu(self, nou_preu):
        if nou_preu > 0:
            self.__preu = nou_preu
        else:
            print("Error: El preu ha de ser major que 0.")