arvot = []

while True:
    arvo = int(input("Uusi arvo: "))

    if arvo == 0:
        print("Heippa ! ")
        break

    arvot.append(arvo)

    print(f"Lista nyt: {arvo}")

    print(f"Lista järjestyksessä: {sorted(arvot)}")




