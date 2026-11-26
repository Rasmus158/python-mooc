# tee ratkaisu tänne





def suodata_laskut():
    with open("laskut.csv") as tiedosto_laskut:
    with open("oikeat.csv", "w") as tiedosto_oikeat:
    with open("vaarat.csv", "w") as tiedosto_vaarat:
    oppilaat = []
    sisalto = tiedosto_laskut.read()
    rivit = sisalto.split("\n")
    for rivi in rivit:
        oppilaat.append(rivi)
    for oppilas in oppillat:
        osat = oppilas.strip().split(";")
        for kohta in osat:
            for kirjain in kohta:
                if kirjain ==  "+":

    

    



if __name__ == "__main__":
