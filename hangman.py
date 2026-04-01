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
    appOn = True
    wordBank = loadBank()

    while appOn:
        print("Would you like to play a game of hangman? (y/n)")
        playGame = input(" --> ").lower()
        if playGame not in ['y', 'yes', 'sure']:
            appOn = False
        else:
            playerWins = 0
            compWins = 0
            gameSeries = True
            print("How long of a series would you like to play?")
            gamesToPlay = int(input(" --> "))
            while gameSeries:
                guessedLetters = {"a": False, "b": False, "c": False, "d": False, "e": False,
                                "f": False, "g": False, "h": False, "i": False, "j": False,
                                "k": False, "l": False, "m": False, "n": False, "o": False,
                                "p": False, "q": False, "r": False, "s": False, "t": False,
                                "u": False, "v": False, "w": False, "x": False, "y": False, "z": False}

                choiceIdx = randint(0, (len(wordBank) - 1))
                chosenWord = wordBank[choiceIdx]
                wrongGuesses = 0
                correctGuesses = []

                while wrongGuesses < 6:
                    printMan(wrongGuesses)
                    print(displayWord(chosenWord, correctGuesses))
                    print("\nGuess a letter (or 'quit' to exit)")
                    guessedLetter = input(" --> ").lower()
                    if guessedLetter == "quit":
                        wrongGuesses = 7
                    elif guessedLetters[guessedLetter] == True:
                        print("Letter already guessed - try again!")
                    else:
                        guessedLetters[guessedLetter] = True
                        if guessedLetter not in chosenWord:
                            wrongGuesses += 1
                        else:
                            correctGuesses.append(guessedLetter)
                    for idx in range(len(chosenWord)):
                        if chosenWord[idx] not in correctGuesses:
                            break
                        if idx == len(chosenWord) - 1:
                            wrongGuesses = 9

                if wrongGuesses == 9:
                    print("Congrats! You've won!")
                    playWins += 1
                else:
                    print("You lost! Try again!")
                    compWins += 1


                if playerWins > (gamesToPlay // 2):
                    print("Congrats player, you've won!")
                    gameSeries = False
                elif compWins > (gamesToPlay // 2):
                    print("You suck!")
                    gameSeries = False
                elif (playerWins + compWins) == gamesToPlay:
                    if playerWins > compWins:
                        print("Congrats player, you've won!")
                    else:
                        print("You suck!")
                    gameSeries = False
                else:
                    continue



# ~~~~~ MAIN CALL ~~~~~
main()