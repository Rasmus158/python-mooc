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

def risunelio(koko):
    pituus = 0
    while pituus < koko :
        viiva(koko,"#")
        pituus += 1

# funktiota kannattaa testata kutsumalla sitä täällä seuraavasti
if __name__ == "__main__":
    risunelio(5)
