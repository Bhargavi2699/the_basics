#we need to make sure that the computer has a number to guess
#so first, we assign a random number to it
#then we need to guess and compare and the computer will tell us if the guess is greater or lesser than the number
#keep looping until we get closer and closer
import random

def guess(x):

    random_number = random.randint(1, x) #randint has range of 1 to x
    #'while' loop is used since we dk how many times we might need to do it   
    user_guess = 0 #since we do not want it to be equal to the random number just yet

    while user_guess != random_number:

        user_guess = int(input(f"Guess a number between 1 and {x}: "))
        print(user_guess)

        if user_guess > random_number:
            print("Your guess is too high. Go lower.")
        elif user_guess < random_number:
            print("Your guess is too low. Go higher.")

    print(f"You have guessed the number {random_number} correctly!!")

#now we make the computer guess OUR number, we need to haave a number in hand for the computer to guess
def computer_guess(x):
    #we need a range for this
    low = 1
    high = x
    #we need to tell the computer how high(lol) or low they actually are
    feedback = '' #comes from us
    while feedback != 'c': #here 'c' stands for the correct answer or critique....
        #here we need to see if low = high or not, as computer will be confused which number it is.
        if low != high:  
            computers_guess = random.randint(low, high) #since both values can change based on user's feedback
        else:
            computers_guess = low #can also be high since low = high
        feedback = input(f"Is the {computers_guess} too high(H), too low(L) or correct (C)? ").lower()
        if feedback == 'h':
            #since, if comp. guessed 8 from a range of 1-10, and it's too high, then the values need to range from 1-7
            high = computers_guess - 1 
        elif feedback == 'l':
            low = computers_guess - 1

    print(f"Dear computer, you guessed the number {computers_guess} right!") #computer_guess coz it's the right answer

computer_guess(100)