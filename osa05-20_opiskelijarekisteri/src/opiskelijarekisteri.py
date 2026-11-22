# tee ratkaisu tänne


def lisaa_opiskelija(opiskelijat: dict, oppilas: str):
     opiskelijat[oppilas] = {}
     
def tulosta(opiskelijat: dict, oppilas: str):
    if oppilas in opiskelijat:
        if len(opiskelijat[oppilas]) == 0:
            print(f"{oppilas}:\n ei suorituksia")
        else:
            kusrrien_maara = len(opiskelijat[oppilas])
            ka = 0
            print(f"{oppilas}:")
            print(f" suorituksia {kusrrien_maara} kurssilta:")
            for kurssi, numero in opiskelijat[oppilas].items():
                if numero == 0:
                    continue
                ka += numero
                print(" ", kurssi, numero)
            print(" keskiarvo", ka/kusrrien_maara)
    else:
        print(f"ei löytynyt ketään nimellä {oppilas}")

def lisaa_suoritus(opiskelijat: dict, oppilas: str , suoritus: tuple):
    if suoritus[1] == 0:
        return
    if suoritus[0] in opiskelijat[oppilas]:
        if suoritus[1] > opiskelijat[oppilas][suoritus[0]]:
            opiskelijat[oppilas][suoritus[0]] = suoritus[1]
    else:
        opiskelijat[oppilas][suoritus[0]] = suoritus[1]

if __name__ == "__main__":
    opiskelijat = {}
    lisaa_opiskelija(opiskelijat, "Pekka")
    lisaa_suoritus(opiskelijat, "Pekka", ("Ohpe", 3))
    lisaa_suoritus(opiskelijat, "Pekka", ("Tira", 2))
    lisaa_suoritus(opiskelijat, "Pekka", ("Lama", 0))
    lisaa_suoritus(opiskelijat, "Pekka", ("Ohpe", 2))
    tulosta(opiskelijat, "Pekka")



