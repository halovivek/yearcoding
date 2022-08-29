# This is random guessing game
import random
secretNumber = random.randint(1,10)
print("i thinking of new number")

# ask the player for the new number
for guessToken in range(1,10):
    print("take the guess")
    guess = int(input())

    if guess < secretNumber:
        print("you have guess the low number")
    elif guess > secretNumber:
        print("you have guess the high number")
    else:
        break


if guess == secretNumber:
        print(" Good Job")
else:
         print("nope, The number is " +str(secretNumber))
         print("the random number is " +str(secretNumber))
