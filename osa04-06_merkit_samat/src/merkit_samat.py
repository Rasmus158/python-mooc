# tee ratkaisu tänne
# funktiota kannattaa testata kutsumalla sitä täällä seuraavasi

def samat(sana,a,b):
    if a >= len(sana) or b >= len(sana):
        return False
    elif sana[a] == sana[b]:
        return True
   
    return False
if __name__ == "__main__":
    print(samat("koodari", 1, 2)) 