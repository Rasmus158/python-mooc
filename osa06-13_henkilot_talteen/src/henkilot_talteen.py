# tee ratkaisu tänne



def tallenna_henkilo(henkilo: tuple):
    nimi = henkilo[0]
    ika = int(henkilo[1])
    pituus = float(henkilo[2])
    with open ("henkilot.csv", "a") as tiedosto:
        tiedosto.write(nimi+";"+str(ika)+";"+str(pituus)+"\n")

        
