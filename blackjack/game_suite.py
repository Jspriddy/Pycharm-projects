import blackjack


games = {"1": "Blackjack", "2": "Hangman"}

print("Please input the number of the game you would like to play or \'q\' to quit:")

for key, game in games.items():
    print(f"{key}: {game}")

while 1:
    for key in games.keys():
        play_game = input("> ")
        if play_game in key:
            chosen_game = games[play_game]
            chosen_game = chosen_game.lower()
            command = f"{chosen_game}.play()"
            exec(command)
