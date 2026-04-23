import random
def get_computer_choice():
    computer_choice = random.choice(['Rock', 'Paper', 'Scissors'])
    return computer_choice


def get_player_choice():
    while True:
        player_choice = input('Enter Rock, Paper or Scissors.\n')
        if player_choice in ("Rock", "Paper", "Scissors"):
            return player_choice
        else:
            print('Please, enter allowed value!')


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


while True:
    print('1 - Start game\n2 - Show rules')
    user_input = input()
    if user_input == '1':
        player_choice = get_player_choice()
        computer_choice = get_computer_choice()
        result = determine_winner(player_choice, computer_choice)
        print(computer_choice)
        if result == 'draw':
            print('draw')
        if result == True:
            print('win')
        if result == False:
            print('lose')
    elif user_input == '2':
        read_file()
    else:
        print('Invalid input!')