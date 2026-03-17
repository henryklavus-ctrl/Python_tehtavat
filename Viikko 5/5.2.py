luvut = []

luku = (input("Anna luku: "))
while (luku != ""):
    luvut.append(int(luku))
    luku = str(input("Anna seuraava luku tai lopeta painamalla Enter: "))

luvut.sort(reverse=True)

print("Viisi suurinta lukua suuruusjärjestyksessä:")
for luku in luvut[:5]:
    print(luku)