word = input("Enter a word: ")

word = word.lower()
checkChars = 0
for i in range(len(word)):
    if word[i] == word[(len(word)-1)-i]:
       checkChars +=1

    if checkChars >= len(word):
        print("This word is a pallendrome")
        break

    if i == len(word)-1:
        print("This word is not a pallendrome")
        break
