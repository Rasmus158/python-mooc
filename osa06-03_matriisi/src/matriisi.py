# tee ratkaisu tänne






def summa():
    summa = 0
    with open ("matriisi.txt") as tiedosto:
        for rivi in tiedosto:
            osat = rivi.split(",")
            for luku in osat:
                summa += int(luku)
    return summa


def maksimi():
    luvut = []
    with open ("matriisi.txt") as tiedosto:
        for rivi in tiedosto:
            osat = rivi.split(",")
            for luku in osat:
                luku = int(luku)
                luvut.append(luku)
    maksimi = max(luvut)
    return maksimi

def rivisummat():
    summat = []
    with open ("matriisi.txt") as tiedosto:
        for rivi in tiedosto:
            summa = 0
            osat = rivi.split(",")
            for luku in osat:
                summa += int(luku)
            summat.append(summa)
    
    return summat




if __name__ == "__main__":
    print(summa())
    print(maksimi())
    print(rivisummat())