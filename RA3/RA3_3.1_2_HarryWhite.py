# Autor: Harry White
# Data: 14-01-26

# Descripció del programa o enunciat de l'exercici:
#Crea una classe Rectangle Atributs: amplada, alçadaMètodes: area() i perimetre()
#Crea 3 rectangles amb diferents mides. Mostra l’àrea de cadascun.

from Rectangle import Rectangle

rectangle1 = Rectangle(4, 5)
rectangle2 = Rectangle(6, 7)
rectangle3 = Rectangle(8, 9)

print(f"Rectangle 1 - Area: {rectangle1.area()}, Perimetre: {rectangle1.perimetre()}")
print(f"Rectangle 2 - Area: {rectangle2.area()}, Perimetre: {rectangle2.perimetre()}")
print(f"Rectangle 3 - Area: {rectangle3.area()}, Perimetre: {rectangle3.perimetre()}")  

