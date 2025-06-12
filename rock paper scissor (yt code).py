import random

ROCK="r"
PAPER="p"
SCISSOR="s"
emojis={ROCK:"🪨",SCISSOR:"✂️",PAPER:"📃"}
choices=(tuple(emojis.keys()))
conti=("y","n")

def get_user_choice():
    while True:
        user_choice = input("enter rock,paper or scissor? (r/p/s):").lower()
        if user_choice in choices:
            return user_choice
        else:
            print("invalid input")
            continue

def display_choices(user_choice,computer_choice):
    print(f"you chose:{emojis[user_choice]}")
    print(f"computer chose:{emojis[computer_choice]}")

def determine_winner(computer_choice,user_choice):
    if computer_choice == user_choice:
        print("That's a tie")
    elif (
            (computer_choice == SCISSOR and user_choice == ROCK) or
            (computer_choice == PAPER and user_choice == SCISSOR) or
            (computer_choice == ROCK and user_choice == PAPER)):
        print("you win")
    else:
        print("you lose")

def game():
    while True:
        user_choice=get_user_choice()

        computer_choice=random.choice(choices)

        display_choices(computer_choice,user_choice)

        determine_winner(computer_choice,user_choice)

        should_continue=input("wanna continue? (y/n):")
        if should_continue not in conti:
            print("enter valid input")
            continue
        if should_continue=="y":
            continue
        elif should_continue=="n":
            break

game()




