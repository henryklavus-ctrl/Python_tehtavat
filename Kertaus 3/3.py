kirjasto = {"Taru sormusten herrasta": ["J.R.R Tolkien", 1954, "Fantasia"],
            "Leijat Helsingin yllä": ["Kjell Westö", 1996, "Fiktio"],
            "Häräntappoase": ["Anna-Leena Härkönen", 1984, "Nuortenkirjallisuus"],
            "Inferno": ["Dan Brown", 2013, "Dekkari"],}


print(f"Taru sormusten herrasta kirjoittaja on {kirjasto['Taru sormusten herrasta'][0]}")
print(f"Taru Häräntappoase kuuluu {kirjasto['Häräntappoase'][2]} genreen")

kirjasto["Inferno"][2] = "Mysteeri"
kirjasto["Pikku prinssi"] = ["Antoine de Saint-Exupery", 1943, "Pienoisromaani"]

del kirjasto["Leijat Helsingin yllä"]

print(kirjasto)
