

def joulukuusi(luku):
    kerros = 0
    tahti = (luku-(luku-1))
    space = (luku-1)
    print("joulukuusi!")
    while kerros < luku:
        if space < 0:
            space +=1
        print(space*" "+tahti*"*")
        kerros +=1
        space -=1
        tahti+=2
    print((luku-2)*" ",(luku-(luku-1))*"*")
    
if __name__ == "__main__":
    joulukuusi(5)

