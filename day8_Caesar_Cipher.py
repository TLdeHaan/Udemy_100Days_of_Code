# Day 8 - Beginner - Caeser Cipher
'''LIBRARIES AND MODULES'''
from day8_Caesar_Cipher_art import logo

'''THEORY'''
def greet(name):
    # Effectively a new variable is created in the function, called name with the value "Angela"
    # name = parameter, "Angela" = argument
    print(f"Hello {name}")
    print(f"How do you do {name}?")


greet("Angela")


def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}?")


greet_with("Jack Bauer", "Nowhere")
greet_with(location="Nowhere", name="Jack Bauer")


'''LESSON 20 DAY 8 - PAINT AREA CALCULATOR'''
# Write your code below this line 👇
import math


def paint_calc(height, width, cover):
    area = height * width
    number_of_cans = math.ceil(area / cover)
    print(f"You'll need {number_of_cans} cans of paint.")


# Write your code above this line 👆
# Define a function called paint_calc() so the code below works.

# 🚨 Don't change the code below 👇
test_h = int(input())  # Height of wall (m)
test_w = int(input())  # Width of wall (m)
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)

'''LESSON 21 DAY 8 - PRIME NUMBERS'''
# Write your code below this line 👇
def prime_checker(number):
    prime = True
    if number > 1 and number <= 100:
        for i in range(2, number):
            if number % i == 0:
                prime = False
        if prime:
            print("It's a prime number.")
        else:
            print("It's not a prime number.")
    elif number == 1:
        print("It's not a prime number.")
    else:
        print("The given number is out of range. Please enter a value between 1 and 100.")

# Write your code above this line 👆

# Do NOT change any of the code below👇
n = int(input())  # Check this number
prime_checker(number=n)


'''CAESAR CIPHER'''
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
#TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.
#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message.
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: \n").lower()
text = input("Type your message: \n").lower()
shift = int(input("Type the shift number: \n"))

# Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount
# and print the encrypted text.
def encrypt(plain_text, shift_amounts):

    cipher_text = ""
    for letter in plain_text:
        position = alphabet.index(letter)
        new_position = position + shift_amounts
        while new_position > 26:
            new_position -= 26
        cipher_text += alphabet[new_position]

    print(f"Here's is the encoded result: {cipher_text}")

# Inside the 'decrypt' function, shift each letter of the 'text' backwards in the alphabet by the shift amount
# and print the decrypted text.
def decrypt(cipher_text, shift_amounts):

    plain_text = ""
    for letter in cipher_text:
        position = alphabet.index(letter)
        new_position = position - shift_amounts
        while new_position < 0:
            new_position += 26
            print(new_position)
        plain_text += alphabet[new_position]
    print(f"Here's is the decoded result: {plain_text}")


if direction == "encode":
    encrypt(plain_text=text, shift_amounts=shift)
elif direction == "decode":
    decrypt(cipher_text=text, shift_amounts=shift)
else:
    print("You entered a unkown type. Please try again")


'''CAESAR CIPHER COMPACT'''
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

def caesar(start_text, shift_amounts, cipher_direction):

    end_text = ""
    if cipher_direction == 'decode':
        shift_amounts *= -1

    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = (position + shift_amounts) % 26
            end_text += alphabet[new_position]
        else:
            end_text += char
    print(f"Here's is the {cipher_direction}d result: {end_text}")

should_continue = True
print(logo)
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: \n").lower()
    text = input("Type your message: \n").lower()
    shift = int(input("Type the shift number: \n"))
    caesar(start_text=text, shift_amounts=shift, cipher_direction=direction)

    result = input("Type 'yes' if you want to go again. Otherwise type 'no'.").lower()
    if result == "no":
        should_continue = False
        print("Goodbye")