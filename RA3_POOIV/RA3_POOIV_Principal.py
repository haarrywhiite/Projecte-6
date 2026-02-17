# Autor: Harry White
# Data: 28-1-26

#HERÈNCIA
#EX1
from Animals import Animal, Gos, Gat

a = Animal()
g = Gos()
c = Gat()

a.parlar()
g.parlar()
c.parlar()

#EX2
from Vehicles import Cotxe

marca_cotxe = "Toyota"
cotxe = Cotxe(marca_cotxe)
cotxe.arrencar()
cotxe.tocar_claxon()

#EX3
from Persones_treballadors import Persona, Treballador

persona = Persona("Harry", 23)
persona.saludar()
treballador = Treballador("Gerard", 22, "Programador")
treballador.saludar()
treballador.mostrar_feina()

#EX4
from Figura_geomètrica import Figura, Quadrat, Cercle
figura = Figura()
figura.area()
quadrat = Quadrat(4)
print(f"Àrea del quadrat: {quadrat.area()}")
cercle = Cercle(3)
print(f"Àrea del cercle: {cercle.area()}")

#EX5
from Biblioteca import LlibrePaper, LlibreDigital
llibre_paper = LlibrePaper("El Quijote", "Miguel de Cervantes", 863)
llibre_digital = LlibreDigital("1984", "George Orwell", "ePub")
print(llibre_paper.mostrar_info())
print(llibre_digital.mostrar_info())

from Empleat import Empleat, Fixe, Autonom
from Missatger import Missatger, Email, SMS, WhatsApp
from Vehicle import Vehicle, Cotxe, Bicicleta, Barca

#POLIMORFISME
#EX1
from Sons_animals import Animal, Gat, Vaca, reproduir_soroll

gat = Gat()
vaca = Vaca()
reproduir_soroll(gat)
reproduir_soroll(vaca)

#EX2

from Dibuixar_Figures import Figura, Cercle, Quadrat, Triangle

figures = [Figura(), Cercle(), Quadrat(), Triangle()]
for f in figures:
    f.dibuixar()



# Exercici 3
def mostrar_sous(llista_empleats):
    print("--- Exercici 3: Empleats i Sous ---")
    for empleat in llista_empleats:
        print(f"El sou de {empleat.nom} és: {empleat.calcular_sou()}")
    print()

# Exercici 4
def enviar_missatges(missatgers, missatge):
    print("--- Exercici 4: Missatgeria ---")
    for msgr in missatgers:
        msgr.enviar(missatge)
    print()

# Exercici 5
def moure_vehicles(vehicles):
    print("--- Exercici 5: Transport ---")
    for v in vehicles:
        v.moure()
    print()

if __name__ == "__main__":
    # Test Exercici 3
    empleats = [
        Fixe("Joan", 1500),
        Autonom("Laura", 40, 20),
        Fixe("Pere", 1800)
    ]
    mostrar_sous(empleats)

    # Test Exercici 4
    missatgers = [
        Email(),
        SMS(),
        WhatsApp()
    ]
    enviar_missatges(missatgers, "Hola, això és una prova de polimorfisme!")

    # Test Exercici 5
    vehicles = [
        Cotxe(),
        Bicicleta(),
        Barca()
    ]
    moure_vehicles(vehicles)
