tiedot = {"John": ["John", 30, "Engineer"],"Emily": ["Emily", 25, "Artist"], "Anna": ["Anna", 22, "Student"]}

print(tiedot["John"][0], tiedot["John"][1])
print(tiedot["Emily"][2])

tiedot["Anna"][2] = "Teacher"

tiedot["James"] = ["James", 28, "Writer"]

tiedot["Sophia"] = ["Sophia", 35, "Doctor"]

del tiedot["Emily"]

print(tiedot)