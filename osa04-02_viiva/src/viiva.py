def viiva(leveys, merkkijono):
    if merkkijono == "":
        merkkijono = "*"
    else: 
        merkkijono = merkkijono[0]
    print(leveys*merkkijono)

# tee ratkaisu tänne
# funktiota kannattaa testata kutsumalla sitä täällä seuraavasti
if __name__ == "__main__":
    viiva(5, "x")
