lista = []

luku = int(input("Uusi arvo: "))

while luku != 0:
    lista.append(luku)

    print("Lista nyt:", lista)

    jarjestetty = sorted(lista)
    print("Lista järjestyksessä:", jarjestetty)

    luku = int(input("Uusi arvo: "))

print("Hei hei!")