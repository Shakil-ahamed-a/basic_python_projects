import random

options=["rock","paper","scissor"]
while True:
    user_input=input("rock,paper or scissor :").lower()
    computer_sign=random.choice(options)
    if computer_sign==user_input:
        print("computer:",computer_sign)
        print("again")
    elif computer_sign=="rock" and user_input=="paper":
        print("computer:",computer_sign)
        print("you win")
    elif computer_sign=="paper" and user_input=="scissor":
        print("computer:",computer_sign)
        print("you win")
    elif computer_sign=="scissor" and user_input=="rock":
        print("computer:",computer_sign)
        print("you win")
    elif computer_sign=="rock" and user_input=="scissor":
        print("computer:",computer_sign)
        print("you loose")
    elif computer_sign=="paper" and user_input=="rock":
        print("computer:",computer_sign)
        print("you loose")
    elif computer_sign=="scissor" and user_input=="paper":
        print("computer:",computer_sign)
        print("you loose")
    else:
        print("invalid input")

    play=input("want to play again:").lower()
    if play=="no":
        break
    elif play=="yes":
        continue
    else:
        print("invalid input")










