# tee ratkaisu tänne






with open ("wordlist.txt") as tiedosto:
    inputti = input("Write text: ").split()
    kansioni = []
    for rivi in tiedosto:
        kansioni.append(rivi.strip())
    for sana in inputti:
        if sana.lower() in kansioni:
            print(sana, end=" ")
        else:
            print("*" + sana+ "*", end=" ")
            


    