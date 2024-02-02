# Day 4 - Beginner - Randomisation and Python Lists
'''LIBRARIES AND MODULES'''
import random
import day4_my_module

'''THEORY'''
# Mersenne Twister is pseudorandom number generator (PRNG) Python uses
random_integer = random.randint(1, 10)
print(random_integer)

print(day4_my_module.pi)

random_float = random.random() # Only from 0.000... to 0.999...
print(random_float)

randomFloat = random.random() * 5 # Increases from 0.000... to 4.999...
print(randomFloat)

love_score = random.randint(1, 100)
print(f"Your love score is {love_score}")

# Lists
states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland",
                     "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island",
                     "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois",
                     "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin",
                     "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado",
                     "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma",
                     "New Mexico", "Arizona", "Alaska", "Hawaii"]
print(states_of_america[0])     # Interpret the 0 as offset from the start. Hence, the first item is not offset = 0.
print(states_of_america[-1])
states_of_america[1] = "Pencilvania"
print(states_of_america[0:3])
states_of_america.append("Angelaland")
print(states_of_america[-1])
states_of_america.extend(["Angelaland", "Jack Bauer Land"])

fruits =["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
dirty_dozen = [fruits, vegetables]
print(dirty_dozen)


'''LESSON 13 DAY 4 - HEADS OR TAILS'''
# Write your code below this line 👇
# Hint: Remember to import the random module first. 🎲
import random
coin = random.randint(0,1)
if coin == 1:
    print("Heads")
else:
    print("Tails")


'''LESSON 14 DAY 4 - BANKER ROULETTE'''
names_string = "Angela, Ben, Jenny, Michael, Chloe"
names = names_string.split(", ")
# The code above converts the input into an array seperating
#each name in the input by a comma and space.
# 🚨 Don't change the code above 👆
import random
number = random.randint(0, len(names) - 1)
print(f"{names[number]} is going to buy the meal today!")


'''LESSON 15 DAY 4 - TREASURE MAP'''
line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input() # Where do you want to put the treasure?
# 🚨 Don't change the code above 👆
# Write your code below this row 👇
number_index = int(position[1]) - 1
letter = position[0].lower()
abc = ["a", "b", "c"]
letter_index = abc.index(letter)

map[number_index][letter_index] = "X"

# Write your code above this row 👆
# 🚨 Don't change the code below 👇
print(f"{line1}\n{line2}\n{line3}")


'''Rock, Paper, Scissors'''
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number, you lose!")
else:
    print(f"You have chosen \n {game_images[user_choice]}")

    computer_choice = random.randint(0, 2)
    print(f"Computer chose {game_images[computer_choice]}")

    if user_choice == 0 and computer_choice == 2:
        print("You win!")
    elif user_choice == 2 and computer_choice == 0:
        print("You lose!")
    elif user_choice > computer_choice:
        print("You win!")
    elif user_choice < computer_choice:
        print("You lose!")
    else:
        print("It's a draw!")