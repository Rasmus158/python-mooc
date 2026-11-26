# tee ratkaisu tänne







def suurin():
    with open("luvut.txt") as tiedosto:
        lukuja = []
        for rivi in tiedosto:
            lukuja.append(int(rivi))
    suurin = max(lukuja)
    return suurin




if __name__ == "__main__":
    print(suurin())
