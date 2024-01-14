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


''' Band Name Generator '''
print("Welcome to the Band Name Generator.")
city_name = input("What's the name of the city you grew up in?\n")
pet_name = input("What's the name of your pet?\n")
print(f"Your band name could be {city_name} {pet_name}")