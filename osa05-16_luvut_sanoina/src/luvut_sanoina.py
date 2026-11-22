# tee ratkaisu tänne







def lukukirja():
    valmis = {}
    valmis[0] = "nolla"
    valmis[1] = "yksi"
    valmis[2] = "kaksi"
    valmis[3] = "kolme"
    valmis[4] = "neljä"
    valmis[5] = "viisi"
    valmis[6] = "kuusi"
    valmis[7] = "seitsemän"
    valmis[8] = "kahdeksan"
    valmis[9] = "yhdeksän"
    valmis[10] = "kymmenen"
    for luku in range(11, 100):
        ensimmäinen_luku = luku // 10
        jälkimmäinen_luku = luku % 10
        if luku % 10 == 0:
            valmis[luku] = valmis[ensimmäinen_luku] + ("kymmentä")
        elif luku >= 11 and luku <= 19:
            valmis[luku] = valmis[jälkimmäinen_luku] + ("toista")
        else:
            valmis[luku] = valmis[ensimmäinen_luku] + ("kymmentä") + valmis[jälkimmäinen_luku] 
    return valmis
    
if __name__=="__main__":
    luvut = lukukirja()
    print(luvut[2])
    print(luvut[11])
    print(luvut[45])
    print(luvut[99])
    print(luvut[0])