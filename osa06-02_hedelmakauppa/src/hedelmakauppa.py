# tee ratkaisu tänne










def lue_hedelmat():
    hedelmät = {}
    with open("hedelmat.csv") as tiedosto:
        for rivi in tiedosto:
            osat = rivi.split(";")
            nimi = osat[0]
            hinta = float(osat[1])
            hedelmät[nimi] = hinta
    return hedelmät

if __name__ == "__main__":
    print(lue_hedelmat())


    




