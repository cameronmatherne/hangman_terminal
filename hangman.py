import random


def stateZero():
    print(" ======")
    print("      |")
    print("      |")
    print("      |")
    print("      |")
    print("========")

def stateOne():
    print(" ======")
    print("  O   |")
    print("      |")
    print("      |")
    print("      |")
    print("========")

def stateTwo():
    print(" ======")
    print("  O   |")
    print("  |   |")
    print("      |")
    print("      |")
    print("========")

def stateThree():
    print(" ======")
    print("  O   |")
    print(" /|   |")
    print("      |")
    print("      |")
    print("========")

def stateFour():
    print(" ======")
    print("  O   |")
    print(" /|\  |")
    print("      |")
    print("      |")
    print("========")

def stateFive():
    print(" ======")
    print("  O   |")
    print(" /|\  |")
    print(" /    |")
    print("      |")
    print("========")

def stateSix():
    print(" ======")
    print("  O   |")
    print(" /|\  |")
    print(" / \  |")
    print("      |")
    print("========")


# load word list 

text_file = open("wordlist.txt", "r")
wordList = text_file.read().splitlines()
text_file.close()

# pick a random word from the list 

index = random.randint(0,999)
wordToGuess = wordList[index]
wordLength = len(wordToGuess)
wordSkeleton = "_" * wordLength
print("Welcome to hangman")
stateZero()


guessCount = 6
foundCount = 0
wrongCount = 0


print("Guesses remaining: " + str(guessCount))
print(wordSkeleton)


def runRound():

    global wordToGuess
    global guessCount
    global wordSkeleton
    global foundCount
    global wrongCount

    temp = foundCount 
    guess = input("Enter a letter: ")


    for i in range(len(wordToGuess)):
        if (wordToGuess[i] == guess):
            foundCount += 1
            wordSkeleton = wordSkeleton[:i] + guess + wordSkeleton[i + 1:]

    if foundCount > temp:
        print("Successful guess!")
        print(wordSkeleton)
        statePicker()
    else:
        guessCount -= 1
        wrongCount += 1 
        print("Invalid guess. Guesses remaining: " + str(guessCount))
        print(wordSkeleton)
        statePicker()


    

def statePicker():
    if wrongCount == 0:
        return stateZero()
    if wrongCount == 1:
        return stateOne()
    if wrongCount == 2:
        return stateTwo()
    if wrongCount == 3:
        return stateThree()
    if wrongCount == 4:
        return stateFour()
    if wrongCount == 5:
        return stateFive()
    if wrongCount == 6:
        return stateSix()
            
        
        
        
while (guessCount > 0):
    runRound()
    
if wordToGuess == wordSkeleton:
    print("Congradulations! You won!")

if guessCount == 0:
    print("Game over. No attempts remaining.")

    














