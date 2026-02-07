Leiviskat = float(input("Leivisköjen määrä: "))
Naulat = float(input("Naulojen määrä: "))
Luodit = float(input("Luotien määrä: "))

Leiviskat_nauloina = 20
Naulat_luoteina = 32
Luodit_grammoina = 13.3

Luodit_yhteensa = (Leiviskat * Leiviskat_nauloina * Naulat_luoteina) + (Naulat * Naulat_luoteina) + Luodit

print("Määrä luoteina:")
print(Luodit_yhteensa)

print("Määrä kilogrammoina:")
print((Luodit_yhteensa * 13.3) / 1000)


