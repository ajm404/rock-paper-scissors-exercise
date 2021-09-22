# this is the "game.py" file...
import random
import os
from dotenv import load_dotenv
load_dotenv()


name = os.getenv ("Player_Name", default= "Player 1")
print(f"Welcome to the game {name}")

user_choice = input("Choose 'rock' or 'paper' or 'scissors': ")
print("you chose:")
print(user_choice)

options = ["rock", "paper", "scissors"]

computer_choice = random.choice(options)
print("Computer chose:")

print(computer_choice)

if user_choice == computer_choice:
    print ("It's a tie!")

if user_choice == "rock":
    if computer_choice == "rock":
        print("Better luck next time.")
    elif computer_choice == "paper":
        print("You lost.")
    elif computer_choice == "scissors":
        print("You won! GG!")
elif user_choice == "paper":
    if computer_choice == "rock":
        print("You won! GG!")
    elif computer_choice == "paper":
        print("Better luck next time.")
    elif computer_choice == "scissors":
        print("You lost.")
elif user_choice == "scissors":
    if computer_choice == "rock":
        print("You lost.")
    elif computer_choice == "paper":
        print("You won! GG!")
    elif computer_choice == "scissors":
        print("Better luck nect time.")
else:
    print("You're not doing it right! Just enter either rock, paper, or scissors next time.")
exit()
