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
   max_tries = len(computer_choice) + 3
   while tries <= max_tries:
    user_input = str(input("Guess a letter: "))
    tries += 1
    if user_input in computer_choice:
      position = computer_choice.find(user_input)
      game_status = status[:position] + user_input + status[position + 1:]
      print(game_status)
      print(f"You have", max_tries - tries, "tries left.")
    else:
      print("Sorry, this letter is not in the word. Guess another letter: ")
      print(game_status)
      print(f"You have", max_tries - tries, "tries left.")
    if "_" not in status:
            print("Congratulations! You've guessed the word correctly.")
            break

