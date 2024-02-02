# Day 1 - Beginner - Working with Variables in Python to Manage Data

''' Print statement '''
print("Hello world!")
print("print('Hello world!')")
print('print("Hello world!")')
print("Hello world!\nHello world!")
print("Hello world!\nHello world!\nHello world!")
print("Hello" + " " + "Angela")

''' Input statements '''
input("What is your name?")
# input() will get user input in console
# Then print() will print the word "Hello" and the user input
print("Hello " + input("What is your name?") + "!")

''' Variables '''
print(len(input("What is your name?")))
name = input("What is your name?")
length = len(name)
print(length)

'''LESSON 1 DAY 1 - PRINTING'''
print("Day 1 - Python Print Function")
print("The function is declared like this:")
print("print('what to print')")

'''LESSON 2 DAY 1 - DEBUGGING PRACTICE'''
# Fix the code below 👇
print("Day 1 - String Manipulation")
print("String Concatenation is done with the \"+\" sign.")
print('e.g. print("Hello " + "world")')
print("New lines can be created with a backslash and n.")

'''LESSON 3 DAY 1 - INPUT FUNCTION'''
# Provide any name in the input pane below.
# That value can be accessed using the input() function.
# Don't put anything inside the input() function!
name = input()
print(len(name))

'''LESSON 4 DAY 1 - VARIABLES'''
# There are two variables, a and b from input
a = input()
b = input()
# 🚨 Don't change the code above ☝️
####################################
# Write your code below this line 👇
c = a
a = b
b = c
# 🚨 Don't change the code below 👇
print("a: " + a)
print("b: " + b)

''' Band Name Generator '''
print("Welcome to the Band Name Generator.")
city_name = input("What's the name of the city you grew up in?\n")
pet_name = input("What's the name of your pet?\n")
print(f"Your band name could be {city_name} {pet_name}")