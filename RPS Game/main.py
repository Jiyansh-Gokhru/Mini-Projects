import random

while True:
    Pick = [0, 1, -1]
    cpuint = random.choice(Pick)
    
    YOU = input("Rock... Paper... Scissors.. Shoot: ")
    
    youdic = {
        "Rock": -1,
        "Paper": 1,
        "Scissors": 0
    }
    
    cpudic = {
        -1: "Rock",
        1: "Paper",
        0: "Scissors"
    }

    try:
        youint = youdic[YOU.capitalize()]
        CPU = cpudic[cpuint]
        
        print(f"You choose {YOU.capitalize()}")
        print(f"CPU choose {CPU}")

        if cpuint == youint:
            print("It's a TIE!")
        elif (cpuint == 1 and youint == 0):
            print("You WON!!")
        elif (cpuint == 1 and youint == -1):
            print("You LOSS!!")
        elif (cpuint == -1 and youint == 0):
            print("You LOSS!!")
        elif (cpuint == -1 and youint == 1):
            print("You WON!!")
        elif (cpuint == 0 and youint == 1):
            print("You LOSS!!")
        elif (cpuint == 0 and youint == -1):
            print("You WON!!")
            
    except KeyError:
        print("Invalid input! Please type Rock, Paper, or Scissors.")

    play_again = input("\nDo you want to play again? (y/n): ").lower()
    if play_again != 'y':
        print("Thanks for playing! Press Enter to exit.")
        input()
        break
