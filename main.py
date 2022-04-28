#Step 5

import random
from replit import clear      # So that console will always clear after user guessed a letter
#TODO-1: - Update the word list to use the 'word_list' from hangman_words.py

from hangman_words import word_list 
chosen_word = random.choice(word_list)             # choose a word randomly from the list 
word_length = len(chosen_word)                     # To find the length of the word chosen

end_of_game = False               # SET CONDITION: when False
lives = 6                 # lives=6 because hangman game rule 

#TODO-3: - Import the logo from hangman_art.py and print it at the start of the game.
from hangman_art import logo, stages
print(logo)
#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):         # Number of _ will be equal to the length of the word 
    display += "_"

while not end_of_game:           # SET CONDITION: when not False means True: programme will run 
    guess = input("Guess a letter: ").lower()                                   # Change user's input letter to lowercase,E.g: doesnt matter they typed B or b
    clear()                                                                     # Will be neater 
    #TODO-4: - If the user has entered a letter they've already guessed, print the letter and let them know.
    if guess in display:
      print(f"You have already previously guessed the letter {guess}")
      
    #Check guessed letter
    for position in range(word_length):                 
        letter = chosen_word[position]
        
        if letter == guess:
            display[position] = letter         #If correct letter, will replace _ with that letter 

    #Check if user is wrong.
    if guess not in chosen_word:           # Use of Python's negation 
        #TODO-5: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
        print(f"The letter '{guess}' you have guessed is incorrect.")
        lives -= 1
        if lives == 0:                 #Set condition for lives 
            end_of_game = True         # SET CONDITION: end_of_game = True means False, programme will stop running 
            print("You lose.")

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True            # SET CONDITION: end_of_game = True means False, programme will stop running 
        print("You win.")

    #TODO-2: - Import the stages from hangman_art.py and make this error go away.
    print(stages[lives])
