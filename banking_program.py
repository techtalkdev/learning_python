# ⭐ banking program 💰


def show_balance(balance):
    print(f"Your Balance: R{balance:.2f}")

def deposit():
    amount = float(input("How much money do you want to deposit: "))

    if amount <= 0:
        print("Sorry, you cannot deposit zero or a negative amount.")
        return 0
    else:
        return amount
def withdraw(balance):
    amount = float(input("How much money do you want to withdraw: "))
    if amount > balance:
        print("Insufficient funds.")
        return 0
    elif amount < 0:
        print('Amount must be greater than zero.')
        return 0
    else:
        return amount

def main():
    is_running = True
    balance = 0

    while is_running:
        print("*****************")
        print("Banking Program🏦")
        print("*****************")

        print("1. Show Balance💰")
        print("2. Deposit ➕")
        print("3. Withdraw ➖")
        print("4. Exit ❌")
        print("*****************")
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            show_balance(balance)
        elif choice == '2':
            balance += deposit()
        elif choice == '3':
            balance -= withdraw(balance)
        elif choice == '4':
            is_running = False
        else:
            print('Invalid choice')

    print("*****************")
    print('Thank you! Have a nice day!')

if __name__ == '__main__':
    main()