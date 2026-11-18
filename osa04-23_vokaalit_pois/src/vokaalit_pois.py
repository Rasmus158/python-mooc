# tee ratkaisu tänne














def ilman_vokaaleja(sana):
    vokaalli = ["a","e","i","o","u","y","ä","ö","å"]
    sana2 = ""
    for kirjain in sana:
        if kirjain in vokaalli:
            continue
        else:
            sana2 = sana2 + kirjain
    return sana2

if __name__ == "__main__":
    mjono = "tämä on esimerkki"
    print(ilman_vokaaleja(mjono))