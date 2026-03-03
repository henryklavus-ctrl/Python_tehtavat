while True:
    tuumat = float(input("Anna tuumat(negatiivinen luku lopettaa ohjelman): "))

    if tuumat < 0:
        print("ohjelma lopetetaan")
        break

    senttimetrit = tuumat * 2.54
    print(senttimetrit)



