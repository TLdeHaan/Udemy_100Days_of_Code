# Day 7 - Beginner - Hangman
'''LIBRARIES AND MODULES'''
import random
from day7_Hangman_art import logo, stages
from day7_Hangman_words import word_list
# from replit import clear

'''THEORY'''
# Always try to start with a flowchart
# Write down the components of the flow chart in your script as comments
# Use small samples to test codes and only add true data at the end

'''HANGMAN'''
print(logo)
lives = len(stages) - 1
chosen_word = random.choice(word_list)
end_of_game = False

# Create blanks
display = []
for i in range(len(chosen_word)):
    display.append("_")
    # or display += "_"

# Create list to keep record of guess letters
guessed = []

# Game mechanics
while not end_of_game:

    print(display)

    guess = input("Guess a letter:").lower()
    # clear()

    # If letter guess before, print the letter and let them know
    if guess in display:
        print(f"You already guessed {guess}. Try again.")

    # If guess is in word. If so, reveal the letter position(s)
    elif guess in chosen_word:
        for i in range(len(chosen_word)):
            if chosen_word[i] == guess:
                display[i] = chosen_word[i]

    # If guess is NOT in word. Subtract life and print new stage
    else:
        lives -= 1
        print(f"The letter \'{guess}\' is not in the word.")
        guessed += guess
        print(stages[lives])

    # If all letters guessed, print that you won
    if "_" not in display:
        end_of_game = True
        print("You win!")

    # If all lives gone, print that you lost
    elif lives == 0:
        end_of_game = True
        print("You lose!")
        print(f"The word was {chosen_word}")

    # If game NOT ended, print guessed letters up to now
    else:
        print(f"Letters not in the word: {guessed}")
