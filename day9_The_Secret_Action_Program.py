# Day 9 - Beginner - The Secret Action Program
'''LIBRARIES AND MODULES'''
from day9_The_Secret_Action_Program_art import logo

'''THEORY'''
programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again."
}

print(programming_dictionary["Bug"])

# Adding new items
programming_dictionary["Loop"] = "The action of doing something over and over again."

# Creating empty dict
empty_dict = {}

# Wipe an existing dict
# programming_dictionary = {}

# Edit an item
programming_dictionary["Bug"] = "A moth in your computer"

# Loop through a dictionary
for thing in programming_dictionary:
    print(thing)

for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])

#Nesting
capitals = {
  "France": "Paris",
  "Germany": "Berlin",
}

#Nesting a List in a Dictionary
travel_log = {
  "France": ["Paris", "Lille", "Dijon"],
  "Germany": ["Berlin", "Hamburg", "Stuttgart"],
}

#Nesting Dictionary in a Dictionary
travel_log = {
  "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
  "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 5},
}

#Nesting Dictionaries in Lists
travel_log = [
{
  "country": "France",
  "cities_visited": ["Paris", "Lille", "Dijon"],
  "total_visits": 12,
},
{
  "country": "Germany",
  "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
  "total_visits": 5,
},
]


'''LESSON 22 DAY 9 - GRADING PROGRAM'''
student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99,
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆
# TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

# TODO-2: Write your code below to add the grades to student_grades.👇
for student in student_scores:
  score = student_scores[student]
  if  score >= 91:
    grade = "Outstanding"
  elif score >= 81:
    grade = "Exceeds Expectations"
  elif score >= 71:
    grade = "Acceptable"
  else:
    grade = "Fail"
  student_grades[student] = grade

# 🚨 Don't change the code below 👇
print(student_grades)


'''LESSON 23 DAY 9 - DICTIONARY IN LIST'''
country = input() # Add country name
visits = int(input()) # Number of visits
list_of_cities = eval(input()) # create list from formatted string

travel_log = [
  {
    "country": "France",
    "visits": 12,
    "cities": ["Paris", "Lille", "Dijon"]
  },
  {
    "country": "Germany",
    "visits": 5,
    "cities": ["Berlin", "Hamburg", "Stuttgart"]
  },
]
# Do NOT change the code above 👆

# TODO: Write the function that will allow new countries
# to be added to the travel_log.
def add_new_country(name, times_visited, cities_visited):
  new_country = {}
  new_country["country"] = name
  new_country["visits"] = times_visited
  new_country["cities"] = cities_visited
  travel_log.append(new_country)

# Do not change the code below 👇
add_new_country(country, visits, list_of_cities)
print(f"I've been to {travel_log[2]['country']} {travel_log[2]['visits']} times.")
print(f"My favourite city was {travel_log[2]['cities'][0]}.")


'''THE SECRET ACTION PROGRAM'''
print(logo)
bidding_finished = False
bids = {}


def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")

while not bidding_finished:
    name = input("What is your name?: ")
    price = int(input("What is your bid?: $"))
    bids[name] = price
    should_continue = input("Are there any other bidders? Type 'yes or 'no'.\n")
    if should_continue == "no":
        bidding_finished = True
        find_highest_bidder(bids)
    elif should_continue == "yes":
        print('\n' * 50)    # Workaround for the clear() or cls function
