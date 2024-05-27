# create function for the random choice of the word, list of 3-5 words
# words should be heterograms, I choose animals for this game
words_options = ["horse", "human", "zebra", "anglerfish", "python"]

import random

computer_choice = random.choice(words_options)

# create default string with len() of the chosen random word
def game_status(computer_choice):
    n = len(computer_choice)
    status = "_ " * n
    return status
status = game_status(computer_choice)

# function for player's letter input


def player_letter(game_status):
   tries = 0
   while tries <= len(computer_choice):
    user_input = str(input("Guess a letter: "))
    tries += 1
    if user_input in computer_choice:
      game_status = status.replace("_ ", user_input)
    else:
      print("Sorry, this letter is not in the word. Guess another letter: ")

    # AttributeError: 'function' object has no attribute 'replace', even when status = str("_ " * n)