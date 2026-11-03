

def anagrammi(sana1, sana2):
    sortsana1 = sorted(sana1)
    sortsana2 = sorted(sana2)
    if sortsana1 == sortsana2:
        return True
    else:
        return False


if __name__ == "__main__":
    anagrammi("apina","apina")