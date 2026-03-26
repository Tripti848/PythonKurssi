def suurin_arvo(a, b, c):
    suurin = a

    if b > suurin:
        suurin = b
    if c > suurin:
        suurin = c

    return suurin

x = int(input("Anna luku: "))
y = int(input("Anna luku: "))
z = int(input("Anna luku: "))

tulos = suurin_arvo(x, y, z)

print("Suurin on:", tulos)