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
                for oppilas in oppilaat:
                    osat = oppilas.strip().split(";")
                    if osat == [""]:
                        continue
                    for kohta in osat:
                        for kirjain in kohta:
                            if kirjain ==  "+":
                                jaettu_lasku = osat[1].split("+")
                                luku1 = int(jaettu_lasku[0])
                                luku2 = int(jaettu_lasku[1])
                                if luku1 + luku2 == int(osat[2]):
                                    tiedosto_oikeat.write(oppilas.strip() + "\n")
                                else:
                                    tiedosto_vaarat.write(oppilas.strip() + "\n")
                            if kirjain ==  "-":                 
                                jaettu_lasku = osat[1].split("-")
                                luku1 = int(jaettu_lasku[0])
                                luku2 = int(jaettu_lasku[1])
                                if luku1 - luku2 == int(osat[2]):
                                    tiedosto_oikeat.write(oppilas.strip() + "\n")
                                else:
                                    tiedosto_vaarat.write(oppilas.strip() + "\n")
                

