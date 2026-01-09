import random

num = random.randint(1, 101)
attempts = 0

while True:
    try:
        guess = int(input("Guess the no. : "))
        attempts += 1

        if guess < num:
            print("Higher the number please!")
        elif guess > num:
            print("Lower the number please!")
        else:
            print("You guessed the number!")
            print(f"Took you {attempts} attempts.")
            break

    except ValueError:
        print("Invalid digit! Please enter a number.")
