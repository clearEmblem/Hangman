import random
from hangman_art import stages
from hangman_art import logo
print(logo)
with open('hangman_words.txt', 'r') as f:
    words = f.readlines()

for i in range(len(words)):
    words[i] = words[i].replace('\n', "")

randNum = random.randint(0, len(words))
randWord = words[randNum - 1]
splitWord = []
for i in randWord:
    splitWord.append(i)
userList = ["_"] * len(splitWord)
count = 6
while splitWord != userList:
    userLetter = input("Guess a letter: ")
    for i in range(0, len(splitWord)):
        if splitWord[i] == userLetter:
            userList[i] = userLetter
    if userLetter not in splitWord:
        count -= 1
        print(stages[count])
        if count == 0:
            print("you lost")
            print(f"the word was {"".join(splitWord)}")
            break
    elif splitWord == userList:
        print("You won!")
        break
    print("".join(userList))
    print(f"you have {count} guesses left")


