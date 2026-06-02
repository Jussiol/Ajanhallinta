from tiedoston_kasittely import lue_asetukset
from valitse_FIFO import valinta

print("Enter jos valmis, 0 lopettaa")
while True:
    asetukset = lue_asetukset()
    #Valitaan aktiviteetti
    aktiviteetti = valinta(asetukset, "aktiviteetit")
    if aktiviteetti == "projekti":
        aktiviteetti = valinta(asetukset, "projektit")

    print(f"{aktiviteetti}")
    
    done = input("Done? ")
    if done == "0":
        break
    
