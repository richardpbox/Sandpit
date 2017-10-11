# This is a game of hangman

# Function to retrieve the target word from a list
def GetTargetWord(difficulty):
    # For now I'm going to just set a word
    word = "HAPPY"
    return (word)

# Function to receive the input letter choice from user
def GetLetterFromUser():
    response = input("Enter a letter (or quit to end game): ")
    if response == "quit":
        exit()
    elif not len(response) == 1:
        print("invalid reponse")
        return (0)
    else:
        return (response)

# Function designed to put the correct letter in the right place in the Guessed Word and returning it.
def PutLetterInGuessedWord(letter,Tword,Gword):
    returnword=[]
    Gletters = list(Gword)
    Tletters = list(Tword)
    # print(str(Tletters))

    for x in range(len(Tword)):
        if Tletters[x] == letter:
            Gletters[x] = Tletters[x]
        else:
            continue
    
    return("".join(Gletters))
    


# Overall control programme logic
# TODO:  Think about adding in try loop outer to catch exceptions etc.

# Set difficulty (next phase to replace)
difficulty = "E"

TargetWord = GetTargetWord(difficulty)

print("The word your looking for is " + str(len(TargetWord)) + " letters long.  Good luck!")

# Main event - now solve the puzzle!
solved = False
GuessedWord = ""

#Create a GuessedWord which is all underscores:
for i in range(len(TargetWord)):
    GuessedWord += "_"
# print(len(GuessedWord))
# print(GuessedWord)

#Create a string of all guesses to date
GuessedLetters = ""

while solved == False:

    guess = GetLetterFromUser()
    if guess in GuessedLetters:
        print("You've already guessed that letter!")
    elif guess in TargetWord:
        GuessedLetters += guess
        # Go through the target word and work out where the letter is - and then put that letter into the GuessedWord in the same place
        newGuessedWord = PutLetterInGuessedWord(guess,TargetWord,GuessedWord)
        GuessedWord = newGuessedWord
        print(GuessedWord)
    else:
        print("Letter not in the target word")

    if TargetWord == GuessedWord:
        print ("SUCCESS!")
        solved = True
    else:
        print("Currently..." + GuessedWord)




