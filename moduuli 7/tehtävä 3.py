lentoasemat = {}

while True:
    print()
    print("1 = uusi lentoasema")
    print("2 = hae lentoasema")
    print("3 = lopeta")

    valinta = input("Valinta: ")

    if valinta == "1":
        koodi = input("Anna ICAO-koodi: ")
        nimi = input("Anna lentoaseman nimi: ")

        lentoasemat[koodi] = nimi

    elif valinta == "2":
        koodi = input("Anna ICAO-koodi: ")

        if koodi in lentoasemat:
            print(lentoasemat[koodi])

        else:
            print("Ei löytynyt")

    elif valinta == "3":
        break