def rightTriange():
    n = 1

    for x in range(5):
        for i in range(n):
            print("*", end="")
        n+=1
        print()

def rightTriangeFlipped():
    n = 0

    for x in range(5):
        s = " "*(5-n)
        print(s,end="")

        for i in range(n):
            print("*", end="")

        n+=1
        print()

def rightTriangeFlippedDown():

    n = 5

    for x in range(5):
        for i in range(n, 0, -1):
            print("*", end="")

        n-=1
        print()

def rightTriangeFlippedDownFlipped():
    n = 5

    for x in range(5):
        print(" "*(5-n), end="")
        for i in range(n, 0, -1):
            print("*", end="")

        n-=1
        print()



def twoTrianges():
    amt = int(input("Enter size: "))
    n = amt
    d= True

    for x in range(amt*2):
        if d:
            for i in range(n):
                print("*", end="")
            n-=1

            if n<0:
                d = False
                n = 2
                continue
        else:
            for i in range(n):
                print("*", end="")
            n+=1        
        print()


def eqtriangle():

    spaces = 2
    count = 1

    for i in range(3):
        i = " "*spaces
        print(i, end='')
        for x in range(count):
            print("*", end="")

        print(i, end='')
        print()

        spaces-=1
        count+=2

def diamond():
    spaces = 2
    count = 1
    up = False

    for i in range(6):
        i = " "*spaces
        print(i, end='')
        for x in range(count):
            print("*", end="")

        print(i, end='')
        print()

        if not up:
            spaces-=1
            count+=2
        else:
            spaces+=1
            count-=2

        
        if spaces < 0:
            up = True
            spaces = 1
            count = 3
            continue

def hollowdiamond():
    spaces = 2
    count = 1
    up = False

    print("*"*5)
    for i in range(3):
        i = "*"*spaces
        print(i, end='')
        for x in range(count):
            print(" ", end="")

        print(i, end='')
        print()

        if not up:
            spaces-=1
            count+=2
        else:
            spaces+=1
            count-=2

        
        if spaces <= 0:
            up = True
            spaces = 2
            count = 1
            continue

    print("*"*5)

hollowdiamond()
