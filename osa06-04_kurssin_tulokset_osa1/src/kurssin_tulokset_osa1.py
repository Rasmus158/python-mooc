# tee ratkaisu tänne

Opiskelijatiedot = input("Opiskelijatiedot: ")
Tehtävätiedot = input("Tehtävätiedot: ")

nimet = {}
with open (Opiskelijatiedot) as tiedosto:
    for rivi in tiedosto:
        rivi = rivi.strip()
        osat = rivi.split(";")
        if osat[0] == "opnro":
            continue
        nimet[osat[0]] = osat[1] + " " + osat[2]

tehtävät = {}
with open (Tehtävätiedot) as tiedosto2:
    for rivi in tiedosto2:
        summa = 0
        osat = rivi.split(";")
        if osat[0] == "opnro":
            continue
        for luku in osat[1:]:
            summa += int(luku)
        tehtävät[osat[0]] = summa

for opnro, nimi in nimet.items():
    print(nimi, tehtävät[opnro])

