# Kirjoita ratkaisu tähän
lista = []
while True:
    luku = int(input("Anna luku: "))
    if luku == 0:
        print("Moi!")
        break
    else:
        lista.append(luku)
        print("Lista:", lista)
        print("Järjestettynä:", sorted(lista))
