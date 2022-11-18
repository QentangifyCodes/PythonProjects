import pyautogui as pg
import time
import random
import keyboard
import threading


try:
    currentNumber = int(input("Enter Starting Number: "))
    maxNumber = int(input("Enter Max Number: "))
except Exception as e:
    input("Invalid number, try again")
    exit()
    
for i in range(5):
    print(f"Starting program in {5-i}")
    time.sleep(1)

print("Started Program")


tabs = [10, 310 , 610]
i = 0

def EnterNumber():
    global currentNumber, tabs, i
    while True:
        pg.typewrite(str(currentNumber))
        pg.press("enter")
        currentNumber+=1
        pg.moveTo(tabs[i],5)
        i+=1

        if i > len(tabs)-1:
            i = 0
        pg.click()
        
        time.sleep(random.randint(3, 5))
        if currentNumber >= maxNumber:
            exit()

        if keyboard.is_pressed("esc"):
            exit()


spam = threading.Thread(target=EnterNumber)  
spam.start()

