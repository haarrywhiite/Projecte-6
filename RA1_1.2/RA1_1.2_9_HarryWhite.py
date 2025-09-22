# Autor: Harry White
# Fecha: 2024-06-22


# Escriu un programa que demani a l’usuari un número , digui si és positiu, negatiu o zero i
# imprimeixi “Gràcies!” al final

input_num = float(input("Introdueix un número: "))
if input_num > 0:
    print("El número és positiu.")
if input_num < 0:
    print("El número és negatiu.")
if input_num == 0:
    print("El número és zero.")

print("Gràcies!")