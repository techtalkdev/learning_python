#rock, paper, scissors game 🗿
import random
options = ('rock', 'paper', 'scissor')
computer_choice = random.choice(options)

while True:
    player_choice = input('Enter your choice(Rock, Paper, Scissor): ').lower()
    if player_choice == 'rock' and computer_choice == 'paper' or player_choice == 'scissor' and computer_choice == 'rock' or player_choice == 'paper' and computer_choice == 'scissor':
        print(f"Computer choice: {computer_choice} | Player choice: {player_choice}")
        print("You lose! The computer wins!😭")
    if player_choice == computer_choice:
        print(f"Player: {player_choice} | Computer: {computer_choice}")
        print("It's a tie!")
    elif player_choice == 'rock' and computer_choice == 'scissor':
        print(f"Player: {player_choice} | Computer: {computer_choice}")
        print("Rock beats Scissor! You win!🥳")
    elif player_choice == 'paper' and computer_choice == 'rock':
        print(f"Player: {player_choice} | Computer: {computer_choice}")
        print("Paper beats Rock! You win!🥳")
    elif player_choice == 'scissor' and computer_choice == 'paper':
        print(f"Player: {player_choice} | Computer: {computer_choice}")
        print("Scissor beats Paper! You win🥳")
    else:
        print('Invalid choice')
