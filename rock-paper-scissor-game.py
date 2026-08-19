"""
workflow of project:
1. input from user(ROCK, PAPPER, SCISSOR)
2. COMPUTER CHOICE ( RANDOM CHOICE FROM COMPUTER)
3. PRINT RESULT


CASES;
A- ROCK
ROCK-ROCK = TIE
ROCK- Paper = computer wins
rock- scissor = user wins

B- paper
paper - paper = tie
paper - rock = user wins
paper - scissor = computer wins

C- scissor
scissor -scissor = tie
scissor - rock = computer winsr
scissor - paper = user wins
r
"""
import random
item_list = ["rock","paper", "scissor"]
user_choice = input("enter your choice (rock,paper,scissor) : ")
comp_choice = random.choice(item_list)

print(f"user choice: {user_choice}, computer choice: {comp_choice}")

if user_choice == comp_choice:
    print(" both chooses same so match is a tie")

elif user_choice == "rock":
    if comp_choice == "paper":
        print("computer wins")
    else:
        print("user wins")

elif user_choice == "paper":
    if comp_choice == "scissor":
        print("computer wins")
    else:
        print("user wins")

elif user_choice == "scissor":
    if comp_choice == "rock":
        print("computer wins")
    else:
        print("user wins")