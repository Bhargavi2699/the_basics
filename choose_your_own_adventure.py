name = input("Enter your name: ").upper()
print("Welcome", name, "to this adventure!")

answer = input("You're on a dirt road, it has come to an end & you can go left or right. Which way would you like to go? ").lower()

if answer == "left":
    #can use a different variable here if you'd like over 
    answer = input("You've come to a river, you can walk around or swim across it. Type walk or swim: ").lower()

    if answer == "walk":
        print("You swam across and were eaten by an alligator.")
    elif answer == "swim":
        print("You walked for many miles, ran out of water and lost the game.")
    else:
        print("Not a valid option. You lose!")

elif answer == "right": #add a blank print() atleast so it doesn't raise a damn error
    answer = input("You've come to a bridge. It looks wobbly. Do you want to cross it or head back (cross/back)? ").lower()

    if answer == "back":
        print("You go back and lose.")
    elif answer == "cross":
        answer = input("You cross the bridge and meet a stranger. Do you talk to them or not (yes/no)? ").lower()
        if answer == "yes":
            print("The stranger gives you DIAMONDS!! You WIN!!")
        elif answer == "no":
            print("You don't talk to the stranger. You lose!")
        else:
            print("Not a valid option. You lose!")
    else:
        print("Not a valid option. You lose!")

else:
    print("Not a valid option. You lose!")

print("Thank you", name,"for playing!")
#can add additional options to see if they have made a correct choice beforehand etc and add you own stuff.