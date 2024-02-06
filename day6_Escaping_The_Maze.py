# Day 6 - Beginner - Randomisation and Python Lists
'''LIBRARIES AND MODULES'''
import random

'''THEORY'''
def my_function():
    print("hello")

my_function()

# Officially spaces is preferred over tab for indentation; luckily Pycharm treats tabs as 4 spaces.

def jump():
    print("move")
    print("jump")
    print("move")

number_of_hurdles = 6
while number_of_hurdles > 0:
    jump()
    number_of_hurdles -= 1
    print(number_of_hurdles)

# Be careful of infinite while loops