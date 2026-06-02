from tiedoston_kasittely import lue_asetukset 
from tiedoston_kasittely import tilasto_init, tilasto_paivita
from tiedoston_kasittely import tilastoon, tulosta_tilasto
from valitse_FIFO import valinta

print("Enter jos valmis, 0 lopettaa")
print("t = tilasto, r = nollaa tilasto")

while True:
    asetukset = lue_asetukset()
    done = input("Done? ")

    if done == "t":
        tulosta_tilasto()
        continue

    if done == "r":
        tilasto_init(asetukset)
        continue

    if done == "0":
        break



    #Valitaan aktiviteetti
    aktiviteetti = valinta(asetukset, "aktiviteetit")

    try:
        tilastoon("aktiviteetit", aktiviteetti, asetukset)
    except:
        tilasto_init(asetukset)
        tilastoon("aktiviteetit", aktiviteetti, asetukset)

    if aktiviteetti == "projekti":
        aktiviteetti = valinta(asetukset, "projektit")
        tilastoon("projektit", aktiviteetti, asetukset)
    print(f"- {aktiviteetti}")
    
        
    
