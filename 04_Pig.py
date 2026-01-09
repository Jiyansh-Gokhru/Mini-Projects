import random
def roll_dice():
    return random.randint(1, 6)
while True: 
    players=input("Number of players(2-4): ")
    if players.isdigit():
        players=int(players)

        if players==1:
            print("At least 2 players are required to play the game.")
        elif 2 <= players <= 4:
            break
        else:
            print("Invalid input. Please enter a number between 2 and 4.")
    else:
        print("Invalid input. Please enter a valid number.")

print("players:", players)

max_scoore=25
print("First player to reach 25 points wins the game!")
playerscores=[0]*players

while max(playerscores)<max_scoore:
    for i in range(players):
        should_continue=input(f"Player {i+1}, do you want to roll the dice? (y/n): ").lower()
        if should_continue=='n':
            print(f"Player {i+1} chose to pass their turn.")
            continue
                
        dice_roll=roll_dice()
        playerscores[i]+=dice_roll
        if dice_roll==1:
            playerscores[i]=0
            print(f"Player {i+1} rolled a 1 and loses all points!\n Total score reset to 0.") 
        print(f"Player {i+1} rolled a {dice_roll}. Total score: {playerscores[i]}")

        if playerscores[i]>=max_scoore:
            print(f"Player {i+1} wins!")
            exit()