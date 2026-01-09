import random

num = random.randint(1,101)
try:
    guess=int(input("Guess the no. : "))

    attempts = 1

    while num!=guess:
        
        if num>guess:
            print("Higher the number please! ")
                    
        else:
            print("Lower the number please! ")
                    

        guess=int(input("Guess the no. : "))
        attempts+=1
            
    else:
        print("You guessed the no.")
        print(f"Took you {attempts} attempts.")

except ValueError:
        print("Invalid digit!")


