import random
while True:
    arvaus = int(input("Anna arvaus: "))
    luku = random.randint(1,10)
    if (arvaus == luku):
        print("Oikein")
        break
    elif (arvaus > luku):
        print("Liian suuri luku")
    elif (arvaus<luku):
        print("Liian pieni luku")
