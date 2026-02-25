pituus = int(input("Anna kuhan pituus senttimetreinä: "))

if pituus < 37:
    puuttuu = 37 - pituus
    print("Kuha on alamittainen. Laske kuha takaisin järveen.")
    print("Puuttuu", puuttuu, "cm alimmasta sallitusta pyyntimitasta.")
else:
    print("Kuha on sallittua mittaa.")