def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return 'draw'
    if (player_choice == 'Rock' and computer_choice == 'Scissors') or (player_choice == 'Paper' and computer_choice == 'Rock' ) or (player_choice == 'Scissors' and computer_choice == 'Paper'):
        return True
    else:
        return False