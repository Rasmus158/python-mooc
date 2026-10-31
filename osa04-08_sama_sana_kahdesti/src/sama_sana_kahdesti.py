laskuri = 0
lista = []
while True:
    sana = input("sana: ")
    if sana in lista:
        break
    lista.append(sana)
    laskuri += 1
print(f"Annoit {laskuri} eri sanaa")
    