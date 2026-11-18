# tee ratkaisu tänne










def muotoile(lista):
    lista_uusi = []
    for luku in lista:
        lista_uusi.append(f"{luku:.2f}")
    return lista_uusi




if __name__ == "__main__":
    lista = [1.234, 0.3333, 0.11111, 3.446]
    lista2 = muotoile(lista)
    print(lista2)