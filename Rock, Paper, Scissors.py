# Import the random module
import random

# Get player input of either rock, paper, or scissors and run validation on input
print()
player = input("Enter your choice of rock, paper, or scissors: ")
while (player != "rock" and player != "paper" and player != "scissors"):
    print()
    player = input("That is an invalid answer.  Please enter rock, paper, or scissors. ")

# Have computer select a random number between 1 and 3
computer = random.randint(1, 3)

# Set of procedures based on computer's selection of 1, 2, or 3
if (computer == 1):
    computer = "rock"

elif (computer == 2):
    computer = "paper"

else:
    (computer == 3)
    computer = "scissors"

# Prints the player and computer choices
print("\nYour choice: ", player, "\n\nComputer choice: ", computer)

# If-elif-else statements used to determine if player or computer won game
if (player == computer):
    print("\nIt's a draw!")

elif (player == "rock"):
    if (computer == "paper"):
        print("\nComputer wins!")
    else:
        print("\nYou win!")

elif (player == "paper"):
    if (computer == "rock"):
        print("\nYou win!")
    else:
        print("\nComputer wins!")

elif (player == "scissors"):
    if (computer == "rock"):
        print("\nComputer wins!")
    else:
        print("\nYou win!")

print("\nAuthor: Tim Powers")


              
