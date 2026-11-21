# tee ratkaisu tänne









pankki = {}
while True:
    komento = input("komento (1 hae, 2 lisää, 3 lopeta): ")

    if komento == "1":
        nimi = input("nimi: ")
        if nimi not in pankki:
            print("ei numeroa")
        else:
            print(pankki[nimi])


    if komento == "2":
        nimi = input("nimi: ")
        numero = input("numero: ")
        pankki[nimi] = numero
        print("ok!")

    if komento == "3":
        print ("lopetetaan...")
        break
