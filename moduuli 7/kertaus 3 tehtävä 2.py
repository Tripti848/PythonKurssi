oppilaat = {"Ali": ["Ali", 7, "Matikka"],"Sara": ["Sara", 8, "Englanti"],"Mira": ["Mira", 9, "Biologia"]}
print(oppilaat["Ali"][1])
print(oppilaat["Sara"][2])

oppilaat["Mira"][2] = "Historia"

oppilaat["Omar"] = ["Omar", 7, "Liikunta"]

del oppilaat["Ali"]

print(oppilaat)