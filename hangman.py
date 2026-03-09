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



# ~~~~~ MAIN DEFINITION ~~~~~
def main():
    # Load word bank
    wordBank = loadBank()

    # Computer chooses a word
    choiceIdx = randint(0, (len(wordBank) - 1))
    chosenWord = wordBank[choiceIdx]

    print(chosenWord)
    


# ~~~~~ MAIN CALL ~~~~~
main()