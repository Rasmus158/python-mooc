# tee ratkaisu tänne



def hae_nimi(tiedosto: str, sana: str):
    with open (tiedosto) as tiedosto:
        kansio = []
        oikeat = []
        oikeat2 = []
        for rivi in tiedosto:
            kansio.append(rivi.strip())
        for kohta in kansio:
            if sana.lower() in kohta.lower():
                if kohta == "":
                    continue
                if kohta[0].isupper():
                    oikeat.append(kohta)
        return oikeat

def hae_aika(tiedosto: str, aika: int):
    ajat = []
    oikea_resepti = []
    with open (tiedosto) as tiedosto:
        for rivi in tiedosto:
           ajat.append(rivi.strip())
        for muuttuja in range(len(ajat)):
            if ajat[muuttuja-1] == "" or muuttuja == 0:
                resepti = ajat[muuttuja]
                valmistus_aika = int(ajat[muuttuja+1])
                if valmistus_aika <= aika:
                    oikea_resepti.append(f"{resepti}, valmistusaika {valmistus_aika} min")

    return oikea_resepti

def hae_raakaaine(tiedosto: str, aine: str):
    gg














if __name__ == "__main__":
    loydetyt = hae_raakaaine("reseptit1.txt", "maito")
    print(loydetyt)
