# Autor: Harry White
# Data: 21-01-26

# Descripció del programa o enunciat de l'exercici:
#1. Compte Bancari Simple Crea una classe CompteBancari amb un atribut privat __saldo. Implementa mètodes públics per: ingressar diners retirar diners consultar el saldo


class CompteBancari:
    def __init__(self,saldo):
        self.__saldo = saldo

    def ingressar_diners(self, quantitat):
        self.__saldo += quantitat

    def retirar_diners(self, quantitat):
        if quantitat <= self.__saldo:
            self.__saldo -= quantitat
        else:
            print("Fons insuficients")

    def consultar_saldo(self):
                print ("El saldo actual és:", self.__saldo)
        
