# tee ratkaisu tänne



def positiivisten_summa (lista):
    positiivisten_summa = []
    for luku in lista:
        if luku < 0:
            continue
        if luku >= 0:
            positiivisten_summa.append(it luku)
    return sum(positiivisten_summa)





if __name__ == "__main__":
    lista = [1, -2, 3, -4, 5]
    vastaus = positiivisten_summa(lista)
    print("vastaus", vastaus)

    
