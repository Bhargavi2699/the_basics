#collect necessary inputs: principal amount, years, annual interest rate
#calculaet monthly payment
#display the final amount

def main():
    print("LOAN CALCULATOR")
    print()

    principal = float(input("Enter the loan amount: "))
    annual_interest_rate = float(input("Enter the annual interest rate: "))
    years = int(input("Enter the number of years: "))

    monthly_interest_rate = annual_interest_rate / 1200 #no of months * 100
    number_of_months = years * 12
    monthly_payment = principal * monthly_interest_rate / (1 - (1 + monthly_interest_rate) ** (-number_of_months))

    #reducing it to 2 decimal places.....ig lol, %.2f is a placeholder
    print("The monthly payment for the loan is: $%.2f " % monthly_payment) 

main()