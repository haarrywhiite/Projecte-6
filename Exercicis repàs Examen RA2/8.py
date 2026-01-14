frase = input("Introdueix una frase: ")
majuscules = ""
for char in frase:
    if char.isupper():
        majuscules += char
        print (majuscules)