# Day 2 - Beginner - Understanding Data Types and How to Manipulate Strings

'''Primitive Data Types'''
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

print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15?"))
total_bill = bill * (1 + tip / 100)

people = int(input("How many people to split the bill?"))
bill_per_person = round(total_bill / people, 2)
bill_per_person = "{:.2f}".format(bill_per_person)  # To guarantee two decimal numbers to be printed

print(f"Each person should pay: ${bill_per_person}")