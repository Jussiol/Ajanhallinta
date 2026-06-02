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
    #avataan asetukset

    asetukset[laji]["vaihtoehdot"] = vaihtoehdot
    asetukset[laji]["estetyt"] = estetyt

    with open(base_dir()  / "asetukset.json", "w", encoding="utf-8") as j:
        json.dump(asetukset, j, ensure_ascii=False, indent=4)

def tilasto_init(asetukset):
    tilasto = {}
    for item in asetukset["aktiviteetit"]["kaikki"]:
        tilasto[item] = 0
    with open(base_dir()  / "tilasto.json", "w", encoding="utf-8") as j:
        json.dump(tilasto, j, ensure_ascii=False, indent=4)

def tilastoon(aktiviteetti):
    #avataan asetukset
    with open(base_dir() / "tilasto.json", encoding= "utf-8") as j:
        tilasto = json.load(j)
    tilasto[aktiviteetti] += 1
    with open(base_dir()  / "tilasto.json", "w", encoding="utf-8") as j:
        json.dump(tilasto, j, ensure_ascii=False, indent=4)

def tulosta_tilasto():
        
    #avataan asetukset
    with open(base_dir() / "tilasto.json", encoding= "utf-8") as j:
        tilasto = json.load(j)
    print()
    print("Tilasto:")
    for avain, arvo in tilasto.items():
        print("   -", avain, arvo)
    print()