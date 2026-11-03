# tee ratkaisu tänne
# huomaa, että tällä kertaa pääohjelmaa ei tule kirjoittaa lohkon
# if __name__ == "__main__":
# sisälle!
def palindromi(sana):   
    pituus = len(sana)
    kirjaimet = list(sana)
    kohta = -1
    lista = []
    while kohta >= (pituus*(-1)):
        lista.append(sana[kohta])
        kohta -= 1
    if lista == kirjaimet:
        return True
    else:
        return False

while True:
    sana = input("Anna palindromi: ")
    if palindromi(sana):
        print(f"{sana} on palindromi!")
        break
    else:
        print("ei ollut palindromi")