minuts = int(input("Introdueix el nombre de minuts: "))
hores = minuts // 60
minuts_restants = minuts % 60
print(f"{hores} hores i {minuts_restants} minuts")