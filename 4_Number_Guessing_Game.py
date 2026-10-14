import random

random_number = random.randint(1, 100)      # get a random number from 1 to 100

while True:
    guess = int(input("Guess a number from 1 - 100: "))
    if guess > random_number:
        print(f"Lower than {guess}")
    elif guess < random_number:
        print(f"Higher then {guess}")
    else:
        print("Correct")
        break