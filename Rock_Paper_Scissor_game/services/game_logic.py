import random

def get_computer_choice():
    return random.choice(["rock","paper","scissor"])

def determine_winner(user_choice,comp_choice):
    if user_choice == comp_choice :
        return "tie"
    elif (user_choice == "rock" and comp_choice == "scissor") or \
         (user_choice == "paper" and comp_choice == "rock") or \
         (user_choice == "scissor" and comp_choice == "paper"):
        return "win"
    else:
        return "lose"
    
