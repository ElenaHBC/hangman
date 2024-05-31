# create function for the random choice of the word, list of 3-5 words
# words should be heterograms, I choose animals for this game
words_options = ["horse", "human", "zebra", "anglerfish", "python"]

import random

computer_choice = random.choice(words_options)

# create default string with len() of the chosen random word
def game_status(computer_choice):
    n = len(computer_choice)
    status = "_" * n
    return status

status = game_status(computer_choice)

# function for player's letter input


def player_letter(status): # using the global variable status
   tries = 0
   max_tries = len(computer_choice) + 3
   while tries < max_tries:
    user_input = str(input("Guess a letter: "))
    tries += 1

    # add an if statemnet checking if the input is a number
    # add a possibility for the user to guess the whole word in one try?

    if user_input in computer_choice:
      position = computer_choice.find(user_input)
      status = status[:position] + user_input + status[position + 1:] # we're already using the global variable outside the function
      new_status = " ".join(status) # saving the user input in a new variable to which we add every new correctly guessed letter
      print(new_status)
      print(f"You have {max_tries - tries} tries left.")
    else:
      print("Sorry, this letter is not in the word. Guess another letter: ")
      print(status)
      print(f"You have {max_tries - tries} tries left.")
    if "_" not in status:
            print("Congratulations! You've guessed the word correctly.")
            break
   else:
      print(f"Game over! The word was: {computer_choice}") 

player_letter(status)