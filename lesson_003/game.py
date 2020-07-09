import random
import os

##############################################################################################
# Guess the secret number: store the best score in a file
"""
    Resources:
        https://www.fing.edu.uy/inco/cursos/fpr/wiki/index.php/Operadores_en_Python
        https://www.it-swarm.dev/es/python/comportamiento-de-los-operadores-de-incremento-y-decremento-en-python/967188637/
        https://www.geeksforgeeks.org/os-module-python-examples/
"""

# Path to file
path = "score.txt"

# Read the store score from score file.
if os.path.exists(path):
    with open(path, "r") as score:
        stored_score = int(score.read())
        print("The best score is: {}".format(stored_score))

secret = 22
attempts = 0

# Game loop init here
while True:
    guess = int(input("Guess the secret number (between 1 and 30): "))
    attempts += 1

    if guess == secret:
        print("You've guessed it - congratulations! It's number " + str(secret))
        print("Attempts needed: " + str(attempts))

        if attempts < stored_score:
            # Write the score into the file
            with open(path, "w") as score:
                score.write(str(attempts))

        break

    elif guess > secret:
        print("Your guess is not correct... try something smaller")
    elif guess < secret:
        print("Your guess is not correct... try something bigger")

##############################################################################################
