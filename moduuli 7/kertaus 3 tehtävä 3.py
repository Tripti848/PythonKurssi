kirjasto = {"Harry Potter": ["Rowling", 1997, "Fantasia"],"Hobitti": ["Tolkien", 1937, "Fantasia"],"Sinuhe": ["Mika Waltari", 1945, "Romaani"]}

print(kirjasto["Harry Potter"][0])
print(kirjasto["Sinuhe"][2])

kirjasto["Hobitti"][2] = "Seikkailu"

kirjasto["Nälkäpeli"] = ["Suzanne Collins", 2008, "Scifi"]

del kirjasto["Sinuhe"]

print(kirjasto)