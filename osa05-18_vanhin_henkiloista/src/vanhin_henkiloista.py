# tee ratkaisu tänne









def vanhin(henkilot: list):
    nimi = ""
    pienin = 10000
    for nimi in henkilot:
        if nimi[1] < pienin:
            pienin = nimi[1]
    for nimi in henkilot:
        if nimi[1] == pienin:
            return nimi[0]






if __name__ == "__main__":
    h1 = ("Arto", 1977)
    h2 = ("Einari", 1985)
    h3 = ("Maija", 1953)
    h4 = ("Essi", 1997)
    hlista = [h1, h2, h3, h4]

    print(vanhin(hlista))

