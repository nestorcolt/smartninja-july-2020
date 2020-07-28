import json
import os

# Path to file
path = "score.json"
game_data = []


def get_game_data():
    # Read the store score from score file.
    if os.path.exists(path):
        with open(path, "r") as my_path_object:
            game_data = json.load(my_path_object)


def play_game(guess, player, secret, attempts):
    if guess == secret:
        data = {"player": player, "attempts": attempts}
        game_data.append(data)
        message = """
            You've guessed it - congratulations! It's number {}
            Attempts needed: {}
        """.format(str(secret), str(attempts))

        with open(path, "w") as my_path_object:
            json.dump(game_data, my_path_object, indent=4, separators=[",", ":"])

        return message

    elif guess > secret:
        return "Your guess is not correct... try something smaller"
    elif guess < secret:
        return "Your guess is not correct... try something bigger"

##############################################################################################
