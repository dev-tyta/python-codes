import random
import sys


print("ROCK, PAPER, SCISSORS")
# This is to keep track of the scores : Wins, losses and ties
ties = 0
wins = 0
losses = 0


while True:
    print(f"{wins} Wins, {losses} Losses, {ties} Ties")
    while True:  # The player input loop
        print("Enter your first letter of your choice, (r)rock, (p)paper, (s)scissors and (q)uit")
        choice = input().lower()
        if choice == "q":
            sys.exit()
        elif choice == "r" or choice == "p" or choice == "s":
            break
        else:
            print("Input either r, p, s, q")
    if choice == "r":
        print("Rock versus ....")
    elif choice == "p":
        print("Paper versus ....")
    elif choice == "s":
        print("Scissors versus ....")

    list_choice = list(["r", "p", "s"])
    comp_choice = random.choice(list_choice)  # Gets the computer choice
    # You could also use this other option
    # computer_rand = random.randint(1,3)
    # if computer_rand == 1:
    #   comp_choice = "r"
    # elif computer_rand == 2:
    #   comp_choice = "s"
    # else:
    #   comp_choice = "p"

    if comp_choice == choice:
        if choice == "s":
            print("Scissors versus Scissors")
        elif choice == "p":
            print("Paper versus Paper")
        else:
            print("Rock versus Rock")
        print("This is a tie")
        ties += 1
    elif comp_choice == "r" and choice == "p":
        print("Paper versus Rock")
        print("You Won!!!")
        wins += 1
    elif comp_choice == "r" and choice == "s":
        print("Scissors versus Rock")
        print("Oww... You Lost!!!")
        losses += 1
    elif comp_choice == "p" and choice == "r":
        print("Rock versus Paper")
        print("Oww... You Lost!!!")
        losses += 1
    elif comp_choice == "p" and choice == "s":
        print("Scissors versus Paper")
        print("You Won!!!")
        wins += 1
    elif comp_choice == "s" and choice == "r":
        print("Rock versus Scissors")
        print("You Won!!!")
        wins += 1
    elif comp_choice == "s" and choice == "p":
        print("Paper versus Scissors")
        print("Oww... You Lost!!!")
        losses += 1
    else:
        print("Not in this game try again")
