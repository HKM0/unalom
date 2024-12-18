import random
import itertools

#****************************************************************************************
# Használat: Add meg a résztvevőket és a NEM párosítható személyeket a resztvevok és nem_parosithatok listákban.
# Példa: resztvevok = ['Anna', 'Béla', 'Cecília', 'Dénes', 'Erika'] 
#        nem_parosithatok = [('Anna', 'Béla'), ('Cecília', 'Dénes')]
#
# vagyis Anna nem párosítható Bélával, Cecília nem párosítható Dénessel.
#****************************************************************************************

resztvevok = ['Anna', 'Béla', 'Cecília', 'Dénes', 'Erika'] 
nem_parosithatok = [('Anna', 'Béla'), ('Cecília', 'Dénes')]

def sorsolas(resztvevok, nem_parosithatok):
    kombinaciok_szama = 0
    valid_parok = []
    
    for permutacio in itertools.permutations(resztvevok):
        parok = []
        valid = True
        for i in range(len(resztvevok)):
            resztvevo = resztvevok[i]
            par = permutacio[i]
            if resztvevo == par or (resztvevo, par) in nem_parosithatok or (par, resztvevo) in nem_parosithatok:
                valid = False
                break
            parok.append((resztvevo, par))
        if valid:
            valid_parok.append(parok)
            kombinaciok_szama += 1
    
    return valid_parok, kombinaciok_szama

valid_parok, kombinaciok_szama = sorsolas(resztvevok, nem_parosithatok)


random.shuffle(valid_parok) # véletlen sorrendbe rendezi a permutációkat és vissza adja az elsőt.
for par in valid_parok[0]:
    print(f"{par[0]} -> {par[1]}")

print(f"\nLehetséges kombinációk száma a megadott feltételekkel: {kombinaciok_szama}")