# QUESTION:

# In this game, there is a list of words present, out of which our interpreter will choose 1 random word. The user first has to input their names and then, will be asked to guess any alphabet. If the random word contains that alphabet, it will be shown as the output(with correct placement) else the program will ask you to guess another alphabet. The user will be given (number of letters in word + 5) turns (which can be changed accordingly) to guess the complete word, if all turns are used so, game will end.



# SOLUTION:

# Importing important librares
import random
import requests
import re

# Words web link, Get the words.
word_site = "https://www.mit.edu/~ecprice/wordlist.10000"
response = requests.get(word_site)

# Define byte strings, Words are in byte format!
byte_strings = response.content.split()

# Convert the byte strings to normal strings
wordsList = [x.decode('UTF8') for x in byte_strings]

# Detect word which contains a character at least twice.
rgx = re.compile(r'.*(.).*\1.*') 

# Function for selecting (non repeating characters) word.
def filter_words(words):
    for word in words:
        if rgx.match(word) is None:
            yield word

# Select a random word.
WORD = random.choice(list(filter_words(wordsList)))

# # If you want to cheating so, uncommint it.
# print(WORD)

# Playing turns.
turns = len(WORD) + 5

# Get user name.
user_name = input("Your name: ")

# Dashes for characters.
dashes = ""
for i in range(1, len(WORD) + 1):
    dashes = dashes + "_"

# Greeting user.
print(f"\n{user_name} you have {turns} chances Good luck!")
print(f"Guess the word {dashes}\n")


# While loop for running & combining all things in game.
while turns > 0:
    # Get user guess.
    user_guess = input("Guess a character: ")

    # If user guess is correct.
    if user_guess in WORD and user_guess != "":
        # Define word index.
        word_index = WORD.index(user_guess)
        # Convert dashes & characters to a list.
        charList = list(dashes)
        # Filled a dash with alphabet at correct index.
        charList[word_index] = user_guess
        # Rejoin all dashes & alphabets
        dashes = "".join(charList)

    # If user guess is wrong.
    elif user_guess not in WORD:
        # 1 turn is subtracted.
        turns -= 1
        # Tell number of turns to user
        print("Wrong, You have", turns, "more guesses\n")

        # If all turns are used.
        if turns == 0:
            # Print loose & end the game with break.
            print("You Loose!")
            print("The word is ", WORD)
            break

    # Printing dashes
    print(dashes,"\n")
    
    # If all dashes are filled.
    if "_" not in dashes:
        # Celebrate winning & end the game with break.
        print(f"Congratulations {user_name} you win!")
        break