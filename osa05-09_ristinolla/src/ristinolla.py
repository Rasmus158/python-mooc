# tee ratkaisu tänne







#paikka == x
#lohko == y



def pelaa_siirto(lauta: list, x: int, y: int, nappula: str):
    if x > 2 or x < 0:
        return False
    if y > 2 or y < 0:
        return False
    if lauta[y][x] == "X":
        return False
    if lauta[y][x] == "O":
        return False
    lauta[y][x] = nappula
    return True









if __name__ == "__main__":
    lauta = [["", "", ""], ["", "", ""], ["", "", ""]]
    print(pelaa_siirto(lauta, 2, 0, "X"))
    print(lauta)