class Empleat:
    def __init__(self, nom):
        self.nom = nom

    def calcular_sou(self):
        pass

class Fixe(Empleat):
    def __init__(self, nom, sou_fixe):
        super().__init__(nom)
        self.sou_fixe = sou_fixe

    def calcular_sou(self):
        return self.sou_fixe

class Autonom(Empleat):
    def __init__(self, nom, hores_treballades, preu_hora):
        super().__init__(nom)
        self.hores_treballades = hores_treballades
        self.preu_hora = preu_hora

    def calcular_sou(self):
        return self.hores_treballades * self.preu_hora
