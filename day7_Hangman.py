# Day 7 - Beginner - Hangman
'''LIBRARIES AND MODULES'''
import random
from day7_Hangman_art import logo, stages
from day7_Hangman_words import word_list

'''THEORY'''
# Always try to start with a flowchart
# Write down the components of the flow chart in your script as comments
# Use small samples to test codes and only add true data at the end

'''HANGMAN'''
lives = len(stages) - 1
chosen_word = random.choice(word_list)
# print(chosen_word)
display = []
for i in range(len(chosen_word)):
    display.append("_")
    # or display += "_"
# print(display)
guessed = []
end_of_game = False

print(logo)
while not end_of_game:
    print(display)

    guess = input("Guess a letter:").lower()
    if guess in display:
        print(f"You already guessed {guess}. Try again.")
    elif guess in chosen_word:
        for i in range(len(chosen_word)):
            if chosen_word[i] == guess:
                display[i] = chosen_word[i]
    else:
        lives -= 1
        print(f"The letter \'{guess}\' is not in the word.")
        guessed += guess
        print(stages[lives])

    if "_" not in display:
        end_of_game = True
        print("You win!")
    elif lives == 0:
        end_of_game = True
        print("You lose!")
        print(f"The word was {chosen_word}")
    else:
        print(f"Letters not in the word: {guessed}")