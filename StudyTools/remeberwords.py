orgwords = ["phenomenon", "pseudonym", "philanthropy", "precede", "voluminous", "query", "requisite", "surmise", "simulate", "synonymous"]
words = orgwords
attempts = 0
import os
clear = lambda: os.system('cls')

while True:
    inp = input(f"Enter a word from the list. {len(words)} word(s) remain: ")
    if words.__contains__(inp.lower()):
        words.remove(inp)
        print("Correct! ")

        if len(words)<=0:
            input("You got them all correct. Press enter to restart")
            words = orgwords
            clear()
    else:
        if attempts < 3:
            print("Incorrect, try again. ")
            attempts+=1
        else:
            print(f"Too many attempts. Remaing words: {words}")
            input("Press enter to restart")
            words = orgwords
            clear()

            