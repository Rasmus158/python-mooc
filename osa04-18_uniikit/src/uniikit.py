# tee ratkaisu tänne


def uniikit(lista):
    lista.sort()
    uusi_lista = []
    luku = 0
    kerta = 0
    for luku in lista:
        if luku in uusi_lista:
            continue
        else:
            uusi_lista.append(luku)   

    return uusi_lista

if __name__ == "__main__":
    lista = [3, 2, 2, 1, 3, 3, 1]
    print(uniikit(lista)) # [1, 2, 3]

