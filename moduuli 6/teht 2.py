import random

def noppa_heitetaan (maara):
    return random.randint(1, maara)

maksimi = int(input("Anna nopan sivujen määrä: "))

silmaluku = 0

while silmaluku != maksimi:
    silmaluku = noppa_heitetaan (maksimi)
    print(silmaluku)
