# Autor: Harry White
# Data: 28-1-26
#Descripció del programa o enunciat de l'exercici
#Exercici 3: Persones i treballadors Crea una classe Persona amb els atributs nom i edat, i un mètode saludar() que imprimeixi "Hola, sóc {nom}". Crea una subclasse Treballador que afegeixi un atribut feina i un mètode mostrar_feina() que imprimeixi "Treballo com a {feina}". Crea una instància de Treballador i prova els mètodes.

class Persona:
    def __init__(self, nom, edat):
        self.nom = nom
        self.edat = edat

    def saludar(self):
        print(f"Hola, sóc {self.nom}")

class Treballador(Persona):
    def __init__(self, nom, edat, feina):
        super().__init__(nom, edat)
        self.feina = feina

    def mostrar_feina(self):
        print(f"Treballo com a {self.feina}")