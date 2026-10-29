# Kirjoita ratkaisu tähän
lista = []
while True:
    print(f"Lista on nyt {lista}")
    syöte = input("(l)isää (p)oista vai e(x)it: ")
    if syöte == "x":
        print("Moi!")
        break
    elif syöte == "l":
        uusi = len(lista) +1
        lista.append(uusi)
    elif syöte == "p":
        lista.pop()
