# tee ratkaisu tänne



def parilliset(lista):
    parilliset = []
    for luku in lista:
        if luku == 0:
            continue
        if luku % 2 == 0:
            parilliset.append(luku)

    return parilliset

    

if __name__ == "__main__":
    lista = [0, 2, 4, 6]
    uusi_lista = parilliset(lista)
    print("alkuperäinen", lista)
    print("uusi", uusi_lista)