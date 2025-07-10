#Python Compound Interest Calculator
#1   A = final amount
#2   P = Initial Principal balance
#3   r = interest rate
#4   t = number of time periods elapsed

your_money = 0
interest_rate = 0
period_of_investment = 0


while your_money <= 0:
    your_money = int(input("Enter the principal amount: "))
    if your_money <= 0:
        print("Your money cannot be zero or less than zero")
    elif your_money >= 0:
        print(f"You made deposited R{your_money} into you account")

while interest_rate <= 0:
    interest_rate = float(input("Enter the interest rate: "))
    if interest_rate <= 0:
        print("Your interest rate cannot be zero or less than zero")
    elif interest_rate >= 0:
        print(f"Your interest rate is {interest_rate}")

while period_of_investment <= 0:
    period_of_investment = int(input("Enter the period of investment: "))
    if period_of_investment <= 0:
        print("Your period of investment cannot be zero or less than zero")
    elif period_of_investment >= 0:
        print(f"Your period of investment is {period_of_investment} years")

total_balance = your_money * pow((1 + interest_rate / 100),period_of_investment)
print("**********************************************")
print(f"Your total balance is {round(total_balance)}")