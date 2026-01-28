# Autor: Harry White
# Data: 28-1-26

#Descripció del programa o enunciat de l'exercici:
#Refés el següent codi per aconseguir baix acoplament, fent que: Factura no creï la impressora, sinó que la rebi des de fora. Es pugui canviar el tipus d’impressora sense modificar la classe Factura.

class ImpressoraPDF:
    def imprimir(self, contingut):
        print(f"Imprimint en PDF: {contingut}")

class Factura:
    def __init__(self, client, import_total, impressora):
        self.client = client
        self.import_total = import_total
        self.impressora = impressora

    def imprimir_factura(self):
        contingut = f"Factura per a {self.client}, import total: {self.import_total}"
        self.impressora.imprimir(contingut)

# Exemple d'ús
impressora_pdf = ImpressoraPDF()
factura = Factura("Client A", 150.0, impressora_pdf)
factura.imprimir_factura()

