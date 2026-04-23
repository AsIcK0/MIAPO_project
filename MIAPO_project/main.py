<<<<<<< HEAD
def get_player_choice():
    while True:
        player_choice = input('Enter Rock, Paper or Scissors.\n')
        if player_choice in ("Rock", "Paper", "Scissors"):
            return player_choice
        else:
            print('Please, enter allowed value!')


import random
def get_computer_choice():
    computer_choice = random.choice(['Rock', 'Paper', 'Scissors'])
    return computer_choice


def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return 'draw'
    if (player_choice == 'Rock' and computer_choice == 'Scissors') or (player_choice == 'Paper' and computer_choice == 'Rock' ) or (player_choice == 'Scissors' and computer_choice == 'Paper'):
        return True
    else:
        return False


def read_file():
    with open('readme.txt', 'r', encoding= 'utf-8') as file:
        content = file.read()
    print(content)

