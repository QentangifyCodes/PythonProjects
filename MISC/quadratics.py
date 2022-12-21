from random import randint
while True:
    try:
        r = int(input("Enter a solution range: "))
        break
    except Exception as e:
        print("Invalid input, try again")

while True:
    p = randint(-r, r)
    symbolp = '+'
    d = randint(-r, r)
    symbold = '+'


    if randint(0, 100) > 75:
        a = randint(2, 10)

    bterm =  (p+d)
    cterm = (p*d)

    if p < 0:
        symbola = -1
    if d < 0:
        symbolb = -1
    print(f"Solve the quadratic x² + {bterm}x + {cterm}")
    input()
    print(f"The answer was (x {symbolp} {p})(x {symbold} {d})")
    if input("Press enter to generate a new quadratic. Type 'q' to quit: ") == 'q':
        break