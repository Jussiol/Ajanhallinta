import random
from tiedoston_kasittely import *

asetukset = lue_asetukset()

aktiviteetit = asetukset["aktiviteetit"]
aktiviteetit_jaljella = asetukset["aktiviteetit_jaljella"]
projektit = asetukset["projektit"]
projektit_jaljella = asetukset["projektit_jaljella"]

print("Enter jos valmis, 0 lopettaa")
while True:
    #alustus
    if not aktiviteetit_jaljella:
        aktiviteetit_jaljella = aktiviteetit.copy()
    if not projektit_jaljella:
        projektit_jaljella = projektit.copy()

    #Valitaan aktiviteetti
    aktiviteetti = random.choice(aktiviteetit_jaljella)
    aktiviteetit_jaljella.remove(aktiviteetti)
    if aktiviteetti == "projekti":
        aktiviteetti = random.choice(projektit_jaljella)
        projektit_jaljella.remove(aktiviteetti)
            
    print(f"{aktiviteetti}")
    kirjoita_asetukset(asetukset, aktiviteetit_jaljella, projektit_jaljella)

    done = input("Done? ")
    if done == "0":
        break
