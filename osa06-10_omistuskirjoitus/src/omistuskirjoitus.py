# tee ratkaisu tänne











nimi = input("Kenelle teos omistetaan: ")
mihin = input("Mihin kirjoitetaan: ")
with open (mihin, "w") as tiedosto:
    tiedosto.write(f"Hei {nimi}, toivomme viihtyisiä hetkiä python-kurssimateriaalin parissa! Terveisin mooc.fi-tiimi")