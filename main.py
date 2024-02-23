#Step 1 
import random

word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

choosen_word = random.choice(word_list)

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
guessed_letter = input("Guess a letter :")
guess = guessed_letter.lower()
#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
check_word_list = [letter for letter in choosen_word]
for x in check_word_list:
  if x == guess:
    print("Right")
  else:
    print("Wrong")
