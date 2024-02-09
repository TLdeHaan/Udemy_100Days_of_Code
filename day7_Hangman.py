# Day 7 - Beginner - Hangman
'''LIBRARIES AND MODULES'''
import random
from day7_Hangman_art import logo, stages
from day7_Hangman_words import word_list

'''HANGMAN'''
# Always try to start with a flowchart
lives = len(stages) - 1
chosen_word = random.choice(word_list)
# print(chosen_word)
display = []
for i in range(len(chosen_word)):
    display.append("_")
    # or display += "_"
# print(display)
end_of_game = False

print(logo)
while not end_of_game:
    guess = input("Guess a letter:").lower()

    if guess in display:
        print(f"You already guessed {guess}. Try again.")
    elif guess in chosen_word:
        for i in range(len(chosen_word)):
            if chosen_word[i] == guess:
                display[i] = chosen_word[i]
    else:
        lives -= 1
        print(f"You've guessed {guess} which is not in the word:")
        print(stages[lives])
    print(display)

    if "_" not in display:
        end_of_game = True
        print("You win!")

    if lives == 0:
        end_of_game = True
        print(stages[lives])
        print("You lose!")