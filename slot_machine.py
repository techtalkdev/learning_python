#⭐ slot machine 🎰
import random

def spin_row():
    symbols = ['🍒', '🍉', '🍋', '🔔', '⭐']

    return [random.choice(symbols) for _ in range(3)]

def print_row(row):
    print('***********')
    print(' | '.join(row))
    print('***********')

def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == '🍒':
            return bet * 10
        elif row[0] == '🍉':
            return bet * 50
        elif row[0] == '🍋':
            return bet * 20
        elif row[0] == '🔔':
            return bet * 30
        elif row[0] == '⭐':
            return bet * 60
    return 0

def main():
    balance = 100

    print('*************************')
    print('Welcome to Python Slots🎰')
    print("Symbols: 🍒 🍉 🍋 🔔 ⭐")
    print('*************************')

    while balance > 0:
        print(f'Current Balance R{balance:.2f}')

        bet = input('PLACE YOUR BET: ')

        if not bet.isdigit():
            print('Please enter a valid number⚠️')
            continue
        bet = int(bet)

        if bet > balance:
            print('Sorry, you do not have enough money!⚠️')
            continue
        if bet <= 0:
            print('Bet must be greater than zero!⚠️')
            continue
        balance -= bet

        row = spin_row()
        print('Spinning...🔁\n')
        print_row(row)

        payout = get_payout(row, bet)

        if payout > 0:
            print(f'You won R{payout:.2f}!')
        else:
            print('Sorry you lost this round. Play again!')

        balance += payout

        play_again = input('Would you like to play again? (y/n): ').upper()
        if play_again != 'Y':
            break

    print('*************************')
    print('GAME OVER!')
    print('Thank you for playing!')
    print(f'Your Final Balance: R{balance}')


if __name__ == '__main__':
    main()