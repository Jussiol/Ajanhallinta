import json
from pathlib import Path

def base_dir():
    polku = Path(__file__).resolve().parent
    return polku

def lue_asetukset():
    #avataan asetukset
    with open(base_dir() / "asetukset.json", encoding= "utf-8") as j:
        asetukset = json.load(j)
    
    return asetukset

def kirjoita_asetukset(asetukset, laji, vaihtoehdot, estetyt):

    asetukset[laji]["vaihtoehdot"] = vaihtoehdot
    asetukset[laji]["estetyt"] = estetyt
    
    #avataan asetukset
    with open(base_dir()  / "asetukset.json", "w", encoding="utf-8") as j:
        json.dump(asetukset, j, ensure_ascii=False, indent=4)

def tilasto_init(asetukset):

    tilasto = {
        "aktiviteetit": {},
        "projektit": {}
    }

    for item in asetukset["aktiviteetit"]["kaikki"]:
        tilasto["aktiviteetit"][item] = 0

    for item in asetukset["projektit"]["kaikki"]:
        tilasto["projektit"][item] = 0

    with open(base_dir() / "tilasto.json", "w", encoding="utf-8") as j:
        json.dump(tilasto, j, ensure_ascii=False, indent=4)

def paivita_osio(tilasto_osio, asetukset_lista):

    # lisätään puuttuvat
    for item in asetukset_lista:

        if item not in tilasto_osio:
            tilasto_osio[item] = 0

    # poistetaan ylimääräiset
    poistettavat = []

    for item in tilasto_osio:

        if item not in asetukset_lista:
            poistettavat.append(item)

    for item in poistettavat:
        del tilasto_osio[item]

def tilasto_paivita(tilasto, asetukset):

    paivita_osio(
        tilasto["aktiviteetit"],
        asetukset["aktiviteetit"]["kaikki"]
    )

    paivita_osio(
        tilasto["projektit"],
        asetukset["projektit"]["kaikki"]
    )

    with open(base_dir() / "tilasto.json", "w", encoding="utf-8") as j:
        json.dump(tilasto, j, ensure_ascii=False, indent=4)


def tilastoon(laji, aktiviteetti, asetukset):
    
    #avataan asetukset
    with open(base_dir() / "tilasto.json", encoding= "utf-8") as j:
        tilasto = json.load(j)
    
    tilasto_paivita(tilasto, asetukset)
    tilasto[laji][aktiviteetti] += 1
    
    with open(base_dir()  / "tilasto.json", "w", encoding="utf-8") as j:
        json.dump(tilasto, j, ensure_ascii=False, indent=4)

def tulosta_tilasto():
        
    #avataan asetukset
    with open(base_dir() / "tilasto.json", encoding= "utf-8") as j:
        tilasto = json.load(j)

    print()
    print("Tilasto:")
    print("Aktiviteetit         | Projektit")
    print("-" * 40)

    aktiviteetit = list(tilasto["aktiviteetit"].items())
    projektit = list(tilasto["projektit"].items())

    pituus = max(len(aktiviteetit), len(projektit))

    for i in range(pituus):

        if i < len(aktiviteetit):
            a_nimi, a_arvo = aktiviteetit[i]
            vasen = f"{a_nimi} {a_arvo}"
        else:
            vasen = ""

        if i < len(projektit):
            p_nimi, p_arvo = projektit[i]
            oikea = f"{p_nimi} {p_arvo}"
        else:
            oikea = ""

        print(f"{vasen:<20} | {oikea}")

    print()

def paiva_akt():
    #avataan asetukset
    with open(base_dir() / "tilasto.json", encoding= "utf-8") as j:
        tilasto = json.load(j)