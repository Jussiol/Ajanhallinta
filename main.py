from tiedoston_kasittely import lue_asetukset 
from tiedoston_kasittely import tilasto_init, tilasto_paivita
from tiedoston_kasittely import tilastoon, tulosta_tilasto
from valitse_FIFO import valinta

def tallenna(aktiviteetti, asetukset):
    try:
        tilastoon("aktiviteetit", aktiviteetti, asetukset)
    except:
        tilasto_init(asetukset)
        tilastoon("aktiviteetit", aktiviteetti, asetukset)

    if aktiviteetti == "projekti":
        aktiviteetti = valinta(asetukset, "projektit")
        tilastoon("projektit", aktiviteetti, asetukset)
    return aktiviteetti

print("Enter jos valmis, 0 lopettaa")
print("p = ohita, 4 = arvo päivän aktivieetit ja lopeta")
print("t = tilasto, r = nollaa tilasto")
print()
done = ""
while True:
    asetukset = lue_asetukset()
    if done != "p":
        done = input("Done? ")
    if done == "" or done == "p":
        #Valitaan aktiviteetti
        aktiviteetti = valinta(asetukset, "aktiviteetit")
        if done != "p":
            aktiviteetti = tallenna(aktiviteetti, asetukset)
        print(f"- {aktiviteetti}")
        done = ""
    if done == "t":
        tulosta_tilasto()
        continue

    if done == "r":
        tilasto_init(asetukset)
        continue
    if done == "p":
        continue
    if done == "4":
        hyvaksytyt = 0
        aktiviteettilista = []
        while hyvaksytyt < 4:
            aktiviteetti = valinta(asetukset, "aktiviteetit")
            ok = input(f"Ok? -> {aktiviteetti}")
            if ok == "":
                naytettava = tallenna(aktiviteetti, asetukset)
                aktiviteettilista.append(naytettava)
                hyvaksytyt += 1
        print()
        print("Päivän ohjelma:")
        for akt in aktiviteettilista:
            print(f"- {akt}")
        print()
        print("Työn iloa!")
        print("Heippa!")
        break

    if done == "0":
        break



    
        
    
