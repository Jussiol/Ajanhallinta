import json
from pathlib import Path

def lue_asetukset():
    #avataan asetukset
    BASE_DIR = Path(__file__).resolve().parent
    ASETUKSET_POLKU = BASE_DIR / "asetukset.json"
    
    with open(ASETUKSET_POLKU, encoding= "utf-8") as j:
        asetukset = json.load(j)
    return asetukset

def kirjoita_asetukset(asetukset, laji, vaihtoehdot, estetyt):
    asetukset[laji]["vaihtoehdot"] = vaihtoehdot
    asetukset[laji]["estetyt"] = estetyt

    with open("asetukset.json", "w", encoding="utf-8") as j:
        json.dump(asetukset, j, ensure_ascii=False, indent=4)