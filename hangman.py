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


# ~~~~~ MAIN DEFINITION ~~~~~
def main():
    wordBank = loadBank()

    choiceIdx = randint(0, (len(wordBank) - 1))
    chosenWord = wordBank[choiceIdx]

    print(chosenWord)

    # # For testing hangman print outputs
    # for wrongGuessNum in range(8):
    #     print("")
    #     printMan(wrongGuessNum)


# ~~~~~ MAIN CALL ~~~~~
main()