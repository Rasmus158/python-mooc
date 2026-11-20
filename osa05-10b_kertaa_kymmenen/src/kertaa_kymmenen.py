# tee ratkaisu tänne











def kertaa_kymmenen(alku: int, loppu: int):
    muutokset = {}
    while True:
        muutokset[alku] = alku * 10
        alku += 1
        if alku > loppu:
            break
    return muutokset




if __name__ == "__main__":
    d = kertaa_kymmenen(3, 6)
    print(d)
