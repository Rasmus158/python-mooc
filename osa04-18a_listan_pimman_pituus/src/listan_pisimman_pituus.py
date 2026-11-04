# tee ratkaisu tänne


def pisimman_pituus(lista):
    suurin = lista[0]
    for sana in lista:
        if len(sana) > len(suurin):
            suurin = sana
    return len(suurin)




if __name__ == "__main__":
    lista = ["pekka", "asdasdasd", "venla", "eero", "antti", "juhani"]
    tulos = pisimman_pituus(lista)
    print(tulos)