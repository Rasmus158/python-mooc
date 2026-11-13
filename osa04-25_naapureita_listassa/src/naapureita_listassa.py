# tee ratkaisu tänne

#oikea vastaus pitäisi oll 4 eli
        #7, 6, 5, 6,



def pisin_naapurijono(lista):
    koko = 0
    suurin = 0
    kohta = 1
    for luku in lista:
        if kohta == len(lista):
            break
        if luku - lista[kohta] in (-1,1):
            kohta += 1
            koko += 1
            if koko > suurin:
                suurin = koko
        else:
            kohta += 1
            koko = 0
            continue
    if suurin == 0:
        return suurin
    
    return suurin + 1






if __name__ == "__main__":
    lista = [1, 2, 5, 7, 6, 5, 6, 3, 4, 1, 0]
    print(pisin_naapurijono(lista))