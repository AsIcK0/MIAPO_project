def get_player_choice():
    while True:
        player_choice = input('Enter Rock, Paper or Scissors.\n')
        if player_choice in ("Rock", "Paper", "Scissors"):
            return player_choice
        else:
            print('Please, enter allowed value!')



