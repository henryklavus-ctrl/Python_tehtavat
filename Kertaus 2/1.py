numero = int(input("Anna luku: "))

print(f"Kertotaulu luvulle {numero}")

for i in range (1,11):
    kertotaulu = numero * i
    print(f"{numero} * {i} = {kertotaulu} ")
