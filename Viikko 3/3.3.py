sukupuoli = input("Sukupuoli: ")
hemoglobiini = float(input("Hemoglobiiniarvo: "))

if sukupuoli == ("Nainen") and 117 < hemoglobiini < 175:
    print("Hemogobliinisi on normaali")
if sukupuoli == ("Nainen") and 117 > hemoglobiini:
    print("Hemogobliinisi on alhainen")
if sukupuoli == ("Nainen") and hemoglobiini > 175:
    print("Hemogobliinisi on korkea")

if sukupuoli == ("Mies") and 134 < hemoglobiini < 195:
    print("Hemogobliinisi on normaali")
if sukupuoli == ("Mies") and 134 > hemoglobiini:
    print("Hemogobliinisi on alhainen")
if sukupuoli == ("Mies") and hemoglobiini > 195:
    print("Hemogobliinisi on korkea")



