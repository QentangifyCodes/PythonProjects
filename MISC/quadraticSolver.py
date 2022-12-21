while True:
    print("\n----------\n")

    while True:
        try:
            a = int(input("Enter A: "))
            b = int(input("Enter B: "))
            c = int(input("Enter C: "))
            break
        except Exception as e:
            print("Something went wrong, try again")
    lessThanZero = False
    steps = 0

    if b**2 - 4*a*c < 0:
        print("This quadratic is not factorable")
        continue
    if a < 0:
        a = a/-1
        b = b/-1
        c = c/-1
        steps += 1
        print(f"[Step{steps}] Divided out a -1")
        lessThanZero = True


    def FindGCF(num1, num2):
        gcf = 1

        num1 = int(num1)
        num2 = int(num2)

        for i in range(1, min(num1, num2)):
            if num1 % i == 0 and num2 % i == 0:
                gcf = i
        
        return gcf

    def FindFactors(a, c):

        num = a*c
        fac1 = 0
        fac2 = 0
        x = 1

        while True:  
            if b == 0:
                if num/x < 0:
                    x+=1
                else:
                    x-=1
            else:
                if num > 0:
                    if b>0:
                        x+=1
                    if b<0:
                        x-=1    
                elif num<0:
                    x-=1

            if x==0:
                x-=1

            fac1 = num/x
            fac2 = x
            if fac1+fac2 == b and fac2*fac1==num:
                break
            
        return fac1, fac2

    factors = FindFactors(a, c)
    steps += 1
    print(f"[Step {steps}] Found 2 factors: {int(factors[0])} and {factors[1]}")
    if a==1:
        steps+=1
        if lessThanZero:
            print(f"[Step{steps}] Factored Form: -(x+{int(factors[0])}) (x+{factors[1]})")
        else:
            print(f"[Step{steps}] Factored Form: (x+{int(factors[0])}) (x+{factors[1]})")
    else:
        gc = FindGCF(a, factors[0])
        gc2 = FindGCF(c, factors[1])

        steps+=1
        print(f"[Step{steps}] Group: {gc}x({a/gc} + {factors[0]/gc}) + {gc2}({factors[1]/gc2}+{gc2})")
        steps+=1
        print(f"[Step{steps}] Factored Form: ({gc}x+{gc2})({int(a/gc)}x+{int(factors[0]/gc)})")
    if input("Press enter to continue. Type q to quit: ")=='q':
        break

