import math
while True:
    luku = float(input("Anna luku: "))
    if luku == 0:
        print("Ohjelma lopetetaan")
        break
    elif luku > 0:
        print(math.sqrt(luku))
    else:
        print("Virheellinen luku")