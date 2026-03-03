import random

luku = random.randint(1, 10)

while True:
    arvaus = int(input("Anna arvaus: "))


    if (arvaus == luku):
        print("Oikein")
        break

    elif (arvaus > luku):
        print("Liian suuri luku")

    elif (arvaus < luku):
        print("Liian pieni luku")
