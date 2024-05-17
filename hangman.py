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