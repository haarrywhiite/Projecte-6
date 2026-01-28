# Autor: Harry White
# Data: 28-1-26

#Descripció del programa o enunciat de l'exercici:
#Refés el codi perquè la classe Comanda no depengui d’una implementació concreta del notificador. El notificador ha de ser passat com a dependència al constructor.

class EmailNotificador:
    def notificar(self, missatge):
        print(f"Enviant email: {missatge}")

class Comanda:
    def __init__(self,client, notificador):
        self.client = client
        self.notificador = notificador

    def confirmar(self):
        print(f"Comanda confirmada per a {self.client}")
        self.notificador.notificar(f"La comanda per a {self.client} ha estat confirmada.")

# Exemple d'ús
notificador_email = EmailNotificador()
comanda = Comanda("Client B", notificador_email)
comanda.confirmar()
