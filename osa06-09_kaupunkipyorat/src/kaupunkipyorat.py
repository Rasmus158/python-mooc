









def hae_asematiedot(tiedosto: str):
    sanakirja = {}
    with open (tiedosto) as tiedosto:
        for rivi in tiedosto:
            osat = rivi.split(";")
            if osat[0] == "Longitude":
                continue
            else:
                sanakirja[osat[3]] = (float(osat[0]), float(osat[1]))
    return sanakirja

def etaisyys(asemat: dict, asema1: str, asema2: str):
    import math
    longitude1 = asemat[asema1][0]
    latitude1 = asemat[asema1][1]
    longitude2 = asemat[asema2][0]
    latitude2 = asemat[asema2][1]
    x_kilometreina = (longitude1 - longitude2) * 55.26
    y_kilometreina = (latitude1 - latitude2) * 111.2
    etaisyys = math.sqrt(x_kilometreina**2 + y_kilometreina**2)
    return etaisyys
    
def suurin_etaisyys(asemat: dict):
    vastaukseni = 0.0
    isoin1 = ""
    isoin2 = ""
    for sema1 in asemat:
        for sema2 in asemat:
            missä_mennään = etaisyys(asemat, sema1, sema2)
            if missä_mennään > vastaukseni:
                vastaukseni = missä_mennään
                isoin1 = sema1
                isoin2 = sema2

    return isoin1, isoin2, vastaukseni











    
if __name__ == "__main__":
    asemat = hae_asematiedot('stations1.csv')
    asema1, asema2, suurin = suurin_etaisyys(asemat)
    print(asema1, asema2, suurin)
