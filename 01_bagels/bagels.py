# %%
"""
Bagels, by Al Sweigart al@inventwithpython.com.
A deductive logic game where you must guess a number based on clues.
"""

# %%
import random

# %%
NUM_DIGITS = 3 # ! Try setting this to something other than 3
MAX_GUESSES = 10 # ! Try setting this to something other than 10

# %%
def main():
    print(
        f"Bagels: a deductive logic game. \n By Al SweigartI am thinking of a {NUM_DIGITS}-digit number with no repeated digits.Try to guess what it is. Here are some clues:When I say:   That Means:Kinda...         One digit is correct, but in the wrong position.Nice       One digit is in the correct position.Bagels        You're an idiot.For example, if the secret number was 248 and your guess was 843, the clues would be Kinda Nice."
    )
# %%
    while True:  # Main game loop.
        # This stores the secret number the player needs to guess:
        secretNum = getSecretNum()
        print("I'm thinking of a number.")
        print(f" You have {MAX_GUESSES} guesses to get it.")

        numGuesses = 1
        while numGuesses <= MAX_GUESSES:
            guess = ""
            # Keep looping until they enter a valid guess.
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print(f"Guess #{numGuesses}: ")
                guess = input("> ")

                clues = getClues(guess, secretNum)
                print(clues)
                numGuesses += 1

                if guess == secretNum:
                    break  # They're correct, so break out of this loop.

                if numGuesses > MAX_GUESSES:
                    print("You ran out of guesses, loser.")
                    print(f"The answer was {secretNum}.")
                # Ask loser if they want to play again.
                    print("Had enough? (yn)")
                    if not input("> ").lower().startswith("y"):
                        print("Coward.")
                        break

# %%

def getSecretNum():
    numbers = list('0123456789') # init list of nums 0-9
    random.shuffle(numbers) # shuffle numbers randomly

    return ''.join(str(numbers[i]) for i in range(NUM_DIGITS))


# %%
def getClues(guess, secretNum):
    """Returns a string with the Kinda, Not Bad, Bagels clues for a guess and secret number pair."""
    if guess == secretNum:
        return "Well I'll be damned."

    clues = []

    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            # A correct digit is in the correct place.
            clues.append("Not Bad!")
        elif guess[i] in secretNum:
        # A correct digit is in the correct place.
            clues.append('Kinda!')

    if not clues:
        return 'Bagels'  # There are no correct digits at all.
    #Sort the clues into alphabetical order so their original order doesn't spoil.
    clues.sort()
    # Make a single string from the list of string clues.
    return ' '.join(clues)


        # If the program is run (instead of imported), run the game:
if __name__ == '__main__':
    main()

# %%
