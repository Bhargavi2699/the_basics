import random

exit = False #if exit = False, then the game keeps going on
user_points = 0
computer_points = 0

while exit == False:
    options = ["rock", "paper", "scissors"]
    user_input = input("Choose rock, paper, scissors or exit: ")
    computer_input = random.choice(options)

    if user_input == "exit":
        print("Goodbye!")
        print("You won a total score of " + str(user_points) + " and computer won a score of " + str(computer_points))
        exit = True

    elif user_input == "rock":
        if computer_input == "rock":
            print("Computer chose rock.")
            print("Tie!")
        elif computer_input == "paper":
            print("Computer chose paper.")
            print("You lose!")
            computer_points += 1
        elif computer_input == "scissors":
            print("Computer chose scissors.")
            print("You win!")
            user_points += 1

    elif user_input == "paper":
        if computer_input == "rock":
            print("Computer chose rock.")
            print("You win!")
            user_points += 1
        elif computer_input == "paper":
            print("Computer chose paper.")
            print("Tie!")
        elif computer_input == "scissors":
            print("Computer chose scissors.")
            print("You lose!")
            computer_points += 1

    elif user_input == "scissors":
        if computer_input == "rock":
            print("Computer chose rock.")
            print("You lose!")
            computer_points += 1            
        elif computer_input == "paper":
            print("Computer chose paper.")
            print("You win!")
            user_points += 1
        elif computer_input == "scissors":
            print("Computer chose scissors.")
            print("Tie!")
            
    elif user_input != "rock" or user_input != "paper" or user_input != "scissors":
        print("Invalid input.")
