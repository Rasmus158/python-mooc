# tee ratkaisu tänne






def uusi_henkilo(nimi: str, ika: int):
    if nimi == "":
        raise ValueError
    if not " " in nimi:
        raise ValueError
    if len(nimi) >= 41:
        raise ValueError
    if ika < 0:
        raise ValueError
    if ika > 150:
        raise ValueError
    return(nimi, ika)







if __name__=="__main__":
    tyyppi = uusi_henkilo("maiju mehilainen", 15)
    print(tyyppi)