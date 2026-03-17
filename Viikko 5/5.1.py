import random
nopat = int(input("Anna arpakuutioiden määrä: "))

summa = 0

for n in range(nopat):
    heitot = random.randint(1,6)
    summa += heitot

print(f"Noppien summa on {summa}")


