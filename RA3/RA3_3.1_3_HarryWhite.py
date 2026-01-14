# Autor: Harry White
# Data: 14-01-26

# Descripció del programa o enunciat de l'exercici:
#Crea una classe Persona Atributs: nom, edat Mètode presentar_se() que imprimeixi “Hola, soc X i tinc Y anys”
#Fes una funció que rebi una llista de persones i imprimeixi només les que tenen més de 30 anys.
from Persona import Persona

def filtrar_persones_meses_de_30(persones):
    for persona in persones:
        if persona.edat > 30:
            persona.presentar_se()

persona1 = Persona("Anna", 25)
persona2 = Persona("Bernat", 35)    
persona3 = Persona("Carla", 40)

llista_persones = [persona1, persona2, persona3]
filtrar_persones_meses_de_30(llista_persones)


