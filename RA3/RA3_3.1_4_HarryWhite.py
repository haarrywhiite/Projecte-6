# Autor: Harry White
# Data: 14-01-26

# Descripció del programa o enunciat de l'exercici:
#Crea una classe Producte Atributs: nom, preu Mètode: aplicar un descompte (donat com a percentatge)
#Fes una funció que rebi una llista de productes i apliqui un descompte del 10% a tots.

from Producte import Producte

def aplicar_descompte(productes, percentatge):
    for producte in productes:
        producte.aplicar_descompte(percentatge)

producte1 = Producte("Monitor", 100)
producte2 = Producte("Teclat", 50)

llista_productes = [producte1, producte2]
aplicar_descompte(llista_productes, 10)

for producte in llista_productes:
    print(f"Producte: {producte.nom}, Preu després del descompte: {producte.preu}€")

