import random #slot machine values need to be random

MAX_LINES = 3 #global constant to keep things dynamic.....or something
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

#going to use a dictionary for symbols in slot machine
#dicts are key value pairs: key:values
symbol_count = {
    "A" : 2, #key - symbol(string):count of symbol in each reel, i.e, A is most valuable symbol that occurs 2 times only.
    "B" : 4,
    "C" : 6,
    "D" : 8
}

#allocating values to the symbols of the machine
symbol_value = {
    "A" : 5, #key - symbol(string):count of symbol in each reel, i.e, A is most valuable symbol that occurs 2 times only.
    "B" : 4,
    "C" : 3,
    "D" : 2
}

#to see how much they've won
def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    #need to look at rows, lines they've bet on
    for line in range(lines):
        #checking if every single symbol in the line or row is the same since symbols matching = winning
        #get 1st symbola nd check if it's the same for the rest of the row
        #we don't have the columns, so we are looking only at the 1st column since it has the 1st value of each row
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else: #will run if break is done, since it is a part of for loop
            winnings += values[symbol] * bet #bet on each line, not total bet
            winning_lines.append(line + 1) #no. of lines we've one on; +1 is because lines start with 0.

    return winnings, winning_lines

#generate outcome of the slot machines with the values above - rows, cols and symbols
def get_slot_machine_spin(rows, cols, symbols):
    #generate which symbols are gonna be in each column baes on the frequency of the available symbols
    #need to randomly pick the number of rows inside each column
    #3 rows = 3 of the symbols that goes inside each column - each column will have a new random pick of symbols
    #we are gonna use a list for this
    all_symbols = []
    #gonna use a for loop to add symbols to the list - 
    #easiest way to randomly select is to create list of all possible values and choose 3 of those values ramdomly.
    #we are also iterating through a dictionary
    #.items gives you both the key and the value of dict, hence 2 variable in for loop
    #once we choose a value we remove it from the list and then choose again
    #for loop is going to add whatever symbols we have to the all_symbols list
    for symbol, symbol_count in symbols.items():
        #add values to the symbols list
        # '_' is an anonymous variable to show you do not care about what happens or the no. of iterations in the list
        #to make sure you do not have an unused variable anymore
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    #for loop to do this to columns - nested list is going to represent values in our column
    #no of rows = how many values we need / generate
    columns = []
    #for every column we need to generate a number of symbols
    for _ in range(cols):
        column = []
        # use [:] to copy a list
        #select a number of values from all_symbols list where : is the slice operator
        #if [:] is not present, then even the object gets copies and anything happening to all_symbols, affects current_symbols
        current_symbols = all_symbols[:]
        for _ in range(rows):           
            value = random.choice(current_symbols)
            #now we are going to remove whatever value is chosen from above to avoid issues
            current_symbols.remove(value)
            #now we add 'value' to the column[] since it is chosen
            column.append(value)

        columns.append(column)
    #every interior list  gives the value of the column
    return columns

def print_slot_machine(columns):#for every single row, we see every single column, and for every single column, we look the first values alone 
    #rigth now our columns look like rows, so they need to be flipped
    #we use transposing operation - usually done for matrix
    #number of rows is based on number of columns, equal to the numebr of elements we currently have in the column
    for row in range(len(columns[0])): #should have a minimum of 1 column atleast
        #loop through all of the columns and print only the 1st value in it/ whatever the current row my index is
        #looping through all of the items in columns
        for i, column in enumerate(columns):#print values that are at the first row, enumerate gives the index as well as the item
            if i != len(columns) - 1:
                print(column[row], end = " | ") #| to have some sort of separation ; end tells print statemnet what to end the line with
            else:
                print(column[row], end = "  ")
        print()
        #based on the value of the symbol we multiply the bet
    pass


#collects user input and gets deposit
#something to call and execute a block of code and potentially return us a value - function definition
def deposit():
    while True: #to ensure the user enters a valid amount
        amount = input("Enter your deposit amount? $")
        if amount.isdigit(): #to check if the amoutn entered is actually a +ve number - inbuilt number
            amount = int(amount) #since the value entered was a string, we convert it to int
            if amount > 0:
                break
            else:
                print("Enter a valid amount greater than 0")
        else:
            print("Please enter a number.")   
    return amount

def get_number_of_lines():
    while True: #to ensure the user enters a valid amount
        lines = input("Enter the number of lines to bet on (1 - " + str(MAX_LINES) + ")? ")
        if lines.isdigit(): #to check if the amoutn entered is actually a +ve number - inbuilt number
            lines = int(lines) #since the value entered was a string, we convert it to int
            if 1 <= lines <= MAX_LINES: #check if the value is between them 
                break
            else:
                print("Enter a valid number of lines")
        else:
            print("Please enter a number.")   
    return lines

def get_bet():
    while True: #to ensure the user enters a valid amount
        amount = input("What would you like to bet for each line? $")
        if amount.isdigit(): #to check if the amoutn entered is actually a +ve number - inbuilt number
            amount = int(amount) #since the value entered was a string, we convert it to int
            if MIN_BET <= amount < MAX_BET:
                break
            else:
                #really easy way to embed values inside strings,
                #a way to use it as a string instead of converting separately.
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}")
        else:
            print("Please enter a number.")   
    return amount

def spin(balance):
    lines = get_number_of_lines()

    #have to also evaluate with balance amount as total_bet cannot be > balance
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"You do not have enough balance to bet on, your current balance is {balance}.")
            
        else:
            break

    print(f"You are betting ${bet} on {lines}. Total bet is: {total_bet}")
    
    #generate the slot machine, the values need to autofilled
    #technically slots are columns but we are just calling them slots for now
    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won ${winnings}.")
    print(f"You won on lines:", *winning_lines) #splat or unpack operator, passes every single line from winning_lines to print
    return winnings - total_bet


#if we end the program, we can just call this fn again and it'll rerun
def main():
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")
        answer = input("Press enter to play (q to quit).")
        if answer == "q":
            break
        balance += spin(balance) #tell us how much we've won or lost
    
    print(f"You left with {balance}")
    
main()