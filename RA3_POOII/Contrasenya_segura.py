# Autor: Harry White
# Data: 21-01-26

# Descripció del programa o enunciat de l'exercici:
# 4. Contrasenya segura Classe Usuari amb atribut privat __contrasenya. Implementa: mètode canviar_contrasenya() (amb validació: mínim 8 caràcters) mètode verificar_contrasenya(clau)

class Usuari:
    def __init__(self, contrasenya):
        self.__contrasenya = contrasenya

    def canviar_contrasenya(self, nova_contrasenya):
        if len(nova_contrasenya) >= 8:
            self.__contrasenya = nova_contrasenya
            print("Contrasenya canviada correctament.")
        else:
            print("Error: La contrasenya ha de tenir almenys 8 caràcters.")

    def verificar_contrasenya(self, clau):
        return self.__contrasenya == clau