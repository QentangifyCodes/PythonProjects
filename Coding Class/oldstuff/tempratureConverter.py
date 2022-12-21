# c = float(input("Please enter a celcius values: "))

# f = (c*1.8)+32

# print("%0.1f degress celcius is equal to %0.1f degress fahrenheit"%(c, f))
# # 0.1f means it will print up to one decimal point, 0.2f is two, etc.

# temp = f

# if temp>= 102 :
#     print("Need to see the doctor")
# elif 102>temp and temp>50:
#     print("You are good to go")
# else:
#     print("You are cold")

# Farenheit to Celcius 
f = float(input("Please enter a Farenheit value: "))

c = (f-32)/1.8

print("%0.1f farenheit is %0.1f celcius"%(f,c))
temp = c

if temp>= 45:
    print("Very hot temprature")
elif 45>temp and temp>20:
    print("Medium temprature")
else:
    print("Very cold")