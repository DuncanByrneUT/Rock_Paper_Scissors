# importing random
import random

user_score_wins = 0
comp_wins = 0

# list that stores the options for the user to type
options = ["rock", "paper", "scissors"]

options[0]

while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit.").lower()
    if user_input == "q":
        break
# not in checks if input is not in there
    if user_input not in options:
        continue
    random_number = random.randint(0, 2)
    # rock = 0, paper = 1, scissors = 2

    comp_pick = options[random_number]
    print("Computer pick", comp_pick + ".")

# users input to see if they win
    if user_input == "rock" and comp_pick == "scissors":
        print("You win!")
        user_score_wins += 1
        continue

    elif user_input == "paper" and comp_pick == "rock":
        print("You win!")
        user_score_wins += 1


    elif user_input == "scissors" and comp_pick == "paper":
        print("You win!")
        user_score_wins += 1

    else:
        print("You lost! :(")
        comp_wins += 1
print("You won", user_score_wins, "times")
print("The computer won", comp_wins, "times")

print("Goodbye!")


