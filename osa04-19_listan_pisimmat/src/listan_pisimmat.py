# tee ratkaisu tänne


def pisimmat(lista):
    suurin = []
    oikeat = []
    pituudet = []
    for sana in lista:
        pituudet.append(len(sana))
    pituudet.sort()
    pisin = pituudet[-1]

    for sana in lista:
        if len(sana) == pisin:
            oikeat.append(sana)
 
    return oikeat  




if __name__ == "__main__":
    lista = ["pekka", "bbbbbbbbb", "aaaaaaaaa", "eero", "antti", "juhani"]
    tulos = pisimmat(lista)
    print(tulos) # ['seitsemäs']