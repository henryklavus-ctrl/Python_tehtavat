kaupungit = []

kaupunki = input("Anna ensimmäinen kaupunki: ")
while kaupunki != "":
    kaupungit.append(kaupunki)
    kaupunki = input("Anna seuraava kaupunki: ")

for kaupunki in kaupungit:
    print(f"{kaupunki}")