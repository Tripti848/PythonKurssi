def laske_summa(lista):
    summa = 0
    for luku in lista:
        summa = summa + luku
    return summa
luvut = [2, 5, 7, 3]
tulos = laske_summa(luvut)
print("Summa on", tulos)