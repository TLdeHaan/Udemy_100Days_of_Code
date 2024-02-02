# Day 2 - Beginner - Understanding Data Types and How to Manipulate Strings

'''THEORY'''
'''
Strings
- Surrounded by quotes
- Subscriptable
- + glues strings together

Integer
- A number without decimal
- underscores (_) are ignored in the console, hence can be used to enhance readability
- Allows calculations 
- Can't concatenate with strings by default -> Convert to string
    - str()
    - f"... {} ..."
- int() takes only the integer component ("rounding down")

Float
- A number with decimal point (.)

Boolean
- Only two values; True or False - Declared names with capital letter
'''

print(type("Hello"))
print(type(12345))
a = float(123)
print(type(a))
print(70 + float("100.5"))  # First it will convert string to float. Second sum to the result

print(int(8/3))
print(round(8/3))
print(round(8/3, 2))
print(8 // 3)   # Floor function

result = 4 / 2
result /= 2
print(result)


'''LESSON 5 DAY 2 - DATA TYPES'''
two_digit_number = input()
# 🚨 Don't change the code above 👆
####################################
# Write your code below this line 👇
first_digit = int(two_digit_number[0])
second_digit = int(two_digit_number[1])
total = first_digit + second_digit
print(total)


'''LESSON 6 DAY 2 - BMI CALCULATOR'''
# 1st input: enter height in meters e.g: 1.65
height = input()
# 2nd input: enter weight in kilograms e.g: 72
weight = input()
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
BMI = int((float(weight) / float(height) ** 2))
print(BMI)


'''LESSON 7 DAY 2 - LIFE IN WEEKS'''
age = input()
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
years_left = 90 - int(age)
weeks_left = 52 * years_left
print("You have " + str(weeks_left) + " weeks left.")


'''Tip Calculator'''
print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15?"))
total_bill = bill * (1 + tip / 100)

people = int(input("How many people to split the bill?"))
bill_per_person = round(total_bill / people, 2)
bill_per_person = "{:.2f}".format(bill_per_person)  # To guarantee two decimal numbers to be printed

print(f"Each person should pay: ${bill_per_person}")