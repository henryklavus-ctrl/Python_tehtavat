import math

luku = int(input("Anna kokonaisluku: "))

if luku < 2:
    print("Luku ei ole alkuluku")

for i in range (2,int(math.sqrt(luku))):
    if luku % i == 0:
        print("Luku ei ole alkuluku")

else:
    print("Luku on alkuluku")



