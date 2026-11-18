# tee ratkaisu tänne


def lyhin(lista):
    pienin = lista[0]
    for sana in lista:
        if len(sana) < len(pienin):
            pienin = sana
    return pienin




if __name__ == "__main__":
    lista = ["pekka", "asdasdasd", "venla", "ee", "antti", "juhani"]
    tulos = lyhin(lista)
    print(tulos)