# tee ratkaisu tänne





while True:
    print("1 - Lisää sana, 2 - Hae sanaa, 3 - Poistu")
    valinta = input("Valinta: ")
    if valinta == "1":
        suomeksi = input("Anna sana suomeksi: ")
        englanniksi = input("Anna sana englanniksi: ")
        with open ("sanakirja.txt", "a") as tiedosto:
            tiedosto.write(f"{suomeksi};{englanniksi}\n") 
            print("Sanapari lisätty")

    if valinta == "2":
        annettu_sana = input("Anna sana: ")
        with open ("sanakirja.txt") as tiedosto:
            lista = []
            for rivi in tiedosto:
                splitattu = rivi.split(";")
                if annettu_sana in splitattu[0] or annettu_sana in splitattu[1]:
                    print(f"{splitattu[0]} - {splitattu[1]}")

    if valinta == "3":
        print("Moi!")
        break