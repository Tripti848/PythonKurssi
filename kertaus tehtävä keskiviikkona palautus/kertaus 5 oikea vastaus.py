print("n\------ TERVETULOA KÄYTTÄMÄÄN LASKINTA-----")

while True:
    print("\n Valitse mitä toimintoa haluat käyttää: \n A: Yhteenkasku \n B: Vähennyslasku""\n C: Kertolasku \n D: Jakolasku")

    Valinta = input ("Valintasi (A - D, Q lopettaa): ") upper()

    if Valinta == "Q":
        print("Ohjelma päättyy.")
        break
    a = float(input("Anna eka luku: "))
    b = float (input("Anna toka luku: "))

    if valinta == "A":
       print("Lukujen summa on" , a+b)
    elif valinta == "B":
        print("Lukujen erotus on" , a-b)
    elif valinta == "C":
        print("Lukujen tulo on:" , a*b)
    elif valinta == "D":
        print("Lukujen lukujäännös on" , a/b)
    else:
        print("Virheellinen valinta. ")


