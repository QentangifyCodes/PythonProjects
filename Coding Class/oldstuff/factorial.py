number = int(input("Enter a factorial: "))

n = 1
for i in range(1, number+1):
    n *= i

print(n)