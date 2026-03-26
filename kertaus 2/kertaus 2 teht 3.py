sanat = ["omena", "autokauppa", "kissa", "tietokone"]

laskuri = 0

for sana in sanat:
    if len(sana) > 5:
        laskuri += 1

print("Yli 5 kirjainta:", laskuri)