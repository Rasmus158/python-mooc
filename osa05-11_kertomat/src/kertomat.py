  

def kertomat(n: int):
    uusi_lista = {}
    luku = 1
    kertoja = 1
    while True:
        kertoja = kertoja * luku
        uusi_lista[luku] = kertoja
        luku += 1
        if luku > n:
            break
    return uusi_lista

if __name__ == "__main__":
    k = kertomat(5)
    print(k[1])
    print(k[3])
    print(k[5])