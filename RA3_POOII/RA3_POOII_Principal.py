#1. Compte Bancari Simple

from CompteBancari import CompteBancari

compte = CompteBancari(1000)

compte.ingressar_diners(500)
compte.consultar_saldo()

compte.retirar_diners(300)
compte.consultar_saldo()

compte.retirar_diners(1500)
compte.consultar_saldo()

#2. Estudiant amb nota protegida

from Estudiant import Estudiant

estudiant = Estudiant(7.5)
print("Nota inicial:", estudiant.llegir_nota())
estudiant.modificar_nota(9.0)
print("Nota modificada:", estudiant.llegir_nota())


#3. Termòstat

from Termostat import Termostat

termostat = Termostat(22)
print("Temperatura inicial:", termostat.temperatura)
termostat.temperatura = 25
print("Temperatura modificada:", termostat.temperatura)


#4. Contrasenya segura

from Contrasenya_segura import Usuari

usuari = Usuari("inicial88")

print("Verificar contrasenya (correcta):", usuari.verificar_contrasenya("inicial88"))

usuari.canviar_contrasenya("curta") 

usuari.canviar_contrasenya("contrasenyaSegura123")

print("Verificar contrasenya (després canvi):", usuari.verificar_contrasenya("contrasenyaSegura123"))

#5. Sensor amb valors limitats

from Sensor import Sensor

sensor = Sensor(50)
print("Valor inicial del sensor:", sensor.valor)
sensor.valor = 80
print("Valor modificat del sensor:", sensor.valor)


#6. Producte amb preu controlat

from Producte import Producte

producte = Producte("Llibre", 25.0)
print("Preu inicial del producte:", producte.obtenir_preu())
producte.modificar_preu(30.0)
print("Preu modificat del producte:", producte.obtenir_preu())
producte.modificar_preu(-5.0)
print("Preu després d'intentar modificar amb valor negatiu:", producte.obtenir_preu())

#7 Temps en hores

from Temps import Rellotge

rellotge = Rellotge(10)
print("Hores inicials:", rellotge.mostrar_hores())
rellotge.hores = 15
print("Hores modificades:", rellotge.mostrar_hores())
rellotge.hores = 25
print("Hores després d'intentar modificar amb valor invàlid:", rellotge.mostrar_hores())

#8 Alumne amb edat controlada

from Alumne import Alumne

alumne = Alumne(20)
print("Edat inicial de l'alumne:", alumne.edat)
alumne.edat = 22
print("Edat modificada de l'alumne:", alumne.edat)
alumne.edat = -5
print("Edat després d'intentar modificar amb valor negatiu:", alumne.edat)

#9 Gestor de puntuació

from Joc import Joc
joc = Joc()
joc.sumar_punts(10)
joc.sumar_punts(20)
print("Puntuació actual:", joc.obtenir_puntuacio())
joc.reiniciar_puntuacio()
print("Puntuació després de reiniciar:", joc.obtenir_puntuacio())

#10 Email d’un usuari

from CompteUsuari import CompteUsuari

usuari = CompteUsuari("usuari1", "contrasenya123", "usuari1@example.com")
print("Email inicial:", usuari.email)
usuari.email = "nou_email_incorrecte"
print("Email després d'intentar assignar un email invàlid:", usuari.email)
usuari.email = "nou_email@example.com"
print("Email després d'assignar un email vàlid:", usuari.email)
