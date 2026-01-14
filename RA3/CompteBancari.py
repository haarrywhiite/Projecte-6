# Autor: Harry White
# Data: 14-01-26

# Descripció del programa o enunciat de l'exercici:
#Crea una classe CompteBancari Atributs: saldo Mètodes: ingressar, retirar, veure saldo

class compteBancari:
    def __init__(self, saldo):
        self.saldo = saldo

    def ingressar(self, guantitat):
        self.saldo += guantitat

    def retirar(self, quantitat):
        if quantitat <= self.saldo:
            self.saldo -= quantitat
        else:
            print("Fons insuficients")

    def veure_saldo(self):
        print ("El saldo actual és:", self.saldo)