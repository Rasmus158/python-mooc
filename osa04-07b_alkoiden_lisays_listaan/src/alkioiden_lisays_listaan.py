luvut = []
maara = 0
monta = int(input("Kuinka monta lukua: "))
while maara < monta:
    anna_luku = int(input(f"Anna luku{maara+1}: "))
    luvut.append (anna_luku)
    maara += 1
print(luvut)