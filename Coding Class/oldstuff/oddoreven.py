# Printing even and odd values

num1 = float(input("Enter a number: "))


if num1%2 == 0:
    print("Number is even")
else:
    print(f"Number is odd. Remainder: {num1%2}")

print("This %d is a number" %num1)