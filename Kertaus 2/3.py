sanat = []

while True:
    sana = input("Anna sana: ")
    sanat.append(sana)
    if sana == "":
        break

kirjaimet = 0

for sana in sanat:

    if len(sana) > 5:
        kirjaimet += 1

print(f"Sanat listassa: {sanat}")
print(f"Sanat, joissa yli 5 kirjainta: {kirjaimet}")