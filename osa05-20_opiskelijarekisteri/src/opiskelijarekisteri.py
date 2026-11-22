# tee ratkaisu tänne








def lisaa_opiskelija(opiskelijat: dict, oppilas: str):
     opiskelijat[oppilas] = []
   

def tulosta(opiskelijat: dict, oppilas: str):
    if oppilas in opiskelijat:
        print(f"{oppilas}:\n ei suorituksia")
    else:
        print(f"ei löytynyt ketään nimellä {oppilas}")

def lisaa_suoritus(opiskelijat: dict, oppilas: str , suoritus: tuple)
    kusrrien_maara = len(opiskelijat[oppilas])
    print(f"{oppilas}:")
    print(f" suorituksia {krussien_maara} kurssilta:")












if __name__ == "__main__":
    opiskelijat = {}
    lisaa_opiskelija(opiskelijat, "Pekka")
    lisaa_suoritus(opiskelijat, "Pekka", ("Ohpe", 3))
    lisaa_suoritus(opiskelijat, "Pekka", ("Tira", 2))
    tulosta(opiskelijat, "Pekka")


