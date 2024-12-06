#Rock-Paper-Scissors
print("Rock-Paper-Scissors")
import random
options = ["rock","paper","scissors"]

while(True):
    user = input("\nEnter you play(rock,paper,scissors):")
    comp = random.choice(options)
    print("Computer choice:",comp)
    if(user == comp):
        print("Match Tie!")
    elif(user == "rock" and comp == "paper"):
        print("You loose")
    elif(user == "rock" and comp == "scissors"):
        print("You win")
    elif(user == "paper" and comp == "rock"):
        print("You win")
    elif(user == "paper" and comp == "scissors"):
        print("You loose")
    elif(user == "scissors" and comp == "rock"):
        print("You loose")
    elif(user == "scissors" and comp == "paper"):
        print("You won")
    ch = input("\nPlay again(y/n)?")
    if ch == 'n':
        break
    else:
        continue
print("Thank you...")
