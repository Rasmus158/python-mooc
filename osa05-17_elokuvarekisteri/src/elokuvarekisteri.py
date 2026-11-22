# tee ratkaisu tänne









def lisaa_elokuva(rekisteri: list, nimi: str, ohjaaja: str, vuosi: int, pituus: int):
    elokuvat = {}
    elokuvat["nimi"] = nimi
    elokuvat["ohjaaja"] = ohjaaja
    elokuvat["vuosi"] = vuosi
    elokuvat["pituus"] = pituus
    rekisteri.append(elokuvat)






if __name__=="__main__":
    rekisteri = []
    lisaa_elokuva(rekisteri, "Pythonin viemää", "Pekka Python", 2017, 116)
    lisaa_elokuva(rekisteri, "Python lentokoneessa", "Renny Pytholin", 2001, 94)
    print(rekisteri)
