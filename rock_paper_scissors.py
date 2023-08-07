import random

user_wins = 0
computer_wins = 0

#lists(data structures) are collections of elements, that can be accessed via index : options[0] = rock
#list is encapsulated in [] and seperated by ',' ;this checks if user_input belongs to one of entries
#indices start from 0 to n-1 for list of 'n' elements

options = ["rock", "paper", "scissors"]

while True:
    user_input = input("Choose Rock/Paper/Scissors or type 'Q' to quit: ").lower()
    #previous i/p converted to lower c for uniformity
    if user_input == "q":
        break #exits the loop (can be used in while or for alone)
    
    #you can also add the list directly instsead of using 'options' variable
    if user_input not in options:
        continue #it will go back directly and ask for proper input 

    #generate a random number that represent R, P, S for the computer
    random_number = random.randint(0, 2)
    #rock : 0, paper : 1, scissors : 2
    #computer_pick chooses one of the values from the index where index is a random number
    computer_pick = options[random_number]
    print("Computer picked", computer_pick + ".")

    if user_input == "rock" and computer_pick == "scissors":
        print("You win!!")
        user_wins += 1
        
    elif user_input == "paper" and computer_pick == "rock":
        print("You win!!")
        user_wins += 1
        
    elif user_input == "scissors" and computer_pick == "paper":
        print("You win!!")
        user_wins += 1

    elif user_input == computer_pick:
        print("It's a tie!")

    else:
        print("Computer Wins!")   
        computer_wins += 1

print("You won", user_wins, "times.")
print("The computer won", computer_wins, "times.")
print("Goodbye!")