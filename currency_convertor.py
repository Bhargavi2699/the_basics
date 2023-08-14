def main():
    print("This program converts US dollars to Pounds Sterling.")
    print()

    dollars = eval(input("Enter the amount in dollars: "))

    pounds = convert_to_pounds(dollars)

    print("That is", pounds, "pounds.")

convert_to_pounds = lambda dollars: dollars * 0.79
main()

#if you want to go bigger, use and API that has the exchange rate available