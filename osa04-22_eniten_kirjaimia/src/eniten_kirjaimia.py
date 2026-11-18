# tee ratkaisu tänne









def eniten_kirjainta(sana):
    suurin = 0
    eniten = ""
    for kirjain in sana:
        maara = sana.count(kirjain)
        if maara > suurin:
            suurin = maara
            eniten = kirjain
   
    return eniten






if __name__ == "__main__":
    mjono = "abcbdbe"
    print(eniten_kirjainta(mjono))

    toinen_jono = "esimerkkimerkkijonokki"
    print(eniten_kirjainta(toinen_jono))