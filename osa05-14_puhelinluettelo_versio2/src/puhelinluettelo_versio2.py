# tee ratkaisu tänne
pankki = {}
while True:
    komento = input("komento (1 hae, 2 lisää, 3 lopeta): ")

    if komento == "1":
        nimi = input("nimi: ")
        if nimi not in pankki:
            print("ei numeroa")
        else:
            for numero in pankki[nimi]:
                print(numero)


    if komento == "2":
        nimi = input("nimi: ")
        numero = input("numero: ")
        if nimi not in pankki:
            pankki[nimi] = []
        pankki[nimi].append(numero)
        print("ok!")

    if komento == "3":
        print ("lopetetaan...")
        break
