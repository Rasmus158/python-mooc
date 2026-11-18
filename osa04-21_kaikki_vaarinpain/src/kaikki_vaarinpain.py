# tee ratkaisu tänne











def kaikki_vaarinpain(lista):
    uusi_lista = []
    for sana in lista:
        uusi_lista.append(sana[::-1])
    uusi_lista.reverse()
    return uusi_lista





if __name__ == "__main__":
    lista = ["Moi", "kaikki", "esimerkki", "vielä yksi"]
    lista2 = kaikki_vaarinpain(lista)
    print(lista2)