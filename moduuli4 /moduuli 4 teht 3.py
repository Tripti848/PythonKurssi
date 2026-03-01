pienin = None
suurin = None

while True:
    s = input("Anna luku (tyhjä lopettaa): ")

    if s == "":
        break

    luku = float(s)

    if pienin is None:
        pienin = luku
        suurin = luku
    else:
        if luku < pienin:
            pienin = luku
        if luku > suurin:
            suurin = luku

print("Pienin:", pienin)
print("Suurin:", suurin)