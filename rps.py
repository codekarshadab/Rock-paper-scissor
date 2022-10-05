# Rock Paper Scissors
import random

def gameWin(comp, you):
    # If two values are equal, declare a tie!
    if comp == you:
        return None

    # Check for all possibilities when computer chose s
    elif comp == 'r':
        if you=='p':
            return True
        elif you=='s':
            return False
    
    # Check for all possibilities when computer chose w
    elif comp == 'p':
        if you=='s':
            return True
        elif you=='r':
            return False
    
    # Check for all possibilities when computer chose g
    elif comp == 's':
        if you=='r':
            return True
        elif you=='p':
            return False

print("Comp Turn: Rock(r) paper(p) or scissor(s)?")
randNo = random.randint(1, 3) 
if randNo == 1:
    comp = 'r'
elif randNo == 2:
    comp = 'p'
elif randNo == 3:
    comp = 's'

you = input("Your Turn: Rock(r) paper(p) or scissor(s)?")
a = gameWin(comp, you)

print(f"Computer chose {comp}")
print(f"You chose {you}")

if a == None:
    print("The game is a tie!")
elif a:
    print("You Win!")
else:
    print("You Lose!")