# kopioi edellisestä tehtävästä funktion viiva koodi tänne
def viiva(leveys, merkkijono):
    if merkkijono == "":
        merkkijono = "*"
    else: 
        merkkijono = merkkijono[0]
    print(leveys*merkkijono)

def risulaatikko(korkeus):
    pituus = 0 
    while pituus < korkeus:
        viiva(10,"#")
        pituus += 1
    



# funktiota kannattaa testata kutsumalla sitä täällä seuraavasti
if __name__ == "__main__":
    risulaatikko(5)
