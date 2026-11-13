# Kirjoita ratkaisu tähän


lista0 = []
lista1 = []
lista2 = []
lista3 = []
lista4 = []
lista5 = []
arvosana = 0
kerta = -1
hylatty = 0
lopulliset_pisteet = 0
pisteiden_summa = 0


while True:
    luvut = input("Koepisteet ja harjoitusten määrä: ")
    kerta += 1
    if luvut == "" or luvut == " ":
        break
    leikattu = luvut.split()
    koe = int(leikattu[0])
    harjoitus = int(leikattu[1])
    harjoituspisteet = harjoitus // 10
    lopulliset_pisteet = koe + harjoituspisteet
    pisteiden_summa += lopulliset_pisteet
    if koe < 10:
        arvosana += 0
        hylatty += 1
        lista0.append("*")
        continue
    if lopulliset_pisteet <= 14:
        arvosana += 0
        hylatty += 1
        lista0.append("*")
    if 15 <= lopulliset_pisteet < 18:
        arvosana += 1
        lista1.append("*")
    if 18 <= lopulliset_pisteet < 21:
        arvosana += 2
        lista2.append("*")
    if 21 <= lopulliset_pisteet < 24:
        arvosana += 3
        lista3.append("*")
    if 24 <= lopulliset_pisteet < 28:
        arvosana += 4
        lista4.append("*")
    if 28 <= lopulliset_pisteet:
        arvosana + 5
        lista5.append("*")
keskiarvo = pisteiden_summa / kerta
Hyväksymisprosentti = ((kerta-hylatty)/kerta)*100

print("Tilasto:")
print(f"Pisteiden keskiarvo: {keskiarvo}")
print(f"Hyväksymisprosentti: {Hyväksymisprosentti:.1f}")
print("Arvosanajakauma:")
print("5: ", *lista5, sep="")
print("4: ", *lista4, sep="")
print("3: ", *lista3, sep="")
print("2: ", *lista2, sep="")
print("1: ", *lista1, sep="")
print("0: ", *lista0, sep="")

    
    




