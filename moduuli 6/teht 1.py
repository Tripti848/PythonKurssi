import random

def noppa_heitetaan ():
    return random.randint(1,6)

silmaluku = 0
while silmaluku != 6:
    silmaluku = noppa_heitetaan()
    print(silmaluku)
