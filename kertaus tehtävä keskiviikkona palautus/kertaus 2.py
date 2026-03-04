
tuntipalkka = int(input("mikä on sinun tuntipalkasi? "))
tunnit = int(input("tehdyt tunnit? "))
paiva= input("Viikonpäivä? ")
if paiva =="sunnuntai":

    paivapalkka = tuntipalkka * tunnit * 2


else:
    paivapalkka = tuntipalkka * tunnit
print("paiväpalkka ", paivapalkka, "euroa")


