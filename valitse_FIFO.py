from random import choice
from tiedoston_kasittely import kirjoita_asetukset

def laske_eston_pituus(maara):
    if maara <= 1:
        return 0
    if maara <= 3:
        return 1
    if maara <= 6:
        return 2
    return 3

def valinta(asetukset, laji):
    kaikki = asetukset[laji]["kaikki"]
    vaihtoehdot = asetukset[laji]["vaihtoehdot"]
    estetyt = asetukset[laji]["estetyt"]

    #siivotaan listat siltä varalta, että "kaikki"-listaa on muutettu
    vaihtoehdot = [x for x in vaihtoehdot if x in kaikki]
    estetyt = [x for x in estetyt if x in kaikki]

    estopituus =laske_eston_pituus(len(kaikki))
    if not vaihtoehdot:
        vaihtoehdot = list(kaikki)
    aktiviteetti = choice(vaihtoehdot)
    estetyt.append(aktiviteetti)
    vaihtoehdot.remove(aktiviteetti)
    
    if len(estetyt) > estopituus:
        vaihtoehdot.append(estetyt.pop(0))
        
    kirjoita_asetukset(asetukset, laji, vaihtoehdot, estetyt)

    return aktiviteetti