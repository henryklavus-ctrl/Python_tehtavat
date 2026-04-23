sanakirja = {"Matti": ["Matti", 7, "historia"],
             "Saara": ["Saara", 9, "matematiikka"],
             "Antti": ["Antti", 8, "liikunta"],
             "Johanna": ["Johanna", 8, "englanti"]}


print(f"Henkilön {sanakirja['Antti'][0]} lempiaine koulussa on {sanakirja["Antti"][2]}")
print(f"Henkilön {sanakirja['Saara'][0]} vuosiluokka on {sanakirja["Saara"][1]}")


sanakirja["Johanna"][2] = "ruotsi"
sanakirja["Markku"] = ["Markku", 7, "biologia"]
del sanakirja["Saara"]

print(sanakirja)