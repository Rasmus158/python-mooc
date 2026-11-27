# tee ratkaisu tänne








def lue(sana: str, luku1: int, luku2: int):
    while True:
        try:
            luku = int(input("syötä luku: "))
            if luku >= luku1 and luku <= luku2:
                return int(luku)
        except ValueError:
            pass
        print(f"Syötteen on oltava kokonaisluku väliltä {luku1}...{luku2}")


if __name__=="__main__":
    luku = lue("syötä luku: ", 5, 10)
    print("syötit luvun:", luku)