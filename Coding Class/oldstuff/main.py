num1 = int(input("Enter Number 1: "))
num2 = int(input("Enter Number 2: "))

operator = input("Enter a operation: ")

if operator == "+":
    print(num1+num2)
elif operator == "-":
    print(num1-num2)
elif operator == "*":
    print(num1*num2)
elif operator == "/":
    print(num1/num2)
elif operator == "expo":
    print(num1**num2)