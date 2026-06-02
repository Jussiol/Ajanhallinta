from tiedoston_kasittely import lue_asetukset, tilastoon, tulosta_tilasto, tilasto_init
from valitse_FIFO import valinta

print("Enter jos valmis, 0 lopettaa")
print("t = tilasto, r = nollaa tilasto")

while True:
    asetukset = lue_asetukset()
    #Valitaan aktiviteetti
    aktiviteetti = valinta(asetukset, "aktiviteetit")
    
    try:
        tilastoon(aktiviteetti)
    except:
        tilasto_init(asetukset)
        tilastoon(aktiviteetti)

    if aktiviteetti == "projekti":
        aktiviteetti = valinta(asetukset, "projektit")

    print(f"{aktiviteetti}")
    
    done = input("Done? ")
    if done == "t":
        tulosta_tilasto()
        done = input("Done? ")
    if done == "0":
        break
    if done == "r":
        tilasto_init(asetukset)
        
    
