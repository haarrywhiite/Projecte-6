frase = input("Introdueix una frase: ")
vocals = "aeiouAEIOU"
num_vocals = 0
for char in frase:
    if char in vocals:
        num_vocals += 1
print("El nombre de vocals és:", num_vocals)