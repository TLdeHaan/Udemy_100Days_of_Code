# Day 5 - Beginner - Randomisation and Python Lists
'''LIBRARIES AND MODULES'''
import random

'''THEORY'''
fruits = ["Apple", "Peach", "Pear"]
for fruit in fruits:
    print(fruit)
    print(fruit + " Pie")

#For loop with Range
for number in range(1, 11, 3):
    print(number)

total = 0
for number in range (1, 101):
    total += number
print(total)

'''LESSON 16 DAY 5 - AVERAGE HEIGHT'''
# Input a Python list of student heights
student_heights = input().split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆

# Write your code below this row 👇
total_height = 0
number_of_students = 0
for student in student_heights:
    total_height += student
    number_of_students += 1
average_height = round(total_height / number_of_students)
print(f"total height = {total_height}")
print(f"number of students = {number_of_students}")
print(f"average height = {average_height}")

'''LESSON 17 DAY 5 - HIGH SCORE'''
# Input a list of student scores
student_scores = input().split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])

# Write your code below this row 👇
high_score = 0
for score in student_scores:
    if score > high_score:
      high_score = score
print(f"The highest score in the class is: {high_score}")

'''LESSON 18 DAY 5 - ADDING EVEN NUMBERS'''
target = int(input()) # Enter a number between 0 and 1000
# 🚨 Do not change the code above ☝️

# Write your code here 👇
total = 0
for number in range(2, target + 1, 2):
  total += number
print(total)

# alternative
# total = 0
# for number in range (1, target + 1):
#   if number % 2 == 0:
#     total += number
# print(total)

'''LESSON 19 DAY 5 - FIZZBUZZ'''
# Write your code here 👇
target = 100
for number in range(1, target + 1):
  if number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")
  elif number % 3 == 0:
    print("Fizz")
  elif number % 5 == 0:
    print("Buzz")
  else:
    print(number)

'''PASSWORD GENERATOR'''
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Easy-level - fixed order; letters-symbols-numbers
password = ""
for char in range(1, nr_letters + 1):
    index = random.randint(1, len(letters))
    password += letters[index]
for char in range(1, nr_symbols + 1):
    index = random.randint(1, len(symbols))
    password += symbols[index]
for char in range(1, nr_numbers + 1):
    index = random.randint(1, len(numbers))
    password += str(numbers[index])
print(password)

# Alternatieve
password = ""
for char in range(1, nr_letters + 1):
    password += random.choice(letters)
for char in range(1, nr_symbols + 1):
    password += random.choice(symbols)
for char in range(1, nr_numbers + 1):
    password += str(random.choice(numbers))
print(password)

# Hard-level - random order; letters-symbols-numbers
password_list = []
for char in range(1, nr_letters + 1):
    password_list.append(random.choice(letters))
for char in range(1, nr_symbols + 1):
    password_list.append(random.choice(symbols))
for char in range(1, nr_numbers + 1):
    password_list.append(str(random.choice(numbers)))
random.shuffle(password_list)

password = ""
for char in password_list:
    password += char
print(f"Your password is: {password}")
