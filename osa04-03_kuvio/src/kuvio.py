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
def nelio(koko, merkki):
    pituus = 0 
    while pituus < koko:
        viiva(koko, merkki)
        pituus += 1
# kopioi edellisestä tehtävästä funktion viiva koodi tänne
def kolmio(koko):
    pituus = 0
    kerros = 1
    while kerros < (koko+1):
        viiva(kerros, "#")
        kerros += 1
def kuvio(koko,merkki1,koko2,merkki2):
    pituus = 0
    kerros = 1
    while kerros < (koko+1):
        viiva(kerros,merkki1)
        kerros += 1
    pituus2 = 0 
    while pituus2 < koko2:
        viiva(koko, merkki2)
        pituus2 += 1        



if __name__ == "__main__":
    kuvio(5, "x", 3, "*")
