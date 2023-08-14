#ask user if they want to generate a password
#if yes, ask for password length
#generate password and print it
#if no, exit program
#can use this program if implementing django or flask

import string
import random

characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")

def generate_password():
    password_length = int(input("How many characters would you like your password to be? "))
    random.shuffle(characters)

    password = []

    for x in range(password_length):
        password.append(random.choice(characters))

    random.shuffle(password)

    password = "".join(password)

    print(password)

option = input("Do you want to generate a password (Yes/No)? ").lower()

if option.lower() == "yes":
    generate_password()
elif option.lower() == "no":
    print("Program ended")
    quit()
else:
    print("Invalid input. Please enter yes or no.")
    quit()
