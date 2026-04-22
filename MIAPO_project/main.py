def get_player_choice():
    while True:
        player_choice = input('Enter Rock, Paper or Scissor.\n')
        if player_choice in ("Rock", "Paper", "Scissor"):
            return player_choice
        else:
            print('Please, enter allowed value!')



