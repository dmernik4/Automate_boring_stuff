# Debugging Coin Toss Program

import random
import logging  # Not in the original file.

logging.disable(logging.CRITICAL)  # Stops all errors - Not in the original file.

logging.basicConfig(
    level=logging.DEBUG, format=" %(asctime)s - %(levelname)s - %(message)s"
)  # Not in the original file.

logging.debug("Start of program.")  # Not in the original file.
guess = ""
while guess not in ("heads", "tails"):
    logging.debug("First guess.")  # Not in the original file.
    print("Guess the coin toss! Enter heads or tails:")
    guess = input()

logging.debug("The first toss.")  # Not in the original file.
toss = random.randint(0, 1)  # 0 is tails, 1 is heads

# After debug check we see that "tails or heads" are not equal to "0 or 1".
# We need to convert "tails" to 0 and "heads" to 1.
if toss == 0:
    toss = "tails"
if toss == 1:
    toss = "heads"

logging.debug(
    "Is " + str(toss) + " equal to " + str(guess) + "?"
)  # Not in the original file.
if toss == guess:
    print("You got it!")

else:
    print("Nope! Guess again!")
    guess = input()
    if toss == guess:
        print("You got it!")
    else:
        print("Nope. You are really bad at this game.")
