# Autor: Harry White
# Data: 21-01-26

# Descripció del programa o enunciat de l'exercici:
#2. Estudiant amb nota protegida Crea una classe Estudiant amb un atribut protegit _nota. Afegeix mètodes per: llegir la nota modificar la nota només si és entre 0 i 10

class Estudiant:
    def __init__(self, nota):
        self._nota = nota

    def llegir_nota(self):
        return self._nota
    
    def modificar_nota(self, nota_nova):
        if 0 <= nota_nova  <= 10:
            self._nota = nota_nova
    




