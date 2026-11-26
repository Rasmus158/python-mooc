

opiskelijatiedot = input("Opiskelijatiedot: ")
tehtävätiedot = input("Tehtävätiedot: ")
koepisteet = input("Koepisteet: ")

nimet = {}
print("nimi                          teht_lkm  teht_pist koe_pist  yht_pist  arvosana")
with open (opiskelijatiedot) as tiedosto:
    for rivi in tiedosto:
        rivi = rivi.strip()
        osat = rivi.split(";")
        if osat[0] == "opnro":
            continue
        nimet[osat[0]] = osat[1] + " " + osat[2]

tehtävät = {}
with open (tehtävätiedot) as tiedosto2:
    for rivi in tiedosto2:
        summa = 0
        osat = rivi.split(";")
        if osat[0] == "opnro":
            continue
        for luku in osat[1:]:
            summa += int(luku)
        tehtävät[osat[0]] = summa

arvosana = {}
with open (koepisteet) as tiedosto3:
    for rivi in tiedosto3:
        summa = 0
        osat = rivi.split(";")
        if osat[0] == "opnro":
            continue
        for luku in osat[1:]:
            summa += int(luku)
        arvosana[osat[0]] = summa

for opnro, nimi in nimet.items():
    yhteispisteet = (tehtävät[opnro]//4) + arvosana[opnro]

    lopullinen_arvosana = 0
    if yhteispisteet <= 14:
        lopullinen_arvosana = 0
    elif yhteispisteet <= 17:
        lopullinen_arvosana = 1
    elif yhteispisteet <= 20:
        lopullinen_arvosana = 2
    elif yhteispisteet <= 23:
        lopullinen_arvosana = 3
    elif yhteispisteet <= 27:
        lopullinen_arvosana = 4
    else:
        lopullinen_arvosana = 5

    
    print(f"{nimi:30}{tehtävät[opnro]:<10}{(tehtävät[opnro]//4):<10}{arvosana[opnro]:<10}{yhteispisteet:<10}{lopullinen_arvosana:<10}")