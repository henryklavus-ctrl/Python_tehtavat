vuosiluku = int(input("Vuosiluku: "))

if (vuosiluku % 4 == 0):
    print("Karkausvuosi")
elif (vuosiluku % 100) and (vuosiluku % 400) == 0:
    print ("Karkausvuosi")
else:
    print("Ei ole karkausvuosi")