import random
#'random' is a module here....so you are importing it's properties and functionalities for this prg.
#it's built-in , no installations required.

#random.randrange(start,stop) --> (-1,10) : does not include 10; (11) : 0-10 is chosen
#if above used random.randint(start,stop) --> (-1,10) : 10 will be included; start & stop are mandatory

top_of_range = input("Enter your value: ")

#isdigit() checks if a variable is a digit and returns True or False
if top_of_range.isdigit():

    #int is used to change a string number to an actual integer
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("Enter a number greater than 0 the next time please.")
        quit() #terminates your prg, inbuilt func.
else:
    print("Type a number the next time please")
    quit()


random_number = random.randint(0, top_of_range)
#print(random_number)

guesses = 0 #counting number of times we make a guess
while True:
    guesses += 1
    user_guess = input("Guess the value: ") 
    #we need to see if user_guess is an int as well and above 0
    if user_guess.isdigit():

    #int is used to change a string number to an actual integer
        user_guess = int(user_guess)

    else:
        print("Type a number the next time please")
        continue #it comes out of the loop and goes to the top again.
    
    if user_guess == random_number:
        print("You guessed it right!")
        break #comes out of the loop as a whole
    elif user_guess > random_number:
        print("You got it above the number!")
    else:
        print("You got it below the number!")

#',' immediately add a space by itself with multiple types.
print("You've got it in", guesses, "guesses") 
#'+' is only used for str type within print stmt for concatenation
#print("You've got it in" + str(guesses) + "guesses")