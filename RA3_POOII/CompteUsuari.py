# Autor: Harry White
# Data: 23-01-26

# Descripció del programa o enunciat de l'exercici:
#10. Email d’un usuari Classe CompteUsuari amb atribut privat __email El setter valida que l’email contingui “@” i “.” El getter retorna l’email actual

class CompteUsuari:
    def __init__(self, nom_usuari, contrasenya, email):
        self.nom_usuari = nom_usuari
        self.__contrasenya = contrasenya
        self.__email = None
        self.email = email  

    def verificar_contrasenya(self, contrasenya):
        return self.__contrasenya == contrasenya

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, nou_email):
        if "@" in nou_email and "." in nou_email:
            self.__email = nou_email
        else:
            print("Email invàlid. Ha de contenir '@' i '.'")
