arvo1 = int(input("Arvo 1: "))
arvo2 = int(input("Arvo 2: "))
arvo3 = int(input("Arvo 3: "))

def suurin_arvo(arvo1, arvo2, arvo3):
    if arvo1 > arvo2 and arvo1 > arvo3:
        return arvo1
    elif arvo2 > arvo1 and arvo2 > arvo3:
        return arvo2
    else:
        return arvo3

suurin = suurin_arvo(arvo1, arvo2, arvo3)

print(f"Suurin arvo {suurin}")

