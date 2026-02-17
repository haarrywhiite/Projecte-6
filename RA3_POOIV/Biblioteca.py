# Autor: Harry White
# Data: 28-01-26
# Descripció del programa o enunciat de l'exercici
#Exercici 5: Biblioteca Crea una classe Llibre amb atributs titol i autor, i un mètode mostrar_info(). Crea dues subclasses: LlibrePaper amb atribut n_pàgines LlibreDigital amb atribut format (PDF, ePub...) Totes dues han de sobreescriure mostrar_info() per mostrar la seva informació específica.

class Llibre:
    def __init__(self, titol, autor):
        self.titol = titol
        self.autor = autor

    def mostrar_info(self):
        return f"Títol: {self.titol}, Autor: {self.autor}"
    
class LlibrePaper(Llibre):
    def __init__(self, titol, autor, n_pagines):
        super().__init__(titol, autor)
        self.n_pagines = n_pagines

    def mostrar_info(self):
        info_basiсa = super().mostrar_info()
        return f"{info_basiсa}, Nombre de pàgines: {self.n_pagines}"
    
class LlibreDigital(Llibre):
    def __init__(self, titol, autor, format):
        super().__init__(titol, autor)
        self.format = format

    def mostrar_info(self):
        info_basiсa = super().mostrar_info()
        return f"{info_basiсa}, Format: {self.format}"
