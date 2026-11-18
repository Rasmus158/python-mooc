# tee ratkaisu tänne

def summa(a,b):
    pituus = len(a)
    pituus2 = 0
    uusi_lista = []
    while pituus > pituus2:
        uusi_lista.append(a[pituus2]+b[pituus2])
        pituus2 += 1
        
    return uusi_lista

            


if __name__ == "__main__":
    a = [1, 2, 3]
    b = [7, 8, 9]
    print(summa(a, b)) # [8, 10, 12]