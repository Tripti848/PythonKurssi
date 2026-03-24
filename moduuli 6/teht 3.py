def muunna_litroiksi(gallonat):
    return gallonat * 3.785

maara = float(input("Anna gallonamäärä: "))

while maara >= 0:
    litrat = muunna_litroiksi(maara)
    print (litrat)
    maara = float (input("Anna gallomäärä: ")
