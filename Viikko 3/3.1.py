kuha = float(input("Anna kuhan pituus: "))

if kuha < 37:
    puuttuva = 37 - kuha
    print(f"Kuha on alamittainen, laske se takaisin järveen")
    print(f"Sen pituudesta puuttuu {puuttuva} senttimetriä")

