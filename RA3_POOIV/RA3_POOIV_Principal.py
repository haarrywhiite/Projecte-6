from Empleat import Empleat, Fixe, Autonom
from Missatger import Missatger, Email, SMS, WhatsApp
from Vehicle import Vehicle, Cotxe, Bicicleta, Barca

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
