# tee ratkaisu tänne





def lisays (sudoku: list, rivi_nro: int, sarake_nro: int, luku:int):
    sudoku[rivi_nro][sarake_nro] = luku


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

    tulosta(sudoku)
    lisays(sudoku, 0, 0, 2)
    lisays(sudoku, 1, 2, 7)
    lisays(sudoku, 5, 7, 3)
    print()
    print("Kolme numeroa lisätty:")
    print()
    tulosta(sudoku)