# Autor: Harry White
# Data: 14-01-26

# Descripció del programa o enunciat de l'exercici:
#Crea una classe CotxeAtributs: marca, model, any Mètode per mostrar la informació del cotxe

class Cotxe:
    def __init__(self, marca, model, any):
        self.marcar = marca
        self.model = model
        self.any = any
    
    def mostrar_info(self):
        print(f"Marca: {self.marcar}, Model: {self.model}, Any: {self.any}")

