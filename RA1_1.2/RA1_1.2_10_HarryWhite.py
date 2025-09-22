# Autor: Harry White
# Fecha: 2024-06-22


# Crea una petita calculadora que demani dos números i faci les operacions bàsiques (+, -,
# *, /).

input_num1 = float(input("Introdueix el primer número: "))
input_num2 = float(input("Introdueix el segon número: "))
suma = input_num1 + input_num2
resta = input_num1 - input_num2
multiplicacio = input_num1 * input_num2
if input_num2 != 0:
    divisio = input_num1 / input_num2
else:
    divisio = "No es pot dividir per zero"
print("Suma:", suma)
print("Resta:", resta)
print("Multiplicació:", multiplicacio)
print("Divisió:", divisio)