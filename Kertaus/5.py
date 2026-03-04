while True:
    laskutoimitus = input("Valitse laskutoimitus: ")
    luku1 = float(input("Syötä luku 1: "))
    luku2 = float(input("Syötä luku 2: "))

    if laskutoimitus == "Yhteenlasku":
        print(luku1 + luku2)
        print("Syötä Q lopettaaksesi: ")
    elif laskutoimitus == "Vähennyslasku":
        print(luku1 - luku2)
        print("Syötä Q lopettaaksesi: ")
    elif laskutoimitus == "Kertolasku":
        print(luku1 * luku2)
        print("Syötä Q lopettaaksesi: ")
    elif laskutoimitus == "Jakolasku":
        print(luku1 / luku2)
        print("Syötä Q lopettaaksesi: ")
    elif laskutoimitus == "Q":
        print("Ohjelma lopetetaan")
        break


