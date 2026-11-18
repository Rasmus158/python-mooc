# tee ratkaisu tänne











def laske_alkiot(matriisi: list, alkio: int):
    maara = 0 
    for sarake in matriisi:
        for kohta in sarake:
            if kohta == alkio:
                maara += 1
            else:
                continue
    return maara




<<<<<<< HEAD
if __name__=="__main__":
=======
if __name__ == "__main__":
>>>>>>> ea751d1917692638aefac71bf0057d250ef1ebfb
    m = [[1, 2, 1], [0, 3, 4], [1, 0, 0]]
    print(laske_alkiot(m, 1))