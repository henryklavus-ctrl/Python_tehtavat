tuntipalkka = float(input("Syötä tuntipalkka: "))
tunnit = float(input("Syötä tunnit: "))
viikonpaiva = input("Syötä viikonpaiva: ")
palkka = tunnit * tuntipalkka
if viikonpaiva == "sunnuntai":
    print("Päiväpalkka: ")
    print(palkka * 2)
else:
    print("Päiväpalkka: ")
    print(palkka)