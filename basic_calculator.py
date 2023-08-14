#define the functions needed for +, -, *, /
#print options to the user : +, -, *, / or exit
#ask for values
#call the functions
#while loop to continue the program until the user wants to exit
def add(a, b):
    answer = a + b
    print(str(a) + " + " + str(b) + " = " + str(answer) + "\n") #+ can be used to concatenate strings

def sub(a, b):
    answer = a - b
    print(str(a) + " - " + str(b) + " = " + str(answer)) #+ can be used to concatenate strings
    print()

def multiply(a, b):
    answer = a * b
    print(str(a) + " * " + str(b) + " = " + str(answer) + "\n") #+ can be used to concatenate strings

def divide(a, b):
    answer = a / b
    print(str(a) + " / " + str(b) + " = " + str(answer)) #+ can be used to concatenate strings
    print()

#printing out the options
while True:
    print("A. Addition")
    print("B. Subtraction")
    print("C. Multiply")
    print("D. Division")
    print("E. Exit")

    choice = input("Please enter your choice: ").lower()

    if choice == 'a':
        print("Addition")
        a = int(input('Enter first number: '))
        b = int(input('Enter second number: '))
        add(a, b)

    elif choice == 'b':
        print("Subtraction")
        a = int(input('Enter first number: '))
        b = int(input('Enter second number: '))
        sub(a, b)

    elif choice == 'c':
        print("Multiplication")
        a = int(input('Enter first number: '))
        b = int(input('Enter second number: '))
        multiply(a, b)

    elif choice == 'd':
        print("Division")
        a = int(input('Enter first number: '))
        b = int(input('Enter second number: '))
        divide(a, b)

    elif choice == 'e':
        print("Exit")
        quit()









