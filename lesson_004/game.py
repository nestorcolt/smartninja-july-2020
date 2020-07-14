import json
import os

# Path to file
path = "score.json"
game_data = []

# Read the store score from score file.
if os.path.exists(path):
    with open(path, "r") as my_path_object:
        game_data = json.load(my_path_object)

player = input("Player name: ")
secret = 22
attempts = 0

while True:
    guess = int(input("Guess the secret number (between 1 and 30): "))
    attempts += 1

    if guess == secret:
        print("You've guessed it - congratulations! It's number " + str(secret))
        print("Attempts needed: " + str(attempts))

        data = {"player": player, "attempts": attempts}
        game_data.append(data)

        with open(path, "w") as my_path_object:
            json.dump(game_data, my_path_object, indent=4, separators=[",", ":"])

        break

    elif guess > secret:
        print("Your guess is not correct... try something smaller")
    elif guess < secret:
        print("Your guess is not correct... try something bigger")

##############################################################################################
