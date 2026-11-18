

def kumpi_voitti(pelilauta: list):
    pisteet_1 = 0
    pisteet_2 = 0
    for kasa in pelilauta:
        for kohta in kasa:
            if kohta == 1:
                pisteet_1 += 1
            if kohta == 2:
                pisteet_2 += 1
            else: 
                continue
    if pisteet_1 > pisteet_2:
        return 1
    if pisteet_1 < pisteet_2:
        return 2
    else:
        return 0


if __name__=="__main__":
    m = [[1, 2, 1], [0, 2, 2], [2, 0, 0]]
    print(kumpi_voitti(m))