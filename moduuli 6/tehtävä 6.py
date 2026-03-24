import math

def laske_hinta(halkaisija, hinta):
    sade = halkaisija / 2
    pinta_ala = math.pi * sade * sade
    pinta_ala = pinta_ala / 10000
    yksikkohinta = hinta / pinta_ala
    return yksikkohinta

