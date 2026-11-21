













def kopioi_ja_lisaa(sudoku: list, rivi_nro: int, sarake_nro: int, luku:int):
    uusi_lista = []
    for rivi in sudoku:
        kopioitu_rivi = rivi[:]
        uusi_lista.append(kopioitu_rivi)
    uusi_lista[rivi_nro][sarake_nro] = luku
    return uusi_lista
def tulosta(sudoku: list):
    for rivi_nro in range(9):
        for sarake_nro in range(9):
            luku = sudoku[rivi_nro][sarake_nro]
            if luku == 0:
                print("_", end=" ")
            else:
                print (luku, end=" ")
            if sarake_nro == 2 or sarake_nro == 5:
                print(" ", end="")
        print()
        if rivi_nro == 2 or rivi_nro == 5:
            print()







if __name__ == "__main__":
    sudoku  = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

    kopio = kopioi_ja_lisaa(sudoku, 0, 0, 2)
    print("Alkuperäinen:")
    tulosta(sudoku)
    print()
    print("Kopio:")
    tulosta(kopio)
