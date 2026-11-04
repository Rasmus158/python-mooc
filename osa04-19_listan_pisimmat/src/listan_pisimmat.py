# tee ratkaisu tänne


def pisimmat(lista):
    suurin = lista[0]
    for sana in lista:
        if len(sana) > len(suurin):
            suurin = sana
        if len(sana) == (suurin):
            suurin.append(sana)
     
    return suurin




if __name__ == "__main__":
    lista = ["pekka", "bbbbbbbbb", "aaaaaaaaa", "eero", "antti", "juhani"]
    tulos = pisimmat(lista)
    print(tulos) # ['seitsemäs']