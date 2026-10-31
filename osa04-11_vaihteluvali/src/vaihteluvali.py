# tee ratkaisu tänne
# funktiota kannattaa testata kutsumalla sitä täällä seuraavasti
def vaihteluvali(lista):
    lista.sort()
    pienin = min(lista)
    suurin = max(lista)
    return suurin-pienin

if __name__ == "__main__":
    lista = [3, 6, -4] 
    tulos = vaihteluvali(lista) 
    print(tulos)