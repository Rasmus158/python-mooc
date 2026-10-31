# tee ratkaisu tänne
# funktiota kannattaa testata kutsumalla sitä täällä seuraavasti

def keskiarvo(lista):
    maara = len(lista)
    summa = sum(lista)
    return summa/maara

if __name__ == "__main__":
    lista = [3, 6, -4] 
    tulos = keskiarvo(lista) 
    print(tulos)
