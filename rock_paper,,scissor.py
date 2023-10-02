import random

def game():
    choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(choices)
    user_choice = input("Enter rock, paper, or scissors: ").lower()

    if user_choice not in choices:
        print("Invalid choice. Please choose rock, paper, or scissors.")
    elif user_choice == computer_choice:
        print(f"Computer chose {computer_choice}. It's a draw!")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        print(f"Computer chose {computer_choice}. You win!")
    else:
        print(f"Computer chose {computer_choice}. You lose!")

game()
