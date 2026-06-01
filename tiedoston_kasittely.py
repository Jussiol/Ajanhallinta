import json
def lue_asetukset():
    #avataan asetukset
    with open("asetukset.json", encoding= "utf-8") as j:
        asetukset = json.load(j)
    return asetukset

def kirjoita_asetukset(asetukset, aktiviteetit_jaljella, projektit_jaljella):
    asetukset["aktiviteetit_jaljella"] = aktiviteetit_jaljella
    asetukset["projektit_jaljella"] = projektit_jaljella
    with open("asetukset.json", "w", encoding="utf-8") as j:
        json.dump(asetukset, j, ensure_ascii=False, indent=4)