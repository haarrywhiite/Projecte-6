
num1 = int(input("Introdudeix la teva nota"))

if num1 < 5:
    print("Suspens")
elif num1 >= 5 and num1 < 6:
    print("Aprovat")
elif num1 >= 6 and num1 < 7:
    print("Bé")
elif num1 >= 7 and num1 < 9:
    print("Notable")
else:
    print("Excel·lent")