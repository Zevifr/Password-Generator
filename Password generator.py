# This is our password generator and password checker. We were trying to achieve a working password generator that makes passwords depending
# on the strength and length chosen. We have given 3 options of low, medium or strong.
# The password checker is a piece of code that can tell you if your password is low, medium or strong based on meeting our own set of criteria.

import random
import string
import re


letters_lowercase = string.ascii_lowercase
letters_uppercase = string.ascii_uppercase
lowerupper = string.ascii_lowercase + string.ascii_uppercase
numbers = string.digits
symbols = ".!@#$%^&*()"

"""
Password generator
"""

def password_generator(length, strength):


    while length < 7:
        print("Password should be at least 7 characters long")
        length = int(input("What do you want the length of your password to be? "))
    while strength not in ["low", "medium", "strong"]:
        print("Please enter a valid option")
        strength = input("How strong would you like your password to be? (low, medium, strong) ")

    original_length = length
    password = []

    password.append(random.choice(letters_lowercase))
    password.append(random.choice(letters_uppercase))
    length -= 2
    if strength == "medium" or strength == "strong":
        password.append(random.choice(numbers))
        length -= 1
    if strength == "strong":
        password.append(random.choice(symbols))
        length -= 1

    if len(password) < original_length:
        password.extend(random.choices(lowerupper, k=original_length - len(password)))

    random.shuffle(password)

    return password

"""
Password strength checker.
"""

def password_checker(password):

    strengthcheck = 0

    if re.search(r'[A-Z, a-z]', password):
        strengthcheck = strengthcheck + 1
    if re.search(r'\d', password):
        strengthcheck = strengthcheck + 1
    if re.search(r'\W', password):
        strengthcheck = strengthcheck + 1


    if len(password) < 7:
        print("password too short - Weak")
    elif strengthcheck == 1:
        print("Low")
    elif strengthcheck == 2:
        print("Medium")
    elif strengthcheck == 3:
        print("Strong")

"""
User input
"""

choice = input("""What would you like to do?
a) Generate a password
b) Check you password strength
""")

if choice == "a":
    try:
        print("".join(password_generator(length=int(input("What do you want the length of your password to be? (Minimum 7 characters) ")),
                                         strength=input("How strong would you like your password to be? (low, medium, strong) "))))
    except:
        print("Please enter a number!")

elif choice == "b":
    password_checker(password=input("What is your password? (Minimum 7 characters) "))

else:
    print("Please select a valid option!")
