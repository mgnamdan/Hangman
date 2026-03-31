# ~~~~~ HELPER FUNCTIONS ~~~~~
from random import randint

def loadBank():
    try:
        with open("wordBank.txt", "r") as bankIn:
            loadedBank = bankIn.readlines()
            for idx in range(len(loadedBank)):
                loadedBank[idx] = loadedBank[idx].replace("\n", "")
        return loadedBank
    except FileNotFoundError:
        return ["cat", "tree", "game", "apple", "tiger",
                "rocket", "puzzle", "guitar", "diamond",
                "mystery", "library", "volcano", "adventure",
                "chocolate", "astronaut"]


def printMan(wrongGuesses):
    
    guesses = {0: noWrongGuesses(),
               1: oneWrongGuess(),
               2: twoWrongGuesses(),
               3: threeWrongGuesses(),
               4: fourWrongGuesses(),
               5: fiveWrongGuesses(),
               6: sixWrongGuesses(),
               7: easterEgg()}

    if wrongGuesses > 7 or wrongGuesses < 0:
        wrongGuesses = 7

    print(guesses[wrongGuesses])


# ~~~~~ OUTPUT/DRAW FUNCTIONS ~~~~~
def noWrongGuesses():
    return """
         +---+
         |   |
             |
             |
             |
             |
        ==========
        """


def oneWrongGuess():
    return """
         +---+
         |   |
         O   |
             |
             |
             |
        ==========
        """


def twoWrongGuesses():
    return """
         +---+
         |   |
         O   |
         |   |
             |
             |
        ==========
        """


def threeWrongGuesses():
    return """
         +---+
         |   |
         O   |
        /|   |
             |
             |
        ==========
        """


def fourWrongGuesses():
    return """
         +---+
         |   |
         O   |
        /|\\  |
             |
             |
        ==========
        """


def fiveWrongGuesses():
    return """
         +---+
         |   |
         O   |
        /|\\  |
        /    |
             |
        ==========
        """


def sixWrongGuesses():
    return """
         +---+
         |   |
         O   |
        /|\\  |
        / \\  |
             |
        ==========
        """


def easterEgg():
    return """
         +---+
         |   |
         O   |
          /  |
        /|   |
        / \\  |
        ==========
        """


def displayWord(targetWord, correctLetters):
    displayedWord = ""
    for idx in range(len(targetWord)):
        if targetWord[idx] in correctLetters:
            displayedWord += targetWord[idx]
        else:
            displayedWord += "_"
        displayedWord += " "
    return displayedWord


# ~~~~~ MAIN DEFINITION ~~~~~
def main():
    wordBank = loadBank()

    wrongGuesses = 0
    guessedLetters = {"a": False, "b": False, "c": False, "d": False, "e": False,
                      "f": False, "g": False, "h": False, "i": False, "j": False,
                      "k": False, "l": False, "m": False, "n": False, "o": False,
                      "p": False, "q": False, "r": False, "s": False, "t": False,
                      "u": False, "v": False, "w": False, "x": False, "y": False, "z": False}

    choiceIdx = randint(0, (len(wordBank) - 1))
    chosenWord = wordBank[choiceIdx]

    chosenWord2 = "mountain"
    correctGuesses = []

    while wrongGuesses < 6:
        print(f"Wrong guesses: {wrongGuesses}")
        print(f"Correct guesses: {correctGuesses}")
        print(displayWord(chosenWord2, correctGuesses))
        print("\nGuess a letter (or 'quit' to exit)")
        guessedLetter = input(" --> ").lower()
        if guessedLetter == "quit":
            wrongGuesses = 7
        elif guessedLetters[guessedLetter] == True:
            pass
        else:
            guessedLetters[guessedLetter] = True
            if guessedLetter not in chosenWord2:
                wrongGuesses += 1
            else:
                correctGuesses.append(guessedLetter)
                print(correctGuesses)


    # print(chosenWord)

    # # For testing hangman print outputs
    # for wrongGuessNum in range(8):
    #     print("")
    #     printMan(wrongGuessNum)


# ~~~~~ MAIN CALL ~~~~~
main()