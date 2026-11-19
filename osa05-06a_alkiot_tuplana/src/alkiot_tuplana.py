# tee ratkaisu tänne








def tuplaa_alkiot(luvut: list):
    valmis = []
    for alkio in luvut:
        tuplattu = alkio + alkio
        valmis.append(tuplattu)
    return valmis

if __name__ == "__main__":
    luvut = [2, 4, 5, 3, 11, -4]
    tuplaluvut = tuplaa_alkiot(luvut)
    print("alkuperäinen:", luvut)
    print("tuplattu:", tuplaluvut)