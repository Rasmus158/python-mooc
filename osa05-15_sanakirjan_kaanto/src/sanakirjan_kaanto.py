# tee ratkaisu tänne











def kaanna(sanakirja: dict):
    uusi_lista = {}
    for avain, arvo in sanakirja.items():
        uusi_lista[arvo] = avain

    sanakirja.clear()
    for avain, arvo in uusi_lista.items():
        sanakirja[avain] = arvo
        

    
    
    

if __name__=="__main__":

    s = {1: "eka", 2: "toka", 3: "kolmas", 4: "neljas"}
    kaanna(s)
    print(s)
