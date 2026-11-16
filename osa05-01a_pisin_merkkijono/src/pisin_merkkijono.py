# tee ratkaisu tänne



def pisin(merkkijonot: list):
    pituudet = []
    suurin = ""
    vastaus = ""
    for merkkijono in merkkijonot:
        if len(merkkijono) > len(suurin):
            suurin = merkkijono
        else:
            continue
    return suurin

 

if __name__ == "__main__":
    jonot = ["eka", "toka", "kolmas"]
    print(pisin(jonot))