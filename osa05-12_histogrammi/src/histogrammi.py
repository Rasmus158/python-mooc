# tee ratkaisu tänne













def histogrammi(sana: str, ekaluku: int, tokaluku: int):
    vastaus = {}
    for kirjain in sana:
        if kirjain in vastaus:
            vastaus[kirjain] += 1
        else:
            vastaus[kirjain] = 1
    for avain, arvo in vastaus.items():
        print(avain, arvo * "*")



if __name__=="__main__":
    sana = "saippuakauppias"
    histogrammi(sana)
