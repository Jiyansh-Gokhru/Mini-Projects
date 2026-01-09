import random
import time

def hs():
    try:
        with open("05_Highscore.txt", "r") as f:
            return f.read()
    except FileNotFoundError:
        return "-1"


def generate_problem():
    left = random.randint(MIN_OPERAND, MAX_OPERAND)
    right = random.randint(MIN_OPERAND, MAX_OPERAND)
    operator = random.choice(OPERATORS)
        
    expr = f"{left} {operator} {right}"
    answer = str(eval(expr))
    return expr, answer


OPERATORS = ["+", "-", "*"]
MIN_OPERAND = 1
MAX_OPERAND = 12
TOTAL_PROBLEMS = 5



correct = 0
input("Press enter to start!")
print("----------------------")

start_time = time.time()

for i in range(TOTAL_PROBLEMS):
    expr, answer = generate_problem()
    
    guess = input("Problem #" + str(i + 1) + ": " + expr + " = ")
    if guess.isdigit() and int(guess) == int(answer):
        print("Correct!")
        correct+=1
        break
    else:
        print("Wrong answer")
        print(f"{answer} was Correct!")
        break
        

end_time = time.time()
total_time = round(end_time - start_time, 2)

print("----------------------")

print(f"Nice work! You finished {TOTAL_PROBLEMS} Problems,\nIn which {correct} were Correct,\nIn {total_time} seconds! ")

print("----------------------")

HIGHSCORE = float(hs())
if((total_time < HIGHSCORE or HIGHSCORE==-1) and correct==TOTAL_PROBLEMS):
    with open("05_Highscore.txt","w") as f:
        f.write(str(total_time))
        print(f"New Record set,\nFor completing All probleams in {total_time} seconds!")

print("----------------------")
