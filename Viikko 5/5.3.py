import math

luku = int(input("Anna kokonaisluku: "))

if luku < 2:
    print("Luku ei ole kokonaisluku")

for i in range (2,int(math.sqrt(luku))):
    if luku % i == 0:
        print("Luku ei ole kokonaisluku")

else:
    print("Luku on kokonaisluku")



